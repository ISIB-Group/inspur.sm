
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_log_setting.py

.. _edit_log_setting_module:


edit_log_setting -- Set bmc system and audit log setting.
=========================================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set bmc system and audit log setting on Inspur server.





Parameters
----------


     
audit_status
  Audit Log Status.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable


     
audit_type
  Audit log type.


  | **required**: False
  | **type**: str
  | **choices**: local, remote, both


     
file_size
  File Size(3-65535bytes), set when type is local(default 30000).


  | **required**: False
  | **type**: int


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
password
  Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_PASSWORD`` will be used instead.


  | **required**: False
  | **type**: str


     
protocol_type
  Protocol Type, set when type is remote.


  | **required**: False
  | **type**: str
  | **choices**: UDP, TCP


     
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



     
rotate_count
  Rotate Count, set when type is local, 0-delete old files(default), 1-bak old files.


  | **required**: False
  | **type**: int
  | **choices**: 0, 1


     
server_addr
  Server Address, set when type is remote.


  | **required**: False
  | **type**: str


     
server_port
  Server Port(0-65535), set when type is remote.


  | **required**: False
  | **type**: int


     
status
  System Log Status.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable


     
type
  System log type.


  | **required**: False
  | **type**: str
  | **choices**: local, remote, both


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Edit log setting test
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

     - name: "Edit bmc system log setting"
       edit_log_setting:
         status: "enable"
         type: "both"
         provider: "{{ ism }}"

     - name: "Edit bmc audit log setting"
       edit_log_setting:
         audit_status: "enable"
         audit_type: "remote"
         server_addr: "100.2.126.11"
         server_port: "514"
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
      
        
