
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_preserve_config.py

.. _edit_preserve_config_module:


edit_preserve_config -- Set preserve config.
============================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set preserve config on Inspur server.





Parameters
----------


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
override
  Configuration items that need to be retained.

  Required when *setting=manual*.


  | **required**: False
  | **type**: list
  | **choices**: authentication, dcmi, fru, hostname, ipmi, kvm, network, ntp, pef, sdr, sel, smtp, snmp, sol, ssh, syslog, user


     
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



     
setting
  Preserve option, all - preserve all config; none - overwrite all config; manual - manual choose.


  | **required**: True
  | **type**: str
  | **choices**: all, none, manual


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Preserve test
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

     - name: "Set preserve all"
       edit_preserve_config:
         setting: "all"
         provider: "{{ ism }}"

     - name: "Set preserve none"
       edit_preserve_config:
         setting: "none"
         provider: "{{ ism }}"

     - name: "Set preserve manual"
       edit_preserve_config:
         setting: "manual"
         override:
           - fru
           - ntp
           - network
           - user
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
      
        
