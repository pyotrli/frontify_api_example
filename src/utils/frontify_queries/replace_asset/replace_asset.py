from src.services.FrontifyClient import FrontifyClient
from src.utils.frontify_queries.replace_asset.replace_asset_executor import replace_asset_executor


def replace_asset(client: FrontifyClient, asset_id: str, file_id: str) -> str:
    replace_asset_input = {
        "input": {
            "assetId": asset_id,
            "fileId": file_id
        }
    }

    data, errors = replace_asset_executor(client, replace_asset_input)

    if errors:
        raise Exception(f'Failed to replace asset|{errors}')

    else:
        return data
