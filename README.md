![bluprint_conf logo](docs/source/images/bluprintconf_logo.png)

# Bluprint_conf

Bluprint_conf is a Python package for loading YAML configurations in your Python
code or Jupyter notebooks, that automatically resolves YAML file paths, so
there is no need to think about absolute or relative paths. Bluprint_conf is a 
light wrapper around [OmegaConf](https://omegaconf.readthedocs.io/en/)

## Installation

Bluprint_conf is automatically added and installed by Bluprint, but if you wish
to use it as a standalone package, it can be installed with:

```sh
pip install bluprint_conf
```

## Usage

Bluprint_conf assumes you have a Python project setup in this type of
"cookiecutter" structure (generated by Bluprint):

```
	my_project
	├── conf
	│   └── config.yaml
	├── data
	│   └── table.csv
	├── notebooks
	│   └── notebook.ipynb
	├── my_project
	│   └── code.py
	└── pyproject.toml
```

where `config.yaml` configuration lives in another folder, separate from any
Python code or notebooks. 

Previously, loading `config.yaml` would require annoyances such as:

- `../../conf/config.yaml` from `code.py`
- `../conf/config.yaml` from `notebook.ipynb`
- `/absolute/path/to/my_project/conf/config.yaml`

which are hard to maintain, need to be updated if we decide to reorganize the 
code in different folders and becomes a mess if we try to share the project.

With Bluprint_conf, you install your `my_project` locally as an editable
package and access `config.yaml` as simple as this in Python scripts:

```py
from bluprint_conf import load_config_yaml
cfg = load_config_yaml()  # default loads: conf/config.yaml
```

To install your project `my_project` as an editable package, Bluprint uses
[PDM](https://pdm-project.org/latest/), but if you want to use this standalone,
run `pip install -e .` in your project folder.
