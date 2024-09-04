# FrontifyClient

## Importing FrontifyClient
Import FrontifyClient to your script to make calls to the Frontify GraphQL API:
```python
from src.services.FrontifyClient import FrontifyClient
```

## Initialising the client
Initialise the client by providing your Frontify domain and Access Token as arguments. Optionally, you may also set the number of retries for failed requests and the timeout in seconds.

```python
client = FrontifyClient(
    domain=frontify_domain,
    access_token=frontify_access_token,
    retries=3,
    timeout=20
)
```

### Arguments
| Argument | Type | Explanation |
| -------- | ---- | ----------- |
| domain | String (str) | The domain of your frontify instance without `https://` e.g. `demo.frontify.com`|
| access_token | String (str) | The access token for authenticating with the API. This token will inherit the permissions of the user creating it, and should be set with the scopes `basic: read` and `basic: write`. Access tokens can be generated at `https://<your-frontify-domain>/api/developer/token` when logged into Frontify |
| retries | Integer (int, optional) | The number of retry attempts for failed requests. Defaults to 0. |
| timeout_in_seconds | Integer (int, optional) |  The timeout for API requests in seconds. Defaults to 10. |

## Making a simple query
After initialising the client, you can use it to make a GraphQL query. In this example, no variables are used.

First define your query. For example:

```python
query = """
query CurrentUser {
  currentUser {
    email
    id
    name
  }
}
"""
```

Then execute the query by calling the `client.graphql()` function:

```python
try:
    data, errors = client.graphql(query)
    if errors:
        print("Errors:", errors)
    else:
        print("Data:", data)
except Exception as e:
    print(f"An error occurred: {e}")
```

If successful, this will return the following:

```json
Data: "currentUser": {
      "email": "my.user@frontify.com",
      "id": "eyJXXXXXXXXXXXn0=",
      "name": "User Name"
    }
```

If errors are present in the query response, these will be returned instead, for example:

```json
Errors: [
    {
      "message": "Cannot query field \"nonexistent\" on type \"User\".",
      "locations": [
        {
          "line": 6,
          "column": 5
        }
      ],
      "extensions": {
        "category": "internal"
      }
    }
  ]
  ```

## Making a query with variables
Variables can also be used, just as they would be in GraphQL. As before, after initialising the client, define your query:

```python
query = """
query Library($id: ID!) {
  library(id: $id){
    id
    name
  }
}
"""
```

Then define your variables:
```python
variables = {"id": "1"}
```

Finally, execute the query and pass the variables as an argument:

```python
try:
    data, errors = client.graphql(query, variables)
    if errors:
        print("Errors:", errors)
    else:
        print("Data:", data)
except Exception as e:
    print(f"An error occurred: {e}")
```

Responses will be returned as above

## Mutations
Mutations can be made in the same way as queries. For example:

```python
query = """
mutation UploadFiles($input: UploadFileInput!) {
  uploadFile(input: $input){
    id
    urls
  }
}
"""

variables = {"input": {"filename": "filename.png", "size": "12345"}}

try:
    data, errors = client.graphql(query, variables)
    if errors:
        print("Errors:", errors)
    else:
        print("Data:", data)
except Exception as e:
    print(f"An error occurred: {e}")
```

## Reusable queries and mutations
For convenience and readability, we suggest making use of the `gql` function made available in `src.utils.graphql`

The `gql` function allows you to create reusable query functions. Instead of writing the same query string multiple times, you can define it once and reuse the generated function.

In the examples included in this repository, we define query functions by separating the query itself into an executor, and a function to perform the query and return the results. This example comes from the [replace_asset](/src/utils/frontify_queries/replace_asset/replace_asset.py) function:

#### Query Executor example
```python
from src.utils.graphql import gql

replace_asset_executor = gql("""
    mutation ReplaceAsset($input: ReplaceAssetInput!) {
        replaceAsset(input: $input) {
            job {
                assetId
            }
        }
    }
""")
```

#### Query Function example
```python
from src.services.FrontifyClient import FrontifyClient
from src.utils.frontify_queries.replace_asset.replace_asset_executor import replace_asset_executor


def replace_asset(client: FrontifyClient, asset_id: str, file_id: str) -> str:
    replace_asset_input = {
        "input": {
            "assetId": asset_id,
            "fileId": file_id
        }
    }

    data, errors = replace_asset_executor(client, replace_asset_input)

    if errors:
        raise Exception(f'Failed to replace asset|{errors}')

    else:
        return data
```

#### Usage
This allows the function to be used as part of a larger script in a much more readable manner. For example, after importing the function it could be used as follows:

```python
replace_asset(client=client, asset_id=my_asset_id, file_id=file_id)
```

## Creating a custom GraphQL client
If you're interested in using your own client to make requests, you can see how this might be constructed in [this example](/readme/CreatingAClient.md).