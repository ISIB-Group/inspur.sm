
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_kvm.py

.. _edit_kvm_module:


edit_kvm -- Set KVM.
====================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set KVM on Inspur server.





Parameters
----------


     
automatic_off
  Automatically OFF Server Monitor, When KVM Launches.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
keyboard_language
  Select the Keyboard Language.

  AD is Auto Detect, DA is Danish, NL-BE is Dutch Belgium, NL-NL is Dutch Netherland,

  GB is English UK ,US is English US, FI is Finnish, FR-BE is French Belgium, FR is French France,

  DE is German Germany, DE-CH is German Switzerland, IT is Italian, JP is Japanese,

  NO is Norwegian, PT is Portuguese, ES is Spanish, SV is Swedish, TR_F is Turkish F, TR_Q is Turkish Q.


  | **required**: False
  | **type**: str
  | **choices**: AD, DA, NL-BE, NL-NL, GB, US, FI, FR-BE, FR, DE, DE-CH, IT, JP, ON, PT, EC, SV, TR_F, TR_Q


     
kvm_encryption
  Encrypt KVM packets.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable


     
local_monitor_off
  Server Monitor OFF Feature Status.


  | **required**: False
  | **type**: str
  | **choices**: enable, disable


     
media_attach
  Two types of VM attach mode are available.

  Attach is Immediately attaches Virtual Media to the server upon bootup.

  Auto is Attaches Virtual Media to the server only when a virtual media session is started.


  | **required**: False
  | **type**: str
  | **choices**: attach, auto


     
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



     
retry_count
  Number of times to be retried in case a KVM failure occurs.Retry count ranges from 1 to 20.


  | **required**: False
  | **type**: int


     
retry_time_interval
  The Identification for retry time interval configuration (5-30) seconds.


  | **required**: False
  | **type**: int


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: KVM test
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

     - name: "Set KVM"
       edit_kvm:
         kvm_encryption: "enable"
         media_attach: "auto"
         keyboard_language: "AD"
         retry_count: 13
         retry_time_interval: 10
         local_monitor_off: "enable"
         automatic_off: "enable"
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
      
        
