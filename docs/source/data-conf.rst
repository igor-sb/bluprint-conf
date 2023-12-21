Data configuration
------------------

Bluprint_conf provides a simple way to read and write data from various sources
in your project. For example, lets say you are working on an analysis in a
notebook. For your analysis you need multiple files, some are stored locally
inside your project folders, some are outside, and some may be accessible only
remotely. Again, assuming your project follows a cookiecutter structure::

	my_project
	├── conf
	│   └── data.yaml
	├── data
	│   ├── input
	│   │   └── input_table.csv
	│   ├── output
	│   │   └── output_table.csv
	│   └── metadata.csv
	...

and say you need another file *manifest.csv* from an S3 bucket as
well as *global_config.csv* stored somewhere outside of your project. Then the
corresponding ``data.yaml`` file used with Bluprint would look like this:

.. code-block:: yaml

	input:
	  tab1: 'input/input_table1.csv'
	output:
	  tab1: 'output/output_table1.csv'
	manifest: 's3://bucket/path/to/manifest.csv'
	metadata: 'metadata.csv'
	global_cfg: '/path/to/global_config.csv'
	  

By default, bluprint_conf ``load_data_yaml()``:

* resolves relative paths relative to ``my_project/data`` (data directory can
  be changed usig ``data_dir`` argument)

* leaves absolute paths unchanged

* leaves URIs unchanged (e.g. web links, S3 buckets, ...)

For example:

.. code-block:: python

	from bluprint_conf import load_data_yaml
	data = load_data_yaml()
	print(data)

.. code-block::

	{
	  'input': {
	    'tab1': '/path/to/my_project/data/input/input_table1.csv'
	  },
	  'output': {
	    'tab1': '/path/to/my_project/data/output/output_table1.csv'
	  }, 
	  'manifest': 's3://bucket/path/to/manifest.csv',
	  'metadata': '/path/to/my_project/data/metadata.csv',
	  'global_cfg': '/path/to/global_config.csv'
	}

The ``data`` OmegaConf dict is then used like this:

.. code-block:: python

	import pandas as pd

	df = pd.read_csv(data['input']['tab1'])
	# or using dot notation
	df = pd.read_csv(data.input.tab1)

The main difference between ``load_config_yaml()`` and ``load_data_yaml()`` is
that ``load_data_yaml()`` does this additional parsing of relative paths.

.. note::
	See `OmegaConf usage <https://omegaconf.readthedocs.io/en/2.3_branch/usage.html#access-and-manipulation>`_ 
	for further information how to handle OmegaConf dicts.