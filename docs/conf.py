import alabaster

html_theme = "alabaster"
extensions = ["alabaster", "myst_parser"]

source_suffix = [".rst", ".md"]

master_doc = "index"
project = "cornerstone"

# These folders are copied to the documentation's HTML output
html_static_path = ["_static"]

# These paths are relative to html_static_path
html_css_files = [
    # local path to css...
]

html_logo = "_static/logo.png"
html_theme_options = {
    "logo": "logo.png",
    "github_user": "kraymer",
    "github_repo": "cornerstone",
}

# Custom sidebar templates, maps document names to template names.
templates_path = ["_templates"]
html_sidebars = {
    "**": [
        "sidebarintro.html",
    ]
}
