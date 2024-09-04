# Replacing an asset on Frontify

## Set up the project
Ensure that the project has been setup as described in the [Initial Setup](/readme/InitialSetup.md) readme.


## Modify the script

Change the `asset_id_to_replace` on line 13 of the `replace_frontify_asset.py` [file](/examples/python/replace_frontify_asset.py).

The `asset_id_to_replace` can be found in the URL of the asset in Frontify, eg demo.frontify.com/screens/**123**

This script will replace the specified asset with the demo asset, which is stored in the `demo_files` directory by default, but you can use your own file by changing the value of the `filepath` argument on line 26.

## Run the script

From the base directory of this repository, run `python examples/python/replace_frontify_asset.py`

This will replace the specified asset with the demo asset, which is stored in the `demo_files` directory

## Code
- [replace_frontify_asset.py](/examples/python/replace_frontify_asset.py)
- [upload_file.py](/examples/python/src/utils/frontify_queries/upload_file/upload_file.py
)


