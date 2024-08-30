import os
from typing import Generator, Tuple

KILOBYTE = 1024
MEGABYTE = 1024 * 1024


def get_file_size_in_bytes(filepath: str) -> int:
    return os.path.getsize(filepath)


def read_file_in_chunks(filepath: str, chunk_size: int) -> Generator[Tuple[int, any], None, None]:
    with open(filepath, mode='rb') as file:
        index = 0
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            yield index, data
            index += 1
