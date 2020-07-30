
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_ntp.py

.. _edit_ntp_module:


edit_ntp -- Set NTP.
====================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set NTP on Inspur server.





Parameters
----------


     
auto_date
  Date auto synchronize.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
ntp_time
  NTP time(YYYYmmddHHMMSS).


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



     
server1
  NTP Server1(ipv4 or ipv6 or domain name), set when auto_dateis enable.


  | **required**: False
  | **type**: str


     
server2
  NTP Server2(ipv4 or ipv6 or domain name), set when auto_date is enable.


  | **required**: False
  | **type**: str


     
server3
  NTP Server3(ipv4 or ipv6 or domain name), set when auto_date is enable.


  | **required**: False
  | **type**: str


     
syn_cycle
  NTP syn cycle(minute).


  | **required**: False
  | **type**: int


     
time_zone
  UTC time zone,chose from {-12, -11.5, -11, ... ,11,11.5,12}.


  | **required**: False
  | **type**: str


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: NTP test
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

     - name: "Set ntp"
       edit_ntp:
         auto_date: "enable"
         server2: "time.nist.gov"
         provider: "{{ ism }}"

     - name: "Set ntp"
       edit_ntp:
         auto_date: "disable"
         ntp_time: "20200609083600"
         provider: "{{ ism }}"

     - name: "set ntp"
       edit_ntp:
         time_zone: 8
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
      
        
