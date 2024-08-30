# frontify_api_example
Example python script to interact with Frontify's GraphQL API

## Getting Started
make a copy of the `.env.example` file

change the filename to `.env`
add your security credentials to the `.env` file


## Replacing an asset on Frontify
change the `asset_id_to_replace` in the `replace_frontify_asset.py` file

the `asset_id_to_replace` can be found in the URL of the asset in Frontify, eg demo.frontify.com/screens/**123**

run `replace_frontify_asset.py`

this will replace the specified asset with the demo asset, which is stored in the `demo_files` directory
