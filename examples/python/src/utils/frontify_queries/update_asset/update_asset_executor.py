from src.utils.graphql import gql

update_asset_executor = gql("""
    mutation UpdateAsset($input: UpdateAssetInput!) {
        updateAsset(input: $input) {
            asset {
            modifiedAt
            }
        }
    }
""")