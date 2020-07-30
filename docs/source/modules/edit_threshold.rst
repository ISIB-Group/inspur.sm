
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_threshold.py

.. _edit_threshold_module:


edit_threshold -- Set threshold information.
============================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set threshold information on Inspur server.





Parameters
----------


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
lc
  Lower critical threshold,should be integer.


  | **required**: False
  | **type**: int


     
lnc
  Lower non critical threshold,should be integer.


  | **required**: False
  | **type**: int


     
lnr
  Lower non recoverable threshold,should be integer.


  | **required**: False
  | **type**: int


     
name
  Sensor name.


  | **required**: True
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



     
uc
  Up critical threshold,should be integer.


  | **required**: False
  | **type**: int


     
unc
  Up non critical threshold,should be integer.


  | **required**: False
  | **type**: int


     
unr
  Up non recoverable threshold,should be integer.


  | **required**: False
  | **type**: int


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Threshold test
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

     - name: "Set threshold information"
       edit_threshold:
         name: "GPU1_Temp"
         uc: 94
         unc: 92
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
      
        
