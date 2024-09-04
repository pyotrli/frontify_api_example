import os
from dotenv import load_dotenv
from src.services.FrontifyClient import FrontifyClient
from src.utils.base64tools import encode_obj_to_base64
from src.utils.frontify_queries.upload_file.upload_file import upload_file
from src.utils.frontify_queries.replace_asset.replace_asset import replace_asset


load_dotenv(override=True)
# security and other configuration headers
frontify_domain = os.getenv('frontify_domain')
frontify_access_token = os.getenv('frontify_access_token')
asset_id_to_replace = 550435  # get this ID from url of asset or via API
asset_id_to_replace_encoded = encode_obj_to_base64(asset_id_to_replace, 'asset')

# configure Frontify Client
client = FrontifyClient(
    domain=frontify_domain,
    access_token=frontify_access_token,
    retries=3
)


# initiate file upload to Frontify and upload file in chunks
# see https://developer.frontify.com/document/1367#/deep-dive/upload-file-create-asset for deep dive
response = upload_file(client=client, filepath='demo_files/travel-walk.svg', filename='travel-walk.svg')

supported = response['filetype_supported']
file_id = response['file_id']
file_size = response['file_size_in_bytes']

# if filetype supported by Frontify library, proceed with replacing an asset on Frontify
if supported:
    try:
        data = replace_asset(client=client, asset_id=asset_id_to_replace_encoded, file_id=file_id)
        asset_url = f'{frontify_domain}/screens/{asset_id_to_replace}'
        print(f'successfully replaced asset: {asset_url}')
    except Exception as e:
        raise Exception(f'Failed to replace asset with error {e}')
