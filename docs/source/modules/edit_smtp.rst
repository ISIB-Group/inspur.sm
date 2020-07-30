
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_smtp.py

.. _edit_smtp_module:


edit_smtp -- Set SMTP information.
==================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set SMTP information on Inspur server.





Parameters
----------


     
email
  Sender email.


  | **required**: False
  | **type**: str


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
interface
  LAN Channel,eth0 is shared,eth1 is dedicated.


  | **required**: True
  | **type**: str
  | **choices**: eth0, eth1, bond0


     
password
  Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_PASSWORD`` will be used instead.


  | **required**: False
  | **type**: str


     
primary_auth
  Primary SMTP server authentication.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable


     
primary_ip
  Primary SMTP server IP.


  | **required**: False
  | **type**: str


     
primary_name
  Primary SMTP server name.


  | **required**: False
  | **type**: str


     
primary_password
  Primary SMTP server Password,lenth be 4 to 64 bits,cannot contain ' '(space),

  Required when *primary_auth=enable*.


  | **required**: False
  | **type**: str


     
primary_port
  Primary SMTP server port,The Identification for retry count configuration(1-65535).


  | **required**: False
  | **type**: int


     
primary_status
  Primary SMTP Support.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable


     
primary_username
  Primary SMTP server Username,lenth be 4 to 64 bits,

  must start with letters and cannot contain ','(comma) ':'(colon) ' '(space) ';'(semicolon) '\'(backslash).


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



     
secondary_auth
  S.econdary SMTP server authentication


  | **required**: False
  | **type**: str
  | **choices**: enable, disable


     
secondary_ip
  Secondary SMTP server IP.


  | **required**: False
  | **type**: str


     
secondary_name
  Secondary SMTP server name.


  | **required**: False
  | **type**: str


     
secondary_password
  Secondary SMTP server Password,lenth be 4 to 64 bits,cannot contain ' '(space),

  Required when *secondary_auth=enable*.


  | **required**: False
  | **type**: str


     
secondary_port
  Secondary SMTP server port,The Identification for retry count configuration(1-65535).


  | **required**: False
  | **type**: int


     
secondary_status
  Secondary SMTP Support.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable


     
secondary_username
  S.econdary SMTP server Username,lenth be 4 to 64 bits,

  must start with letters and cannot contain ','(comma) ':'(colon) ' '(space) ';'(semicolon) '\'(backslash).


  | **required**: False
  | **type**: str


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Smtp test
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

     - name: "Set smtp information"
       edit_smtp:
         interface: "eth0"
         email: "inspur@Inspur.com"
         primary_status: "enable"
         primary_ip: "100.2.2.2"
         primary_name: "inspur"
         primary_auth: "disable"
         provider: "{{ ism }}"

     - name: "Set smtp information"
       edit_smtp:
         interface: "eth0"
         email: "inspur@Inspur.com"
         primary_status: "enable"
         primary_ip: "100.2.2.2"
         primary_name: "inspur"
         primary_auth: "enable"
         primary_username: "test"
         primary_password: "123456"
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
      
        
