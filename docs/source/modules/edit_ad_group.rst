
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_ad_group.py

.. _edit_ad_group_module:


edit_ad_group -- Set active directory group information.
========================================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set active directory group information on Inspur server.





Parameters
----------


     
domain
  Group domain.


  | **required**: False
  | **type**: str


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
id
  Group id.


  | **required**: True
  | **type**: str
  | **choices**: 1, 2, 3, 4, 5


     
kvm
  Kvm privilege.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable


     
name
  Group name.


  | **required**: False
  | **type**: str


     
password
  Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_PASSWORD`` will be used instead.


  | **required**: False
  | **type**: str


     
pri
  Group privilege.


  | **required**: False
  | **type**: str
  | **choices**: administrator, user, operator, oem, none


     
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


     
vm
  Vmedia privilege.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Ad group test
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

     - name: "Edit active directory group information"
       edit_ad_group:
         id: "1"
         name: "wbs"
         domain: "inspur.com"
         pri: "administrator"
         kvm: "enable"
         vm: "disable"
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
      
        
