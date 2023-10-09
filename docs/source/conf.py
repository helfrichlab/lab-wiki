# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lab Wiki'
copyright = '2022, Helfrich Lab'
author = 'Helfrich Lab'

release = '0.1'
version = '0.1.0'

# -- General configuration

import sphinx_rtd_theme

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "collapse_navigation" : True
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
