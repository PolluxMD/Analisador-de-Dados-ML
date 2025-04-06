# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Analisador de Dados ML'
copyright = '2025, Erick Zimmermann 2314290003'
author = 'Erick Zimmermann 2314290003'
release = '15/04'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # Para suporte ao estilo de docstrings Google/Numpy

]

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))


templates_path = ['_templates']
exclude_patterns = []

language = 'Pt-br'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
