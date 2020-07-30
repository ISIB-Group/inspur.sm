
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_service.py

.. _edit_service_module:


edit_service -- Set service settings.
=====================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set service settings on Inspur server.





Parameters
----------


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
interface
  It shows the interface in which service is running.

  The user can choose any one of the available interfaces.


  | **required**: False
  | **type**: str
  | **choices**: eth0, eth1, both, bond0


     
non_secure_port
  Used to configure non secure port number for the service.

  Port value ranges from 1 to 65535.


  | **required**: False
  | **type**: int


     
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



     
secure_port
  Used to configure secure port number for the service.

  Port value ranges from 1 to 65535.


  | **required**: False
  | **type**: int


     
service_name
  Displays service name of the selected slot(readonly).


  | **required**: True
  | **type**: str
  | **choices**: web, kvm, cd-media, fd-media, hd-media, ssh, telnet, solssh, snmp


     
state
  Displays the current status of the service, either active or inactive state.

  Check this option to start the inactive service.


  | **required**: False
  | **type**: str
  | **choices**: active, inactive


     
timeout
  Displays the session timeout value of the service.

  For web, SSH and telnet service, user can configure the session timeout value.

  Web timeout value ranges from 300 to 1800 seconds.

  SSH and Telnet timeout value ranges from 60 to 1800 seconds.

  timeout value should be in multiples of 60 seconds.


  | **required**: False
  | **type**: int


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Edit service test
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

     - name: "Edit kvm"
       edit_service:
         service_name: "kvm"
         state: "active"
         timeout: "1200"
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
      
        
