===============
OpenStackClient
===============

OpenStackClient (aka OSC) is a command-line client for OpenStack that
brings the command set for Compute, Identity, Image, Network, Object
Storage and Block Storage APIs together in a single shell with a uniform
command structure.

The ``openstackclient`` package is a metapackage that installs
``python-openstackclient`` and a number of optional plugins all at the same
time to simplify the installation of OSC.  The major version of
``openstackclient`` will always correspond to the major version of
``python-openstackclient`` that will be installed.

Getting Started
---------------

* Install OpenStackClient from `PyPi`_ or a `tarball`_

Contributing
============

OpenStackClient utilizes all of the usual OpenStack processes and requirements
for contributions.  The code is hosted `on OpenStack's Git server`_. Bug
reports may be submitted to the appropriate project in the the
`openstackclient Storyboard group`_. Code may be submitted to those projects
using `Gerrit`_. Developers may also be found in the `IRC channel`_
``#openstack-sdks``.

.. _`on OpenStack's Git server`: https://opendev.org/openstack/openstackclient/
.. _`openstackclient Storyboard group`: https://storyboard.openstack.org/#!/project_group/80
.. _Gerrit: http://docs.openstack.org/infra/manual/developers.html#development-workflow
.. _Bug reports: https://storyboard.openstack.org/#!/project/975
.. _PyPi: https://pypi.org/project/openstackclient
.. _tarball: http://tarballs.openstack.org/openstackclient
.. _IRC channel: https://wiki.openstack.org/wiki/IRC
