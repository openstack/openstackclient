===============
OpenStackClient
===============

.. image:: https://img.shields.io/pypi/v/openstackclient.svg
    :target: https://pypi.org/project/openstackclient/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/openstackclient.svg
    :target: https://pypi.org/project/openstackclient/
    :alt: Downloads

OpenStackClient (aka OSC) is a command-line client for OpenStack that brings
the command set for Compute, Identity, Image, Object Store and Block Storage
APIs together in a single shell with a uniform command structure.

The primary goal is to provide a unified shell command structure and a common
language to describe operations in OpenStack.

* `PyPi`_ - package installation
* `Online Documentation`_
* `Launchpad project`_ - release management
* `Blueprints`_ - feature specifications
* `Bugs`_ - issue tracking
* `Source`_
* `Developer` - getting started as a developer
* `Contributing` - contributing code
* `Testing` - testing code
* IRC: #openstack-sdks on Freenode (irc.freenode.net)
* License: Apache 2.0

.. _PyPi: https://pypi.org/project/openstackclient
.. _Online Documentation: http://docs.openstack.org/developer/python-openstackclient/
.. _Launchpad project: https://launchpad.net/python-openstackclient
.. _Blueprints: https://blueprints.launchpad.net/python-openstackclient
.. _Bugs: https://bugs.launchpad.net/python-openstackclient
.. _Source: https://git.openstack.org/cgit/openstack/openstackclient
.. _Developer: http://docs.openstack.org/project-team-guide/project-setup/python.html
.. _Contributing: http://docs.openstack.org/infra/manual/developers.html
.. _Testing: http://docs.openstack.org/developer/python-openstackclient/developing.html#testing

Getting Started
===============

OpenStack Client can be installed from PyPI using pip::

    pip install openstackclient

There are a few variants on getting help.  A list of global options and supported
commands is shown with ``--help``::

   openstack --help

There is also a ``help`` command that can be used to get help text for a specific
command::

    openstack --help
    openstack server create --help
