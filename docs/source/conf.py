# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Python OC Lettings site"
copyright = "2023, Aurel"
author = "Aurel"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
import os, sys
# from ...oc_lettings_site import settings

# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
# import django
# django.setup()

sys.path.insert(0, os.path.abspath(".."))

# sys.path.insert(0, os.path.abspath("..oc_lettings_site/"))
# sys.path.insert(0, os.path.abspath("..lettings/"))
# sys.path.insert(0, os.path.abspath("..profiles/"))

extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
