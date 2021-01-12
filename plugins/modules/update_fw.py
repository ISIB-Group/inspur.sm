#!/usr/bin/python
# -*- coding:utf-8 -*-

# Copyright (C) 2020 Inspur Inc. All Rights Reserved.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = '''
---
module: update_fw
version_added: "0.1.0"
author:
    - WangBaoshan (@ISIB-group)
short_description: Update firmware.
description:
   - Update firmware on Inspur server.
options:
    url:
        description:
            - Firmware image url.
        required: true
        type: str
    mode:
        description:
            - (BMC)active mode, Manual or Auto(default).
        default: Auto
        choices: ['Auto', 'Manual']
        type: str
    type:
        description:
            - Firmware type.
        choices: ['BMC', 'BIOS']
        type: str
    over_ride:
        description:
            - Reserve Configrations,0-reserve, 1-override.
        default: 0
        choices: [0, 1]
        type: int
    has_me:
        description:
            - (M5-BIOS)update me or not when update bios,only work in INTEL platform,0-no,1-yes.
        default: 1
        choices: [0, 1]
        type: int
    dual_image:
        description:
            - (M5)update dual image(default) or not.
        default: dual
        choices: ['single', 'dual']
        type: str
extends_documentation_fragment:
    - inspur.sm.ism
'''

EXAMPLES = '''
- name: Update fw test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "update bios"
    inspur.sm.update_fw:
      url: "/home/wbs/SA5112M5_BIOS_4.1.8_Standard_20200117.bin"
      type: "BIOS"
      provider: "{{ ism }}"

  - name: "update bmc"
    inspur.sm.update_fw:
      url: "/home/wbs/SA5112M5_BMC_4.17.7_Standard_20200430"
      mode: "Auto"
      type: "BMC"
      dual_image: "dual"
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


class Update(object):
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
        self.module.params['subcommand'] = 'fwupdate'
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
        url=dict(type='str', required=True),
        mode=dict(type='str', default='Auto', choices=['Auto', 'Manual']),
        over_ride=dict(type='int', default=0, choices=[0, 1]),
        type=dict(type='str', required=False, choices=['BMC', 'BIOS']),
        has_me=dict(type='int', default=1, choices=[0, 1]),
        dual_image=dict(type='str', default='dual', choices=['single', 'dual']),
    )
    argument_spec.update(ism_argument_spec)
    update_obj = Update(argument_spec)
    update_obj.work()


if __name__ == '__main__':
    main()
