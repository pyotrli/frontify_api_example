from src.utils.graphql import gql

create_asset_executor = gql("""
    mutation CreateAsset($input: CreateAssetInput!) {
        createAsset(input: $input) {
            job {
                assetId
            }
        }
    }
""")