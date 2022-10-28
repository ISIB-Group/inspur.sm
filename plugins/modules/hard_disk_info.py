#!/usr/bin/python
# -*- coding:utf-8 -*-

# Copyright (C) 2020 Inspur Inc. All Rights Reserved.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = '''
---
module: hard_disk_info
version_added: "0.1.0"
author:
    - WangBaoshan (@ISIB-group)
short_description: Get hard disk information.
description:
   - Get hard disk information on Inspur server.
deprecated:
   removed_in: 3.0.0
   why: he Ansible collection M(inspur.sm) is deprecated. Use M(inspur.ispim) instead.
   alternative: Use M(inspur.ispim.hard_disk_info) instead.
options: {}
extends_documentation_fragment:
    - inspur.sm.ism
'''

EXAMPLES = '''
- name: Hard disk test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Get hard disk information"
    inspur.sm.hard_disk_info:
      provider: "{{ ism }}"
'''

RETURN = '''
message:
    description: Messages returned after module execution.
    returned: always
    type: str
state:
    description: Status after module execution.
    returned: always
    type: str
changed:
    description: Check to see if a change was made on the device.
    returned: always
    type: bool
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.inspur.sm.plugins.module_utils.ism import (ism_argument_spec, get_connection)


class Harddisk(object):
    def __init__(self, argument_spec):
        self.spec = argument_spec
        self.module = None
        self.init_module()
        self.results = dict()

    def init_module(self):
        """Init module object"""

        self.module = AnsibleModule(
            argument_spec=self.spec, supports_check_mode=True)

    def run_command(self):
        self.module.params['subcommand'] = 'getharddisk'
        self.results = get_connection(self.module)

    def show_result(self):
        """Show result"""
        self.module.exit_json(**self.results)

    def work(self):
        """Worker"""
        self.run_command()
        self.show_result()


def main():
    argument_spec = dict()
    argument_spec.update(ism_argument_spec)
    disk_obj = Harddisk(argument_spec)
    disk_obj.work()


if __name__ == '__main__':
    main()
