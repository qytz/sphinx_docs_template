# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "sphinx_docs_template"
copyright = "2024, qytz"
author = "qytz"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    # "sphinxcontrib.apidoc",
    # "sphinx.ext.autodoc",
    # "sphinx.ext.autosummary",
    "autoapi.extension",
    "sphinxcontrib.mermaid",
    "sphinx_design",
    "sphinx_togglebutton",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "zh_CN"

# auto api options
autoapi_dirs = [""]

# latex pdf options for cjk
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    "papersize": "a4paper",
    # The font size ('10pt', '11pt' or '12pt').
    "pointsize": "10pt",
    # Additional stuff for the LaTeX preamble.
    "preamble": r"""
    \addto\captionsenglish{\renewcommand{\chaptername}{}}
    \usepackage[UTF8, scheme = plain]{ctex}
    """,
    # Latex figure (float) alignment
    "figure_align": "htbp",
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# html_style = "_static/basic_mod_extend.css"
html_css_files = [
    "css/basic_mod_extend.css",
]
# html_theme = "alabaster"
# html_theme = "shibuya"
# html_theme = "sphinx_rtd_theme"
# html_theme = "furo"
# html_theme = "piccolo_theme"
# html_theme = "pydata_sphinx_theme"
html_theme = "sphinx_book_theme"

html_static_path = ["_static"]
