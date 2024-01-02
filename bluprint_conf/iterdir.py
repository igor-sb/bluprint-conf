"""Code for iterating directory for yaml files."""

import os
from pathlib import Path


def find_yaml_files_in_dir(
    index_dir: str | Path,
) -> list[Path]:
    indexed_files = []
    for root, _, indexed_file_list in os.walk(index_dir):
        for indexed_file in indexed_file_list:  # noqa: WPS110
            indexed_file_with_path = Path(root) / indexed_file
            if indexed_file.endswith('.yaml') or indexed_file.endswith('.yml'):
                indexed_files.append(indexed_file_with_path)
    indexed_files.sort()
    return indexed_files
