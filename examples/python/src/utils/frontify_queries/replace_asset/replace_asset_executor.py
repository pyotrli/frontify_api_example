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
