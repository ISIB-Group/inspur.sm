#!/usr/bin/python
# -*- coding:utf-8 -*-

# Copyright (C) 2020 Inspur Inc. All Rights Reserved.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = '''
---
module: edit_snmp
version_added: "0.1.0"
author:
    - WangBaoshan (@ISIB-group)
short_description: Set snmp.
description:
   - Set snmp on Inspur server.
options:
    version:
        description:
            - SNMP trap version option, 0 - 'v1', 1 - 'v2c', 2 - 'v3', 3 - 'all', 4 - 'customize'.
        choices: [0, 1, 2, 3, 4]
        type: int
    snmp_status:
        description:
            - NMP read/write status of customize,
            - the input parameters are 'v1get', 'v1set', 'v2cget', 'v2cset', 'v3get', 'v3set',separated by commas,such as v1get,v1set,v2cget.
        type: list
        elements: str
    community:
        description:
            - Community of v1/v2c or v1get/v1set/v2cget/v2cset.
        type: str
    v3username:
        description:
            - Set user name of V3 trap or v3get/v3set.
        type: str
    auth_protocol:
        description:
            - Choose authentication of V3 trap or v3get/v3set.
        choices: ['NONE', 'SHA', 'MD5']
        type: str
    auth_password:
        description:
            - Set auth password of V3 trap or v3get/v3set,
            - Password is a string of 8 to 16 alpha-numeric characters.
            - Required when I(auth_protocol) is either C(SHA) or C(MD5).
        type: str
    priv_protocol:
        description:
            - Choose Privacy of V3 trap or v3get/v3set.
        choices: ['NONE', 'DES', 'AES']
        type: str
    priv_password:
        description:
            - Set privacy password of V3 trap or v3get/v3set,
            - password is a string of 8 to 16 alpha-numeric characters.
            - Required when I(priv_protocol) is either C(DES) or C(AES).
        type: str
extends_documentation_fragment:
    - inspur.sm.ism
'''

EXAMPLES = '''
- name: Snmp test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Set snmp get/set"
    inspur.sm.edit_snmp:
      community: "test"
      v3username: "Inspur"
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


class SNMP(object):
    def __init__(self, argument_spec):
        self.spec = argument_spec
        self.module = None
        self.init_module()
        self.results = dict()

    def init_module(self):
        """Init module object"""

        self.module = AnsibleModule(
            argument_spec=self.spec, supports_check_mode=False)

    def run_command(self):
        self.module.params['subcommand'] = 'setsnmp'
        self.results = get_connection(self.module)
        if self.results['State'] == 'Success':
            self.results['changed'] = True

    def show_result(self):
        """Show result"""
        self.module.exit_json(**self.results)

    def work(self):
        """Worker"""
        self.run_command()
        self.show_result()


def main():
    argument_spec = dict(
        version=dict(type='int', required=False, choices=[0, 1, 2, 3, 4]),
        snmp_status=dict(type='list', elements='str', required=False),
        community=dict(type='str', required=False),
        v3username=dict(type='str', required=False),
        auth_protocol=dict(type='str', required=False, choices=['NONE', 'SHA', 'MD5']),
        auth_password=dict(type='str', required=False),
        priv_protocol=dict(type='str', required=False, choices=['NONE', 'DES', 'AES']),
        priv_password=dict(type='str', required=False),
    )
    argument_spec.update(ism_argument_spec)
    snmp_obj = SNMP(argument_spec)
    snmp_obj.work()


if __name__ == '__main__':
    main()
