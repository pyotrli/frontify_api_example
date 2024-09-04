import os
from dotenv import load_dotenv
from src.services.FrontifyClient import FrontifyClient
from src.utils.frontify_queries.remove_tags.remove_tags import remove_tags
from src.utils.base64tools import encode_obj_to_base64

load_dotenv(override=True)
# security and other configuration headers
frontify_domain = os.getenv('frontify_domain')
frontify_access_token = os.getenv('frontify_access_token')
asset_id = 550435  # get this ID from url of asset or via API
asset_id = encode_obj_to_base64(asset_id, 'asset')

# configure Frontify Client
client = FrontifyClient(
    domain=frontify_domain,
    access_token=frontify_access_token,
    retries=3
)

# add tags to asset on Frontify
tags = ['tag1', 'tag2', 'tag3']
try:
    data = remove_tags(client=client, asset_id=asset_id, tags=tags)
    print(f'successfully removed tags to asset: {data}')
except Exception as e:
    raise Exception(f'Failed to remove tags to asset with error {e}')