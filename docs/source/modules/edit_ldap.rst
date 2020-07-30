
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_ldap.py

.. _edit_ldap_module:


edit_ldap -- Set ldap information.
==================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set ldap information on Inspur server.





Parameters
----------


     
address
  Server Address.


  | **required**: False
  | **type**: str


     
attr
  Attribute of User Login.


  | **required**: False
  | **type**: str
  | **choices**: cn, uid


     
base
  Search Base,

  Search base is a string of 4 to 64 alpha-numeric characters;

  It must start with an alphabetical character;

  Special Symbols like dot(.), comma(,), hyphen(-), underscore(_), equal-to(=) are allowed.


  | **required**: False
  | **type**: str


     
ca
  CA certificate file path,Required when *encry=StartTLS*.


  | **required**: False
  | **type**: str


     
ce
  Certificate file path,Required when *encry=StartTLS*.


  | **required**: False
  | **type**: str


     
cn
  Common name type,Required when *encry=StartTLS*.


  | **required**: False
  | **type**: str
  | **choices**: ip, fqdn


     
code
  Password,Required when *enable=enable*.


  | **required**: False
  | **type**: str


     
dn
  Bind DN.

  Bind DN is a string of 4 to 64 alpha-numeric characters;

  It must start with an alphabetical character;

  Special Symbols like dot(.), comma(,), hyphen(-), underscore(_), equal-to(=) are allowed.


  | **required**: False
  | **type**: str


     
enable
  LDAP/E-Directory Authentication Status.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable


     
encry
  Encryption Type.


  | **required**: False
  | **type**: str
  | **choices**: no, SSL, StartTLS


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
password
  Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_PASSWORD`` will be used instead.


  | **required**: False
  | **type**: str


     
pk
  Private Key file path,Required when *encry=StartTLS*.


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



     
server_port
  Server Port.


  | **required**: False
  | **type**: int


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Ldap test
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

     - name: "Set ldap information"
       edit_ldap:
         enable: "disable"
         provider: "{{ ism }}"

     - name: "Set ldap information"
       edit_ldap:
         enable: "enable"
         encry: "SSL"
         address: "100.2.2.2"
         server_port: 389
         dn: "cn=manager,ou=login,dc=domain,dc=com"
         code: "123456"
         base: "cn=manager"
         attr: "uid"
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
      
        
