
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/update_fw.py

.. _update_fw_module:


update_fw -- Update firmware.
=============================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Update firmware on Inspur server.





Parameters
----------


     
dual_image
  update dual image or not.


  | **required**: False
  | **type**: str
  | **default**: dual
  | **choices**: single, dual


     
has_me
  update me or not when update bios,0-no,1-yes.


  | **required**: False
  | **type**: int
  | **choices**: 0, 1


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
mode
  active mode, Manual or Auto.


  | **required**: False
  | **type**: str
  | **default**: Auto
  | **choices**: Auto, Manual


     
over_ride
  Reserve Configrations:0-reserve, 1-override.


  | **required**: False
  | **type**: int
  | **choices**: 0, 1


     
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



     
type
  Firmware type.


  | **required**: False
  | **type**: str
  | **choices**: BMC, BIOS


     
url
  Firmware image url.


  | **required**: False
  | **type**: str


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Update fw test
     hosts: ism
     collections:
       - isnpur.sm
     connection: local
     gather_facts: no
     vars:
       ism:
         host: "{{ ansible_ssh_host }}"
         username: "{{ username }}"
         password: "{{ password }}"

     tasks:

     - name: "Update bmc"
       update_fw:
         url: "/home/wbs/"
         mode: "Auto"
         type: "BMC"
         dual_image: "dual"
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
      
        
