# Updating an asset on Frontify

## Set up the project
Ensure that the project has been setup as described in the [Initial Setup](/readme/InitialSetup.md) readme.


## Modify the script

Change the integer value on line 26 of the `update_frontify_asset.py` [file](/examples/python/update_frontify_asset.py) to determine the asset to update. This numeric ID can be found in the URL of the asset in Frontify, eg demo.frontify.com/screens/**12345**

The information to update is specified with the help of the `AssetData` dataclass, which is defined on line 12 of the [update_asset.py file](/examples/python/update_frontify_asset.py).

`AssetData` takes the following optional fields:
| Field | Type | Description |
| ----- | ---- | ----------- |
| title | String (str) | The new title for the asset |
| description | String (str) | The new description for the asset |
| filename | String (str) | The new filename for the asset when accessed through the API |
| expiresAt | String (str) | The expiration date for the asset in Frontify's expected date format: `2019-12-17T11:36:05+01:00` |
| author | String (str) | The value to be used in the `Creator` field of the legal tab in the backend view of an asset. E.g. `Photogropher name` |
| copyright | Copyright (dataclass) | A Copyright dataclass which requires the copyright status (`"UNKNOWN\|PUBLIC\|COPYRIGHTED"`) and the copyright notice (str). <br> <br> All fields of Copyright are required. <br> <br> For example: <pre python>from src.utils.frontify_queries.update_asset.update_asset import Copyright&#13;copyright=Copyright(&#13;    status: "COPYRIGHTED",&#13;    notice: "This is copyrighted"&#13;)</pre>
|

## Run the script

From the base directory of this repository, run `python examples/python/update_frontify_asset.py`

This will update the specified asset with the information passed in the `assetUpdateData` variable which is defined on line 19.

## Code
- [update_frontify_asset.py](/examples/python/update_frontify_asset.py)
- [update_asset.py](/examples/python/src/utils/frontify_queries/update_asset/update_asset.py
)

## Documentation
Check out the following Frontify Documentation for the `updateAsset` mutation and associated types:
- [updateAsset](https://frontify.github.io/graphql-reference/mutations/updateAsset)
- [UpdateAssetInput](https://frontify.github.io/graphql-reference/type/UpdateAssetInput)
- [UpdateAssetDataInput](https://frontify.github.io/graphql-reference/type/UpdateAssetDataInput)
