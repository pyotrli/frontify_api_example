from src.services.FrontifyClient import FrontifyClient
from src.utils.frontify_queries.remove_tags.remove_tags_executor import remove_tags_executor


def remove_tags(client: FrontifyClient, asset_id: str, tags: list) -> dict:
    tags = [{'value': tag} for tag in tags]
    data, errors = remove_tags_executor(client, {
        'input': {
            'id': asset_id,
            'tags': tags
        }
    })

    if errors:
        raise Exception(f'Failed to add tags|Error: {errors}')

    return data['removeAssetTags']['asset']['tags']