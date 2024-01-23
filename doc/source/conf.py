# OpenStack Command Line Client documentation build configuration file
#
# This file is execfile()d with the current directory set to its containing
# dir.

# -- General configuration ----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'openstackdocstheme',
]

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'OpenStack Command Line Client'
copyright = '2012-present OpenStack Foundation'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['**tests**']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'native'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['openstackclient.']

# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'openstackdocs'

# -- Options for openstackdocstheme extension ---------------------------------

# openstackdocstheme options
openstackdocs_repo_name = 'openstack/openstackclient'
openstackdocs_auto_name = False
openstackdocs_use_storyboard = True
