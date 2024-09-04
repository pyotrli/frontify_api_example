from src.utils.graphql import gql

remove_tags_executor = gql("""
    mutation removeAssetTags($input:RemoveAssetTagsInput!) {
        removeAssetTags(input: $input){
            asset{
                tags{
                    value
                }
            }
        }
    }
""")