import os
from pathlib import Path


def find_yaml_files_in_dir(
    index_dir: str | Path,
) -> list[tuple[str, ...]]:
    indexed_files = []
    for root, _, files in os.walk(index_dir):
        for file in files:  # noqa: WPS110
            file_path = Path(root) / file
            if file.endswith('.yaml') or file.endswith('.yml'):
                indexed_files.append(
                    file_path.parts[len(Path(index_dir).parts):],
                )
    return sorted(indexed_files)
