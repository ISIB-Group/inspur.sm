
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_virtual_media.py

.. _edit_virtual_media_module:


edit_virtual_media -- Set virtual media.
========================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set virtual media on Inspur server.





Parameters
----------


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
local_media_support
  To enable or disable Local Media Support,check or uncheck the checkbox respectively.


  | **required**: False
  | **type**: str
  | **choices**: Enable, Disable


     
mount
  whether to mount virtual media.


  | **required**: False
  | **type**: str
  | **choices**: Enable, Disable


     
mount_type
  mount type, 0 is CD,1 is FD,2 is HD.


  | **required**: False
  | **type**: int
  | **choices**: 0, 1, 2


     
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



     
remote_domain_name
  Remote Domain Name,Domain Name field is optional.


  | **required**: False
  | **type**: str


     
remote_media_support
  To enable or disable Remote Media support,check or uncheck the checbox respectively.


  | **required**: False
  | **type**: str
  | **choices**: Enable, Disable


     
remote_password
  Remote Password.

  Required when *remote_share_type=cifs*.


  | **required**: False
  | **type**: str


     
remote_server_address
  Address of the server where the remote media images are stored.


  | **required**: False
  | **type**: str


     
remote_share_type
  Share Type of the remote media server either NFS or Samba(CIFS).


  | **required**: False
  | **type**: str
  | **choices**: nfs, cifs


     
remote_source_path
  Source path to the remote media images..


  | **required**: False
  | **type**: str


     
remote_user_name
  Remote User Name.

  Required when *remote_share_type=cifs*.


  | **required**: False
  | **type**: str


     
same_settings
  same settings with CD,0 is No,1 is Yes.

  Required when *mount_type=0*.


  | **required**: False
  | **type**: int
  | **choices**: 0, 1


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Media test
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

     - name: "Set local media"
       edit_virtual_media:
         local_media_support: "Enable"
         provider: "{{ ism }}"

     - name: "Set remote media"
       edit_virtual_media:
         remote_media_support: "Enable"
         mount_type: 0
         same_settings: 0
         mount: "Enable"
         remote_server_address: "100.2.28.203"
         remote_source_path: "/data/nfs/server/"
         remote_share_type: "nfs"
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
      
        
