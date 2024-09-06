import os
from dotenv import load_dotenv
from src.services.FrontifyClient import FrontifyClient
from src.utils.frontify_queries.update_asset.update_asset import update_asset, AssetData
from src.utils.base64tools import encode_obj_to_base64

load_dotenv(override=True)
# security and other configuration headers
frontify_domain = os.getenv('frontify_domain')
frontify_access_token = os.getenv('frontify_access_token')

# configure Frontify Client
client = FrontifyClient(
    domain=frontify_domain,
    access_token=frontify_access_token,
    retries=3
)

assetUpdateData = AssetData(
    title="New Asset Title"
)

# AssetData mimics the UpdateAssetDataInput type in the Frontify API https://frontify.github.io/graphql-reference/type/UpdateAssetDataInput
# All fields are optional

asset_id = encode_obj_to_base64(12345, "asset")

try:
    response  = update_asset(client=client, asset_id=asset_id, asset_data=assetUpdateData)
    print(f'Asset updated at {response}')
except Exception as e:
    raise Exception(f'Failed to update asset with error {e}')