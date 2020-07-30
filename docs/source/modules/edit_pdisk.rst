
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_pdisk.py

.. _edit_pdisk_module:


edit_pdisk -- Set physical disk.
================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set physical disk on Inspur server.





Parameters
----------


     
ctrl_id
  Raid controller ID,Required when *Info=None*.


  | **required**: False
  | **type**: int


     
device_id
  physical drive id,Required when *Info=None*.


  | **required**: False
  | **type**: int


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
info
  Show controller and pdisk info.


  | **required**: False
  | **type**: str
  | **choices**: show


     
option
  Set operation options fo physical disk,

  UG is Unconfigured Good,UB is Unconfigured Bad,

  OFF is offline,FAIL is Failed,RBD is Rebuild,

  ON is Online,JB is JBOD,ES is Drive Erase stop,

  EM is Drive Erase Simple,EN is Drive Erase Normal,

  ET is Drive Erase Through,LOC is Locate,STL is Stop Locate,

  Required when *Info=None*.


  | **required**: False
  | **type**: str
  | **choices**: UG, UB, OFF, FAIL, RBD, ON, JB, ES, EM, EN, ET, LOC, STL


     
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




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Edit pdisk test
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

     - name: "Show pdisk information"
       edit_pdisk:
         info: "show"
         provider: "{{ ism }}"

     - name: "Edit pdisk"
       edit_pdisk:
         ctrl_id: 0
         device_id: 1
         option: "LOC"
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
      
        
