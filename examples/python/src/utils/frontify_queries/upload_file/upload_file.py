from src.services.FrontifyClient import FrontifyClient
from src.utils.files import get_file_size_in_bytes, read_file_in_chunks
from src.utils.frontify_queries.upload_file.upload_file_executor import upload_file_executor


CHUNK_SIZE_IN_BYTES = 200 * 1024 * 1024  # 200MB chunks when uploading to Frontify


def upload_file(client: FrontifyClient, filepath: str, filename: str) -> dict:
    file_size = get_file_size_in_bytes(filepath)
    if file_size == 0:
        raise Exception('file size is zero')
    data, errors = upload_file_executor(client, {
        'input': {
            'filename': filename,
            'size': file_size,
            'chunkSize': CHUNK_SIZE_IN_BYTES
        }
    })

    if errors:
        raise Exception(f'Failed to upload file|Error: {errors}')

    for (index, chunk) in read_file_in_chunks(filepath, CHUNK_SIZE_IN_BYTES):
        url = data['uploadFile']['urls'][index]
        client.upload_chunk(url, chunk)

    return {
        'filetype_supported': True,
        'file_id': data['uploadFile']['id'],
        'file_size_in_bytes': file_size
    }
