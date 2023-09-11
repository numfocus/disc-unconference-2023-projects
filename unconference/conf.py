import os

author = "NumFOCUS DISC Unconference 2023 attendees. Content is licensed under CC BY-SA 4.0 unless otherwise specified."
comments_config = {"hypothesis": False, "utterances": False}
exclude_patterns = ["**.ipynb_checkpoints", ".DS_Store", "Thumbs.db", "_build"]
extensions = [
    "sphinx_togglebutton",
    "sphinx_copybutton",
    "myst_nb",
    "jupyter_book",
    "sphinx_thebe",
    "sphinx_comments",
    "sphinx_external_toc",
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "sphinx_book_theme",
    "sphinx_jupyterbook_latex",
]
language = os.environ.get("WEBSITE_LANGUAGE", "en")
locale_dirs = ["../locales"]
gettext_uuid = True
gettext_compact = False
external_toc_exclude_missing = False
external_toc_path = "_toc.yml"
html_baseurl = ""
html_favicon = ""
html_logo = "images/logo.png"
html_sourcelink_suffix = ""
html_theme = "sphinx_book_theme"
html_show_copyright = False
html_theme_options = {
    "search_bar_text": "Search this book...",
    "launch_buttons": {
        "notebook_interface": "classic",
        "binderhub_url": "",
        "jupyterhub_url": "",
        "thebe": False,
        "colab_url": "",
    },
    "path_to_docs": "unconference",
    "repository_url": "https://github.com/numfocus/disc-unconference-2023-projects",
    "repository_branch": "main",
    "home_page_in_toc": True,
    "analytics": {"google_analytics_id": ""},
    "use_repository_button": True,
    "use_edit_page_button": False,
    "use_issues_button": True,
    "article_header_start": ["toggle-primary-sidebar", "version-switcher"],
    "switcher": {
        "json_url": "https://raw.githubusercontent.com/numfocus/disc-unconference-2023-projects/main/switcher.json",
        "version_match": language,
    },
}
html_title = "DISC Unconference 2023 Projects"
latex_engine = "pdflatex"
myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "linkify",
    "substitution",
    "tasklist",
]
myst_url_schemes = ["mailto", "http", "https"]
nb_execution_allow_errors = False
nb_execution_cache_path = ""
nb_execution_excludepatterns = []
nb_execution_in_temp = False
nb_execution_mode = "force"
nb_execution_timeout = 30
nb_output_stderr = "show"
numfig = True
pygments_style = "sphinx"
suppress_warnings = ["myst.domains"]
use_jupyterbook_latex = True
use_multitoc_numbering = True
