
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_dns.py

.. _edit_dns_module:


edit_dns -- Set dns information.
================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set dns information on Inspur server.





Parameters
----------


     
dns_iface
  DNS Interface,input like 'eth0', 'eth1', 'bond0',Required when *dns_manual=auto*.


  | **required**: False
  | **type**: str


     
dns_manual
  DNS Settings.


  | **required**: False
  | **type**: str
  | **choices**: manual, auto


     
dns_priority
  IP Priority,Required when *dns_manual=auto*.


  | **required**: False
  | **type**: str
  | **choices**: 4, 6


     
dns_server1
  DNS Server1 ipv4 or ipv6 address,Required when *dns_manual=manual*.


  | **required**: False
  | **type**: str


     
dns_server2
  DNS Server2 ipv4 or ipv6 address,Required when *dns_manual=manual*.


  | **required**: False
  | **type**: str


     
dns_server3
  DNS Server3 ipv4 or ipv6 address,Required when *dns_manual=manual*.


  | **required**: False
  | **type**: str


     
dns_status
  DNS status.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable


     
domain_iface
  Network Interface,input like 'eth0_v4', 'eth0_v6', 'eth1_v4', 'eth1_v6', 'bond0_v4', 'bond0_v6',

  Required when *domain_manual=auto*.


  | **required**: False
  | **type**: str


     
domain_manual
  Domain Settings.


  | **required**: False
  | **type**: str
  | **choices**: manual, auto


     
domain_name
  Domain Name, Required when *domain_manual=manual*.


  | **required**: False
  | **type**: str


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
host_cfg
  Host Settings.


  | **required**: False
  | **type**: str
  | **choices**: manual, auto


     
host_name
  Host Name,Required when *host_cfg=manual*.


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

   
   - name: DNS test
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

     - name: "Set dns information"
       edit_dns:
         dns_status: "disable"
         provider: "{{ ism }}"

     - name: "Set dns information"
       edit_dns:
         dns_status: "enable"
         host_cfg: "manual"
         host_name: "123456789"
         domain_manual: "auto"
         domain_iface: "eth0_v4"
         dns_manual: "manual"
         dns_server1: "100.2.2.2"
         dns_server2: "100.2.2.3"
         dns_server3: "100.2.2.4"
         provider: "{{ ism }}"

     - name: "Set dns information"
       edit_dns:
         dns_status: "enable"
         host_cfg: "manual"
         host_name: "123456789"
         domain_manual: "manual"
         domain_name: "inspur.com"
         dns_manual: "auto"
         dns_iface: "eth0"
         dns_priority: "4"
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
      
        
