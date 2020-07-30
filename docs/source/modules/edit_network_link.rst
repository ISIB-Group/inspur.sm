
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_network_link.py

.. _edit_network_link_module:


edit_network_link -- Set network link.
======================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set network link on Inspur server.





Parameters
----------


     
auto_nego
  This option is enabled to allow the device to perform automatic configuration to

  achieve the best possible mode of operation(speed and duplex) over a link.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable


     
duplex_mode
  Select any one of the following Duplex Mode.

  Required when *auto_nego=disable*.


  | **required**: False
  | **type**: str
  | **choices**: HALF, FULL


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
interface
  Interface name.


  | **required**: True
  | **type**: str
  | **choices**: shared, dedicated, both


     
link_speed
  Link speed will list all the supported capabilities of the network interface. It can be 10/100 Mbps.

  Required when *auto_nego=disable*.


  | **required**: False
  | **type**: int
  | **choices**: 10, 100


     
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

   
   - name: link test
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

     - name: "Set network link"
       edit_network_link:
         interface: "dedicated"
         auto_nego: "enable"
         provider: "{{ ism }}"

     - name: "Set network link"
       edit_network_link:
         interface: "dedicated"
         auto_nego: "disable"
         link_speed: 100
         duplex_mode: "FULL"
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
      
        
