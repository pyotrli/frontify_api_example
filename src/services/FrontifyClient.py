from json import JSONDecodeError
from typing import Union, Dict, Tuple, List, Optional
import requests
from requests.exceptions import RequestException


class FrontifyClient:
    def __init__(self, domain: str, access_token: str, retries: int = 0, timeout_in_seconds: int = 10):
        self.domain = domain
        self.access_token = access_token
        self.retries = retries
        self.timeout_in_seconds = timeout_in_seconds

    def graphql(self, query: str, variables: Union[None, Dict] = None) -> Tuple[dict, Optional[List[dict]]]:
        tries = 0
        while tries < self.retries:
            tries += 1

            try:
                response = requests.post(
                    f"https://{self.domain}/graphql",
                    headers={
                        'Authorization': f'Bearer {self.access_token}',
                        'x-frontify-beta': 'enabled',
                        'X-Client-Name': 'frontify-api-example-script',
                        'X-Client-Version': 'v1.0',
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/77.0.3865.90 Safari/537.36 '
                    },
                    json={'query': query, 'variables': variables},
                    timeout=self.timeout_in_seconds
                )
                json = response.json()
                return json['data'], json['errors'] if 'errors' in json else None
            except JSONDecodeError as json_error:
                json_error_msg = f'json error occurred: {json_error}, response: {response},' \
                                 f'full text: {response.text}'
                print(json_error_msg)
                raise Exception(json_error_msg)
            except ConnectionError as error:
                raise error
            except RequestException:
                continue
        raise Exception(f'Request failed too many times: {self.retries}')

    def upload_chunk(self, url: str, body):
        response = requests.put(url, data=body)
        if response.status_code < 200 or response.status_code > 299:
            raise Exception(f'Failed Uploading with status code {response.status_code}: {response.text}')
