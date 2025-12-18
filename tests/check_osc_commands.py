#! /usr/bin/env python
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
This module will use `importlib.metadata` to scan commands for all OSC plugins
with the purpose of detecting duplicate commands.
"""

import importlib.metadata
import traceback

import yaml

from openstackclient import shell


def find_duplicates():
    """Find duplicates commands.

    Here we use `importlib.metadata` to find all modules. There will be many
    modules on a system, so we filter them out based on "openstack" since that
    is the prefix that OpenStackClient plugins will have.

    Each module has various entry points, each OpenStackClient command will
    have an entrypoint. Each entry point has a short name (ep.name) which
    is the command the user types, as well as a group (ep.module_name)
    which indicates from which module the entry point is from.

    For example, the module and entry point for v3 user list is::

        module => openstackclient.identity.v3.user
        ep.name => user_list
        ep.group => openstackclient.identity.v3

    We keep a running tally of valid commands, duplicate commands and commands
    that failed to load.

    The resultant data structure for valid commands should look like::

        {
            'user_list': [
                'openstackclient.identity.v3',
                'openstackclient.identity.v2',
            ],
            'flavor_list': [
                openstackclient.compute.v2',
            ],
        }

    The same can be said for the duplicate and failed commands.
    """

    valid_cmds = {}
    duplicate_cmds = {}
    failed_cmds = {}
    ignored_cmds = {}

    # TODO(stephenfin): We can remove this check once our minimum depends on
    # a release including change I5dd9bc9743bea779ea1b4a71264c9a77c80033b3
    ignored_modules: tuple[str] = ()
    if hasattr(shell, 'IGNORED_MODULES'):
        ignored_modules = shell.IGNORED_MODULES

    # find all modules on the system
    for dist in importlib.metadata.distributions():
        for ep in dist.entry_points:
            # OpenStackClient plugins are prefixed with "openstack"
            if not ep.group.startswith('openstack'):
                continue

            # Check for a colon since valid entrypoints will have one. For
            # example:
            #
            #   quota_show = openstackclient.common.quota:ShowQuota
            #
            # Plugin entrypoints will not. For example:
            #
            #   orchestration = heatclient.osc.plugin
            if ':' not in ep.value:
                continue

            ep_name = ep.name.replace(' ', '_')

            if any(ep.value.startswith(x) for x in ignored_modules):
                ignored_cmds.setdefault(ep_name, []).append(ep.group)
                continue

            try:
                ep.load()
            except Exception:
                exc_string = traceback.format_exc()
                message = f"{ep.group}\n{exc_string}"
                failed_cmds.setdefault(ep_name, []).append(message)

            if _is_valid_command(ep_name, ep.group, valid_cmds):
                valid_cmds.setdefault(ep_name, []).append(ep.group)
            else:
                duplicate_cmds.setdefault(ep_name, []).append(ep.group)

    if duplicate_cmds:
        print("Duplicate commands found...\n")
        print(duplicate_cmds)
        return True

    if failed_cmds:
        print("Some commands failed to load...\n")
        print(failed_cmds)
        return True

    overlap_cmds = _check_command_overlap(valid_cmds)
    if overlap_cmds:
        print("WARNING: Some commands overlap...\n")
        print(yaml.dump(overlap_cmds))
        print()
        # FIXME(stevemar): when we determine why commands are overlapping
        # we can uncomment the line below.
        # return True

    # Safely return False here with the full set of commands
    print("Final set of commands...\n")
    print(yaml.dump(valid_cmds))
    print("Ignored commands...\n")
    print(yaml.dump(ignored_cmds))
    print("Found no duplicate or overlapping commands, OK to merge!")
    return False


def _check_command_overlap(valid_cmds):
    """Determine if the entry point overlaps with another command.

    For example, if one plugin creates the command "object1 action",
    and another plugin creates the command "object1 action object2",
    the object2 command is unreachable since it overlaps the
    namespace.
    """
    overlap_cmds = {}
    for ep_name, ep_mods in valid_cmds.items():
        # Skip openstack.cli.base client entry points
        for ep_mod in ep_mods:
            for ep_name_search in valid_cmds.keys():
                if ep_name_search.startswith(ep_name + "_"):
                    overlap_cmds.setdefault(ep_name, []).append(ep_name_search)
    return overlap_cmds


def _is_valid_command(ep_name, ep_group, valid_cmds):
    """Determine if the entry point is valid.

    Aside from a simple check to see if the entry point short name is in our
    tally, we also need to check for allowed duplicates. For instance, in the
    case of supporting multiple versions, then we want to allow for duplicate
    commands. Both the identity v2 and v3 APIs support `user_list`, so these
    are fine.

    In order to determine if an entry point is a true duplicate we can check to
    see if the module name roughly matches the module name of the entry point
    that was initially added to the set of valid commands.

    The following should trigger a match::

        openstackclient.identity.v3.user and openstackclient.identity.v*.user

    Whereas, the following should fail::

        openstackclient.identity.v3.user and openstackclient.baremetal.v3.user

    """

    if ep_name not in valid_cmds:
        return True
    else:
        # there already exists an entry in the dictionary for the command...
        module_parts = ep_group.split(".")
        for valid_module_name in valid_cmds[ep_name]:
            valid_module_parts = valid_module_name.split(".")
            if (
                module_parts[0] == valid_module_parts[0]
                and module_parts[1] == valid_module_parts[1]
            ):
                return True
    return False


if __name__ == '__main__':
    print("Checking 'openstack' plug-ins")
    if find_duplicates():
        exit(1)
    else:
        exit(0)
