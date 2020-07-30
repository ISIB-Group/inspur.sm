
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/add_user.py

.. _add_user_module:


add_user -- Create user.
========================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Create user on Inspur server.





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


     
priv
  User access, select one or more from None/KVM/VMM/SOL.


  | **required**: True
  | **type**: list
  | **choices**: kvm, vmm, sol, none


     
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



     
role_id
  user group, default user group,'Administrator', 'Operator', 'Commonuser','OEM','NoAccess',

  use command ``user_group_info`` can get all group information.


  | **required**: True
  | **type**: str


     
uname
  User name of new user.


  | **required**: True
  | **type**: str


     
upass
  User password of new user.


  | **required**: True
  | **type**: str


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Add user test
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

     - name: "Add user"
       add_user:
         uname: "wbs"
         upass: "admin"
         role_id: "Administrator"
         priv: "kvm,sol"
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
      
        
