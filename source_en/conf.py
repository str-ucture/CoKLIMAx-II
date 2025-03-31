# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CoKLIMAx'
copyright = '2024, str.ucture GmbH'
author = 'str.ucture GmbH'
release = '1.0.0'
 
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_copybutton',
    'myst_nb',
    'nbsphinx',
    'sphinx_new_tab_link',
    # "sphinx.ext.mathjax",
    # 'sphinx_intl'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# html_theme_options = {
    # 'logo_only': False,
    # 'prev_next_buttons_location': 'bottom',
    # 'style_external_links': False,
    # 'vcs_pageview_mode': '',
    # 'flyout_display': 'hidden',
    # 'version_selector': True,
    # 'language_selector': True,
    # # Toc options
    # 'collapse_navigation': False,
    # 'sticky_navigation': True,
    # 'navigation_depth': 1,
    # 'includehidden': True,
    # 'titles_only': False
# }

html_css_files = ['css/custom.css']
html_logo = "_static/logos/coklimax_logo_new.png"

language='en'