##### SUMMARY
<!--- Describe the change below, including rationale and design decisions -->
Inspur server supports ansible management device
Basic management of the server based on restful interface
<!--- HINT: Include "Fixes #nnn" if you are fixing an existing issue -->

##### ISSUE TYPE
<!--- Pick one below and delete the rest -->
- New Module Pull Request

##### COMPONENT NAME
<!--- Write the short name of the module, plugin, task or feature below -->
- ad_group_info - Get active directory group information.
- ad_info - Get active directory information.
- adapter_info - Get adapter information.
- add_ad_group - Add active directory group information.
- add_ldap_group - Add ldap group information.
- add_ldisk - Create logical disk.
- add_user - Create user.
- add_user_group - Create user group.
- alert_policy_info - Get alert policy.
- audit_log_info - Get BMC audit log information.
- auto_capture_info - Get auto capture screen information.
- backplane_info - Get disk backplane information.
- backup - Backup server settings.
- bios_export - Export BIOS config.
- bios_import - Import BIOS config.
- bios_info - Get BIOS setup.
- bmc_info - Get BMC information.
- boot_image_info - Get bmc boot image information.
- boot_option_info - Get BIOS boot options.
- clear_audit_log - Clear BMC audit log.
- clear_event_log - Clear event log.
- clear_system_log - Clear BMC system log.
- collect_blackbox - Collect blackbox log.
- collect_log - Collect logs.
- connect_media_info - Get remote images redirection information.
- cpu_info - Get CPU information.
- del_ad_group - Delete active directory group information.
- del_ldap_group - Delete ldap group information.
- del_session - Delete session.
- del_user - Delete user.
- del_user_group - Delete user group.
- dns_info - Get dns information.
- download_auto_screenshot - Download auto screenshots.
- download_manual_screenshot - Download manual screenshots.
- edit_ad - Set active directory information.
- edit_ad_group - Set active directory group information.
- edit_alert_policy - Set alert policy.
- edit_auto_capture - Set auto capture screen.
- edit_bios - Set BIOS setup attributes.
- edit_boot_image - Set bmc boot image.
- edit_boot_option - Set BIOS boot options.
- edit_connect_media - Start/Stop virtual media Image
- edit_dns - Set dns information.
- edit_event_log_policy - Set event log policy.
- edit_fan - Set fan information.
- edit_fru - Set fru settings.
- edit_ipv4 - Set ipv4 information.
- edit_ipv6 - Set ipv6 information.
- edit_kvm - Set KVM.
- edit_ldap - Set ldap information.
- edit_ldap_group - Set ldap group information.
- edit_ldisk - Set logical disk.
- edit_log_setting - Set bmc system and audit log setting.
- edit_manual_capture - Set manual capture screen.
- edit_media_instance - Set Virtual Media Instance
- edit_ncsi - Set ncsi information.
- edit_network - Set network information.
- edit_network_bond - Set network bond.
- edit_network_link - Set network link.
- edit_ntp - Set NTP.
- edit_pass_user - Change user password.
- edit_pdisk - Set physical disk.
- edit_power_budget - Set power budget information.
- edit_power_restore - Set power restore information.
- edit_power_status - Set power status information.
- edit_preserve_config - Set preserve config.
- edit_priv_user - Change user privilege.
- edit_psu_config - Set psu config information.
- edit_psu_peak - Set psu peak information.
- edit_restore_factory_default - Set preserver config.
- edit_service - Set service settings.
- edit_smtp - Set SMTP information.
- edit_snmp - Set snmp.
- edit_snmp_trap - Set snmp trap.
- edit_threshold - Set threshold information.
- edit_uid - Set UID.
- edit_user_group - Set user group.
- edit_virtual_media - Set virtual media.
- edit_vlan - Set vlan information.
- event_log_info - Get event log information.
- event_log_policy_info - Get event log policy information.
- fan_info - Get fan information.
- fru_info - Get fru information.
- fw_version_info - Get firmware version information.
- hard_disk_info - Get hard disk information.
- kvm_info - Get KVM information.
- ldap_group_info - Get ldap group information.
- ldap_info - Get ldap information.
- ldisk_info - Get logical disks information.
- log_setting_info - Get bmc log setting information.
- media_instance_info - Get Virtual Media Instance information.
- mem_info - Get memory information.
- ncsi_info - Get ncsi information.
- network_bond_info - Get network bond information.
- network_info - Get network information.
- network_link_info - Get network link information.
- ntp_info - Get NTP information.
- pcie_info - Get PCIE information.
- pdisk_info - Get physical disks information.
- power_budget_info - Get power budget information.
- power_consumption_info - Get power consumption information.
- power_restore_info - Get power restore information.
- power_status_info - Get power status information.
- preserver_config_info - Get preserver config information.
- psu_config_info - Get psu config information.
- psu_info - Get psu information.
- psu_peak_info - Get psu peak information.
- raid_info - Get RAID/HBA card and controller information.
- reset_bmc - BMC reset.
- reset_kvm - KVM reset.
- restore - Restore server settings.
- self_test_info - Get self test information.
- sensor_info - Get sensor information.
- server_info - Get server status information.
- service_info - Get service information.
- session_info - Get online session information.
- smtp_info - Get SMTP information.
- snmp_info - Get snmp get/set information.
- snmp_trap_info - Get snmp trap information.
- system_log_info - Get BMC system log information.
- temp_info - Get temp information.
- threshold_info - Get threshold information.
- uid_info - Get UID information.
- update_cpld - Update CPLD.
- update_fw - Update firmware.
- user_group_info - Get user group information.
- user_info - Get user information.
- virtual_media_info - Get Virtual Media information.
- volt_info - Get volt information.
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
* [Inspur support] inspur_sm_sdk
<!--- Paste verbatim command output below, e.g. before and after your change -->
```paste below
An example of static manifest for Inspur Server Manage is followed. The network functions is satisfied based on the assumed that Ansible moudle is available.

[root@localhost ansible]# ansible localhost -m user_info -a 'host=100.2.126.128 username=admin password=admin'
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
