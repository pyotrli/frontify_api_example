# Frontify API Examples
A collection of Python scripts to showcase basic interactactions with Frontify's GraphQL API

### Disclaimer:
- This project is not an official Frontify product and is not affiliated with Frontify in any way

- This project includes zero test coverage

- The code in this repository is provided "as is", with all faults. There are no warranties or gauranteed, expressed or implied. The 
quality and maintenance of this repository is not guaranteed and
should be used for inspiration only and a way to get started quickly

Table of Contents
=================

  * [Getting Started](#Getting-Started)
  * [FrontifyClient](#FrontifyClient)
  * [Example Scripts](#Example-Scripts)
    * [File operations](##File-Operations)
        * [Upload an asset](###Upload-an-asset)
        * [Replace an asset](###Update-an-asset)
        * [Replace an asset](###Replace-an-asset)
        * [Replace an asset](###Delete-an-asset)
    * [Tags](##Tags)
        * [Add tags](###Add-tags)
        * [Remove tags](###Remove-tags)
    * [Metadata](##Metadata)
        * [Add metadata](###Add-metadata)
        * [Update metadata](###Update-metadata)
        * [Remove metadata](###Remove-metadata)

  * [License](/LICENSE)

# Getting Started
Make a copy of the `.env.example` file.

Change the filename to `.env`.

Add your security credentials to the `.env` file - this is ignored if using the gitignore included with this repository, and will ensure you do not commit secrets or other sensitive variables.

# FrontifyClient
FrontifyClient is an example GraphQL client for interacting with Frontify's public API. You can find the client code [here](/examples/python/src/services/FrontifyClient.py) and usage examples [here](/readme/FrontifyClient.md).

# Example Scripts
## File Operations
Scripts that interact with Assets.

### Upload an asset
Upload a file to Frontify using the [uploadFile](https://frontify.github.io/graphql-reference/mutations/uploadFile) and [createAsset](https://frontify.github.io/graphql-reference/mutations/createAsset) mutations.

It is recommended to check out the [developer documentation](https://developer.frontify.com/d/XFPCrGNrXQQM/graphql-api#/deep-dive/upload-file-create-asset) on how to upload an asset to Frontify before using this script.

- [Script](/examples/python/upload_frontify_asset.py)
- [Usage instructions](/readme/AssetUpload.md)

### Update an asset
Update asset information, including title, filename, description, copyright, expiry date and author. Uses the [updateAsset mutation](https://frontify.github.io/graphql-reference/mutations/updateAsset)

- [Script](/examples/python/update_frontify_asset.py)
- [Usage instructions](/readme/AssetUpdate.md)


### Replace an asset
Create a new asset revision by replacing the asset with the use of the [replaceAsset mutation](https://frontify.github.io/graphql-reference/mutations/replaceAsset)

- [Script](/examples/python/replace_frontify_asset.py)
- [Usage instructions](/readme/AssetReplacement.md)

### Delete an asset
Delete an asset from your Frontify instance using the [deleteAsset mutation](https://frontify.github.io/graphql-reference/mutations/deleteAsset).

- [Script](/examples/python/delete_frontify_asset.py)
- [Usage instructions](/readme/DeleteReplacement.md)

## Tags
Scripts that interact with Tags.

### Add tags
Add tags to an asset using the [addAssetTags mutation](https://frontify.github.io/graphql-reference/mutations/addAssetTags)

- [Script](/examples/python/replace_frontify_asset.py)
- [Usage instructions](/readme/AssetReplacement.md)

### Remove tages
Remove tags from an asset using the [removeAssetTags mutation](https://frontify.github.io/graphql-reference/mutations/removeAssetTags)

- [Script](/examples/python/replace_frontify_asset.py)
- [Usage instructions](/readme/AssetReplacement.md)

## Metadata
Scripts that interact with Mutations. 

Check out the [developer documentation on using custom metadata fields](https://developer.frontify.com/d/XFPCrGNrXQQM/graphql-api#/deep-dive/custom-metadata-1) and make sure you're familiar with the [metadata types](https://help.frontify.com/en/articles/4057240-metadata-and-tags-in-libraries#h_f4d37c46ec) available in Frontify.

### Add metadata

- [Script](/examples/python/replace_frontify_asset.py)
- [Usage instructions](/readme/AssetReplacement.md)
### Update metadata

- [Script](/examples/python/replace_frontify_asset.py)
- [Usage instructions](/readme/AssetReplacement.md)
### Remove metadata

- [Script](/examples/python/replace_frontify_asset.py)
- [Usage instructions](/readme/AssetReplacement.md)
