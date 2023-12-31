"""Test multiple YAML loading."""

from bluprint_conf.config import load_configs, load_config_yaml


def test_load_configs():
    expected_config = load_config_yaml(
        'tests/yaml/snapshots/first_and_second.yaml',
    )