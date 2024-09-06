from json import JSONDecodeError
from typing import Union, Dict, Tuple, List, Optional
import requests
from requests.exceptions import RequestException
import time
from collections import deque
from datetime import datetime, timedelta


class RateLimitException(Exception):
    pass


class FrontifyClient:
    """
    A client for interacting with the Frontify GraphQL API and uploading files in chunks.

    Attributes:
        domain (str): Your Frontify domain, eg: demo.frontify.com
        access_token (str): The access token for authenticating with the API.
        retries (int): The number of retry attempts for failed requests.
        timeout_in_seconds (int): The timeout for API requests in seconds.
    """

    def __init__(
        self,
        domain: str,
        access_token: str,
        retries: int = 0,
        timeout_in_seconds: int = 10,
    ):
        """
        Initializes the FrontifyClient with the given parameters.

        Args:
            domain (str): Your Frontify domain, eg: demo.frontify.com
            access_token (str): The access token for authenticating with the API.
            retries (int, optional): The number of retry attempts for failed requests. Defaults to 0.
            timeout_in_seconds (int, optional): The timeout for API requests in seconds. Defaults to 10.
        """
        self.domain = domain
        self.access_token = access_token
        self.retries = retries
        self.timeout_in_seconds = timeout_in_seconds
        self.base_delay = 1
        self.max_delay = 16
        self.rate_limit = 2500
        self.time_window = 300
        self.request_times = deque()  # Stores the times of requests made

    def graphql(
        self, query: str, variables: Union[None, Dict] = None
    ) -> Tuple[dict, Optional[List[dict]]]:
        """
        Executes a GraphQL query against the Frontify API.

        Args:
            query (str): The GraphQL query string.
            variables (Union[None, Dict], optional): The variables for the GraphQL query. Defaults to None.

        Returns:
            Tuple[dict, Optional[List[dict]]]: A tuple containing the data and any errors returned by the API.

        Raises:
            Exception: If the request fails too many times or if a JSON decode error occurs.
            ConnectionError: If a connection error occurs.
        """
        tries = 0
        while tries < self.retries:
            tries += 1
            delay = self.base_delay
            try:
                self._check_rate_limit()
                response = requests.post(
                    f"https://{self.domain}/graphql",
                    headers={
                        "Authorization": f"Bearer {self.access_token}",
                        "x-frontify-beta": "enabled",
                        "X-Client-Name": "frontify-api-example-script",
                        "X-Client-Version": "v1.0",
                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/77.0.3865.90 Safari/537.36 ",
                    },
                    json={"query": query, "variables": variables},
                    timeout=self.timeout_in_seconds,
                )
                json = response.json()
                self._record_request()
                return json["data"], json["errors"] if "errors" in json else None
            except JSONDecodeError as json_error:
                json_error_msg = (
                    f"json error occurred: {json_error}, response: {response},"
                    f"full text: {response.text}"
                )
                print(json_error_msg)
                raise Exception(json_error_msg)
            except ConnectionError as error:
                raise error
            except RequestException as e:
                tries += 1
                if tries >= self.retries:
                    raise Exception(f"Max retries reached: {e}")

                print(f"Attempt {tries} failed: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
                delay = min(self.max_delay, delay * 2)
                continue
        raise Exception(f"Request failed too many times: {self.retries}")

    def upload_chunk(self, url: str, body):
        """
        Uploads a chunk of data to the specified URL.

        Args:
            url (str): The URL to upload the chunk to.
            body: The data to upload.

        Raises:
            Exception: If the upload fails with a status code outside the range 200-299.
        """
        response = requests.put(url, data=body)
        if response.status_code < 200 or response.status_code > 299:
            raise Exception(
                f"Failed Uploading with status code {response.status_code}: {response.text}"
            )

    def _check_rate_limit(self):
        """
        Checks if the current request can be made within the rate limit.
        Raises RateLimitException if the rate limit would be exceeded.
        """
        current_time = datetime.now()

        # Remove requests that are outside the time window
        while (
            self.request_times
            and (current_time - self.request_times[0]).total_seconds()
            > self.time_window
        ):
            self.request_times.popleft()

        if len(self.request_times) >= self.rate_limit:
            raise RateLimitException("Rate limit exceeded.")

    def _record_request(self):
        """
        Records the time of a successful request.
        """
        self.request_times.append(datetime.now())

    def _time_until_reset(self):
        """
        Calculates the time until the rate limit resets.
        """
        if not self.request_times:
            return 0

        # Calculate the time until the oldest request falls out of the time window
        time_since_first_request = (
            datetime.now() - self.request_times[0]
        ).total_seconds()
        return max(0, self.time_window - time_since_first_request)
