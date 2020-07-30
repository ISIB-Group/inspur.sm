
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/event_log_info.py

.. _event_log_info_module:


event_log_info -- Get event log information.
============================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Get event log information on Inspur server.





Parameters
----------


     
count
  Get the most recent log of a specified number.


  | **required**: False
  | **type**: int


     
event_file
  Store logs to a file.


  | **required**: False
  | **type**: str


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
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



     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Event log info test
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

     - name: "Get event log information"
       event_log_info:
         log_time: "2020-06-01T12:30+08:00"
         provider: "{{ ism }}"

     - name: "Get event log information"
       event_log_info:
         count: 30
         provider: "{{ ism }}"

     - name: "Get event log information"
       event_log_info:
         event_file: "/home/wbs/wbs.log"
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
      
        
