"""Code for manipulating YAML configuration files."""

from pathlib import Path

from importlib_resources import files
from omegaconf import DictConfig, ListConfig, OmegaConf

from bluprint_conf.iterdir import find_yaml_files_in_dir


def load_config_yaml(
    config_file: str | Path = 'conf/config.yaml',
    use_package_path_for_config: bool = True,
) -> DictConfig | ListConfig:
    """Load project configuration yaml

    Parses relative paths and opens yaml configuration using OmegaConf.

    Args:
        config_file (str | Path, optional): Relative or absolute path to the
          yaml configuration.

        use_package_path_for_config (bool, optional): If this is True, then
          relative path of `config_file` is parsed with respect to the project
          root and not with respect to the path of the calling script.

    Returns:
        DictConfig | ListConfig: Return value of OmegaConf.create().
    """
    if not Path(config_file).is_absolute() and use_package_path_for_config:
        config_file = absolute_path_in_project(config_file)
    return OmegaConf.load(config_file)


def absolute_path_in_project(path_to_file: str | Path) -> Path:
    """Returns absolute path to a file in a Bluprint project

    Args:
        path_to_file (str | Path): Relative path to a file.

    Returns:
        Path: pathlib Path object specifying the absolute path to file.
    """
    dir_name = str(Path(path_to_file).parent)
    if dir_name == '.':
        return Path(files(path_to_file).joinpath('_').parent)
    dir_as_module = dir_name.strip('/').replace('/', '.')
    file_basename = Path(path_to_file).name
    return Path(files(dir_as_module).joinpath(file_basename))


def load_config_yamls(
    config_dir: str | Path,
    use_package_path_for_config: bool = True,
) -> DictConfig | ListConfig:
    """Load multiple yamls into a single config

    Recursively iterates `config_dir`, loading all .yaml and .yml files, then
    merges them all into a single OmegaConf dictionary.

    Args:

        config_dir (str | Path): Directory with one or more yaml files.

        use_package_path_for_config (bool, optional): If this is True,
          then relative paths are parsed with respect to the project root and
          not with respect to the path of the calling script.

    Returns:
    
        DictConfig | ListConfig: Return value of OmegaConf.create().
    """
    if not Path(config_dir).is_absolute() and use_package_path_for_config:
        config_dir = absolute_path_in_project(config_dir)
    yaml_files = find_yaml_files_in_dir(config_dir)
    configs = [
        load_config_yaml(yaml_file, use_package_path_for_config)
        for yaml_file in yaml_files
    ]
    return OmegaConf.unsafe_merge(*configs)
