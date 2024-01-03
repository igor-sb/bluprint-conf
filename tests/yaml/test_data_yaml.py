"""Test data.yaml loading with file parsing."""

from bluprint_conf.config import load_config_yaml
from bluprint_conf.data import add_prefix_to_nested_config


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
