from src.services.FrontifyClient import FrontifyClient
from src.utils.frontify_queries.add_tags.add_tags_executor import add_tags_executor


def add_tags(client: FrontifyClient, asset_id: str, tags: list) -> dict:
    tags = [{'value': tag} for tag in tags]
    data, errors = add_tags_executor(client, {
        'input': {
            'id': asset_id,
            'tags': tags
        }
    })

    if errors:
        raise Exception(f'Failed to add tags|Error: {errors}')

    return data['addAssetTags']['asset']['tags']