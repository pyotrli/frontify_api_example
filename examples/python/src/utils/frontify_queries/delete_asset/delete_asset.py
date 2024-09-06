from src.services.FrontifyClient import FrontifyClient
from src.utils.frontify_queries.delete_asset.delete_asset_executor import delete_asset_executor

def delete_asset(client: FrontifyClient, asset_id: str) -> dict:
    data, errors = delete_asset_executor(client, {
        'input': {
            'id': asset_id
        }
    })

    if errors:
        raise Exception(f'Failed to delete asset|Error: {errors}')

    return data['deleteAsset']