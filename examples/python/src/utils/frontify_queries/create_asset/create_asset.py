import os

from src.services.FrontifyClient import FrontifyClient
from src.utils.frontify_queries.create_asset.create_asset_executor import (
    create_asset_executor,
)


def create_asset(
    client: FrontifyClient,
    parentid: str,
    fileid: str,
    title: str = None,
    filename: str = None,
    directory: str = None, # directory path in the format "folder1/folder2"
    description: str = "",
    author: str = "",
    copyright: str = None,
    copyright_notice: str = None,
    tags: list = None,
    expires_at: str = None,
    externalId: str = "",
    skip_exif: bool = True,
) -> str:
    """

    :rtype: object
    """
    if filename is None and title is None:
        raise ValueError("Either 'filename' or 'title' must be provided.")
    
    create_asset_input = {
        "input": {
            "parentId": parentid,
            "fileId": fileid,
            "externalId": externalId,
            "title": title,
            "author": author,
            "description": description,
            "skipFileMetadata": skip_exif,
        }
    }

    # TODO: find more elegant way of constructing copyright var
    # Copyright status may either be "UNKNOWN", "COPYRIGHTED", "PUBLIC"
    # If no status provided, default to "UNKNOWN", otherwise the notice will not be shown
    if copyright or copyright_notice:
        if copyright is None:
            copyright = {"status": "UNKNOWN", "notice": copyright_notice}
        elif copyright_notice is None:
            copyright = {"status": copyright, "notice": ""}
        else:
            copyright = {"status": copyright, "notice": copyright_notice}

        create_asset_input["input"]["copyright"] = copyright

    if tags is not None:
        tags = [{"value": tag} for tag in tags]
        create_asset_input["input"]["tags"] = tags

    if directory is not None:
        directory = []
        for folder_name in directory.split("/"):
            folder_name = folder_name.strip()
            directory.append(folder_name)
        create_asset_input["input"]["directory"] = directory

    # if no title provided - use filename
    if title is None:
        filename_no_ext, extension = os.path.splitext(filename)
        create_asset_input["input"]["title"] = filename_no_ext

    if expires_at is not None:
        # Frontify's expected date format: 2019-12-17T11:36:05+01:00
        create_asset_input["input"]["expiresAt"] = expires_at

    data, errors = create_asset_executor(client, create_asset_input)

    if errors:
        raise Exception(f"Failed to create asset|Error: {errors}")

    return data["createAsset"]["job"]["assetId"]
