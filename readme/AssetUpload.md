# Upload an asset to Frontify

## Set up the project
Ensure that the project has been setup as described in the [Initial Setup](/readme/InitialSetup.md) readme.


## Modify the script

This script will upload the demo asset, which is stored in the `demo_files` directory by default, with the title "Example Asset" but you can use your own file by changing the value of the `filepath` argument on line 24.

Additionally, the `create_asset` function supports the following arguments:

| Argument | Type | Explanation |
| -------- | ---- | ----------- |
| client | FrontifyClient [Required] | The Frontify GraphQL client included in this repository |
| projectid | String (str) [Required] | The ID of the library or project where the asset should be uploaded. This can be an string representation of an integer as found in the library URL, such as demo.frontify.com/projects/**12345**/library, or can be the Base64 style ID returned from the Frontify API. <br> <br> NB: Base64 IDs can be generated using the base64tools found in [base64tools.py](/examples/python/src/utils/base64tools.py) <br> <br> See also, [Using Base64 Tools](/readme/UsingBase64Tools.md) |
| title | String (str) [Optional: if not used, filename is required] | The title to be used for the asset |
| filename | String (str) [Optional: if not used, title is required] | Used to construct a title from the filename. If used in place of `title`, the filename without extension will be used as the title |
| directory | String (str) [Optional] | A string representation of the directory path in the format `Folder/SubFolder` |
| description | String (str) [Optional] | The asset description |
| author | String (str) [Optional] | The value to be used in the `Creator` field of the legal tab in the backend view of an asset. E.g. `Photogropher name` |
| copyright | String (str) [Optional] | The Copyright Status to be applied to an asset. Valid values are "UNKNOWN", "COPYRIGHTED", "PUBLIC. <br> <br> NB: a Copyright Status is required to apply a Copyright Notice |
| copyright_notice | String (str) [Optional] | The Copyright Notice to be applied to an asset. Copyright Notices require a status to be applied in order to be correctly displayed. If a Copyright Notice is passed with no Copyright Status, it will default to the "UNKNOWN" status |
| tags | List (list) [Optional] | A list of tags to apply to an asset, e.g. `['tag1', 'tag2'] |
| expires_at | String (str) [Optional] | The expiry date of an asset in the format `2019-12-17T11:36:05+01:00` |
| externalId | String (str) [Optional] | An external ID to attach to an asset. This will only be accessible through API calls, but can be useful when synching assets between different systems |
| skip_exif | Boolean (bool) [Optional, default True] | Skip embedded metadata in the file such as keywords |

## Run the script

From the base directory of this repository, run `python examples/python/upload_frontify_asset.py`

This will replace the specified asset with the demo asset, which is stored in the `demo_files` directory

## Documentation
[Frontify Developer Documentation - Upload a file and create an asset](https://developer.frontify.com/d/XFPCrGNrXQQM/graphql-api#/deep-dive/upload-file-create-asset)

## Code
- [replace_frontify_asset.py](/examples/python/upload_frontify_asset.py)
- [upload_file.py](/examples/python/src/utils/frontify_queries/upload_file/upload_file.py
)
- [create_asset.py](/examples/python/src/utils/frontify_queries/create_asset/create_asset.py)


