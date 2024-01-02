"""Test multiple YAML loading."""

from bluprint_conf.config import load_config_yaml, load_configs


def test_load_configs():
    actual_config = load_configs('tests/yaml/fixtures/confs')
    expected_config = load_config_yaml(
        'tests/yaml/snapshots/first_and_second.yaml',
    )
    assert actual_config == expected_config
