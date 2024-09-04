# frontify_api_example
Example python script to interact with Frontify's GraphQL API.
Frontify's documentation is available on [developer.frontify.com](https://developer.frontify.com/).

## Getting Started
- clone the repo
- create a venv
- activate your venv
- install packages (list in `requirements.txt`)
- make a copy of the `.env.example` file
- change the copied filename to `.env`
- add your security credentials to the `.env` file

you are now ready to run example scipts (eg `replace_frontify_asset.py`)


## Replacing an asset on Frontify
change the `asset_id_to_replace` in the `replace_frontify_asset.py` file

the `asset_id_to_replace` can be found in the URL of the asset in Frontify, eg demo.frontify.com/screens/**123**

run `replace_frontify_asset.py`

this will replace the specified asset with the demo asset, which is stored in the `demo_files` directory

## Disclaimers
- This is not an official script provided by Frontify
- There are no tests and quality / maintenance are not guaranteed
- This example should be used for inspiration and a way to get started quickly

## Requirements
- Tested with Python 3.11.5, but should be compatible with earlier versions as well
