# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "ECoG tutorials"
copyright = "CC BY"
author = "Zaid Zada"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "nbsphinx",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
# html_logo = "_static/logo.png"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

# -- Options for alabaster -------------------------------------------------
# https://alabaster.readthedocs.io/en/latest/customization.html
html_theme_options = {
    "logo": "logo.png",
    "github_user": "hassonlab",
    "github_repo": "podcast-ecog-tutorials",
}


# -- Options for nbsphinx -------------------------------------------------
nbsphinx_execute = "never"
nbsphinx_assume_equations = False
