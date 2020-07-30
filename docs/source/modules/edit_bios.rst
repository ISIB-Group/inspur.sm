
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_bios.py

.. _edit_bios_module:


edit_bios -- Set BIOS setup attributes.
=======================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set BIOS setup attributes on Inspur server.





Parameters
----------


     
attribute
  BIOS setup option,Required when *file_url=None*.


  | **required**: False
  | **type**: str


     
file_url
  BIOS option file.attribute must be used with value,

  Mutually exclusive with fileurl format,"/directory/filename".


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


     
value
  BIOS setup option value,Required when *file_url=None*.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Bios test
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

     - name: "Set bios setup"
       edit_bios:
         attribute: "VMX"
         value: "Disable"
         provider: "{{ ism }}"

     - name: "Set bios setup"
       edit_bios:
         attribute: "VMX"
         value: "Enable"
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
      
        
