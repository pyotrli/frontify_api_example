# Creating a Custom Python GraphQL Client
Creating a custom Python GraphQL client can streamline your interactions with a GraphQL API, making your code cleaner and more maintainable. Instead of using the requests library for each individual call, a custom client can encapsulate common functionality, handle errors more gracefully, and provide a more intuitive interface for making queries and mutations.

## Why Use a Custom Client?
1. Code Reusability: Encapsulate common logic for making requests, handling errors, and parsing responses.
2. Maintainability: Centralize changes to the API endpoint or authentication logic in one place.
3. Readability: Simplify the syntax for making GraphQL queries and mutations, making your code easier to read and understand.

## Steps to Create a Custom GraphQL Client
1. Install Dependencies: Ensure you have the `requests` library installed.

```curl 
pip install requests
```

2. Define the Client Class:

- Create a class to handle the GraphQL requests.
- Include methods for making queries and mutations.
- Handle errors and responses within the class.

Example Implementation:

```python 
import requests

class GraphQLClient:
    def __init__(self, endpoint, headers=None):
        self.endpoint = endpoint
        self.headers = headers if headers else {}

    def execute(self, query, variables=None):
        payload = {
            'query': query,
            'variables': variables
        }
        response = requests.post(self.endpoint, json=payload, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Query failed with status code {response.status_code}: {response.text}")

# Usage example
if __name__ == "__main__":
    endpoint = "https://api.example.com/graphql"
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN"
    }
    client = GraphQLClient(endpoint, headers)

    query = """
    query GetUser($id: ID!) {
        user(id: $id) {
            id
            name
            email
        }
    }
    """
    variables = {"id": "1"}
    try:
        response = client.execute(query, variables)
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")
```

## Our example - FrontifyClient
[FrontifyClient](../src/services/FrontifyClient.py) is an example of how a GraphQL client may be constructed for the Frontify API. 

The Frontify Client included in this repository also includes an example of how you might implement exponential backoffs as suggested by the [Frontify Developer Documentation](https://developer.frontify.com/d/XFPCrGNrXQQM/graphql-api#/access-control/rate-limiting-and-limitations-1) on rate limiting and staying in line with Frontify guidelines to not perform over 2500 requests in a 5 minute rolling window.

### Arguments
| Argument | Type | Explanation |
| -------- | ---- | ----------- |
| domain | String (str) | The domain of your frontify instance without `https://` e.g. `demo.frontify.com`|
| access_token | String (str) | The access token for authenticating with the API. This token will inherit the permissions of the user creating it, and should be set with the scopes `basic: read` and `basic: write`. Access tokens can be generated at `https://<your-frontify-domain>/api/developer/token` when logged into Frontify |
| retries | Integer (int, optional) | The number of retry attempts for failed requests. Defaults to 0. |
| timeout_in_seconds | Integer (int, optional) |  The timeout for API requests in seconds. Defaults to 10. |

### Returns
The `FrontifyClient` will return a tuple containing the data and any errors returned by the API. 

### Usage
Full usage example can be found in [this readme](/readme/FrontifyClient.md)