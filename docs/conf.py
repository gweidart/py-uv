import os
import sys

sys.path.insert(0, os.path.abspath('..'))

project = 'Astral\'s uv Python API'
project_copyright = '2024, @gweidart'
author = '@gweidart'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'
html_static_path = ['_static']
