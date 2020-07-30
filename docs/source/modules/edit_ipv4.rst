
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_ipv4.py

.. _edit_ipv4_module:


edit_ipv4 -- Set ipv4 information.
==================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set ipv4 information on Inspur server.





Parameters
----------


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
interface_name
  Set interface_name.


  | **required**: True
  | **type**: str
  | **choices**: eth0, eth1, bond0


     
ipv4_address
  If DHCP is disabled, specify a static IPv4 address to be configured for the selected interface,

  Required when *ipv4_dhcp_enable=static*.


  | **required**: False
  | **type**: str


     
ipv4_dhcp_enable
  Enable 'Enable DHCP' to dynamically configure IPv4 address using Dynamic Host Configuration Protocol (DHCP).


  | **required**: False
  | **type**: str
  | **choices**: dhcp, static


     
ipv4_gateway
  If DHCP is disabled, specify a static Default Gateway to be configured for the selected interface,

  Required when *ipv4_dhcp_enable=static*.


  | **required**: False
  | **type**: str


     
ipv4_status
  Enable or disable IPV4.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable


     
ipv4_subnet
  If DHCP is disabled, specify a static Subnet Mask to be configured for the selected interface,

  Required when *ipv4_dhcp_enable=static*.


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

   
   - name: Ipv4 test
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

     - name: "Set ipv4 information"
       edit_ipv4:
         interface_name: "eth0"
         ipv4_status: "disable"
         provider: "{{ ism }}"

     - name: "Set ipv4 information"
       edit_ipv4:
         interface_name: "eth0"
         ipv4_status: "enable"
         ipv4_dhcp_enable: "dhcp"
         provider: "{{ ism }}"

     - name: "Set ipv4 information"
       edit_ipv4:
         interface_name: "eth0"
         ipv4_status: "enable"
         ipv4_dhcp_enable: "static"
         ipv4_address: "100.2.36.10"
         ipv4_subnet: "255.255.255.0"
         ipv4_gateway: "100.2.36.1"
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
      
        
