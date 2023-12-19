.. image:: docs/source/images/bluprintconf_logo.png

Bluprint_conf
=============

Bluprint_conf is a Python package for loading YAML configurations in your Python
code or Jupyter notebooks, that automatically resolves YAML file paths, so
there is no need to think about absolute or relative paths. Bluprint_conf is a 
light wrapper around `OmegaConf <https://omegaconf.readthedocs.io/en/>`_ .

Installation
------------

Bluprint_conf is automatically added and installed by Bluprint, but if you wish
to use it as a standalone package, it can be installed with:

.. code-block:: bash

   pip install bluprint_conf


Usage
-----

.. code-block:: python

	from bluprint_conf import load_config_yaml
	cfg = load_config_yaml()  # by default loads: conf/config.yaml
