
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/psu_peak_info.py

.. _psu_peak_info_module:


psu_peak_info -- Get psu peak information.
==========================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Get psu peak information on Inspur server.





Parameters
----------


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


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

   
   - name: Psu peak test
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

     - name: "Get psu peak information"
       psu_peak_info:
         provider: "{{ ism }}"









Return Values
-------------


   
                              
       message
        | messages returned after module execution
      
        | **returned**: always
        | **type**: str
      
      
                              
       state
        | status after module execution
      
        | **returned**: always
        | **type**: str
      
      
                              
       changed
        | check to see if a change was made on the device
      
        | **returned**: always
        | **type**: bool
      
        
