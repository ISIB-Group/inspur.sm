#!/usr/bin/python
# -*- coding:utf-8 -*-

# Copyright (C) 2020 Inspur Inc. All Rights Reserved.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = '''
---
module: edit_psu_peak
version_added: "0.1.0"
author:
    - WangBaoshan (@ISIB-group)
short_description: Set psu peak information.
description:
   - Set psu peak information on Inspur server.
options:
    status:
        description:
            - Power peak status.
        choices: ['enable', 'disable']
        type: str
        required: true
    time:
        description:
            - Maximum random time, range of values(1-600), unit(second).
        type: int
extends_documentation_fragment:
    - inspur.sm.ism
'''

EXAMPLES = '''
- name: Psu peak test
  hosts: ism
  collections:
    - isnpur.sm
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Set psu peak information"
    edit_psu_peak:
      status: "disable"
      provider: "{{ ism }}"

  - name: "Set psu peak information"
    edit_psu_peak:
      status: "eanble"
      time: 10
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


class Psu(object):
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
        self.module.params['subcommand'] = 'setpsupeak'
        self.results = get_connection(self.module)

    def show_result(self):
        """Show result"""
        self.module.exit_json(**self.results)

    def work(self):
        """Worker"""
        self.run_command()
        self.show_result()


def main():
    argument_spec = dict(
        status=dict(type='str', required=True, choices=['enable', 'disable']),
        time=dict(type='int', required=False),
    )
    argument_spec.update(ism_argument_spec)
    psu_obj = Psu(argument_spec)
    psu_obj.work()


if __name__ == '__main__':
    main()
