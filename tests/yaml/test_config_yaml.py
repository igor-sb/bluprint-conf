"""Test multiple YAML loading."""

import os
from pathlib import Path

from bluprint_conf.config import load_config_yaml, load_config_yamls


def test_load_configs():
    actual_config = load_config_yamls('tests/yaml/fixtures/confs')
    expected_config = load_config_yaml(
        'tests/yaml/snapshots/first_and_second.yaml',
    )
    assert actual_config == expected_config


def test_absolute_load_configs():
    current_dir = Path(os.getcwd())
    abs_cfg_path = current_dir / 'tests' / 'yaml' / 'fixtures' / 'confs'
    actual_config = load_config_yamls(abs_cfg_path)
    expected_config = load_config_yaml(
        'tests/yaml/snapshots/first_and_second.yaml',
    )
    assert actual_config == expected_config
