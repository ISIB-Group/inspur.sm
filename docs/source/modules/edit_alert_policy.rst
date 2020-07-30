
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_alert_policy.py

.. _edit_alert_policy_module:


edit_alert_policy -- Set alert policy.
======================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set alert policy on Inspur server.





Parameters
----------


     
channel
  LAN Channel.


  | **required**: False
  | **type**: str
  | **choices**: shared, dedicated


     
destination
  Alert destination,when type is snmp,fill in IP;

  when type is email,fill in user name;

  when type is snmpdomain,fill in domain.


  | **required**: False
  | **type**: str


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
id
  Alert id.


  | **required**: True
  | **type**: int
  | **choices**: 1, 2, 3


     
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



     
status
  Alert policy status.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable


     
type
  Alert Type.


  | **required**: False
  | **type**: str
  | **choices**: snmp, email, snmpdomain


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Alert policy test
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

     - name: "Set alert policy"
       edit_alert_policy:
         id: 1
         status: "enable"
         type: "snmp"
         destination: "100.2.2.2"
         channel: "shared"
         provider: "{{ ism }}"

     - name: "Set alert policy"
       edit_alert_policy:
         id: 1
         status: "disable"
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
      
        
