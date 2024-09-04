# Delete an asset from Frontify

## Set up the project
Ensure that the project has been setup as described in the [Initial Setup](/readme/InitialSetup.md) readme.


## Modify the script

Change the `asset_id` on line 11 of the `delete_frontify_asset.py` [file](/examples/python/replace_frontify_asset.py) to the ID of the asset you want to delete.

The `asset_id` can be found in the URL of the asset in Frontify, eg demo.frontify.com/screens/**123**

## Run the script

From the base directory of this repository, run `python examples/python/add_frontify_tags.py`

This will delete the asset specified on line 11.

## Code
- [delete_frontify_asset.py](/examples/python/delete_frontify_asset.py)
- [delete_asset.py](/examples/python/src/utils/frontify_queries/delete_asset/delete_asset.py
)

## Documentation
- [deleteAsset mutation](https://frontify.github.io/graphql-reference/mutations/deleteAsset)
