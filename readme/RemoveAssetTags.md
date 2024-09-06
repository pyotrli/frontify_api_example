# Remove tags from an asset on Frontify

## Set up the project
Ensure that the project has been setup as described in the [Initial Setup](/readme/InitialSetup.md) readme.


## Modify the script

Change the `asset_id` on line 11 of the `remove_frontify_tags.py` [file](/examples/python/remove_frontify_tags.py) to the ID of the asset you want to add tags to.

The `asset_id` can be found in the URL of the asset in Frontify, eg demo.frontify.com/screens/**123**

This script will remove tags from your specified asset, leaving any other tags in place. You can specify the tags to remove by providing a list of tags, as shown on line 22.

## Run the script

From the base directory of this repository, run `python examples/python/remove_frontify_tags.py`

This will remove the tags specified on line 22 to the specified asset.

## Code
- [remove_frontify_tags.py](/examples/python/remove_frontify_tags.py)
- [remove_tags.py](/examples/python/src/utils/frontify_queries/remove_tags/remove_tags.py
)

## Documentation
- [removeAssetTags mutation](https://frontify.github.io/graphql-reference/mutations/removeAssetTags)
