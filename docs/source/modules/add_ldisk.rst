
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/add_ldisk.py

.. _add_ldisk_module:


add_ldisk -- Create logical disk.
=================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Create logical disk on Inspur server.





Parameters
----------


     
access
  Access Policy, 1 - Read Write, 2 - Read Only, 3 - Blocked,Required when *Info=None*.


  | **required**: False
  | **type**: int
  | **choices**: 1, 2, 3


     
cache
  Drive Cache, 1 - Unchanged, 2 - Enabled,3 - Disabled,Required when *Info=None*.


  | **required**: False
  | **type**: int
  | **choices**: 1, 2, 3


     
ctrl_id
  Raid controller ID,Required when *Info=None*.


  | **required**: False
  | **type**: int


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
info
  Show controller and physical drive info.


  | **required**: False
  | **type**: str
  | **choices**: show


     
init
  Init State, 1 - No Init, 2 - Quick Init, 3 - Full Init,Required when *Info=None*.


  | **required**: False
  | **type**: int
  | **choices**: 1, 2, 3


     
io
  IO Policy, 1 - Direct IO, 2 - Cached IO,Required when *Info=None*.


  | **required**: False
  | **type**: int
  | **choices**: 1, 2


     
level
  RAID Level, 0 - RAID0, 1 - RAID1, 5 - RAID5, 6 - RAID6, 10 - RAID10,Required when *Info=None*.


  | **required**: False
  | **type**: int
  | **choices**: 0, 1, 5, 6, 10


     
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



     
r
  Read Policy, 1 - Read Ahead, 2 - No Read Ahead,Required when *Info=None*.


  | **required**: False
  | **type**: int
  | **choices**: 1, 2


     
select
  Select Size, from 1 to 100,Required when *Info=None*.


  | **required**: False
  | **type**: int


     
size
  Strip Size, 1 - 64k, 2 - 128k, 3 - 256k, 4 - 512k, 5 - 1024k,Required when *Info=None*.


  | **required**: False
  | **type**: int
  | **choices**: 1, 2, 3, 4, 5


     
slot
  Slot Num,input multiple slotNumber like 0,1,2...,Required when *Info=None*.


  | **required**: False
  | **type**: list


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str


     
w
  Write Policy, 1 - Write Throgh, 2 - Write Back, 3 - Write caching ok if bad BBU,Required when *Info=None*.


  | **required**: False
  | **type**: int
  | **choices**: 1, 2, 3




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Add ldisk test
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

     - name: "Show pdisk information"
       add_ldisk:
         info: "show"
         provider: "{{ ism }}"

     - name: "Add ldisk"
       add_ldisk:
         ctrl_id: 0
         level: 1
         size: 1
         access: 1
         r: 1
         w: 1
         io: 1
         cache: 1
         init: 2
         select: 10
         slot: 0,1
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
      
        
