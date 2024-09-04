# Add tags to an asset on Frontify

## Set up the project
Ensure that the project has been setup as described in the [Initial Setup](/readme/InitialSetup.md) readme.


## Modify the script

Change the `asset_id` on line 11 of the `add_frontify_tags.py` [file](/examples/python/replace_frontify_asset.py) to the ID of the asset you want to add tags to.

The `asset_id` can be found in the URL of the asset in Frontify, eg demo.frontify.com/screens/**123**

This script will add new tags to your specified asset, leaving any existing tags in place. You can specify the tags to add by providing a list of tags, as shown on line 22.

## Run the script

From the base directory of this repository, run `python examples/python/add_frontify_tags.py`

This will add the tags specified on line 22 to the specified asset.

## Code
- [add_frontify_tags.py](/examples/python/add_frontify_tags.py)
- [add_tags.py](/examples/python/src/utils/frontify_queries/add_tags/add_tags.py
)

## Documentation
- [addAssetTags mutation](https://frontify.github.io/graphql-reference/mutations/addAssetTags)
