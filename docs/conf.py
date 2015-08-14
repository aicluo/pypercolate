# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import importlib
import inspect
from sphinx import apidoc


# Are we building on ReadTheDocs?
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'


# mock modules for Read the Docs
# http://read-the-docs.readthedocs.org/en/latest/faq.html#i-get-import-errors-on-libraries-that-depend-on-c-modules
from unittest.mock import MagicMock

class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        return Mock()

MOCK_MODULES = ['numpy', 'scipy', 'scipy.stats', 'matplotlib', 'networkx', ]
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

import alabaster

__location__ = os.path.join(os.getcwd(), os.path.dirname(
    inspect.getfile(inspect.currentframe())))

package = "percolate"
namespace = []
root_pkg = namespace[0] if namespace else package
namespace_pkg = ".".join([namespace[-1], package]) if namespace else package
output_dir = os.path.join(__location__, "../docs/reference")
module_dir = os.path.join(__location__, "..", root_pkg)
cmd_line_template = "sphinx-apidoc -f -o {outputdir} {moduledir} {moduledir}/test"
cmd_line = cmd_line_template.format(outputdir=output_dir, moduledir=module_dir)
apidoc.main(cmd_line.split(" "))

# convert tutorial to rst
import subprocess

IPYTHON = (
    'ipython' if not on_rtd
    else
    '/home/docs/checkouts/readthedocs.org/user_builds/pypercolate/envs/latest/bin/ipython3'
)

subprocess.call(
    "{} nbconvert --to rst tutorial-bond-square-lattice.ipynb".format(IPYTHON),
    shell=True
)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.3'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.todo',
              'sphinx.ext.autosummary', 'sphinx.ext.viewcode', 'sphinx.ext.coverage',
              'sphinx.ext.doctest', 'sphinx.ext.ifconfig',
              'sphinx.ext.mathjax', 'sphinxcontrib.bibtex',
              'sphinx.ext.napoleon',
              'IPython.sphinxext.ipython_console_highlighting',
              'IPython.sphinxext.ipython_directive',
              'releases',
              'alabaster',
              ]

todo_include_todos = True

releases_github_path = 'andsor/pypercolate'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'pypercolate'
copyright = u'2014--2015, Andreas Sorge'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''  # Is set by calling `setup.py docs`
# The full version, including alpha/beta/rc tags.
release = ''  # Is set by calling `setup.py docs`

version = importlib.import_module(namespace_pkg).__version__
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
from collections import OrderedDict

extra_nav_links = OrderedDict()
extra_nav_links['Package (PyPI)'] = 'http://pypi.python.org/pypi/percolate'
extra_nav_links['Source (GitHub)'] = 'http://github.com/andsor/pypercolate'
extra_nav_links['Issues (GitHub)'] = 'http://github.com/andsor/pypercolate/issues'
extra_nav_links['Bibliography (CiteULike)'] = 'http://www.citeulike.org/group/19226'

html_theme_options = {
    'logo': 'pypercolate-logo-plain.svg',
    'logo_name': True,
    'description': 'A scientific Python package for Monte Carlo simulation of percolation on graphs',
    'github_button': True,
    'github_banner': True,
    'github_user': 'andsor',
    'github_repo': 'pypercolate',
    'extra_nav_links': extra_nav_links,
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [alabaster.get_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
html_title = 'pypercolate documentation'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'pypercolate'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = "_static/pypercolate-logo-plain.svg"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': [
        'about.html', 'navigation.html', 'searchbox.html', 'sourcelink.html',
    ]
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'percolate-doc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'\usepackage{amsmath,amssymb}',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'user_guide.tex', u'pypercolate Documentation',
        u'Andreas Sorge', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "_static/pypercolate-logo-cropped.pdf"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
latex_domain_indices = False

# -- External mapping ------------------------------------------------------------
python_version = '.'.join(map(str, sys.version_info[0:2]))
intersphinx_mapping = {
    'sphinx': ('http://sphinx.pocoo.org', None),
    'python': ('http://docs.python.org/' + python_version, None),
    'matplotlib': ('http://matplotlib.sourceforge.net', None),
    'numpy': ('http://docs.scipy.org/doc/numpy', None),
    'scipy': ('http://docs.scipy.org/doc/scipy/reference/', None),
    'networkx': (
        'http://networkx.github.io/documentation/latest', None
    ),
}
