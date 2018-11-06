Add a task to see the debug output

```
  tasks:
    - debug: var=hostvars[inventory_hostname]
```

output

```
Bhavesh/practice/vagrant via pyenv
➜ ansible-playbook -i hosts  redis_server.yml -u vagrant
[DEPRECATION WARNING]: Instead of sudo/sudo_user, use become/become_user and make sure become_method is 'sudo' (default). This feature will be removed in version 2.9. Deprecation
warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.

PLAY [Install Redis] ********************************************************************************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************************************************************
ok: [172.28.128.13]

TASK [debug] ****************************************************************************************************************************************************************************
ok: [172.28.128.13] => {
    "hostvars[inventory_hostname]": {
        "ansible_all_ipv4_addresses": [
            "10.0.2.15",
            "172.28.128.13"
        ],
        "ansible_all_ipv6_addresses": [
            "fe80::a00:27ff:fe97:31f6"
        ],
        "ansible_apparmor": {
            "status": "enabled"
        },
        "ansible_architecture": "i386",
        "ansible_bios_date": "12/01/2006",
        "ansible_bios_version": "VirtualBox",
        "ansible_check_mode": false,
        "ansible_cmdline": {
            "BOOT_IMAGE": "/boot/vmlinuz-3.13.0-161-generic",
            "console": "ttyS0",
            "ro": true,
            "root": "UUID=2220679a-bcf3-402c-9e25-d36ec301949e"
        },
        "ansible_date_time": {
            "date": "2018-11-06",
            "day": "06",
            "epoch": "1541533018",
            "hour": "19",
            "iso8601": "2018-11-06T19:36:58Z",
            "iso8601_basic": "20181106T193658037480",
            "iso8601_basic_short": "20181106T193658",
            "iso8601_micro": "2018-11-06T19:36:58.037547Z",
            "minute": "36",
            "month": "11",
            "second": "58",
            "time": "19:36:58",
            "tz": "UTC",
            "tz_offset": "+0000",
            "weekday": "Tuesday",
            "weekday_number": "2",
            "weeknumber": "45",
            "year": "2018"
        },
        "ansible_default_ipv4": {
            "address": "10.0.2.15",
            "alias": "eth0",
            "broadcast": "10.0.2.255",
            "gateway": "10.0.2.2",
            "interface": "eth0",
            "macaddress": "08:00:27:97:31:f6",
            "mtu": 1500,
            "netmask": "255.255.255.0",
            "network": "10.0.2.0",
            "type": "ether"
        },
        "ansible_default_ipv6": {},
        "ansible_device_links": {
            "ids": {
                "sda": [
                    "ata-VBOX_HARDDISK_VB0a12b175-65ac9ff7"
                ],
                "sda1": [
                    "ata-VBOX_HARDDISK_VB0a12b175-65ac9ff7-part1"
                ]
            },
            "labels": {
                "sda1": [
                    "cloudimg-rootfs"
                ]
            },
            "masters": {},
            "uuids": {
                "sda1": [
                    "2220679a-bcf3-402c-9e25-d36ec301949e"
                ]
            }
        },
        "ansible_devices": {
            "loop0": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "0",
                "sectorsize": "512",
                "size": "0.00 Bytes",
                "support_discard": "0",
                "vendor": null,
                "virtual": 1
            },
            "loop1": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "0",
                "sectorsize": "512",
                "size": "0.00 Bytes",
                "support_discard": "0",
                "vendor": null,
                "virtual": 1
            },
            "loop2": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "0",
                "sectorsize": "512",
                "size": "0.00 Bytes",
                "support_discard": "0",
                "vendor": null,
                "virtual": 1
            },
            "loop3": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "0",
                "sectorsize": "512",
                "size": "0.00 Bytes",
                "support_discard": "0",
                "vendor": null,
                "virtual": 1
            },
            "loop4": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "0",
                "sectorsize": "512",
                "size": "0.00 Bytes",
                "support_discard": "0",
                "vendor": null,
                "virtual": 1
            },
            "loop5": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "0",
                "sectorsize": "512",
                "size": "0.00 Bytes",
                "support_discard": "0",
                "vendor": null,
                "virtual": 1
            },
            "loop6": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "0",
                "sectorsize": "512",
                "size": "0.00 Bytes",
                "support_discard": "0",
                "vendor": null,
                "virtual": 1
            },
            "loop7": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "0",
                "sectorsize": "512",
                "size": "0.00 Bytes",
                "support_discard": "0",
                "vendor": null,
                "virtual": 1
            },
            "ram0": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "131072",
                "sectorsize": "512",
                "size": "64.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "ram1": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "131072",
                "sectorsize": "512",
                "size": "64.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "ram10": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "131072",
                "sectorsize": "512",
                "size": "64.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "ram11": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "131072",
                "sectorsize": "512",
                "size": "64.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "ram12": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "131072",
                "sectorsize": "512",
                "size": "64.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "ram13": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "131072",
                "sectorsize": "512",
                "size": "64.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "ram14": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "131072",
                "sectorsize": "512",
                "size": "64.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "ram15": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "131072",
                "sectorsize": "512",
                "size": "64.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "ram2": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "131072",
                "sectorsize": "512",
                "size": "64.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "ram3": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "131072",
                "sectorsize": "512",
                "size": "64.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "ram4": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "131072",
                "sectorsize": "512",
                "size": "64.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "ram5": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "131072",
                "sectorsize": "512",
                "size": "64.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "ram6": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "131072",
                "sectorsize": "512",
                "size": "64.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "ram7": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "131072",
                "sectorsize": "512",
                "size": "64.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "ram8": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "131072",
                "sectorsize": "512",
                "size": "64.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "ram9": {
                "holders": [],
                "host": "",
                "links": {
                    "ids": [],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "",
                "sectors": "131072",
                "sectorsize": "512",
                "size": "64.00 MB",
                "support_discard": "4096",
                "vendor": null,
                "virtual": 1
            },
            "sda": {
                "holders": [],
                "host": "SATA controller: Intel Corporation 82801HM/HEM (ICH8M/ICH8M-E) SATA Controller [AHCI mode] (rev 02)",
                "links": {
                    "ids": [
                        "ata-VBOX_HARDDISK_VB0a12b175-65ac9ff7"
                    ],
                    "labels": [],
                    "masters": [],
                    "uuids": []
                },
                "model": "VBOX HARDDISK",
                "partitions": {
                    "sda1": {
                        "holders": [],
                        "links": {
                            "ids": [
                                "ata-VBOX_HARDDISK_VB0a12b175-65ac9ff7-part1"
                            ],
                            "labels": [
                                "cloudimg-rootfs"
                            ],
                            "masters": [],
                            "uuids": [
                                "2220679a-bcf3-402c-9e25-d36ec301949e"
                            ]
                        },
                        "sectors": "83884032",
                        "sectorsize": 512,
                        "size": "40.00 GB",
                        "start": "2048",
                        "uuid": "2220679a-bcf3-402c-9e25-d36ec301949e"
                    }
                },
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "deadline",
                "sectors": "83886080",
                "sectorsize": "512",
                "size": "40.00 GB",
                "support_discard": "0",
                "vendor": "ATA",
                "virtual": 1
            }
        },
        "ansible_diff_mode": false,
        "ansible_distribution": "Ubuntu",
        "ansible_distribution_file_parsed": true,
        "ansible_distribution_file_path": "/etc/os-release",
        "ansible_distribution_file_variety": "Debian",
        "ansible_distribution_major_version": "14",
        "ansible_distribution_release": "trusty",
        "ansible_distribution_version": "14.04",
        "ansible_dns": {
            "nameservers": [
                "10.0.2.3"
            ],
            "search": [
                "ant.amazon.com"
            ]
        },
        "ansible_domain": "",
        "ansible_effective_group_id": 1000,
        "ansible_effective_user_id": 1000,
        "ansible_env": {
            "HOME": "/home/vagrant",
            "LANG": "en_US.UTF-8",
            "LOGNAME": "vagrant",
            "MAIL": "/var/mail/vagrant",
            "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games",
            "PWD": "/home/vagrant",
            "SHELL": "/bin/bash",
            "SHLVL": "1",
            "SSH_CLIENT": "172.28.128.1 60684 22",
            "SSH_CONNECTION": "172.28.128.1 60684 172.28.128.13 22",
            "SSH_TTY": "/dev/pts/3",
            "TERM": "xterm-256color",
            "USER": "vagrant",
            "XDG_RUNTIME_DIR": "/run/user/1000",
            "XDG_SESSION_ID": "54",
            "_": "/bin/sh"
        },
        "ansible_eth0": {
            "active": true,
            "device": "eth0",
            "features": {
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "off [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off",
                "rx_checksumming": "off",
                "rx_fcs": "off",
                "rx_vlan_filter": "on [fixed]",
                "rx_vlan_offload": "on",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_segmentation": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipip_segmentation": "off [fixed]",
                "tx_lockless": "off [fixed]",
                "tx_mpls_segmentation": "off [fixed]",
                "tx_nocache_copy": "on",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "off [fixed]",
                "tx_sit_segmentation": "off [fixed]",
                "tx_tcp6_segmentation": "off [fixed]",
                "tx_tcp_ecn_segmentation": "off [fixed]",
                "tx_tcp_segmentation": "on",
                "tx_udp_tnl_segmentation": "off [fixed]",
                "tx_vlan_offload": "on [fixed]",
                "tx_vlan_stag_hw_insert": "off [fixed]",
                "udp_fragmentation_offload": "off [fixed]",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "ipv4": {
                "address": "10.0.2.15",
                "broadcast": "10.0.2.255",
                "netmask": "255.255.255.0",
                "network": "10.0.2.0"
            },
            "ipv6": [
                {
                    "address": "fe80::a00:27ff:fe97:31f6",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "08:00:27:97:31:f6",
            "module": "e1000",
            "mtu": 1500,
            "pciid": "0000:00:03.0",
            "promisc": false,
            "speed": 1000,
            "timestamping": [
                "tx_software",
                "rx_software",
                "software"
            ],
            "type": "ether"
        },
        "ansible_eth1": {
            "active": true,
            "device": "eth1",
            "features": {
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "off [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off",
                "rx_checksumming": "off",
                "rx_fcs": "off",
                "rx_vlan_filter": "on [fixed]",
                "rx_vlan_offload": "on",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_segmentation": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipip_segmentation": "off [fixed]",
                "tx_lockless": "off [fixed]",
                "tx_mpls_segmentation": "off [fixed]",
                "tx_nocache_copy": "on",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "off [fixed]",
                "tx_sit_segmentation": "off [fixed]",
                "tx_tcp6_segmentation": "off [fixed]",
                "tx_tcp_ecn_segmentation": "off [fixed]",
                "tx_tcp_segmentation": "on",
                "tx_udp_tnl_segmentation": "off [fixed]",
                "tx_vlan_offload": "on [fixed]",
                "tx_vlan_stag_hw_insert": "off [fixed]",
                "udp_fragmentation_offload": "off [fixed]",
                "vlan_challenged": "off [fixed]"
            },
            "hw_timestamp_filters": [],
            "ipv4": {
                "address": "172.28.128.13",
                "broadcast": "172.28.128.255",
                "netmask": "255.255.255.0",
                "network": "172.28.128.0"
            },
            "macaddress": "08:00:27:3f:a4:8d",
            "module": "e1000",
            "mtu": 1500,
            "pciid": "0000:00:08.0",
            "promisc": false,
            "speed": 1000,
            "timestamping": [
                "tx_software",
                "rx_software",
                "software"
            ],
            "type": "ether"
        },
        "ansible_facts": {
            "all_ipv4_addresses": [
                "10.0.2.15",
                "172.28.128.13"
            ],
            "all_ipv6_addresses": [
                "fe80::a00:27ff:fe97:31f6"
            ],
            "ansible_local": {},
            "apparmor": {
                "status": "enabled"
            },
            "architecture": "i386",
            "bios_date": "12/01/2006",
            "bios_version": "VirtualBox",
            "cmdline": {
                "BOOT_IMAGE": "/boot/vmlinuz-3.13.0-161-generic",
                "console": "ttyS0",
                "ro": true,
                "root": "UUID=2220679a-bcf3-402c-9e25-d36ec301949e"
            },
            "date_time": {
                "date": "2018-11-06",
                "day": "06",
                "epoch": "1541533018",
                "hour": "19",
                "iso8601": "2018-11-06T19:36:58Z",
                "iso8601_basic": "20181106T193658037480",
                "iso8601_basic_short": "20181106T193658",
                "iso8601_micro": "2018-11-06T19:36:58.037547Z",
                "minute": "36",
                "month": "11",
                "second": "58",
                "time": "19:36:58",
                "tz": "UTC",
                "tz_offset": "+0000",
                "weekday": "Tuesday",
                "weekday_number": "2",
                "weeknumber": "45",
                "year": "2018"
            },
            "default_ipv4": {
                "address": "10.0.2.15",
                "alias": "eth0",
                "broadcast": "10.0.2.255",
                "gateway": "10.0.2.2",
                "interface": "eth0",
                "macaddress": "08:00:27:97:31:f6",
                "mtu": 1500,
                "netmask": "255.255.255.0",
                "network": "10.0.2.0",
                "type": "ether"
            },
            "default_ipv6": {},
            "device_links": {
                "ids": {
                    "sda": [
                        "ata-VBOX_HARDDISK_VB0a12b175-65ac9ff7"
                    ],
                    "sda1": [
                        "ata-VBOX_HARDDISK_VB0a12b175-65ac9ff7-part1"
                    ]
                },
                "labels": {
                    "sda1": [
                        "cloudimg-rootfs"
                    ]
                },
                "masters": {},
                "uuids": {
                    "sda1": [
                        "2220679a-bcf3-402c-9e25-d36ec301949e"
                    ]
                }
            },
            "devices": {
                "loop0": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "0",
                    "sectorsize": "512",
                    "size": "0.00 Bytes",
                    "support_discard": "0",
                    "vendor": null,
                    "virtual": 1
                },
                "loop1": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "0",
                    "sectorsize": "512",
                    "size": "0.00 Bytes",
                    "support_discard": "0",
                    "vendor": null,
                    "virtual": 1
                },
                "loop2": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "0",
                    "sectorsize": "512",
                    "size": "0.00 Bytes",
                    "support_discard": "0",
                    "vendor": null,
                    "virtual": 1
                },
                "loop3": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "0",
                    "sectorsize": "512",
                    "size": "0.00 Bytes",
                    "support_discard": "0",
                    "vendor": null,
                    "virtual": 1
                },
                "loop4": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "0",
                    "sectorsize": "512",
                    "size": "0.00 Bytes",
                    "support_discard": "0",
                    "vendor": null,
                    "virtual": 1
                },
                "loop5": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "0",
                    "sectorsize": "512",
                    "size": "0.00 Bytes",
                    "support_discard": "0",
                    "vendor": null,
                    "virtual": 1
                },
                "loop6": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "0",
                    "sectorsize": "512",
                    "size": "0.00 Bytes",
                    "support_discard": "0",
                    "vendor": null,
                    "virtual": 1
                },
                "loop7": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "0",
                    "sectorsize": "512",
                    "size": "0.00 Bytes",
                    "support_discard": "0",
                    "vendor": null,
                    "virtual": 1
                },
                "ram0": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "131072",
                    "sectorsize": "512",
                    "size": "64.00 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "ram1": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "131072",
                    "sectorsize": "512",
                    "size": "64.00 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "ram10": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "131072",
                    "sectorsize": "512",
                    "size": "64.00 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "ram11": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "131072",
                    "sectorsize": "512",
                    "size": "64.00 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "ram12": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "131072",
                    "sectorsize": "512",
                    "size": "64.00 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "ram13": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "131072",
                    "sectorsize": "512",
                    "size": "64.00 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "ram14": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "131072",
                    "sectorsize": "512",
                    "size": "64.00 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "ram15": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "131072",
                    "sectorsize": "512",
                    "size": "64.00 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "ram2": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "131072",
                    "sectorsize": "512",
                    "size": "64.00 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "ram3": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "131072",
                    "sectorsize": "512",
                    "size": "64.00 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "ram4": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "131072",
                    "sectorsize": "512",
                    "size": "64.00 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "ram5": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "131072",
                    "sectorsize": "512",
                    "size": "64.00 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "ram6": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "131072",
                    "sectorsize": "512",
                    "size": "64.00 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "ram7": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "131072",
                    "sectorsize": "512",
                    "size": "64.00 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "ram8": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "131072",
                    "sectorsize": "512",
                    "size": "64.00 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "ram9": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "",
                    "sectors": "131072",
                    "sectorsize": "512",
                    "size": "64.00 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "sda": {
                    "holders": [],
                    "host": "SATA controller: Intel Corporation 82801HM/HEM (ICH8M/ICH8M-E) SATA Controller [AHCI mode] (rev 02)",
                    "links": {
                        "ids": [
                            "ata-VBOX_HARDDISK_VB0a12b175-65ac9ff7"
                        ],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": "VBOX HARDDISK",
                    "partitions": {
                        "sda1": {
                            "holders": [],
                            "links": {
                                "ids": [
                                    "ata-VBOX_HARDDISK_VB0a12b175-65ac9ff7-part1"
                                ],
                                "labels": [
                                    "cloudimg-rootfs"
                                ],
                                "masters": [],
                                "uuids": [
                                    "2220679a-bcf3-402c-9e25-d36ec301949e"
                                ]
                            },
                            "sectors": "83884032",
                            "sectorsize": 512,
                            "size": "40.00 GB",
                            "start": "2048",
                            "uuid": "2220679a-bcf3-402c-9e25-d36ec301949e"
                        }
                    },
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "deadline",
                    "sectors": "83886080",
                    "sectorsize": "512",
                    "size": "40.00 GB",
                    "support_discard": "0",
                    "vendor": "ATA",
                    "virtual": 1
                }
            },
            "distribution": "Ubuntu",
            "distribution_file_parsed": true,
            "distribution_file_path": "/etc/os-release",
            "distribution_file_variety": "Debian",
            "distribution_major_version": "14",
            "distribution_release": "trusty",
            "distribution_version": "14.04",
            "dns": {
                "nameservers": [
                    "10.0.2.3"
                ],
                "search": [
                    "ant.amazon.com"
                ]
            },
            "domain": "",
            "effective_group_id": 1000,
            "effective_user_id": 1000,
            "env": {
                "HOME": "/home/vagrant",
                "LANG": "en_US.UTF-8",
                "LOGNAME": "vagrant",
                "MAIL": "/var/mail/vagrant",
                "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games",
                "PWD": "/home/vagrant",
                "SHELL": "/bin/bash",
                "SHLVL": "1",
                "SSH_CLIENT": "172.28.128.1 60684 22",
                "SSH_CONNECTION": "172.28.128.1 60684 172.28.128.13 22",
                "SSH_TTY": "/dev/pts/3",
                "TERM": "xterm-256color",
                "USER": "vagrant",
                "XDG_RUNTIME_DIR": "/run/user/1000",
                "XDG_SESSION_ID": "54",
                "_": "/bin/sh"
            },
            "eth0": {
                "active": true,
                "device": "eth0",
                "features": {
                    "fcoe_mtu": "off [fixed]",
                    "generic_receive_offload": "on",
                    "generic_segmentation_offload": "on",
                    "highdma": "off [fixed]",
                    "l2_fwd_offload": "off [fixed]",
                    "large_receive_offload": "off [fixed]",
                    "loopback": "off [fixed]",
                    "netns_local": "off [fixed]",
                    "ntuple_filters": "off [fixed]",
                    "receive_hashing": "off [fixed]",
                    "rx_all": "off",
                    "rx_checksumming": "off",
                    "rx_fcs": "off",
                    "rx_vlan_filter": "on [fixed]",
                    "rx_vlan_offload": "on",
                    "rx_vlan_stag_filter": "off [fixed]",
                    "rx_vlan_stag_hw_parse": "off [fixed]",
                    "scatter_gather": "on",
                    "tcp_segmentation_offload": "on",
                    "tx_checksum_fcoe_crc": "off [fixed]",
                    "tx_checksum_ip_generic": "on",
                    "tx_checksum_ipv4": "off [fixed]",
                    "tx_checksum_ipv6": "off [fixed]",
                    "tx_checksum_sctp": "off [fixed]",
                    "tx_checksumming": "on",
                    "tx_fcoe_segmentation": "off [fixed]",
                    "tx_gre_segmentation": "off [fixed]",
                    "tx_gso_robust": "off [fixed]",
                    "tx_ipip_segmentation": "off [fixed]",
                    "tx_lockless": "off [fixed]",
                    "tx_mpls_segmentation": "off [fixed]",
                    "tx_nocache_copy": "on",
                    "tx_scatter_gather": "on",
                    "tx_scatter_gather_fraglist": "off [fixed]",
                    "tx_sit_segmentation": "off [fixed]",
                    "tx_tcp6_segmentation": "off [fixed]",
                    "tx_tcp_ecn_segmentation": "off [fixed]",
                    "tx_tcp_segmentation": "on",
                    "tx_udp_tnl_segmentation": "off [fixed]",
                    "tx_vlan_offload": "on [fixed]",
                    "tx_vlan_stag_hw_insert": "off [fixed]",
                    "udp_fragmentation_offload": "off [fixed]",
                    "vlan_challenged": "off [fixed]"
                },
                "hw_timestamp_filters": [],
                "ipv4": {
                    "address": "10.0.2.15",
                    "broadcast": "10.0.2.255",
                    "netmask": "255.255.255.0",
                    "network": "10.0.2.0"
                },
                "ipv6": [
                    {
                        "address": "fe80::a00:27ff:fe97:31f6",
                        "prefix": "64",
                        "scope": "link"
                    }
                ],
                "macaddress": "08:00:27:97:31:f6",
                "module": "e1000",
                "mtu": 1500,
                "pciid": "0000:00:03.0",
                "promisc": false,
                "speed": 1000,
                "timestamping": [
                    "tx_software",
                    "rx_software",
                    "software"
                ],
                "type": "ether"
            },
            "eth1": {
                "active": true,
                "device": "eth1",
                "features": {
                    "fcoe_mtu": "off [fixed]",
                    "generic_receive_offload": "on",
                    "generic_segmentation_offload": "on",
                    "highdma": "off [fixed]",
                    "l2_fwd_offload": "off [fixed]",
                    "large_receive_offload": "off [fixed]",
                    "loopback": "off [fixed]",
                    "netns_local": "off [fixed]",
                    "ntuple_filters": "off [fixed]",
                    "receive_hashing": "off [fixed]",
                    "rx_all": "off",
                    "rx_checksumming": "off",
                    "rx_fcs": "off",
                    "rx_vlan_filter": "on [fixed]",
                    "rx_vlan_offload": "on",
                    "rx_vlan_stag_filter": "off [fixed]",
                    "rx_vlan_stag_hw_parse": "off [fixed]",
                    "scatter_gather": "on",
                    "tcp_segmentation_offload": "on",
                    "tx_checksum_fcoe_crc": "off [fixed]",
                    "tx_checksum_ip_generic": "on",
                    "tx_checksum_ipv4": "off [fixed]",
                    "tx_checksum_ipv6": "off [fixed]",
                    "tx_checksum_sctp": "off [fixed]",
                    "tx_checksumming": "on",
                    "tx_fcoe_segmentation": "off [fixed]",
                    "tx_gre_segmentation": "off [fixed]",
                    "tx_gso_robust": "off [fixed]",
                    "tx_ipip_segmentation": "off [fixed]",
                    "tx_lockless": "off [fixed]",
                    "tx_mpls_segmentation": "off [fixed]",
                    "tx_nocache_copy": "on",
                    "tx_scatter_gather": "on",
                    "tx_scatter_gather_fraglist": "off [fixed]",
                    "tx_sit_segmentation": "off [fixed]",
                    "tx_tcp6_segmentation": "off [fixed]",
                    "tx_tcp_ecn_segmentation": "off [fixed]",
                    "tx_tcp_segmentation": "on",
                    "tx_udp_tnl_segmentation": "off [fixed]",
                    "tx_vlan_offload": "on [fixed]",
                    "tx_vlan_stag_hw_insert": "off [fixed]",
                    "udp_fragmentation_offload": "off [fixed]",
                    "vlan_challenged": "off [fixed]"
                },
                "hw_timestamp_filters": [],
                "ipv4": {
                    "address": "172.28.128.13",
                    "broadcast": "172.28.128.255",
                    "netmask": "255.255.255.0",
                    "network": "172.28.128.0"
                },
                "macaddress": "08:00:27:3f:a4:8d",
                "module": "e1000",
                "mtu": 1500,
                "pciid": "0000:00:08.0",
                "promisc": false,
                "speed": 1000,
                "timestamping": [
                    "tx_software",
                    "rx_software",
                    "software"
                ],
                "type": "ether"
            },
            "facter_architecture": "i386",
            "facter_augeasversion": "1.2.0",
            "facter_blockdevice_sda_model": "VBOX HARDDISK",
            "facter_blockdevice_sda_size": 42949672960,
            "facter_blockdevice_sda_vendor": "ATA",
            "facter_blockdevices": "sda",
            "facter_domain": "ant.amazon.com",
            "facter_facterversion": "1.7.5",
            "facter_filesystems": "ext2,ext3,ext4,vfat",
            "facter_fqdn": "ubuntu-a.ant.amazon.com",
            "facter_hardwareisa": "i686",
            "facter_hardwaremodel": "i686",
            "facter_hostname": "ubuntu-a",
            "facter_id": "vagrant",
            "facter_interfaces": "eth0,eth1,lo",
            "facter_ipaddress": "10.0.2.15",
            "facter_ipaddress_eth0": "10.0.2.15",
            "facter_ipaddress_eth1": "172.28.128.13",
            "facter_ipaddress_lo": "127.0.0.1",
            "facter_is_virtual": "true",
            "facter_kernel": "Linux",
            "facter_kernelmajversion": "3.13",
            "facter_kernelrelease": "3.13.0-161-generic",
            "facter_kernelversion": "3.13.0",
            "facter_lsbdistcodename": "trusty",
            "facter_lsbdistdescription": "Ubuntu 14.04.5 LTS",
            "facter_lsbdistid": "Ubuntu",
            "facter_lsbdistrelease": "14.04",
            "facter_lsbmajdistrelease": "14",
            "facter_macaddress": "08:00:27:97:31:f6",
            "facter_macaddress_eth0": "08:00:27:97:31:f6",
            "facter_macaddress_eth1": "08:00:27:3f:a4:8d",
            "facter_memoryfree": "386.86 MB",
            "facter_memoryfree_mb": "386.86",
            "facter_memorysize": "495.17 MB",
            "facter_memorysize_mb": "495.17",
            "facter_memorytotal": "495.17 MB",
            "facter_mtu_eth0": "1500",
            "facter_mtu_eth1": "1500",
            "facter_mtu_lo": "65536",
            "facter_netmask": "255.255.255.0",
            "facter_netmask_eth0": "255.255.255.0",
            "facter_netmask_eth1": "255.255.255.0",
            "facter_netmask_lo": "255.0.0.0",
            "facter_network_eth0": "10.0.2.0",
            "facter_network_eth1": "172.28.128.0",
            "facter_network_lo": "127.0.0.0",
            "facter_operatingsystem": "Ubuntu",
            "facter_operatingsystemrelease": "14.04",
            "facter_osfamily": "Debian",
            "facter_path": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games",
            "facter_physicalprocessorcount": 1,
            "facter_processor0": "Intel(R) Core(TM) i7-5557U CPU @ 3.10GHz",
            "facter_processorcount": "1",
            "facter_ps": "ps -ef",
            "facter_puppetversion": "3.4.3",
            "facter_rubysitedir": "/usr/local/lib/site_ruby/1.9.1",
            "facter_rubyversion": "1.9.3",
            "facter_selinux": "false",
            "facter_sshdsakey": "AAAAB3NzaC1kc3MAAACBAK56mnvTORwkWIQLjaJPFTVxx+mRqfZ9xX3YmrYwhcMYgEpIldHXLrPaUqWG+qv+Mab9oFGTAfgKmV1kg9dDVTeOJQ/+6Is49ZcXntOpftrKOFakL//TP3EvhpA7Go3AOD1vWggZGmvpt8WFqOdV0YfJcGTPj8rx1jn2ZKit7JTxAAAAFQDdHiC5s7voC1AvAEAX3iAWdto6mQAAAIASeHhuQjLQD0p4ArI8XG/ntmtGn5q3wzTEown2DLiQa9SeASmeZNcqFtBgi6kj8O6G1TzkTHlzdnlZ3jnmjxoIXUIlC9rmjQtrwjlQ//ECjkAVFLgaZCL5J1+Ac7oUMp4VBAedQ4hH5wWAgOsf77YTQJlgiAYX7hrVHqhbR9GLPwAAAIBXUS9IBULysp+GY25NkCTljzJh7drINLAttNq+6pINb6Z3KOSsy9qsZsx0t+P1soPnd27d5lqnkOUOO8L3n6AIDxdaXx6+Sabtd+bTv7cqhq6QsLnU2Z++BoFwA8e3vvKt93rjkBr9nwSyeT1KLErKDVAgLu2LImOzd4Z8EZa+YA==",
            "facter_sshecdsakey": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDIuYZMhwUecIboGpQiYKyofk290b78CwZmT4ofBxyGwWqNR7CSXL7SgOem1x4dMLmmMxGqAbSkuoTLNOByRZY8=",
            "facter_sshfp_dsa": "SSHFP 2 1 5056908a4b35ba887a7bcb8a8faec30dbc7f2872\nSSHFP 2 2 eab9aabdd0013bdd2c3e01a1f13af9529ad0e4536a6d848696f458b79994d9b0",
            "facter_sshfp_ecdsa": "SSHFP 3 1 04b63504942a7a1ce2da9690e92204098d9efd6f\nSSHFP 3 2 933d8847b718e6e015ec1781b8dcb81b1de7e03df8740b977fc3e1892362093d",
            "facter_sshfp_rsa": "SSHFP 1 1 3d53b7b9b478f6925a9c14822455e44633789965\nSSHFP 1 2 5cde1c6808c1d806b52f05e4e3842ab1a59bbc0ee13110da0d253ab486846d20",
            "facter_sshrsakey": "AAAAB3NzaC1yc2EAAAADAQABAAABAQC2uIdHdpKOK3GIbYDLtUvHhUo9rSERuT6WqmZ9G3x7X0ynnofbKMAuzHKtZ5fJBF2YLcDZNX08nZcPAjILQXN6rVoW6mBD/HOcU6NHplSouAnArqYrPrUwm/GHrS+vIQOhjQ547019FxzkiMCrIDyU23fK9klK6ePYY4hicvQX9dD8/n4B5YusSA3L+W0znxAp+d+XrpDcbyO3CPrI7Tvzw9N0irftssnx5DP5f8kxeDGwYoSjxlA+l3hnMgxP59W2kr8LlLinRPVExvQNkj+N8qWMyjnYP9yzSoHn7NiwiI/mdjiIABHEmkxKBYzukX2grkBHp3W6TqFMAjVofku/",
            "facter_swapfree": "0.00 MB",
            "facter_swapfree_mb": "0.00",
            "facter_swapsize": "0.00 MB",
            "facter_swapsize_mb": "0.00",
            "facter_timezone": "UTC",
            "facter_uniqueid": "007f0101",
            "facter_uptime": "1:10 hours",
            "facter_uptime_days": 0,
            "facter_uptime_hours": 1,
            "facter_uptime_seconds": 4206,
            "facter_virtual": "virtualbox",
            "fips": false,
            "form_factor": "Other",
            "fqdn": "Ubuntu-A",
            "gather_subset": [
                "all"
            ],
            "hostname": "ubuntu-a",
            "interfaces": [
                "lo",
                "eth1",
                "eth0"
            ],
            "is_chroot": false,
            "iscsi_iqn": "",
            "kernel": "3.13.0-161-generic",
            "lo": {
                "active": true,
                "device": "lo",
                "features": {
                    "fcoe_mtu": "off [fixed]",
                    "generic_receive_offload": "on",
                    "generic_segmentation_offload": "on",
                    "highdma": "on [fixed]",
                    "l2_fwd_offload": "off [fixed]",
                    "large_receive_offload": "off [fixed]",
                    "loopback": "on [fixed]",
                    "netns_local": "on [fixed]",
                    "ntuple_filters": "off [fixed]",
                    "receive_hashing": "off [fixed]",
                    "rx_all": "off [fixed]",
                    "rx_checksumming": "on [fixed]",
                    "rx_fcs": "off [fixed]",
                    "rx_vlan_filter": "off [fixed]",
                    "rx_vlan_offload": "off [fixed]",
                    "rx_vlan_stag_filter": "off [fixed]",
                    "rx_vlan_stag_hw_parse": "off [fixed]",
                    "scatter_gather": "on",
                    "tcp_segmentation_offload": "on",
                    "tx_checksum_fcoe_crc": "off [fixed]",
                    "tx_checksum_ip_generic": "on [fixed]",
                    "tx_checksum_ipv4": "off [fixed]",
                    "tx_checksum_ipv6": "off [fixed]",
                    "tx_checksum_sctp": "off [fixed]",
                    "tx_checksumming": "on",
                    "tx_fcoe_segmentation": "off [fixed]",
                    "tx_gre_segmentation": "off [fixed]",
                    "tx_gso_robust": "off [fixed]",
                    "tx_ipip_segmentation": "off [fixed]",
                    "tx_lockless": "on [fixed]",
                    "tx_mpls_segmentation": "off [fixed]",
                    "tx_nocache_copy": "off [fixed]",
                    "tx_scatter_gather": "on [fixed]",
                    "tx_scatter_gather_fraglist": "on [fixed]",
                    "tx_sit_segmentation": "off [fixed]",
                    "tx_tcp6_segmentation": "on",
                    "tx_tcp_ecn_segmentation": "on",
                    "tx_tcp_segmentation": "on",
                    "tx_udp_tnl_segmentation": "off [fixed]",
                    "tx_vlan_offload": "off [fixed]",
                    "tx_vlan_stag_hw_insert": "off [fixed]",
                    "udp_fragmentation_offload": "on",
                    "vlan_challenged": "on [fixed]"
                },
                "hw_timestamp_filters": [],
                "ipv4": {
                    "address": "127.0.0.1",
                    "broadcast": "host",
                    "netmask": "255.0.0.0",
                    "network": "127.0.0.0"
                },
                "ipv6": [
                    {
                        "address": "::1",
                        "prefix": "128",
                        "scope": "host"
                    }
                ],
                "mtu": 65536,
                "promisc": false,
                "timestamping": [
                    "rx_software",
                    "software"
                ],
                "type": "loopback"
            },
            "lsb": {
                "codename": "trusty",
                "description": "Ubuntu 14.04.5 LTS",
                "id": "Ubuntu",
                "major_release": "14",
                "release": "14.04"
            },
            "machine": "i686",
            "machine_id": "5afee93f1bceaef72b1460d35be1dd04",
            "memfree_mb": 110,
            "memory_mb": {
                "nocache": {
                    "free": 403,
                    "used": 92
                },
                "real": {
                    "free": 110,
                    "total": 495,
                    "used": 385
                },
                "swap": {
                    "cached": 0,
                    "free": 0,
                    "total": 0,
                    "used": 0
                }
            },
            "memtotal_mb": 495,
            "module_setup": true,
            "mounts": [
                {
                    "block_available": 9530402,
                    "block_size": 4096,
                    "block_total": 10312784,
                    "block_used": 782382,
                    "device": "/dev/sda1",
                    "fstype": "ext4",
                    "inode_available": 2549102,
                    "inode_total": 2621440,
                    "inode_used": 72338,
                    "mount": "/",
                    "options": "rw",
                    "size_available": 39036526592,
                    "size_total": 42241163264,
                    "uuid": "2220679a-bcf3-402c-9e25-d36ec301949e"
                }
            ],
            "nodename": "ubuntu-a",
            "ohai_block_device": {
                "loop0": {
                    "removable": "0",
                    "size": "0"
                },
                "loop1": {
                    "removable": "0",
                    "size": "0"
                },
                "loop2": {
                    "removable": "0",
                    "size": "0"
                },
                "loop3": {
                    "removable": "0",
                    "size": "0"
                },
                "loop4": {
                    "removable": "0",
                    "size": "0"
                },
                "loop5": {
                    "removable": "0",
                    "size": "0"
                },
                "loop6": {
                    "removable": "0",
                    "size": "0"
                },
                "loop7": {
                    "removable": "0",
                    "size": "0"
                },
                "ram0": {
                    "removable": "0",
                    "size": "131072"
                },
                "ram1": {
                    "removable": "0",
                    "size": "131072"
                },
                "ram10": {
                    "removable": "0",
                    "size": "131072"
                },
                "ram11": {
                    "removable": "0",
                    "size": "131072"
                },
                "ram12": {
                    "removable": "0",
                    "size": "131072"
                },
                "ram13": {
                    "removable": "0",
                    "size": "131072"
                },
                "ram14": {
                    "removable": "0",
                    "size": "131072"
                },
                "ram15": {
                    "removable": "0",
                    "size": "131072"
                },
                "ram2": {
                    "removable": "0",
                    "size": "131072"
                },
                "ram3": {
                    "removable": "0",
                    "size": "131072"
                },
                "ram4": {
                    "removable": "0",
                    "size": "131072"
                },
                "ram5": {
                    "removable": "0",
                    "size": "131072"
                },
                "ram6": {
                    "removable": "0",
                    "size": "131072"
                },
                "ram7": {
                    "removable": "0",
                    "size": "131072"
                },
                "ram8": {
                    "removable": "0",
                    "size": "131072"
                },
                "ram9": {
                    "removable": "0",
                    "size": "131072"
                },
                "sda": {
                    "model": "VBOX HARDDISK",
                    "removable": "0",
                    "rev": "1.0",
                    "size": "83886080",
                    "state": "running",
                    "timeout": "30",
                    "vendor": "ATA"
                }
            },
            "ohai_chef_packages": {
                "chef": {
                    "chef_root": "/usr/lib/ruby/vendor_ruby",
                    "version": "11.8.2"
                },
                "ohai": {
                    "ohai_root": "/usr/lib/ruby/vendor_ruby/ohai",
                    "version": "6.14.0"
                }
            },
            "ohai_command": {
                "ps": "ps -ef"
            },
            "ohai_counters": {
                "network": {
                    "interfaces": {
                        "eth0": {
                            "rx": {
                                "bytes": "621873",
                                "drop": "0",
                                "errors": "0",
                                "overrun": "0",
                                "packets": "2309"
                            },
                            "tx": {
                                "bytes": "176404",
                                "carrier": "0",
                                "collisions": "0",
                                "drop": "0",
                                "errors": "0",
                                "packets": "1580",
                                "queuelen": "1000"
                            }
                        },
                        "eth1": {
                            "rx": {
                                "bytes": "7981579",
                                "drop": "0",
                                "errors": "0",
                                "overrun": "0",
                                "packets": "10224"
                            },
                            "tx": {
                                "bytes": "1412084",
                                "carrier": "0",
                                "collisions": "0",
                                "drop": "0",
                                "errors": "0",
                                "packets": "6582",
                                "queuelen": "1000"
                            }
                        },
                        "lo": {
                            "rx": {
                                "bytes": "0",
                                "drop": "0",
                                "errors": "0",
                                "overrun": "0",
                                "packets": "0"
                            },
                            "tx": {
                                "bytes": "0",
                                "carrier": "0",
                                "collisions": "0",
                                "drop": "0",
                                "errors": "0",
                                "packets": "0"
                            }
                        }
                    }
                }
            },
            "ohai_cpu": {
                "0": {
                    "cache_size": "4096 KB",
                    "core_id": "0",
                    "cores": "1",
                    "family": "6",
                    "flags": [
                        "fpu",
                        "vme",
                        "de",
                        "pse",
                        "tsc",
                        "msr",
                        "pae",
                        "mce",
                        "cx8",
                        "apic",
                        "sep",
                        "mtrr",
                        "pge",
                        "mca",
                        "cmov",
                        "pat",
                        "pse36",
                        "clflush",
                        "mmx",
                        "fxsr",
                        "sse",
                        "sse2",
                        "ht",
                        "syscall",
                        "nx",
                        "rdtscp",
                        "lm",
                        "constant_tsc",
                        "xtopology",
                        "nonstop_tsc",
                        "eagerfpu",
                        "pni",
                        "pclmulqdq",
                        "ssse3",
                        "cx16",
                        "sse4_1",
                        "sse4_2",
                        "movbe",
                        "popcnt",
                        "aes",
                        "xsave",
                        "avx",
                        "rdrand",
                        "lahf_lm",
                        "abm",
                        "3dnowprefetch",
                        "rsb_ctxsw",
                        "retpoline",
                        "fsgsbase",
                        "avx2",
                        "invpcid",
                        "rdseed",
                        "flush_l1d"
                    ],
                    "mhz": "3099.419",
                    "model": "61",
                    "model_name": "Intel(R) Core(TM) i7-5557U CPU @ 3.10GHz",
                    "physical_id": "0",
                    "stepping": "4",
                    "vendor_id": "GenuineIntel"
                },
                "real": 1,
                "total": 1
            },
            "ohai_current_user": "vagrant",
            "ohai_dmi": {
                "dmidecode_version": "2.12"
            },
            "ohai_domain": null,
            "ohai_etc": {
                "group": {
                    "adm": {
                        "gid": 4,
                        "members": [
                            "syslog",
                            "ubuntu"
                        ]
                    },
                    "admin": {
                        "gid": 110,
                        "members": []
                    },
                    "audio": {
                        "gid": 29,
                        "members": [
                            "ubuntu"
                        ]
                    },
                    "backup": {
                        "gid": 34,
                        "members": []
                    },
                    "bin": {
                        "gid": 2,
                        "members": []
                    },
                    "cdrom": {
                        "gid": 24,
                        "members": [
                            "ubuntu"
                        ]
                    },
                    "colord": {
                        "gid": 112,
                        "members": []
                    },
                    "crontab": {
                        "gid": 103,
                        "members": []
                    },
                    "daemon": {
                        "gid": 1,
                        "members": []
                    },
                    "dialout": {
                        "gid": 20,
                        "members": [
                            "ubuntu"
                        ]
                    },
                    "dip": {
                        "gid": 30,
                        "members": [
                            "ubuntu"
                        ]
                    },
                    "disk": {
                        "gid": 6,
                        "members": []
                    },
                    "fax": {
                        "gid": 21,
                        "members": []
                    },
                    "floppy": {
                        "gid": 25,
                        "members": [
                            "ubuntu"
                        ]
                    },
                    "fuse": {
                        "gid": 105,
                        "members": []
                    },
                    "games": {
                        "gid": 60,
                        "members": []
                    },
                    "gnats": {
                        "gid": 41,
                        "members": []
                    },
                    "irc": {
                        "gid": 39,
                        "members": []
                    },
                    "kmem": {
                        "gid": 15,
                        "members": []
                    },
                    "landscape": {
                        "gid": 109,
                        "members": []
                    },
                    "libuuid": {
                        "gid": 101,
                        "members": []
                    },
                    "list": {
                        "gid": 38,
                        "members": []
                    },
                    "lp": {
                        "gid": 7,
                        "members": []
                    },
                    "mail": {
                        "gid": 8,
                        "members": []
                    },
                    "man": {
                        "gid": 12,
                        "members": []
                    },
                    "messagebus": {
                        "gid": 106,
                        "members": []
                    },
                    "mlocate": {
                        "gid": 107,
                        "members": []
                    },
                    "netdev": {
                        "gid": 102,
                        "members": [
                            "ubuntu"
                        ]
                    },
                    "news": {
                        "gid": 9,
                        "members": []
                    },
                    "nogroup": {
                        "gid": 65534,
                        "members": []
                    },
                    "operator": {
                        "gid": 37,
                        "members": []
                    },
                    "plugdev": {
                        "gid": 46,
                        "members": [
                            "ubuntu"
                        ]
                    },
                    "proxy": {
                        "gid": 13,
                        "members": []
                    },
                    "puppet": {
                        "gid": 114,
                        "members": []
                    },
                    "redis": {
                        "gid": 115,
                        "members": []
                    },
                    "root": {
                        "gid": 0,
                        "members": []
                    },
                    "sasl": {
                        "gid": 45,
                        "members": []
                    },
                    "scanner": {
                        "gid": 111,
                        "members": []
                    },
                    "shadow": {
                        "gid": 42,
                        "members": []
                    },
                    "src": {
                        "gid": 40,
                        "members": []
                    },
                    "ssh": {
                        "gid": 108,
                        "members": []
                    },
                    "staff": {
                        "gid": 50,
                        "members": []
                    },
                    "sudo": {
                        "gid": 27,
                        "members": [
                            "ubuntu"
                        ]
                    },
                    "sys": {
                        "gid": 3,
                        "members": []
                    },
                    "syslog": {
                        "gid": 104,
                        "members": []
                    },
                    "tape": {
                        "gid": 26,
                        "members": []
                    },
                    "tty": {
                        "gid": 5,
                        "members": []
                    },
                    "ubuntu": {
                        "gid": 1001,
                        "members": []
                    },
                    "users": {
                        "gid": 100,
                        "members": []
                    },
                    "utmp": {
                        "gid": 43,
                        "members": []
                    },
                    "uucp": {
                        "gid": 10,
                        "members": []
                    },
                    "vagrant": {
                        "gid": 1000,
                        "members": []
                    },
                    "vboxsf": {
                        "gid": 113,
                        "members": []
                    },
                    "video": {
                        "gid": 44,
                        "members": [
                            "ubuntu"
                        ]
                    },
                    "voice": {
                        "gid": 22,
                        "members": []
                    },
                    "www-data": {
                        "gid": 33,
                        "members": []
                    }
                },
                "passwd": {
                    "backup": {
                        "dir": "/var/backups",
                        "gecos": "backup",
                        "gid": 34,
                        "shell": "/usr/sbin/nologin",
                        "uid": 34
                    },
                    "bin": {
                        "dir": "/bin",
                        "gecos": "bin",
                        "gid": 2,
                        "shell": "/usr/sbin/nologin",
                        "uid": 2
                    },
                    "colord": {
                        "dir": "/var/lib/colord",
                        "gecos": "colord colour management daemon,,,",
                        "gid": 112,
                        "shell": "/bin/false",
                        "uid": 106
                    },
                    "daemon": {
                        "dir": "/usr/sbin",
                        "gecos": "daemon",
                        "gid": 1,
                        "shell": "/usr/sbin/nologin",
                        "uid": 1
                    },
                    "games": {
                        "dir": "/usr/games",
                        "gecos": "games",
                        "gid": 60,
                        "shell": "/usr/sbin/nologin",
                        "uid": 5
                    },
                    "gnats": {
                        "dir": "/var/lib/gnats",
                        "gecos": "Gnats Bug-Reporting System (admin)",
                        "gid": 41,
                        "shell": "/usr/sbin/nologin",
                        "uid": 41
                    },
                    "irc": {
                        "dir": "/var/run/ircd",
                        "gecos": "ircd",
                        "gid": 39,
                        "shell": "/usr/sbin/nologin",
                        "uid": 39
                    },
                    "landscape": {
                        "dir": "/var/lib/landscape",
                        "gecos": "",
                        "gid": 109,
                        "shell": "/bin/false",
                        "uid": 103
                    },
                    "libuuid": {
                        "dir": "/var/lib/libuuid",
                        "gecos": "",
                        "gid": 101,
                        "shell": "",
                        "uid": 100
                    },
                    "list": {
                        "dir": "/var/list",
                        "gecos": "Mailing List Manager",
                        "gid": 38,
                        "shell": "/usr/sbin/nologin",
                        "uid": 38
                    },
                    "lp": {
                        "dir": "/var/spool/lpd",
                        "gecos": "lp",
                        "gid": 7,
                        "shell": "/usr/sbin/nologin",
                        "uid": 7
                    },
                    "mail": {
                        "dir": "/var/mail",
                        "gecos": "mail",
                        "gid": 8,
                        "shell": "/usr/sbin/nologin",
                        "uid": 8
                    },
                    "man": {
                        "dir": "/var/cache/man",
                        "gecos": "man",
                        "gid": 12,
                        "shell": "/usr/sbin/nologin",
                        "uid": 6
                    },
                    "messagebus": {
                        "dir": "/var/run/dbus",
                        "gecos": "",
                        "gid": 106,
                        "shell": "/bin/false",
                        "uid": 102
                    },
                    "news": {
                        "dir": "/var/spool/news",
                        "gecos": "news",
                        "gid": 9,
                        "shell": "/usr/sbin/nologin",
                        "uid": 9
                    },
                    "nobody": {
                        "dir": "/nonexistent",
                        "gecos": "nobody",
                        "gid": 65534,
                        "shell": "/usr/sbin/nologin",
                        "uid": 65534
                    },
                    "pollinate": {
                        "dir": "/var/cache/pollinate",
                        "gecos": "",
                        "gid": 1,
                        "shell": "/bin/false",
                        "uid": 105
                    },
                    "proxy": {
                        "dir": "/bin",
                        "gecos": "proxy",
                        "gid": 13,
                        "shell": "/usr/sbin/nologin",
                        "uid": 13
                    },
                    "puppet": {
                        "dir": "/var/lib/puppet",
                        "gecos": "Puppet configuration management daemon,,,",
                        "gid": 114,
                        "shell": "/bin/false",
                        "uid": 108
                    },
                    "redis": {
                        "dir": "/var/lib/redis",
                        "gecos": "redis server,,,",
                        "gid": 115,
                        "shell": "/bin/false",
                        "uid": 109
                    },
                    "root": {
                        "dir": "/root",
                        "gecos": "root",
                        "gid": 0,
                        "shell": "/bin/bash",
                        "uid": 0
                    },
                    "sshd": {
                        "dir": "/var/run/sshd",
                        "gecos": "",
                        "gid": 65534,
                        "shell": "/usr/sbin/nologin",
                        "uid": 104
                    },
                    "statd": {
                        "dir": "/var/lib/nfs",
                        "gecos": "",
                        "gid": 65534,
                        "shell": "/bin/false",
                        "uid": 107
                    },
                    "sync": {
                        "dir": "/bin",
                        "gecos": "sync",
                        "gid": 65534,
                        "shell": "/bin/sync",
                        "uid": 4
                    },
                    "sys": {
                        "dir": "/dev",
                        "gecos": "sys",
                        "gid": 3,
                        "shell": "/usr/sbin/nologin",
                        "uid": 3
                    },
                    "syslog": {
                        "dir": "/home/syslog",
                        "gecos": "",
                        "gid": 104,
                        "shell": "/bin/false",
                        "uid": 101
                    },
                    "ubuntu": {
                        "dir": "/home/ubuntu",
                        "gecos": "Ubuntu",
                        "gid": 1001,
                        "shell": "/bin/bash",
                        "uid": 1001
                    },
                    "uucp": {
                        "dir": "/var/spool/uucp",
                        "gecos": "uucp",
                        "gid": 10,
                        "shell": "/usr/sbin/nologin",
                        "uid": 10
                    },
                    "vagrant": {
                        "dir": "/home/vagrant",
                        "gecos": "",
                        "gid": 1000,
                        "shell": "/bin/bash",
                        "uid": 1000
                    },
                    "www-data": {
                        "dir": "/var/www",
                        "gecos": "www-data",
                        "gid": 33,
                        "shell": "/usr/sbin/nologin",
                        "uid": 33
                    }
                }
            },
            "ohai_filesystem": {
                "/dev/sda1": {
                    "fs_type": "ext4",
                    "kb_available": "38121608",
                    "kb_size": "41251136",
                    "kb_used": "1393616",
                    "label": "cloudimg-rootfs",
                    "mount": "/",
                    "mount_options": [
                        "rw"
                    ],
                    "percent_used": "4%",
                    "uuid": "2220679a-bcf3-402c-9e25-d36ec301949e"
                },
                "devpts": {
                    "fs_type": "devpts",
                    "mount": "/dev/pts",
                    "mount_options": [
                        "rw",
                        "noexec",
                        "nosuid",
                        "gid=5",
                        "mode=0620"
                    ]
                },
                "none": {
                    "fs_type": "pstore",
                    "kb_available": "418379372",
                    "kb_size": "487374848",
                    "kb_used": "68995476",
                    "mount": "/sys/fs/pstore",
                    "mount_options": [
                        "rw"
                    ],
                    "percent_used": "15%"
                },
                "proc": {
                    "fs_type": "proc",
                    "mount": "/proc",
                    "mount_options": [
                        "rw",
                        "noexec",
                        "nosuid",
                        "nodev"
                    ]
                },
                "rootfs": {
                    "fs_type": "rootfs",
                    "mount": "/",
                    "mount_options": [
                        "rw"
                    ]
                },
                "rpc_pipefs": {
                    "fs_type": "rpc_pipefs",
                    "mount": "/run/rpc_pipefs",
                    "mount_options": [
                        "rw"
                    ]
                },
                "sysfs": {
                    "fs_type": "sysfs",
                    "mount": "/sys",
                    "mount_options": [
                        "rw",
                        "noexec",
                        "nosuid",
                        "nodev"
                    ]
                },
                "systemd": {
                    "fs_type": "cgroup",
                    "mount": "/sys/fs/cgroup/systemd",
                    "mount_options": [
                        "rw",
                        "noexec",
                        "nosuid",
                        "nodev",
                        "none",
                        "name=systemd"
                    ]
                },
                "tmpfs": {
                    "fs_type": "tmpfs",
                    "kb_available": "50312",
                    "kb_size": "50708",
                    "kb_used": "396",
                    "mount": "/run",
                    "mount_options": [
                        "rw",
                        "noexec",
                        "nosuid",
                        "size=10%",
                        "mode=0755"
                    ],
                    "percent_used": "1%"
                },
                "udev": {
                    "fs_type": "devtmpfs",
                    "kb_available": "249824",
                    "kb_size": "249836",
                    "kb_used": "12",
                    "mount": "/dev",
                    "mount_options": [
                        "rw",
                        "mode=0755"
                    ],
                    "percent_used": "1%"
                },
                "vagrant": {
                    "fs_type": "vboxsf",
                    "mount": "/vagrant",
                    "mount_options": [
                        "uid=1000",
                        "gid=1000",
                        "rw"
                    ]
                }
            },
            "ohai_fqdn": "Ubuntu-A",
            "ohai_hostname": "ubuntu-a",
            "ohai_idletime": "1 hours 05 minutes 34 seconds",
            "ohai_idletime_seconds": 3934,
            "ohai_ipaddress": "10.0.2.15",
            "ohai_kernel": {
                "machine": "i686",
                "modules": {
                    "ablk_helper": {
                        "refcount": "1",
                        "size": "13357"
                    },
                    "aes_i586": {
                        "refcount": "1",
                        "size": "16995"
                    },
                    "aesni_intel": {
                        "refcount": "0",
                        "size": "18156"
                    },
                    "ahci": {
                        "refcount": "1",
                        "size": "29739"
                    },
                    "auth_rpcgss": {
                        "refcount": "1",
                        "size": "48950"
                    },
                    "crc32_pclmul": {
                        "refcount": "0",
                        "size": "12967"
                    },
                    "cryptd": {
                        "refcount": "1",
                        "size": "15578"
                    },
                    "dm_crypt": {
                        "refcount": "0",
                        "size": "22589"
                    },
                    "e1000": {
                        "refcount": "0",
                        "size": "128548"
                    },
                    "fscache": {
                        "refcount": "1",
                        "size": "56803"
                    },
                    "gf128mul": {
                        "refcount": "2",
                        "size": "14503"
                    },
                    "joydev": {
                        "refcount": "0",
                        "size": "17101"
                    },
                    "libahci": {
                        "refcount": "1",
                        "size": "31310"
                    },
                    "lockd": {
                        "refcount": "2",
                        "size": "78462"
                    },
                    "lrw": {
                        "refcount": "1",
                        "size": "13057"
                    },
                    "nfs": {
                        "refcount": "0",
                        "size": "213471"
                    },
                    "nfs_acl": {
                        "refcount": "1",
                        "size": "12733"
                    },
                    "nfsd": {
                        "refcount": "2",
                        "size": "247731"
                    },
                    "psmouse": {
                        "refcount": "0",
                        "size": "95439"
                    },
                    "serio_raw": {
                        "refcount": "0",
                        "size": "13230"
                    },
                    "sunrpc": {
                        "refcount": "6",
                        "size": "246791"
                    },
                    "vboxguest": {
                        "refcount": "2",
                        "size": "223958"
                    },
                    "vboxsf": {
                        "refcount": "1",
                        "size": "42570"
                    },
                    "video": {
                        "refcount": "0",
                        "size": "18903"
                    },
                    "xts": {
                        "refcount": "1",
                        "size": "12749"
                    }
                },
                "name": "Linux",
                "os": "GNU/Linux",
                "release": "3.13.0-161-generic",
                "version": "#211-Ubuntu SMP Wed Oct 3 14:59:21 UTC 2018"
            },
            "ohai_keys": {
                "ssh": {
                    "host_dsa_public": "AAAAB3NzaC1kc3MAAACBAK56mnvTORwkWIQLjaJPFTVxx+mRqfZ9xX3YmrYwhcMYgEpIldHXLrPaUqWG+qv+Mab9oFGTAfgKmV1kg9dDVTeOJQ/+6Is49ZcXntOpftrKOFakL//TP3EvhpA7Go3AOD1vWggZGmvpt8WFqOdV0YfJcGTPj8rx1jn2ZKit7JTxAAAAFQDdHiC5s7voC1AvAEAX3iAWdto6mQAAAIASeHhuQjLQD0p4ArI8XG/ntmtGn5q3wzTEown2DLiQa9SeASmeZNcqFtBgi6kj8O6G1TzkTHlzdnlZ3jnmjxoIXUIlC9rmjQtrwjlQ//ECjkAVFLgaZCL5J1+Ac7oUMp4VBAedQ4hH5wWAgOsf77YTQJlgiAYX7hrVHqhbR9GLPwAAAIBXUS9IBULysp+GY25NkCTljzJh7drINLAttNq+6pINb6Z3KOSsy9qsZsx0t+P1soPnd27d5lqnkOUOO8L3n6AIDxdaXx6+Sabtd+bTv7cqhq6QsLnU2Z++BoFwA8e3vvKt93rjkBr9nwSyeT1KLErKDVAgLu2LImOzd4Z8EZa+YA==",
                    "host_rsa_public": "AAAAB3NzaC1yc2EAAAADAQABAAABAQC2uIdHdpKOK3GIbYDLtUvHhUo9rSERuT6WqmZ9G3x7X0ynnofbKMAuzHKtZ5fJBF2YLcDZNX08nZcPAjILQXN6rVoW6mBD/HOcU6NHplSouAnArqYrPrUwm/GHrS+vIQOhjQ547019FxzkiMCrIDyU23fK9klK6ePYY4hicvQX9dD8/n4B5YusSA3L+W0znxAp+d+XrpDcbyO3CPrI7Tvzw9N0irftssnx5DP5f8kxeDGwYoSjxlA+l3hnMgxP59W2kr8LlLinRPVExvQNkj+N8qWMyjnYP9yzSoHn7NiwiI/mdjiIABHEmkxKBYzukX2grkBHp3W6TqFMAjVofku/"
                }
            },
            "ohai_languages": {
                "perl": {
                    "archname": "i686-linux-gnu-thread-multi-64int",
                    "version": "5.18.2"
                },
                "python": {
                    "builddate": "Nov 23 2017, 15:50:55",
                    "version": "2.7.6"
                },
                "ruby": {
                    "bin_dir": "/usr/bin",
                    "gem_bin": "/usr/bin/gem1.9.1",
                    "gems_dir": "/var/lib/gems/1.9.1",
                    "host": "i686-pc-linux-gnu",
                    "host_cpu": "i686",
                    "host_os": "linux-gnu",
                    "host_vendor": "pc",
                    "platform": "i686-linux",
                    "release_date": "2013-11-22",
                    "ruby_bin": "/usr/bin/ruby1.9.1",
                    "target": "i686-pc-linux-gnu",
                    "target_cpu": "i686",
                    "target_os": "linux",
                    "target_vendor": "pc",
                    "version": "1.9.3"
                }
            },
            "ohai_lsb": {
                "codename": "trusty",
                "description": "Ubuntu 14.04.5 LTS",
                "id": "Ubuntu",
                "release": "14.04"
            },
            "ohai_macaddress": "08:00:27:97:31:F6",
            "ohai_memory": {
                "active": "286168kB",
                "anon_pages": "71644kB",
                "bounce": "0kB",
                "buffers": "17772kB",
                "cached": "283316kB",
                "commit_limit": "253528kB",
                "committed_as": "157236kB",
                "dirty": "404kB",
                "free": "106644kB",
                "high_free": "0kB",
                "high_total": "0kB",
                "inactive": "86556kB",
                "low_free": "106644kB",
                "low_total": "507056kB",
                "mapped": "11892kB",
                "nfs_unstable": "0kB",
                "page_tables": "1112kB",
                "slab": "19196kB",
                "slab_reclaimable": "13716kB",
                "slab_unreclaim": "5480kB",
                "swap": {
                    "cached": "0kB",
                    "free": "0kB",
                    "total": "0kB"
                },
                "total": "507056kB",
                "vmalloc_chunk": "500868kB",
                "vmalloc_total": "512056kB",
                "vmalloc_used": "6456kB",
                "writeback": "0kB"
            },
            "ohai_network": {
                "default_gateway": "10.0.2.2",
                "default_interface": "eth0",
                "interfaces": {
                    "eth0": {
                        "addresses": {
                            "08:00:27:97:31:F6": {
                                "family": "lladdr"
                            },
                            "10.0.2.15": {
                                "broadcast": "10.0.2.255",
                                "family": "inet",
                                "netmask": "255.255.255.0",
                                "prefixlen": "24",
                                "scope": "Global"
                            },
                            "fe80::a00:27ff:fe97:31f6": {
                                "family": "inet6",
                                "prefixlen": "64",
                                "scope": "Link"
                            }
                        },
                        "arp": {
                            "10.0.2.2": "52:54:00:12:35:02",
                            "10.0.2.3": "52:54:00:12:35:03"
                        },
                        "encapsulation": "Ethernet",
                        "flags": [
                            "BROADCAST",
                            "MULTICAST",
                            "UP",
                            "LOWER_UP"
                        ],
                        "mtu": "1500",
                        "number": "0",
                        "routes": [
                            {
                                "destination": "default",
                                "family": "inet",
                                "via": "10.0.2.2"
                            },
                            {
                                "destination": "10.0.2.0/24",
                                "family": "inet",
                                "proto": "kernel",
                                "scope": "link",
                                "src": "10.0.2.15"
                            },
                            {
                                "destination": "fe80::/64",
                                "family": "inet6",
                                "metric": "256",
                                "proto": "kernel"
                            }
                        ],
                        "state": "up",
                        "type": "eth"
                    },
                    "eth1": {
                        "addresses": {
                            "08:00:27:3F:A4:8D": {
                                "family": "lladdr"
                            },
                            "172.28.128.13": {
                                "broadcast": "172.28.128.255",
                                "family": "inet",
                                "netmask": "255.255.255.0",
                                "prefixlen": "24",
                                "scope": "Global"
                            }
                        },
                        "arp": {
                            "172.28.128.1": "0a:00:27:00:00:01",
                            "172.28.128.2": "08:00:27:f2:1a:35"
                        },
                        "encapsulation": "Ethernet",
                        "flags": [
                            "BROADCAST",
                            "MULTICAST",
                            "UP",
                            "LOWER_UP"
                        ],
                        "mtu": "1500",
                        "number": "1",
                        "routes": [
                            {
                                "destination": "172.28.128.0/24",
                                "family": "inet",
                                "proto": "kernel",
                                "scope": "link",
                                "src": "172.28.128.13"
                            }
                        ],
                        "state": "up",
                        "type": "eth"
                    },
                    "lo": {
                        "addresses": {
                            "127.0.0.1": {
                                "family": "inet",
                                "netmask": "255.0.0.0",
                                "prefixlen": "8",
                                "scope": "Node"
                            },
                            "::1": {
                                "family": "inet6",
                                "prefixlen": "128",
                                "scope": "Node"
                            }
                        },
                        "encapsulation": "Loopback",
                        "flags": [
                            "LOOPBACK",
                            "UP",
                            "LOWER_UP"
                        ],
                        "mtu": "65536",
                        "state": "unknown"
                    }
                },
                "listeners": {
                    "tcp": {
                        "111": {
                            "address": "*",
                            "name": "",
                            "pid": 0
                        },
                        "22": {
                            "address": "*",
                            "name": "",
                            "pid": 0
                        },
                        "51657": {
                            "address": "*",
                            "pid": 0
                        },
                        "52342": {
                            "address": "*",
                            "name": "",
                            "pid": 0
                        },
                        "6379": {
                            "address": "127.0.0.1",
                            "name": "",
                            "pid": 0
                        }
                    }
                }
            },
            "ohai_ohai_time": 1541533017.9386108,
            "ohai_os": "linux",
            "ohai_os_version": "3.13.0-161-generic",
            "ohai_platform": "ubuntu",
            "ohai_platform_family": "debian",
            "ohai_platform_version": "14.04",
            "ohai_uptime": "1 hours 10 minutes 07 seconds",
            "ohai_uptime_seconds": 4207,
            "ohai_virtualization": {
                "role": "guest",
                "system": "vbox"
            },
            "os_family": "Debian",
            "pkg_mgr": "apt",
            "processor": [
                "0",
                "GenuineIntel",
                "Intel(R) Core(TM) i7-5557U CPU @ 3.10GHz"
            ],
            "processor_cores": 1,
            "processor_count": 1,
            "processor_threads_per_core": 1,
            "processor_vcpus": 1,
            "product_name": "VirtualBox",
            "product_serial": "NA",
            "product_uuid": "NA",
            "product_version": "1.2",
            "python": {
                "executable": "/usr/bin/python",
                "has_sslcontext": false,
                "type": "CPython",
                "version": {
                    "major": 2,
                    "micro": 6,
                    "minor": 7,
                    "releaselevel": "final",
                    "serial": 0
                },
                "version_info": [
                    2,
                    7,
                    6,
                    "final",
                    0
                ]
            },
            "python_version": "2.7.6",
            "real_group_id": 1000,
            "real_user_id": 1000,
            "selinux": {
                "status": "Missing selinux Python library"
            },
            "selinux_python_present": false,
            "service_mgr": "upstart",
            "ssh_host_key_dsa_public": "AAAAB3NzaC1kc3MAAACBAK56mnvTORwkWIQLjaJPFTVxx+mRqfZ9xX3YmrYwhcMYgEpIldHXLrPaUqWG+qv+Mab9oFGTAfgKmV1kg9dDVTeOJQ/+6Is49ZcXntOpftrKOFakL//TP3EvhpA7Go3AOD1vWggZGmvpt8WFqOdV0YfJcGTPj8rx1jn2ZKit7JTxAAAAFQDdHiC5s7voC1AvAEAX3iAWdto6mQAAAIASeHhuQjLQD0p4ArI8XG/ntmtGn5q3wzTEown2DLiQa9SeASmeZNcqFtBgi6kj8O6G1TzkTHlzdnlZ3jnmjxoIXUIlC9rmjQtrwjlQ//ECjkAVFLgaZCL5J1+Ac7oUMp4VBAedQ4hH5wWAgOsf77YTQJlgiAYX7hrVHqhbR9GLPwAAAIBXUS9IBULysp+GY25NkCTljzJh7drINLAttNq+6pINb6Z3KOSsy9qsZsx0t+P1soPnd27d5lqnkOUOO8L3n6AIDxdaXx6+Sabtd+bTv7cqhq6QsLnU2Z++BoFwA8e3vvKt93rjkBr9nwSyeT1KLErKDVAgLu2LImOzd4Z8EZa+YA==",
            "ssh_host_key_ecdsa_public": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDIuYZMhwUecIboGpQiYKyofk290b78CwZmT4ofBxyGwWqNR7CSXL7SgOem1x4dMLmmMxGqAbSkuoTLNOByRZY8=",
            "ssh_host_key_ed25519_public": "AAAAC3NzaC1lZDI1NTE5AAAAIKIy2PCxmrHCd5hltfjElJMb6SJ1k7mt8hu1yi6+y1rA",
            "ssh_host_key_rsa_public": "AAAAB3NzaC1yc2EAAAADAQABAAABAQC2uIdHdpKOK3GIbYDLtUvHhUo9rSERuT6WqmZ9G3x7X0ynnofbKMAuzHKtZ5fJBF2YLcDZNX08nZcPAjILQXN6rVoW6mBD/HOcU6NHplSouAnArqYrPrUwm/GHrS+vIQOhjQ547019FxzkiMCrIDyU23fK9klK6ePYY4hicvQX9dD8/n4B5YusSA3L+W0znxAp+d+XrpDcbyO3CPrI7Tvzw9N0irftssnx5DP5f8kxeDGwYoSjxlA+l3hnMgxP59W2kr8LlLinRPVExvQNkj+N8qWMyjnYP9yzSoHn7NiwiI/mdjiIABHEmkxKBYzukX2grkBHp3W6TqFMAjVofku/",
            "swapfree_mb": 0,
            "swaptotal_mb": 0,
            "system": "Linux",
            "system_capabilities": [
                ""
            ],
            "system_capabilities_enforced": "True",
            "system_vendor": "innotek GmbH",
            "uptime_seconds": 4207,
            "user_dir": "/home/vagrant",
            "user_gecos": "",
            "user_gid": 1000,
            "user_id": "vagrant",
            "user_shell": "/bin/bash",
            "user_uid": 1000,
            "userspace_architecture": "i386",
            "userspace_bits": "32",
            "virtualization_role": "guest",
            "virtualization_type": "virtualbox"
        },
        "ansible_fips": false,
        "ansible_forks": 5,
        "ansible_form_factor": "Other",
        "ansible_fqdn": "Ubuntu-A",
        "ansible_hostname": "ubuntu-a",
        "ansible_interfaces": [
            "lo",
            "eth1",
            "eth0"
        ],
        "ansible_inventory_sources": [
            "/Users/pabhaves/Desktop/Bhavesh/practice/vagrant/hosts"
        ],
        "ansible_is_chroot": false,
        "ansible_iscsi_iqn": "",
        "ansible_kernel": "3.13.0-161-generic",
        "ansible_lo": {
            "active": true,
            "device": "lo",
            "features": {
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "on [fixed]",
                "netns_local": "on [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "on [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on [fixed]",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_segmentation": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipip_segmentation": "off [fixed]",
                "tx_lockless": "on [fixed]",
                "tx_mpls_segmentation": "off [fixed]",
                "tx_nocache_copy": "off [fixed]",
                "tx_scatter_gather": "on [fixed]",
                "tx_scatter_gather_fraglist": "on [fixed]",
                "tx_sit_segmentation": "off [fixed]",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_tnl_segmentation": "off [fixed]",
                "tx_vlan_offload": "off [fixed]",
                "tx_vlan_stag_hw_insert": "off [fixed]",
                "udp_fragmentation_offload": "on",
                "vlan_challenged": "on [fixed]"
            },
            "hw_timestamp_filters": [],
            "ipv4": {
                "address": "127.0.0.1",
                "broadcast": "host",
                "netmask": "255.0.0.0",
                "network": "127.0.0.0"
            },
            "ipv6": [
                {
                    "address": "::1",
                    "prefix": "128",
                    "scope": "host"
                }
            ],
            "mtu": 65536,
            "promisc": false,
            "timestamping": [
                "rx_software",
                "software"
            ],
            "type": "loopback"
        },
        "ansible_local": {},
        "ansible_lsb": {
            "codename": "trusty",
            "description": "Ubuntu 14.04.5 LTS",
            "id": "Ubuntu",
            "major_release": "14",
            "release": "14.04"
        },
        "ansible_machine": "i686",
        "ansible_machine_id": "5afee93f1bceaef72b1460d35be1dd04",
        "ansible_memfree_mb": 110,
        "ansible_memory_mb": {
            "nocache": {
                "free": 403,
                "used": 92
            },
            "real": {
                "free": 110,
                "total": 495,
                "used": 385
            },
            "swap": {
                "cached": 0,
                "free": 0,
                "total": 0,
                "used": 0
            }
        },
        "ansible_memtotal_mb": 495,
        "ansible_mounts": [
            {
                "block_available": 9530402,
                "block_size": 4096,
                "block_total": 10312784,
                "block_used": 782382,
                "device": "/dev/sda1",
                "fstype": "ext4",
                "inode_available": 2549102,
                "inode_total": 2621440,
                "inode_used": 72338,
                "mount": "/",
                "options": "rw",
                "size_available": 39036526592,
                "size_total": 42241163264,
                "uuid": "2220679a-bcf3-402c-9e25-d36ec301949e"
            }
        ],
        "ansible_nodename": "ubuntu-a",
        "ansible_os_family": "Debian",
        "ansible_pkg_mgr": "apt",
        "ansible_playbook_python": "/usr/local/Cellar/ansible/2.7.1/libexec/bin/python3.7",
        "ansible_processor": [
            "0",
            "GenuineIntel",
            "Intel(R) Core(TM) i7-5557U CPU @ 3.10GHz"
        ],
        "ansible_processor_cores": 1,
        "ansible_processor_count": 1,
        "ansible_processor_threads_per_core": 1,
        "ansible_processor_vcpus": 1,
        "ansible_product_name": "VirtualBox",
        "ansible_product_serial": "NA",
        "ansible_product_uuid": "NA",
        "ansible_product_version": "1.2",
        "ansible_python": {
            "executable": "/usr/bin/python",
            "has_sslcontext": false,
            "type": "CPython",
            "version": {
                "major": 2,
                "micro": 6,
                "minor": 7,
                "releaselevel": "final",
                "serial": 0
            },
            "version_info": [
                2,
                7,
                6,
                "final",
                0
            ]
        },
        "ansible_python_version": "2.7.6",
        "ansible_real_group_id": 1000,
        "ansible_real_user_id": 1000,
        "ansible_run_tags": [
            "all"
        ],
        "ansible_selinux": {
            "status": "Missing selinux Python library"
        },
        "ansible_selinux_python_present": false,
        "ansible_service_mgr": "upstart",
        "ansible_skip_tags": [],
        "ansible_ssh_host_key_dsa_public": "AAAAB3NzaC1kc3MAAACBAK56mnvTORwkWIQLjaJPFTVxx+mRqfZ9xX3YmrYwhcMYgEpIldHXLrPaUqWG+qv+Mab9oFGTAfgKmV1kg9dDVTeOJQ/+6Is49ZcXntOpftrKOFakL//TP3EvhpA7Go3AOD1vWggZGmvpt8WFqOdV0YfJcGTPj8rx1jn2ZKit7JTxAAAAFQDdHiC5s7voC1AvAEAX3iAWdto6mQAAAIASeHhuQjLQD0p4ArI8XG/ntmtGn5q3wzTEown2DLiQa9SeASmeZNcqFtBgi6kj8O6G1TzkTHlzdnlZ3jnmjxoIXUIlC9rmjQtrwjlQ//ECjkAVFLgaZCL5J1+Ac7oUMp4VBAedQ4hH5wWAgOsf77YTQJlgiAYX7hrVHqhbR9GLPwAAAIBXUS9IBULysp+GY25NkCTljzJh7drINLAttNq+6pINb6Z3KOSsy9qsZsx0t+P1soPnd27d5lqnkOUOO8L3n6AIDxdaXx6+Sabtd+bTv7cqhq6QsLnU2Z++BoFwA8e3vvKt93rjkBr9nwSyeT1KLErKDVAgLu2LImOzd4Z8EZa+YA==",
        "ansible_ssh_host_key_ecdsa_public": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDIuYZMhwUecIboGpQiYKyofk290b78CwZmT4ofBxyGwWqNR7CSXL7SgOem1x4dMLmmMxGqAbSkuoTLNOByRZY8=",
        "ansible_ssh_host_key_ed25519_public": "AAAAC3NzaC1lZDI1NTE5AAAAIKIy2PCxmrHCd5hltfjElJMb6SJ1k7mt8hu1yi6+y1rA",
        "ansible_ssh_host_key_rsa_public": "AAAAB3NzaC1yc2EAAAADAQABAAABAQC2uIdHdpKOK3GIbYDLtUvHhUo9rSERuT6WqmZ9G3x7X0ynnofbKMAuzHKtZ5fJBF2YLcDZNX08nZcPAjILQXN6rVoW6mBD/HOcU6NHplSouAnArqYrPrUwm/GHrS+vIQOhjQ547019FxzkiMCrIDyU23fK9klK6ePYY4hicvQX9dD8/n4B5YusSA3L+W0znxAp+d+XrpDcbyO3CPrI7Tvzw9N0irftssnx5DP5f8kxeDGwYoSjxlA+l3hnMgxP59W2kr8LlLinRPVExvQNkj+N8qWMyjnYP9yzSoHn7NiwiI/mdjiIABHEmkxKBYzukX2grkBHp3W6TqFMAjVofku/",
        "ansible_swapfree_mb": 0,
        "ansible_swaptotal_mb": 0,
        "ansible_system": "Linux",
        "ansible_system_capabilities": [
            ""
        ],
        "ansible_system_capabilities_enforced": "True",
        "ansible_system_vendor": "innotek GmbH",
        "ansible_uptime_seconds": 4207,
        "ansible_user_dir": "/home/vagrant",
        "ansible_user_gecos": "",
        "ansible_user_gid": 1000,
        "ansible_user_id": "vagrant",
        "ansible_user_shell": "/bin/bash",
        "ansible_user_uid": 1000,
        "ansible_userspace_architecture": "i386",
        "ansible_userspace_bits": "32",
        "ansible_verbosity": 0,
        "ansible_version": {
            "full": "2.7.1",
            "major": 2,
            "minor": 7,
            "revision": 1,
            "string": "2.7.1"
        },
        "ansible_virtualization_role": "guest",
        "ansible_virtualization_type": "virtualbox",
        "facter_architecture": "i386",
        "facter_augeasversion": "1.2.0",
        "facter_blockdevice_sda_model": "VBOX HARDDISK",
        "facter_blockdevice_sda_size": 42949672960,
        "facter_blockdevice_sda_vendor": "ATA",
        "facter_blockdevices": "sda",
        "facter_domain": "ant.amazon.com",
        "facter_facterversion": "1.7.5",
        "facter_filesystems": "ext2,ext3,ext4,vfat",
        "facter_fqdn": "ubuntu-a.ant.amazon.com",
        "facter_hardwareisa": "i686",
        "facter_hardwaremodel": "i686",
        "facter_hostname": "ubuntu-a",
        "facter_id": "vagrant",
        "facter_interfaces": "eth0,eth1,lo",
        "facter_ipaddress": "10.0.2.15",
        "facter_ipaddress_eth0": "10.0.2.15",
        "facter_ipaddress_eth1": "172.28.128.13",
        "facter_ipaddress_lo": "127.0.0.1",
        "facter_is_virtual": "true",
        "facter_kernel": "Linux",
        "facter_kernelmajversion": "3.13",
        "facter_kernelrelease": "3.13.0-161-generic",
        "facter_kernelversion": "3.13.0",
        "facter_lsbdistcodename": "trusty",
        "facter_lsbdistdescription": "Ubuntu 14.04.5 LTS",
        "facter_lsbdistid": "Ubuntu",
        "facter_lsbdistrelease": "14.04",
        "facter_lsbmajdistrelease": "14",
        "facter_macaddress": "08:00:27:97:31:f6",
        "facter_macaddress_eth0": "08:00:27:97:31:f6",
        "facter_macaddress_eth1": "08:00:27:3f:a4:8d",
        "facter_memoryfree": "386.86 MB",
        "facter_memoryfree_mb": "386.86",
        "facter_memorysize": "495.17 MB",
        "facter_memorysize_mb": "495.17",
        "facter_memorytotal": "495.17 MB",
        "facter_mtu_eth0": "1500",
        "facter_mtu_eth1": "1500",
        "facter_mtu_lo": "65536",
        "facter_netmask": "255.255.255.0",
        "facter_netmask_eth0": "255.255.255.0",
        "facter_netmask_eth1": "255.255.255.0",
        "facter_netmask_lo": "255.0.0.0",
        "facter_network_eth0": "10.0.2.0",
        "facter_network_eth1": "172.28.128.0",
        "facter_network_lo": "127.0.0.0",
        "facter_operatingsystem": "Ubuntu",
        "facter_operatingsystemrelease": "14.04",
        "facter_osfamily": "Debian",
        "facter_path": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games",
        "facter_physicalprocessorcount": 1,
        "facter_processor0": "Intel(R) Core(TM) i7-5557U CPU @ 3.10GHz",
        "facter_processorcount": "1",
        "facter_ps": "ps -ef",
        "facter_puppetversion": "3.4.3",
        "facter_rubysitedir": "/usr/local/lib/site_ruby/1.9.1",
        "facter_rubyversion": "1.9.3",
        "facter_selinux": "false",
        "facter_sshdsakey": "AAAAB3NzaC1kc3MAAACBAK56mnvTORwkWIQLjaJPFTVxx+mRqfZ9xX3YmrYwhcMYgEpIldHXLrPaUqWG+qv+Mab9oFGTAfgKmV1kg9dDVTeOJQ/+6Is49ZcXntOpftrKOFakL//TP3EvhpA7Go3AOD1vWggZGmvpt8WFqOdV0YfJcGTPj8rx1jn2ZKit7JTxAAAAFQDdHiC5s7voC1AvAEAX3iAWdto6mQAAAIASeHhuQjLQD0p4ArI8XG/ntmtGn5q3wzTEown2DLiQa9SeASmeZNcqFtBgi6kj8O6G1TzkTHlzdnlZ3jnmjxoIXUIlC9rmjQtrwjlQ//ECjkAVFLgaZCL5J1+Ac7oUMp4VBAedQ4hH5wWAgOsf77YTQJlgiAYX7hrVHqhbR9GLPwAAAIBXUS9IBULysp+GY25NkCTljzJh7drINLAttNq+6pINb6Z3KOSsy9qsZsx0t+P1soPnd27d5lqnkOUOO8L3n6AIDxdaXx6+Sabtd+bTv7cqhq6QsLnU2Z++BoFwA8e3vvKt93rjkBr9nwSyeT1KLErKDVAgLu2LImOzd4Z8EZa+YA==",
        "facter_sshecdsakey": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDIuYZMhwUecIboGpQiYKyofk290b78CwZmT4ofBxyGwWqNR7CSXL7SgOem1x4dMLmmMxGqAbSkuoTLNOByRZY8=",
        "facter_sshfp_dsa": "SSHFP 2 1 5056908a4b35ba887a7bcb8a8faec30dbc7f2872\nSSHFP 2 2 eab9aabdd0013bdd2c3e01a1f13af9529ad0e4536a6d848696f458b79994d9b0",
        "facter_sshfp_ecdsa": "SSHFP 3 1 04b63504942a7a1ce2da9690e92204098d9efd6f\nSSHFP 3 2 933d8847b718e6e015ec1781b8dcb81b1de7e03df8740b977fc3e1892362093d",
        "facter_sshfp_rsa": "SSHFP 1 1 3d53b7b9b478f6925a9c14822455e44633789965\nSSHFP 1 2 5cde1c6808c1d806b52f05e4e3842ab1a59bbc0ee13110da0d253ab486846d20",
        "facter_sshrsakey": "AAAAB3NzaC1yc2EAAAADAQABAAABAQC2uIdHdpKOK3GIbYDLtUvHhUo9rSERuT6WqmZ9G3x7X0ynnofbKMAuzHKtZ5fJBF2YLcDZNX08nZcPAjILQXN6rVoW6mBD/HOcU6NHplSouAnArqYrPrUwm/GHrS+vIQOhjQ547019FxzkiMCrIDyU23fK9klK6ePYY4hicvQX9dD8/n4B5YusSA3L+W0znxAp+d+XrpDcbyO3CPrI7Tvzw9N0irftssnx5DP5f8kxeDGwYoSjxlA+l3hnMgxP59W2kr8LlLinRPVExvQNkj+N8qWMyjnYP9yzSoHn7NiwiI/mdjiIABHEmkxKBYzukX2grkBHp3W6TqFMAjVofku/",
        "facter_swapfree": "0.00 MB",
        "facter_swapfree_mb": "0.00",
        "facter_swapsize": "0.00 MB",
        "facter_swapsize_mb": "0.00",
        "facter_timezone": "UTC",
        "facter_uniqueid": "007f0101",
        "facter_uptime": "1:10 hours",
        "facter_uptime_days": 0,
        "facter_uptime_hours": 1,
        "facter_uptime_seconds": 4206,
        "facter_virtual": "virtualbox",
        "gather_subset": [
            "all"
        ],
        "group_names": [
            "redis_master",
            "web"
        ],
        "groups": {
            "all": [
                "172.28.128.13",
                "172.28.128.14"
            ],
            "redis_master": [
                "172.28.128.13"
            ],
            "ungrouped": [],
            "web": [
                "172.28.128.13",
                "172.28.128.14"
            ]
        },
        "inventory_dir": "/Users/pabhaves/Desktop/Bhavesh/practice/vagrant",
        "inventory_file": "/Users/pabhaves/Desktop/Bhavesh/practice/vagrant/hosts",
        "inventory_hostname": "172.28.128.13",
        "inventory_hostname_short": "172",
        "module_setup": true,
        "ohai_block_device": {
            "loop0": {
                "removable": "0",
                "size": "0"
            },
            "loop1": {
                "removable": "0",
                "size": "0"
            },
            "loop2": {
                "removable": "0",
                "size": "0"
            },
            "loop3": {
                "removable": "0",
                "size": "0"
            },
            "loop4": {
                "removable": "0",
                "size": "0"
            },
            "loop5": {
                "removable": "0",
                "size": "0"
            },
            "loop6": {
                "removable": "0",
                "size": "0"
            },
            "loop7": {
                "removable": "0",
                "size": "0"
            },
            "ram0": {
                "removable": "0",
                "size": "131072"
            },
            "ram1": {
                "removable": "0",
                "size": "131072"
            },
            "ram10": {
                "removable": "0",
                "size": "131072"
            },
            "ram11": {
                "removable": "0",
                "size": "131072"
            },
            "ram12": {
                "removable": "0",
                "size": "131072"
            },
            "ram13": {
                "removable": "0",
                "size": "131072"
            },
            "ram14": {
                "removable": "0",
                "size": "131072"
            },
            "ram15": {
                "removable": "0",
                "size": "131072"
            },
            "ram2": {
                "removable": "0",
                "size": "131072"
            },
            "ram3": {
                "removable": "0",
                "size": "131072"
            },
            "ram4": {
                "removable": "0",
                "size": "131072"
            },
            "ram5": {
                "removable": "0",
                "size": "131072"
            },
            "ram6": {
                "removable": "0",
                "size": "131072"
            },
            "ram7": {
                "removable": "0",
                "size": "131072"
            },
            "ram8": {
                "removable": "0",
                "size": "131072"
            },
            "ram9": {
                "removable": "0",
                "size": "131072"
            },
            "sda": {
                "model": "VBOX HARDDISK",
                "removable": "0",
                "rev": "1.0",
                "size": "83886080",
                "state": "running",
                "timeout": "30",
                "vendor": "ATA"
            }
        },
        "ohai_chef_packages": {
            "chef": {
                "chef_root": "/usr/lib/ruby/vendor_ruby",
                "version": "11.8.2"
            },
            "ohai": {
                "ohai_root": "/usr/lib/ruby/vendor_ruby/ohai",
                "version": "6.14.0"
            }
        },
        "ohai_command": {
            "ps": "ps -ef"
        },
        "ohai_counters": {
            "network": {
                "interfaces": {
                    "eth0": {
                        "rx": {
                            "bytes": "621873",
                            "drop": "0",
                            "errors": "0",
                            "overrun": "0",
                            "packets": "2309"
                        },
                        "tx": {
                            "bytes": "176404",
                            "carrier": "0",
                            "collisions": "0",
                            "drop": "0",
                            "errors": "0",
                            "packets": "1580",
                            "queuelen": "1000"
                        }
                    },
                    "eth1": {
                        "rx": {
                            "bytes": "7981579",
                            "drop": "0",
                            "errors": "0",
                            "overrun": "0",
                            "packets": "10224"
                        },
                        "tx": {
                            "bytes": "1412084",
                            "carrier": "0",
                            "collisions": "0",
                            "drop": "0",
                            "errors": "0",
                            "packets": "6582",
                            "queuelen": "1000"
                        }
                    },
                    "lo": {
                        "rx": {
                            "bytes": "0",
                            "drop": "0",
                            "errors": "0",
                            "overrun": "0",
                            "packets": "0"
                        },
                        "tx": {
                            "bytes": "0",
                            "carrier": "0",
                            "collisions": "0",
                            "drop": "0",
                            "errors": "0",
                            "packets": "0"
                        }
                    }
                }
            }
        },
        "ohai_cpu": {
            "0": {
                "cache_size": "4096 KB",
                "core_id": "0",
                "cores": "1",
                "family": "6",
                "flags": [
                    "fpu",
                    "vme",
                    "de",
                    "pse",
                    "tsc",
                    "msr",
                    "pae",
                    "mce",
                    "cx8",
                    "apic",
                    "sep",
                    "mtrr",
                    "pge",
                    "mca",
                    "cmov",
                    "pat",
                    "pse36",
                    "clflush",
                    "mmx",
                    "fxsr",
                    "sse",
                    "sse2",
                    "ht",
                    "syscall",
                    "nx",
                    "rdtscp",
                    "lm",
                    "constant_tsc",
                    "xtopology",
                    "nonstop_tsc",
                    "eagerfpu",
                    "pni",
                    "pclmulqdq",
                    "ssse3",
                    "cx16",
                    "sse4_1",
                    "sse4_2",
                    "movbe",
                    "popcnt",
                    "aes",
                    "xsave",
                    "avx",
                    "rdrand",
                    "lahf_lm",
                    "abm",
                    "3dnowprefetch",
                    "rsb_ctxsw",
                    "retpoline",
                    "fsgsbase",
                    "avx2",
                    "invpcid",
                    "rdseed",
                    "flush_l1d"
                ],
                "mhz": "3099.419",
                "model": "61",
                "model_name": "Intel(R) Core(TM) i7-5557U CPU @ 3.10GHz",
                "physical_id": "0",
                "stepping": "4",
                "vendor_id": "GenuineIntel"
            },
            "real": 1,
            "total": 1
        },
        "ohai_current_user": "vagrant",
        "ohai_dmi": {
            "dmidecode_version": "2.12"
        },
        "ohai_domain": null,
        "ohai_etc": {
            "group": {
                "adm": {
                    "gid": 4,
                    "members": [
                        "syslog",
                        "ubuntu"
                    ]
                },
                "admin": {
                    "gid": 110,
                    "members": []
                },
                "audio": {
                    "gid": 29,
                    "members": [
                        "ubuntu"
                    ]
                },
                "backup": {
                    "gid": 34,
                    "members": []
                },
                "bin": {
                    "gid": 2,
                    "members": []
                },
                "cdrom": {
                    "gid": 24,
                    "members": [
                        "ubuntu"
                    ]
                },
                "colord": {
                    "gid": 112,
                    "members": []
                },
                "crontab": {
                    "gid": 103,
                    "members": []
                },
                "daemon": {
                    "gid": 1,
                    "members": []
                },
                "dialout": {
                    "gid": 20,
                    "members": [
                        "ubuntu"
                    ]
                },
                "dip": {
                    "gid": 30,
                    "members": [
                        "ubuntu"
                    ]
                },
                "disk": {
                    "gid": 6,
                    "members": []
                },
                "fax": {
                    "gid": 21,
                    "members": []
                },
                "floppy": {
                    "gid": 25,
                    "members": [
                        "ubuntu"
                    ]
                },
                "fuse": {
                    "gid": 105,
                    "members": []
                },
                "games": {
                    "gid": 60,
                    "members": []
                },
                "gnats": {
                    "gid": 41,
                    "members": []
                },
                "irc": {
                    "gid": 39,
                    "members": []
                },
                "kmem": {
                    "gid": 15,
                    "members": []
                },
                "landscape": {
                    "gid": 109,
                    "members": []
                },
                "libuuid": {
                    "gid": 101,
                    "members": []
                },
                "list": {
                    "gid": 38,
                    "members": []
                },
                "lp": {
                    "gid": 7,
                    "members": []
                },
                "mail": {
                    "gid": 8,
                    "members": []
                },
                "man": {
                    "gid": 12,
                    "members": []
                },
                "messagebus": {
                    "gid": 106,
                    "members": []
                },
                "mlocate": {
                    "gid": 107,
                    "members": []
                },
                "netdev": {
                    "gid": 102,
                    "members": [
                        "ubuntu"
                    ]
                },
                "news": {
                    "gid": 9,
                    "members": []
                },
                "nogroup": {
                    "gid": 65534,
                    "members": []
                },
                "operator": {
                    "gid": 37,
                    "members": []
                },
                "plugdev": {
                    "gid": 46,
                    "members": [
                        "ubuntu"
                    ]
                },
                "proxy": {
                    "gid": 13,
                    "members": []
                },
                "puppet": {
                    "gid": 114,
                    "members": []
                },
                "redis": {
                    "gid": 115,
                    "members": []
                },
                "root": {
                    "gid": 0,
                    "members": []
                },
                "sasl": {
                    "gid": 45,
                    "members": []
                },
                "scanner": {
                    "gid": 111,
                    "members": []
                },
                "shadow": {
                    "gid": 42,
                    "members": []
                },
                "src": {
                    "gid": 40,
                    "members": []
                },
                "ssh": {
                    "gid": 108,
                    "members": []
                },
                "staff": {
                    "gid": 50,
                    "members": []
                },
                "sudo": {
                    "gid": 27,
                    "members": [
                        "ubuntu"
                    ]
                },
                "sys": {
                    "gid": 3,
                    "members": []
                },
                "syslog": {
                    "gid": 104,
                    "members": []
                },
                "tape": {
                    "gid": 26,
                    "members": []
                },
                "tty": {
                    "gid": 5,
                    "members": []
                },
                "ubuntu": {
                    "gid": 1001,
                    "members": []
                },
                "users": {
                    "gid": 100,
                    "members": []
                },
                "utmp": {
                    "gid": 43,
                    "members": []
                },
                "uucp": {
                    "gid": 10,
                    "members": []
                },
                "vagrant": {
                    "gid": 1000,
                    "members": []
                },
                "vboxsf": {
                    "gid": 113,
                    "members": []
                },
                "video": {
                    "gid": 44,
                    "members": [
                        "ubuntu"
                    ]
                },
                "voice": {
                    "gid": 22,
                    "members": []
                },
                "www-data": {
                    "gid": 33,
                    "members": []
                }
            },
            "passwd": {
                "backup": {
                    "dir": "/var/backups",
                    "gecos": "backup",
                    "gid": 34,
                    "shell": "/usr/sbin/nologin",
                    "uid": 34
                },
                "bin": {
                    "dir": "/bin",
                    "gecos": "bin",
                    "gid": 2,
                    "shell": "/usr/sbin/nologin",
                    "uid": 2
                },
                "colord": {
                    "dir": "/var/lib/colord",
                    "gecos": "colord colour management daemon,,,",
                    "gid": 112,
                    "shell": "/bin/false",
                    "uid": 106
                },
                "daemon": {
                    "dir": "/usr/sbin",
                    "gecos": "daemon",
                    "gid": 1,
                    "shell": "/usr/sbin/nologin",
                    "uid": 1
                },
                "games": {
                    "dir": "/usr/games",
                    "gecos": "games",
                    "gid": 60,
                    "shell": "/usr/sbin/nologin",
                    "uid": 5
                },
                "gnats": {
                    "dir": "/var/lib/gnats",
                    "gecos": "Gnats Bug-Reporting System (admin)",
                    "gid": 41,
                    "shell": "/usr/sbin/nologin",
                    "uid": 41
                },
                "irc": {
                    "dir": "/var/run/ircd",
                    "gecos": "ircd",
                    "gid": 39,
                    "shell": "/usr/sbin/nologin",
                    "uid": 39
                },
                "landscape": {
                    "dir": "/var/lib/landscape",
                    "gecos": "",
                    "gid": 109,
                    "shell": "/bin/false",
                    "uid": 103
                },
                "libuuid": {
                    "dir": "/var/lib/libuuid",
                    "gecos": "",
                    "gid": 101,
                    "shell": "",
                    "uid": 100
                },
                "list": {
                    "dir": "/var/list",
                    "gecos": "Mailing List Manager",
                    "gid": 38,
                    "shell": "/usr/sbin/nologin",
                    "uid": 38
                },
                "lp": {
                    "dir": "/var/spool/lpd",
                    "gecos": "lp",
                    "gid": 7,
                    "shell": "/usr/sbin/nologin",
                    "uid": 7
                },
                "mail": {
                    "dir": "/var/mail",
                    "gecos": "mail",
                    "gid": 8,
                    "shell": "/usr/sbin/nologin",
                    "uid": 8
                },
                "man": {
                    "dir": "/var/cache/man",
                    "gecos": "man",
                    "gid": 12,
                    "shell": "/usr/sbin/nologin",
                    "uid": 6
                },
                "messagebus": {
                    "dir": "/var/run/dbus",
                    "gecos": "",
                    "gid": 106,
                    "shell": "/bin/false",
                    "uid": 102
                },
                "news": {
                    "dir": "/var/spool/news",
                    "gecos": "news",
                    "gid": 9,
                    "shell": "/usr/sbin/nologin",
                    "uid": 9
                },
                "nobody": {
                    "dir": "/nonexistent",
                    "gecos": "nobody",
                    "gid": 65534,
                    "shell": "/usr/sbin/nologin",
                    "uid": 65534
                },
                "pollinate": {
                    "dir": "/var/cache/pollinate",
                    "gecos": "",
                    "gid": 1,
                    "shell": "/bin/false",
                    "uid": 105
                },
                "proxy": {
                    "dir": "/bin",
                    "gecos": "proxy",
                    "gid": 13,
                    "shell": "/usr/sbin/nologin",
                    "uid": 13
                },
                "puppet": {
                    "dir": "/var/lib/puppet",
                    "gecos": "Puppet configuration management daemon,,,",
                    "gid": 114,
                    "shell": "/bin/false",
                    "uid": 108
                },
                "redis": {
                    "dir": "/var/lib/redis",
                    "gecos": "redis server,,,",
                    "gid": 115,
                    "shell": "/bin/false",
                    "uid": 109
                },
                "root": {
                    "dir": "/root",
                    "gecos": "root",
                    "gid": 0,
                    "shell": "/bin/bash",
                    "uid": 0
                },
                "sshd": {
                    "dir": "/var/run/sshd",
                    "gecos": "",
                    "gid": 65534,
                    "shell": "/usr/sbin/nologin",
                    "uid": 104
                },
                "statd": {
                    "dir": "/var/lib/nfs",
                    "gecos": "",
                    "gid": 65534,
                    "shell": "/bin/false",
                    "uid": 107
                },
                "sync": {
                    "dir": "/bin",
                    "gecos": "sync",
                    "gid": 65534,
                    "shell": "/bin/sync",
                    "uid": 4
                },
                "sys": {
                    "dir": "/dev",
                    "gecos": "sys",
                    "gid": 3,
                    "shell": "/usr/sbin/nologin",
                    "uid": 3
                },
                "syslog": {
                    "dir": "/home/syslog",
                    "gecos": "",
                    "gid": 104,
                    "shell": "/bin/false",
                    "uid": 101
                },
                "ubuntu": {
                    "dir": "/home/ubuntu",
                    "gecos": "Ubuntu",
                    "gid": 1001,
                    "shell": "/bin/bash",
                    "uid": 1001
                },
                "uucp": {
                    "dir": "/var/spool/uucp",
                    "gecos": "uucp",
                    "gid": 10,
                    "shell": "/usr/sbin/nologin",
                    "uid": 10
                },
                "vagrant": {
                    "dir": "/home/vagrant",
                    "gecos": "",
                    "gid": 1000,
                    "shell": "/bin/bash",
                    "uid": 1000
                },
                "www-data": {
                    "dir": "/var/www",
                    "gecos": "www-data",
                    "gid": 33,
                    "shell": "/usr/sbin/nologin",
                    "uid": 33
                }
            }
        },
        "ohai_filesystem": {
            "/dev/sda1": {
                "fs_type": "ext4",
                "kb_available": "38121608",
                "kb_size": "41251136",
                "kb_used": "1393616",
                "label": "cloudimg-rootfs",
                "mount": "/",
                "mount_options": [
                    "rw"
                ],
                "percent_used": "4%",
                "uuid": "2220679a-bcf3-402c-9e25-d36ec301949e"
            },
            "devpts": {
                "fs_type": "devpts",
                "mount": "/dev/pts",
                "mount_options": [
                    "rw",
                    "noexec",
                    "nosuid",
                    "gid=5",
                    "mode=0620"
                ]
            },
            "none": {
                "fs_type": "pstore",
                "kb_available": "418379372",
                "kb_size": "487374848",
                "kb_used": "68995476",
                "mount": "/sys/fs/pstore",
                "mount_options": [
                    "rw"
                ],
                "percent_used": "15%"
            },
            "proc": {
                "fs_type": "proc",
                "mount": "/proc",
                "mount_options": [
                    "rw",
                    "noexec",
                    "nosuid",
                    "nodev"
                ]
            },
            "rootfs": {
                "fs_type": "rootfs",
                "mount": "/",
                "mount_options": [
                    "rw"
                ]
            },
            "rpc_pipefs": {
                "fs_type": "rpc_pipefs",
                "mount": "/run/rpc_pipefs",
                "mount_options": [
                    "rw"
                ]
            },
            "sysfs": {
                "fs_type": "sysfs",
                "mount": "/sys",
                "mount_options": [
                    "rw",
                    "noexec",
                    "nosuid",
                    "nodev"
                ]
            },
            "systemd": {
                "fs_type": "cgroup",
                "mount": "/sys/fs/cgroup/systemd",
                "mount_options": [
                    "rw",
                    "noexec",
                    "nosuid",
                    "nodev",
                    "none",
                    "name=systemd"
                ]
            },
            "tmpfs": {
                "fs_type": "tmpfs",
                "kb_available": "50312",
                "kb_size": "50708",
                "kb_used": "396",
                "mount": "/run",
                "mount_options": [
                    "rw",
                    "noexec",
                    "nosuid",
                    "size=10%",
                    "mode=0755"
                ],
                "percent_used": "1%"
            },
            "udev": {
                "fs_type": "devtmpfs",
                "kb_available": "249824",
                "kb_size": "249836",
                "kb_used": "12",
                "mount": "/dev",
                "mount_options": [
                    "rw",
                    "mode=0755"
                ],
                "percent_used": "1%"
            },
            "vagrant": {
                "fs_type": "vboxsf",
                "mount": "/vagrant",
                "mount_options": [
                    "uid=1000",
                    "gid=1000",
                    "rw"
                ]
            }
        },
        "ohai_fqdn": "Ubuntu-A",
        "ohai_hostname": "ubuntu-a",
        "ohai_idletime": "1 hours 05 minutes 34 seconds",
        "ohai_idletime_seconds": 3934,
        "ohai_ipaddress": "10.0.2.15",
        "ohai_kernel": {
            "machine": "i686",
            "modules": {
                "ablk_helper": {
                    "refcount": "1",
                    "size": "13357"
                },
                "aes_i586": {
                    "refcount": "1",
                    "size": "16995"
                },
                "aesni_intel": {
                    "refcount": "0",
                    "size": "18156"
                },
                "ahci": {
                    "refcount": "1",
                    "size": "29739"
                },
                "auth_rpcgss": {
                    "refcount": "1",
                    "size": "48950"
                },
                "crc32_pclmul": {
                    "refcount": "0",
                    "size": "12967"
                },
                "cryptd": {
                    "refcount": "1",
                    "size": "15578"
                },
                "dm_crypt": {
                    "refcount": "0",
                    "size": "22589"
                },
                "e1000": {
                    "refcount": "0",
                    "size": "128548"
                },
                "fscache": {
                    "refcount": "1",
                    "size": "56803"
                },
                "gf128mul": {
                    "refcount": "2",
                    "size": "14503"
                },
                "joydev": {
                    "refcount": "0",
                    "size": "17101"
                },
                "libahci": {
                    "refcount": "1",
                    "size": "31310"
                },
                "lockd": {
                    "refcount": "2",
                    "size": "78462"
                },
                "lrw": {
                    "refcount": "1",
                    "size": "13057"
                },
                "nfs": {
                    "refcount": "0",
                    "size": "213471"
                },
                "nfs_acl": {
                    "refcount": "1",
                    "size": "12733"
                },
                "nfsd": {
                    "refcount": "2",
                    "size": "247731"
                },
                "psmouse": {
                    "refcount": "0",
                    "size": "95439"
                },
                "serio_raw": {
                    "refcount": "0",
                    "size": "13230"
                },
                "sunrpc": {
                    "refcount": "6",
                    "size": "246791"
                },
                "vboxguest": {
                    "refcount": "2",
                    "size": "223958"
                },
                "vboxsf": {
                    "refcount": "1",
                    "size": "42570"
                },
                "video": {
                    "refcount": "0",
                    "size": "18903"
                },
                "xts": {
                    "refcount": "1",
                    "size": "12749"
                }
            },
            "name": "Linux",
            "os": "GNU/Linux",
            "release": "3.13.0-161-generic",
            "version": "#211-Ubuntu SMP Wed Oct 3 14:59:21 UTC 2018"
        },
        "ohai_keys": {
            "ssh": {
                "host_dsa_public": "AAAAB3NzaC1kc3MAAACBAK56mnvTORwkWIQLjaJPFTVxx+mRqfZ9xX3YmrYwhcMYgEpIldHXLrPaUqWG+qv+Mab9oFGTAfgKmV1kg9dDVTeOJQ/+6Is49ZcXntOpftrKOFakL//TP3EvhpA7Go3AOD1vWggZGmvpt8WFqOdV0YfJcGTPj8rx1jn2ZKit7JTxAAAAFQDdHiC5s7voC1AvAEAX3iAWdto6mQAAAIASeHhuQjLQD0p4ArI8XG/ntmtGn5q3wzTEown2DLiQa9SeASmeZNcqFtBgi6kj8O6G1TzkTHlzdnlZ3jnmjxoIXUIlC9rmjQtrwjlQ//ECjkAVFLgaZCL5J1+Ac7oUMp4VBAedQ4hH5wWAgOsf77YTQJlgiAYX7hrVHqhbR9GLPwAAAIBXUS9IBULysp+GY25NkCTljzJh7drINLAttNq+6pINb6Z3KOSsy9qsZsx0t+P1soPnd27d5lqnkOUOO8L3n6AIDxdaXx6+Sabtd+bTv7cqhq6QsLnU2Z++BoFwA8e3vvKt93rjkBr9nwSyeT1KLErKDVAgLu2LImOzd4Z8EZa+YA==",
                "host_rsa_public": "AAAAB3NzaC1yc2EAAAADAQABAAABAQC2uIdHdpKOK3GIbYDLtUvHhUo9rSERuT6WqmZ9G3x7X0ynnofbKMAuzHKtZ5fJBF2YLcDZNX08nZcPAjILQXN6rVoW6mBD/HOcU6NHplSouAnArqYrPrUwm/GHrS+vIQOhjQ547019FxzkiMCrIDyU23fK9klK6ePYY4hicvQX9dD8/n4B5YusSA3L+W0znxAp+d+XrpDcbyO3CPrI7Tvzw9N0irftssnx5DP5f8kxeDGwYoSjxlA+l3hnMgxP59W2kr8LlLinRPVExvQNkj+N8qWMyjnYP9yzSoHn7NiwiI/mdjiIABHEmkxKBYzukX2grkBHp3W6TqFMAjVofku/"
            }
        },
        "ohai_languages": {
            "perl": {
                "archname": "i686-linux-gnu-thread-multi-64int",
                "version": "5.18.2"
            },
            "python": {
                "builddate": "Nov 23 2017, 15:50:55",
                "version": "2.7.6"
            },
            "ruby": {
                "bin_dir": "/usr/bin",
                "gem_bin": "/usr/bin/gem1.9.1",
                "gems_dir": "/var/lib/gems/1.9.1",
                "host": "i686-pc-linux-gnu",
                "host_cpu": "i686",
                "host_os": "linux-gnu",
                "host_vendor": "pc",
                "platform": "i686-linux",
                "release_date": "2013-11-22",
                "ruby_bin": "/usr/bin/ruby1.9.1",
                "target": "i686-pc-linux-gnu",
                "target_cpu": "i686",
                "target_os": "linux",
                "target_vendor": "pc",
                "version": "1.9.3"
            }
        },
        "ohai_lsb": {
            "codename": "trusty",
            "description": "Ubuntu 14.04.5 LTS",
            "id": "Ubuntu",
            "release": "14.04"
        },
        "ohai_macaddress": "08:00:27:97:31:F6",
        "ohai_memory": {
            "active": "286168kB",
            "anon_pages": "71644kB",
            "bounce": "0kB",
            "buffers": "17772kB",
            "cached": "283316kB",
            "commit_limit": "253528kB",
            "committed_as": "157236kB",
            "dirty": "404kB",
            "free": "106644kB",
            "high_free": "0kB",
            "high_total": "0kB",
            "inactive": "86556kB",
            "low_free": "106644kB",
            "low_total": "507056kB",
            "mapped": "11892kB",
            "nfs_unstable": "0kB",
            "page_tables": "1112kB",
            "slab": "19196kB",
            "slab_reclaimable": "13716kB",
            "slab_unreclaim": "5480kB",
            "swap": {
                "cached": "0kB",
                "free": "0kB",
                "total": "0kB"
            },
            "total": "507056kB",
            "vmalloc_chunk": "500868kB",
            "vmalloc_total": "512056kB",
            "vmalloc_used": "6456kB",
            "writeback": "0kB"
        },
        "ohai_network": {
            "default_gateway": "10.0.2.2",
            "default_interface": "eth0",
            "interfaces": {
                "eth0": {
                    "addresses": {
                        "08:00:27:97:31:F6": {
                            "family": "lladdr"
                        },
                        "10.0.2.15": {
                            "broadcast": "10.0.2.255",
                            "family": "inet",
                            "netmask": "255.255.255.0",
                            "prefixlen": "24",
                            "scope": "Global"
                        },
                        "fe80::a00:27ff:fe97:31f6": {
                            "family": "inet6",
                            "prefixlen": "64",
                            "scope": "Link"
                        }
                    },
                    "arp": {
                        "10.0.2.2": "52:54:00:12:35:02",
                        "10.0.2.3": "52:54:00:12:35:03"
                    },
                    "encapsulation": "Ethernet",
                    "flags": [
                        "BROADCAST",
                        "MULTICAST",
                        "UP",
                        "LOWER_UP"
                    ],
                    "mtu": "1500",
                    "number": "0",
                    "routes": [
                        {
                            "destination": "default",
                            "family": "inet",
                            "via": "10.0.2.2"
                        },
                        {
                            "destination": "10.0.2.0/24",
                            "family": "inet",
                            "proto": "kernel",
                            "scope": "link",
                            "src": "10.0.2.15"
                        },
                        {
                            "destination": "fe80::/64",
                            "family": "inet6",
                            "metric": "256",
                            "proto": "kernel"
                        }
                    ],
                    "state": "up",
                    "type": "eth"
                },
                "eth1": {
                    "addresses": {
                        "08:00:27:3F:A4:8D": {
                            "family": "lladdr"
                        },
                        "172.28.128.13": {
                            "broadcast": "172.28.128.255",
                            "family": "inet",
                            "netmask": "255.255.255.0",
                            "prefixlen": "24",
                            "scope": "Global"
                        }
                    },
                    "arp": {
                        "172.28.128.1": "0a:00:27:00:00:01",
                        "172.28.128.2": "08:00:27:f2:1a:35"
                    },
                    "encapsulation": "Ethernet",
                    "flags": [
                        "BROADCAST",
                        "MULTICAST",
                        "UP",
                        "LOWER_UP"
                    ],
                    "mtu": "1500",
                    "number": "1",
                    "routes": [
                        {
                            "destination": "172.28.128.0/24",
                            "family": "inet",
                            "proto": "kernel",
                            "scope": "link",
                            "src": "172.28.128.13"
                        }
                    ],
                    "state": "up",
                    "type": "eth"
                },
                "lo": {
                    "addresses": {
                        "127.0.0.1": {
                            "family": "inet",
                            "netmask": "255.0.0.0",
                            "prefixlen": "8",
                            "scope": "Node"
                        },
                        "::1": {
                            "family": "inet6",
                            "prefixlen": "128",
                            "scope": "Node"
                        }
                    },
                    "encapsulation": "Loopback",
                    "flags": [
                        "LOOPBACK",
                        "UP",
                        "LOWER_UP"
                    ],
                    "mtu": "65536",
                    "state": "unknown"
                }
            },
            "listeners": {
                "tcp": {
                    "111": {
                        "address": "*",
                        "name": "",
                        "pid": 0
                    },
                    "22": {
                        "address": "*",
                        "name": "",
                        "pid": 0
                    },
                    "51657": {
                        "address": "*",
                        "pid": 0
                    },
                    "52342": {
                        "address": "*",
                        "name": "",
                        "pid": 0
                    },
                    "6379": {
                        "address": "127.0.0.1",
                        "name": "",
                        "pid": 0
                    }
                }
            }
        },
        "ohai_ohai_time": 1541533017.9386108,
        "ohai_os": "linux",
        "ohai_os_version": "3.13.0-161-generic",
        "ohai_platform": "ubuntu",
        "ohai_platform_family": "debian",
        "ohai_platform_version": "14.04",
        "ohai_uptime": "1 hours 10 minutes 07 seconds",
        "ohai_uptime_seconds": 4207,
        "ohai_virtualization": {
            "role": "guest",
            "system": "vbox"
        },
        "omit": "__omit_place_holder__73b3ec316a8d0253d2fd748dcf9d7daf924cb851",
        "playbook_dir": "/Users/pabhaves/Desktop/Bhavesh/practice/vagrant"
    }
}

TASK [Ensure Redis is present] **********************************************************************************************************************************************************
ok: [172.28.128.13]

TASK [Ensure Redis is started] **********************************************************************************************************************************************************
ok: [172.28.128.13]

TASK [Ensure Redis Configuration] *******************************************************************************************************************************************************
changed: [172.28.128.13]

RUNNING HANDLER [Redis Restart] *********************************************************************************************************************************************************
changed: [172.28.128.13]

PLAY RECAP ******************************************************************************************************************************************************************************
172.28.128.13              : ok=6    changed=2    unreachable=0    failed=0


Bhavesh/practice/vagrant via pyenv took 18s
➜
```