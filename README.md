##### SUMMARY
<!--- Describe the change below, including rationale and design decisions -->
Inspur server supports ansible management device  --user management
Basic management of the server based on restful interface
<!--- HINT: Include "Fixes #nnn" if you are fixing an existing issue -->

##### ISSUE TYPE
<!--- Pick one below and delete the rest -->
- New Module Pull Request

##### COMPONENT NAME
<!--- Write the short name of the module, plugin, task or feature below -->
- is_add_user.py -  Create user.
- is_add_user_group.py - Create user group.
- is_del_user.py - Delete user 
- is_del_user_group.py - Delete user group
- is_edit_pass_user.py - Change user password
- is_edit_priv_user.py - Change user privilege
- is_edit_user_group.py - Set user group
- is_user_group_info.py -  Get user group information
- is_user_info.py - Get user information
##### ADDITIONAL INFORMATION
<!--- Include additional information to help people understand the change here -->
Circumstance instruction:
Ansible module is suitable for ansible version 2.2

Main steps:

Install suitable Ansible master
Install inspur_sdk 
<!--- A step-by-step reproduction of the problem is helpful if there is no related issue -->
Thes modules require the following to be installed on the Ansible server:

* Python 2.7 or later
* [Ansible](http://www.ansible.com) 2.2 or later
* [Inspur support] inspur_sdk  - Copy inspur_sdk to ansible plugins
<!--- Paste verbatim command output below, e.g. before and after your change -->
```paste below
An example of static manifest for Inspur Server Manage is followed. The network functions is satisfied based on the assumed that Ansible moudle is available.

[root@localhost ansible]# ansible localhost -m is_user_info -a 'host=100.2.126.128 username=admin password=admin'
localhost | SUCCESS => {
    "Message": [
        {
            "User": [
                {
                    "Enable": "true", 
                    "Locked": "false", 
                    "Privilege": [
                        "KVM", 
                        "VMM"
                    ], 
                    "RoleId": "Administrator", 
                    "UserId": 1, 
                    "UserName": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
                }, 
                {
                    "Enable": "true", 
                    "Locked": "false", 
                    "Privilege": [
                        "KVM", 
                        "VMM"
                    ], 
                    "RoleId": "Administrator", 
                    "UserId": 2, 
                    "UserName": "root"
                }, 
                {
                    "Enable": "true", 
                    "Locked": "false", 
                    "Privilege": [], 
                    "RoleId": "Commonuser", 
                    "UserId": 3, 
                    "UserName": "yuwenjie"
                }, 
                {
                    "Enable": "true", 
                    "Locked": "false", 
                    "Privilege": [
                        "KVM"
                    ], 
                    "RoleId": "Operator", 
                    "UserId": 4, 
                    "UserName": "wbs"
                }
            ]
        }
    ], 
    "State": "Success", 
    "changed": false, 
    "proposed": {
        "host": "100.2.126.128", 
        "password": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER", 
        "provider": null, 
        "subcommand": "getuser", 
        "username": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"
    }
}


```
