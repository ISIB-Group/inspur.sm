
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_media_instance.py

.. _edit_media_instance_module:


edit_media_instance -- Set Virtual Media Instance
=================================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set Virtual Media Instance on Inspur server.





Parameters
----------


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
kvm_num_cd
  Select the number of Remote KVM CD/DVD devices that support for virtual Media redirection,

  The max support number of html5 KVM is 2 and java KVM is 4.


  | **required**: False
  | **type**: int
  | **choices**: 0, 1, 2, 3, 4


     
kvm_num_fd
  Select the number of Remote KVM floppy devices that support for Virtual Media redirection.


  | **required**: False
  | **type**: int
  | **choices**: 0, 1, 2, 3, 4


     
kvm_num_hd
  Select the number of Remote KVM Hard disk devices to support for Virtual Media redirection.


  | **required**: False
  | **type**: int
  | **choices**: 0, 1, 2, 3, 4


     
num_cd
  Select the number of CD/DVD devices that support for Virtual Media redirection.


  | **required**: False
  | **type**: int
  | **choices**: 0, 1, 2, 3, 4


     
num_fd
  Select the number of floppy devices that support for Virtual Media redirection.


  | **required**: False
  | **type**: int
  | **choices**: 0, 1, 2, 3, 4


     
num_hd
  Select the number of harddisk devices that support for Virtual Media redirection.


  | **required**: False
  | **type**: int
  | **choices**: 0, 1, 2, 3, 4


     
password
  Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_PASSWORD`` will be used instead.


  | **required**: False
  | **type**: str


     
power_save_mode
  Check this option to enable Power Save Mode in BMC.


  | **required**: False
  | **type**: str
  | **choices**: Enable, Disable


     
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



     
sd_media
  Check this option to enable SD Media support in BMC.


  | **required**: False
  | **type**: str
  | **choices**: Enable, Disable


     
secure_channel
  Check this option to enable encrypt media recirection packets.


  | **required**: False
  | **type**: str
  | **choices**: Enable, Disable


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Media instance test
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

     - name: "Set media instance"
       edit_media_instance:
         num_fd: 1
         num_cd: 1
         num_hd: 1
         kvm_num_fd: 1
         kvm_num_cd: 1
         kvm_num_hd: 1
         sd_media: "Enable"
         secure_channel: "Enable"
         power_save_mode: "Enable"
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
      
        
