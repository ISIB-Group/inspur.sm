
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_snmp.py

.. _edit_snmp_module:


edit_snmp -- Set snmp.
======================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set snmp on Inspur server.





Parameters
----------


     
auth_password
  Set auth password of V3 trap or v3get/v3set,

  Password is a string of 8 to 16 alpha-numeric characters,

  Required when *auth_protocol* is either ``SHA`` or ``MD5``.


  | **required**: False
  | **type**: str


     
auth_protocol
  Choose authentication of V3 trap or v3get/v3set.


  | **required**: False
  | **type**: str
  | **choices**: NONE, SHA, MD5


     
community
  Community of v1/v2c or v1get/v1set/v2cget/v2cset.


  | **required**: False
  | **type**: str


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
password
  Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_PASSWORD`` will be used instead.


  | **required**: False
  | **type**: str


     
priv_password
  Set privacy password of V3 trap or v3get/v3set,

  password is a string of 8 to 16 alpha-numeric characters,

  Required when *priv_protocol* is either ``DES`` or ``AES``.


  | **required**: False
  | **type**: str


     
priv_protocol
  Choose Privacy of V3 trap or v3get/v3set.


  | **required**: False
  | **type**: str
  | **choices**: NONE, DES, AES


     
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



     
snmp_status
  NMP read/write status of customize,

  the input parameters are 'v1get', 'v1set', 'v2cget', 'v2cset', 'v3get', 'v3set',separated by commas,such as v1get,v1set,v2cget.


  | **required**: False
  | **type**: list


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str


     
v3username
  Set user name of V3 trap or v3get/v3set.


  | **required**: False
  | **type**: str


     
version
  SNMP trap version option, 0 - 'v1', 1 - 'v2c', 2 - 'v3', 3 - 'all', 4 - 'customize'.


  | **required**: False
  | **type**: int
  | **choices**: 0, 1, 2, 3, 4




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Snmp test
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

     - name: "Set snmp get/set"
       edit_snmp:
         community: "test"
         v3username: "Inspur"
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
      
        
