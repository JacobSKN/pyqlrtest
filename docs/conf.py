# Configuration file for the Sphinx documentation builder.
import os
import sys
sys.path.insert(0, os.path.abspath('../..')) # Adjust if your package is elsewhere

project = 'pyqlrtest'
copyright = '2025, Jacob Schildknecht/ZEW' # Update this
author = 'Jacob Schildknecht/ZEW' # Update this


try:
    from qlrtest import __version__ as release
except ImportError:
    release = '0.1.0'


extensions = [
    'sphinx.ext.autodoc',      # Include documentation from docstrings
    'sphinx.ext.napoleon',     # Support for NumPy and Google style docstrings
    'sphinx.ext.intersphinx',  # Link to other projects' documentation
    'sphinx.ext.viewcode',     # Add links to source code
    'sphinx.ext.githubpages',  # Helps with GitHub Pages publishing
    'myst_parser',             # For Markdown support
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# HTML output settings
html_theme = 'alabaster' # or 'sphinx_rtd_theme'
# html_static_path = ['_static'] # if you have static files

# Autodoc settings
autodoc_member_order = 'bysource'

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https.docs.python.org/3', None),
    'numpy': ('https.numpy.org/doc/stable/', None),
    'scipy': ('https.docs.scipy.org/doc/scipy/', None),
    'statsmodels': ('https.www.statsmodels.org/stable/', None),
    'pandas': ('https.pandas.pydata.org/pandas-docs/stable/', None),
}

# MyST Parser settings (if using Markdown)
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}