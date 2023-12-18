"""Code for manipulating YAML configuration files."""

from importlib import resources
from pathlib import Path, PurePath
from typing import Any
from urllib.parse import urlparse

from omegaconf import DictConfig, ListConfig, OmegaConf


def add_prefix_to_nested_config(
    conf: DictConfig | ListConfig,
    prefix: str,
) -> DictConfig | ListConfig:

    def recurse_or_add_suffix(conf_value: Any) -> Any:  # noqa: WPS430
        if isinstance(conf_value, DictConfig | ListConfig):
            return add_prefix_to_nested_config(conf_value, prefix)
        if _is_abs_path(conf_value) or _is_uri(conf_value):
            return conf_value
        return str(Path(prefix) / str(conf_value))

    if isinstance(conf, ListConfig):
        return OmegaConf.create([
            recurse_or_add_suffix(conf_value)
            for conf_value in conf
        ])
    elif isinstance(conf, DictConfig):
        return OmegaConf.create({
            conf_key: recurse_or_add_suffix(conf_values)
            for conf_key, conf_values in conf.items()
        })


def _is_abs_path(conf_value: Any) -> bool:
    return PurePath(str(conf_value)).is_absolute()


def _is_uri(conf_value: Any) -> bool:
    parsed_url = urlparse(str(conf_value))
    return all([parsed_url.scheme, parsed_url.netloc])


def load_data_yaml(
    config_file: str | Path = 'conf/data.yaml',
    data_dir: str = 'data',
) -> DictConfig | ListConfig:
    conf = load_config_yaml(config_file)
    data_path = str(resources.files(data_dir).joinpath(''))
    return add_prefix_to_nested_config(conf, prefix=data_path)


def absolute_package_path(filename: str | Path) -> Path:
    dir_name = str(Path(filename).parent)
    dir_as_module = dir_name.strip('/').replace('/', '.')
    file_basename = Path(filename).name
    return (
        resources.files(dir_as_module).joinpath(file_basename)  # type: ignore
    )


def load_config_yaml(
    config_file: str | Path = 'conf/config.yaml',
    use_package_path: bool = True,
) -> DictConfig | ListConfig:
    if not Path(config_file).is_absolute() and use_package_path:
        config_file = absolute_package_path(config_file)
    return OmegaConf.load(config_file)
