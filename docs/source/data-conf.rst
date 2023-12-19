Data configuration
------------------

Bluprint_conf provides a simple way to read and write data from various sources
in your project. For example if this is your project tree::

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

and say you need another file ``manifest.csv`` which is stored in an S3 bucket as
well as ``global_config.csv`` stored somewhere outside of your project. Then the
corresponding yaml file could be:

.. code-block:: yaml

	input:
	  tab1: 'input/input_table1.csv'
	output:
	  tab1: 'output/output_table1.csv'
	manifest: 's3://bucket/path/to/manifest.csv'
	metadata: 'metadata.csv'
	global_cfg: '/path/to/global_config.csv'
	  

By default, bluprint_conf ``load_data_yaml()`` parses this yaml such as:

- relative paths are taken with respect to ``my_project/data`` (data directory can be changed usig ``data_dir`` argument)

- absolute paths are unchanged

- URIs are unchanged (e.g. web links, S3 buckets, ...)

For example:

.. code-block:: python

	from bluprint_conf import load_data_yaml
	data = load_data_yaml()
	print(data)

.. code-block::

	{
	  'input': {
	    'tab1': '/path/to/my_project/input/input_table1.csv'
	  },
	  'output': {
	    'tab1': '/path/to/my_project/output/output_table1.csv'
	  }, 
	  'manifest': 's3://bucket/path/to/manifest.csv',
	  'metadata': '/path/to/my_project/metadata.csv',
	  'global_cfg': '/path/to/global_config.csv'
	}

The ``data`` OmegaConf dict can be used in place of file paths:

.. code-block:: python

	import pandas as pd

	df = pd.read_csv(data['input']['tab1'])
	# or using dot notation
	df = pd.read_csv(data.input.tab1)

See `OmegaConf usage <https://omegaconf.readthedocs.io/en/2.3_branch/usage.html#access-and-manipulation>`_
for further information how to handle OmegaConf dicts.