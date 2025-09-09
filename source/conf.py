from pygments.lexers.smv import NuSMVLexer
from sphinx.highlighting import lexers

import os
import sys

sys.path.insert(0, os.path.abspath('_ext'))

# Lexer configuration
lexers['smv'] = NuSMVLexer()
pygments_style = "vs"

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'HyperQB'
copyright = '2025, TART @ MSU'
author = 'TART @ MSU'
release = '2.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_title = "HyperQB"
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#4CAF50",
        "color-brand-content": "#388E3C",
    },
    "dark_css_variables": {
        "color-brand-primary": "#81C784",
        "color-brand-content": "#C8E6C9",
    },
}
html_static_path = ['_static']
html_css_files = ['custom.css']

mathjax3_config = {
    "tex": {
        "macros": {
            "llbracket": r"{\lbrack\!\lbrack}",
            "rrbracket": r"{\rbrack\!\rbrack}",
        }
    }
}

extensions = [
    'sphinx.ext.mathjax',
    'sphinx_tabs.tabs',
    'hyperltl_ext',
    'sphinx_design'
]