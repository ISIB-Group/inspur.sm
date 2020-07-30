
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_snmp_trap.py

.. _edit_snmp_trap_module:


edit_snmp_trap -- Set snmp trap.
================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set snmp trap on Inspur server.





Parameters
----------


     
auth_password
  Set auth password of V3 trap, password is a string of 8 to 16 alpha-numeric characters,

  Required when *auth_protocol* is either ``SHA`` or ``MD5``.


  | **required**: False
  | **type**: str


     
auth_protocol
  Choose authentication.


  | **required**: False
  | **type**: str
  | **choices**: NONE, SHA, MD5


     
community
  Community of v1/v2c.


  | **required**: False
  | **type**: str


     
contact
  Set contact, can set NULL.


  | **required**: False
  | **type**: str


     
engine_id
  Set Engine ID of V3 trap, engine ID is a string of 10 to 48 hex characters, must even, can set NULL.


  | **required**: False
  | **type**: str


     
event_severity
  Event Severity.


  | **required**: False
  | **type**: str
  | **choices**: all, warning, critical


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
location
  Set host Location, can set NULL.


  | **required**: False
  | **type**: str


     
os
  Set host OS, can set NULL.


  | **required**: False
  | **type**: str


     
password
  Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_PASSWORD`` will be used instead.


  | **required**: False
  | **type**: str


     
priv_password
  Set privacy password of V3 trap, password is a string of 8 to 16 alpha-numeric characters,

  Required when *priv_protocol* is either ``DES`` or ``AES``.


  | **required**: False
  | **type**: str


     
priv_protocol
  Choose Privacy.


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



     
system_id
  Set system ID, can set NULL.


  | **required**: False
  | **type**: str


     
system_name
  Set system name, can set NULL.


  | **required**: False
  | **type**: str


     
trap_port
  Set SNMP trap Port(1-65535).


  | **required**: False
  | **type**: int


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str


     
v3username
  Set user name of V3 trap.


  | **required**: False
  | **type**: str


     
version
  SNMP trap version.


  | **required**: False
  | **type**: str
  | **choices**: 1, 2c, 3




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Trap test
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

     - name: "Set snmp trap v2c"
       edit_snmp_trap:
         version: "2c"
         event_severity: "warning"
         inspur: "test"
         system_name: "Inspur"
         provider: "{{ ism }}"

     - name: "Set snmp trap v3"
       edit_snmp_trap:
         version: "3"
         event_severity: "all"
         v3username: "Inspur"
         engine_id: "1234567890"
         auth_protocol: "SHA"
         auth_password: "12345678"
         priv_protocol: "AES"
         priv_password: "123454678"
         trap_port: 162
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
      
        
