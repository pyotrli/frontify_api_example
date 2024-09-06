from src.utils.graphql import gql

add_tags_executor = gql("""
    mutation addAssetTags($input:AddAssetTagsInput!) {
        addAssetTags(input: $input){
            asset{
                tags{
                    value
                }
            }
        }
    }
""")