
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_ad.py

.. _edit_ad_module:


edit_ad -- Set active directory information.
============================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set active directory information on Inspur server.





Parameters
----------


     
addr1
  Domain Controller Server Address1.


  | **required**: False
  | **type**: str


     
addr2
  Domain Controller Server Address2.


  | **required**: False
  | **type**: str


     
addr3
  Domain Controller Server Address3.


  | **required**: False
  | **type**: str


     
code
  Secret Password.


  | **required**: False
  | **type**: str


     
domain
  User Domain Name.


  | **required**: False
  | **type**: str


     
enable
  Active Directory Authentication Status.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
name
  Secret Username.


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



     
timeout
  The Time Out configuration(15-300).


  | **required**: False
  | **type**: int


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Ad test
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

     - name: "Set active directory information"
       edit_ad:
         enable: "disable"
         provider: "{{ ism }}"

     - name: "Set active directory information"
       edit_ad:
         enable: "enable"
         name: "inspur"
         code: "123456"
         timeout: 120
         domain: "inspur.com"
         addr1: "100.2.2.2"
         addr2: "100.2.2.3"
         addr3: "100.2.2.4"
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
      
        
