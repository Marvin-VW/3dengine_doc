from template_project_python import __version__

import os
import sys
sys.path.insert(0, os.path.abspath('.'))


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

html_theme = "sphinx_rtd_theme"

master_doc = "index"
project = "3D Engine Python"
copyright = "2024, Marvin-VW"
author = "Marvin Lorenz"
version = release = __version__
