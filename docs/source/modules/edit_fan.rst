
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_fan.py

.. _edit_fan_module:


edit_fan -- Set fan information.
================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set fan information on Inspur server.





Parameters
----------


     
fan_speed
  fan speed (duty ratio), range in 1 - 100.


  | **required**: False
  | **type**: int


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
id
  fan id 255 is for all fans,0~n.


  | **required**: False
  | **type**: int


     
mode
  Control mode, Manual or Automatic ,Manual must be used with fans_peed.


  | **required**: False
  | **type**: str
  | **choices**: Automatic, Manual


     
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

   
   - name: Fan test
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

     - name: "Set fan information"
       edit_fan:
         mode: "Automatic"
         provider: "{{ ism }}"

     - name: "Set fan information"
       edit_fan:
         mode: "Manual"
         id: 1
         fan_speed: 80
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
      
        
