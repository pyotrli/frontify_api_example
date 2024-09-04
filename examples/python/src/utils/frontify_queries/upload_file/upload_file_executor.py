from src.utils.graphql import gql

upload_file_executor = gql("""
    mutation UploadFile($input: UploadFileInput!) {
        uploadFile(input: $input) {
            id
            urls
        }
    }
""")
