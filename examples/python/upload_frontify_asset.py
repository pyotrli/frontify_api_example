import os
from dotenv import load_dotenv
from src.services.FrontifyClient import FrontifyClient
from src.utils.frontify_queries.upload_file.upload_file import upload_file
from src.utils.frontify_queries.create_asset.create_asset import create_asset
from src.utils.base64tools import decode_base64_string


load_dotenv(override=True)
# security and other configuration headers
frontify_domain = os.getenv('frontify_domain')
frontify_access_token = os.getenv('frontify_access_token')
parent_id = os.getenv('frontify_project_id')

# configure Frontify Client
client = FrontifyClient(
    domain=frontify_domain,
    access_token=frontify_access_token,
    retries=3
    timeout_in_seconds=600  # create_asset mutation can take a long time for large files
)

# initiate file upload to Frontify and upload file in chunks
# see https://developer.frontify.com/document/1367#/deep-dive/upload-file-create-asset for deep dive
response = upload_file(client=client, filepath='demo_files/travel-walk.svg', filename='travel-walk.svg')

supported = response['filetype_supported']
fileid = response['file_id']
file_size = response['file_size_in_bytes']

# if filetype supported by Frontify library, proceed with replacing an asset on Frontify
if supported:
    try:
        assetId = create_asset(client=client, fileid=fileid, title="Example asset", parentid=project_id)
        decoded_asset_id = decode_base64_string(assetId)['identifier']
        print(f'successfully created asset at https://{frontify_domain}/screens/{decoded_asset_id}')
    except Exception as e:
        raise Exception(f'Failed to replace asset with error {e}')