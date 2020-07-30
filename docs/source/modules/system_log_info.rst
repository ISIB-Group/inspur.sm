
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/system_log_info.py

.. _system_log_info_module:


system_log_info -- Get BMC system log information.
==================================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Get BMC system log information on Inspur server.





Parameters
----------


     
count
  Get the most recent log of a specified number.


  | **required**: False
  | **type**: int


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
level
  Log level.


  | **required**: False
  | **type**: str
  | **default**: alert
  | **choices**: alert, critical, error, notice, warning, debug, emergency, info


     
log_time
  Get logs after the specified date, time should be YYYY-MM-DDTHH:MM+HH:MM, like 2019-06-27T12:30+08:00.


  | **required**: False
  | **type**: str


     
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



     
system_file
  Store logs to a file.


  | **required**: False
  | **type**: str


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Bmc system log info test
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

     - name: "Get bmc system log information"
       system_log_info:
         level: "alert"
         log_time: "2020-06-01T12:30+08:00"
         provider: "{{ ism }}"

     - name: "Get bmc system log information"
       system_log_info:
         count: 30
         provider: "{{ ism }}"

     - name: "Get bmc system log information"
       system_log_info:
         system_file: "/home/wbs/wbs.log"
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
      
        
