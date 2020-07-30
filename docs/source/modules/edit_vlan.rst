
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_vlan.py

.. _edit_vlan_module:


edit_vlan -- Set vlan information.
==================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set vlan information on Inspur server.





Parameters
----------


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
interface_name
  Set interface_name.


  | **required**: True
  | **type**: str
  | **choices**: eth0, eth1, bond0


     
password
  Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_PASSWORD`` will be used instead.


  | **required**: False
  | **type**: str


     
provider
  A dict object containing connection details.


  | **required**: False
  | **type**: dict


     
  host
    Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


    | **required**: False
    | **type**: str


     
  password
    Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_PASSWORD`` will be used instead.


    | **required**: False
    | **type**: str


     
  username
    Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


    | **required**: False
    | **type**: str



     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str


     
vlan_id
  The Identification for VLAN configuration(2-4094).


  | **required**: False
  | **type**: int


     
vlan_priority
  The priority for VLAN configuration(1-7).


  | **required**: False
  | **type**: int


     
vlan_status
  Enable or disable vlan.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Vlan test
     hosts: ism
     collections:
       - inspur.sm
     connection: local
     gather_facts: no
     vars:
       ism:
         host: "{{ ansible_ssh_host }}"
         username: "{{ username }}"
         password: "{{ password }}"

     tasks:

     - name: "Set vlan information"
       edit_vlan:
         interface_name: "eth0"
         vlan_status: "disable"
         provider: "{{ ism }}"

     - name: "Set vlan information"
       edit_vlan:
         interface_name: "eth0"
         vlan_status: "enable"
         vlan_id: 2
         vlan_priority: 1
         provider: "{{ ism }}"









Return Values
-------------


   
                              
       message
        | Messages returned after module execution.
      
        | **returned**: always
        | **type**: str
      
      
                              
       state
        | Status after module execution.
      
        | **returned**: always
        | **type**: str
      
      
                              
       changed
        | Check to see if a change was made on the device.
      
        | **returned**: always
        | **type**: bool
      
        
