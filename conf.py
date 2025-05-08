# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GREM Schulprogramm'
copyright = '2025, Prof. Dr. Dennis Müller'
author = 'Prof. Dr. Dennis Müller'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 
              'sphinx.ext.autodoc', 
              'sphinx.ext.autosummary', 
              'sphinx.ext.intersphinx',
              'sphinx.ext.viewcode',
              'sphinxcontrib.mermaid',
              'sphinx.ext.mathjax',
              'sphinx_togglebutton']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

suppress_warnings = [
    "myst.xref_missing",
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

language = 'de'

html_theme_options = {
    "navigation_depth": 3,
    'collapse_navigation': False
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'canonical_url': '',
}
