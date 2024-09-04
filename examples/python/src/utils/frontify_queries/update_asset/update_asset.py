from dataclasses import dataclass, asdict
from typing import Optional
from src.services.FrontifyClient import FrontifyClient
from src.utils.frontify_queries.update_asset.update_asset_executor import update_asset_executor

@dataclass(frozen=True)
class Copyright:
    status: Optional[str]
    notice: Optional[str]

@dataclass(frozen=True)
class AssetData:
    title: Optional[str] = None
    description: Optional[str] = None
    filename: Optional[str] = None
    expiresAt: Optional[str] = None #must be in Frontify's expected date format: 2019-12-17T11:36:05+01:00
    author: Optional[str] = None
    copyright: Optional[Copyright] = None

def update_asset(client: FrontifyClient, asset_id: int, asset_data: AssetData  ) -> dict:
    asset_data = {key: value for key, value in asdict(asset_data).items() if value is not None}
    data, errors = update_asset_executor(client, {
        'input': {
            'id': asset_id,
            'data': asset_data
        }
    })

    if errors:
        raise Exception(f'Failed to update asset|Error: {errors}')

    return data['updateAsset']['asset']['modifiedAt']