from src.utils.graphql import gql

delete_asset_executor = gql("""
    mutation deleteAsset($input: DeleteAssetInput!) {
        deleteAsset(input: $input) {
            id
        }
    }
""")