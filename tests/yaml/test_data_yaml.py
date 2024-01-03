"""Test data.yaml loading with file parsing."""

import os

from pathlib import Path

from bluprint_conf.config import load_config_yaml
from bluprint_conf.data import (
    add_prefix_to_nested_config,
    load_data_yaml,
    load_data_yamls,
)


def test_add_prefix_to_nested_config():
    actual_test_config = load_config_yaml('tests/yaml/fixtures/test.yaml')
    actual_test_config = add_prefix_to_nested_config(
        actual_test_config,
        prefix='/xyz/',
    )
    expected_test_config = load_config_yaml(
        'tests/yaml/snapshots/prefixed_test.yaml',
    )
    assert dict(actual_test_config) == dict(expected_test_config)


def test_load_data_yaml():
    current_dir = Path(os.getcwd())
    expected_data = {
        'test_data': {
            'absolute': '/a/3a.bin',
            'relative_with_subdir': f'{current_dir}/tests/fixtures/3b/3b2.csv',
            'relative_simple': f'{current_dir}/tests/fixtures/3c.jpeg',
            's3_uri': 's3://example-bucket/path/to/object',
        },
    }
    data = load_data_yaml(
        'tests/yaml/fixtures/data.yaml',
        data_dir='tests/fixtures',
    )
    assert data == expected_data
