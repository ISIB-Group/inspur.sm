
:github_url: https://github.com/ISIB-Group/ISM4A/tree/master/plugins/modules/edit_power_budget.py

.. _edit_power_budget_module:


edit_power_budget -- Set power budget information.
==================================================



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Set power budget information on Inspur server.





Parameters
----------


     
action
  Type to action.

  Required when *range=False*.


  | **required**: False
  | **type**: str
  | **choices**: add, delete, open, close


     
end1
  Pause period of add, end time,must be greater than start time,from 0 to 24.


  | **required**: False
  | **type**: int


     
end2
  Pause period of add, end time,must be greater than start time,from 0 to 24.


  | **required**: False
  | **type**: int


     
end3
  Pause period of add, end time,must be greater than start time,from 0 to 24.


  | **required**: False
  | **type**: int


     
end4
  Pause period of add, end time,must be greater than start time,from 0 to 24.


  | **required**: False
  | **type**: int


     
end5
  Pause period of add, end time,must be greater than start time,from 0 to 24.


  | **required**: False
  | **type**: int


     
host
  Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.


  | **required**: False
  | **type**: str


     
id
  Policy id.

  Required when *range=False*.


  | **required**: False
  | **type**: int
  | **choices**: 1, 2, 3, 4


     
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



     
range
  Range of power budget watts.


  | **required**: False
  | **type**: bool
  | **choices**: True, False


     
start1
  Pause period of add, start time, from 0 to 24.


  | **required**: False
  | **type**: int


     
start2
  Pause period of add, start time, from 0 to 24.


  | **required**: False
  | **type**: int


     
start3
  Pause period of add, start time, from 0 to 24.


  | **required**: False
  | **type**: int


     
start4
  Pause period of add, start time, from 0 to 24.


  | **required**: False
  | **type**: int


     
start5
  Period of add, start time, from 0 to 24.


  | **required**: False
  | **type**: int


     
username
  Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable ``ANSIBLE_NET_USERNAME`` will be used instead.


  | **required**: False
  | **type**: str


     
watts
  Power budget watts of add.

  Required when *action=add*.


  | **required**: False
  | **type**: int


     
week1
  Pause period of add,repetition period,the input parameters are 'Mon','Tue','Wed','Thur','Fri','Sat','Sun',separated by commas,such as Mon,Wed,Fri.


  | **required**: False
  | **type**: list


     
week2
  Pause period of add,repetition period,the input parameters are 'Mon','Tue','Wed','Thur','Fri','Sat','Sun',separated by commas,such as Mon,Wed,Fri.


  | **required**: False
  | **type**: list


     
week3
  Pause period of add,repetition period,the input parameters are 'Mon','Tue','Wed','Thur','Fri','Sat','Sun',separated by commas,such as Mon,Wed,Fri.


  | **required**: False
  | **type**: list


     
week4
  Pause period of add,repetition period,the input parameters are 'Mon','Tue','Wed','Thur','Fri','Sat','Sun',separated by commas,such as Mon,Wed,Fri.


  | **required**: False
  | **type**: list


     
week5
  Pause period of add,repetition period,the input parameters are 'Mon','Tue','Wed','Thur','Fri','Sat','Sun',separated by commas,such as Mon,Wed,Fri.


  | **required**: False
  | **type**: list




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Power budget test
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

     - name: "Get power budget range"
       edit_power_budget:
         range: True
         provider: "{{ ism }}"

     - name: "add power budget"
       edit_power_budget:
         action: "add"
         id: 1
         watts: 1500
         start1: 2
         end1: 5
         week1:
           - Mon
           - Wed
           - Fri
         provider: "{{ ism }}"

     - name: "Set power budget status to open"
       edit_power_budget:
         action: "open"
         id: 1
         provider: "{{ ism }}"

     - name: "Set power budget status to close"
       edit_power_budget:
         action: "close"
         id: 1
         provider: "{{ ism }}"

     - name: "Delete power budget"
       edit_power_budget:
         action: "delete"
         id: 1
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
      
        
