"""Tests for package paths."""

import os
from pathlib import Path

from bluprint_conf.config import absolute_path_in_project


def test_absolute_path_in_project():
    assert absolute_path_in_project('tests') == Path(os.getcwd()) / 'tests'
