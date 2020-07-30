
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_fru.py

.. _edit_fru_module:


edit_fru -- Set fru settings.
=============================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set fru settings on Inspur server.





Parameters
----------


     
attribute
  Attribute,CP is Chassis Part Number,CS is Chassis Serial,PM is Product Manufacturer,

  PPN is Product Part Number,PS is Product Serial,PN is Product Name,PV is Product Version，

  PAT is Product Asset Tag,BM is Board Mfg,BPN is Board Product Name,BS is Board Serial,

  BP is Board Part Number.


  | **required**: True
  | **type**: str
  | **choices**: CP, CS, PM, PPN, PS, PN, PV, PAT, BM, BPN, BS, BP


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


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


     
value
  Set the value of attribute .


  | **required**: True
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Fru test
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

     - name: "Set Fru"
       edit_fru:
         attribute: "CP"
         value: "Inspur"
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
      
        
