import os
from dotenv import load_dotenv
from src.services.FrontifyClient import FrontifyClient
from src.utils.frontify_queries.delete_asset.delete_asset import delete_asset
from src.utils.base64tools import encode_obj_to_base64

load_dotenv(override=True)
# security and other configuration headers
frontify_domain = os.getenv('frontify_domain')
frontify_access_token = os.getenv('frontify_access_token')
asset_id = 12345  # get this ID from url of asset or via API
asset_id = encode_obj_to_base64(asset_id, 'asset')

# configure Frontify Client
client = FrontifyClient(
    domain=frontify_domain,
    access_token=frontify_access_token,
    retries=3
)

# delete asset on Frontify
try:
    data = delete_asset(client=client, asset_id=asset_id)
    print(f'successfully added tags to asset: {data}')
except Exception as e:
    raise Exception(f'Failed to add tags to asset with error {e}')