## Setup vagrant hosts

```
vagrant destroy && vagrant up
```

---

## Copy RSA key

```
ansible-playbook -i hosts copy_rsa_key.yml -u vagrant --ask-pass
```

### Output

```
➜ ansible-playbook -i hosts copy_rsa_key.yml -u vagrant --ask-pass
SSH password:

PLAY [Allow login with SSH Public Key] *****************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************
ok: [172.28.128.16]
ok: [172.28.128.17]

TASK [Ensure the ~/.ssh directory exists] **************************************************************************************************************************************
ok: [172.28.128.17]
ok: [172.28.128.16]

TASK [Check if authorized_keys file present] ***********************************************************************************************************************************
ok: [172.28.128.17]
ok: [172.28.128.16]

TASK [Set authorized key for user vagrant copying it from current user] ********************************************************************************************************
changed: [172.28.128.16]
changed: [172.28.128.17]

PLAY RECAP *********************************************************************************************************************************************************************
172.28.128.16              : ok=4    changed=1    unreachable=0    failed=0
172.28.128.17              : ok=4    changed=1    unreachable=0    failed=0
```

---

## Setup dependencies, start redis-server, and test redis-server

```
ansible-playbook -i hosts  start.yml -u vagrant
```

### Output

```
➜ ansible-playbook -i hosts  start.yml -u vagrant
[DEPRECATION WARNING]: 'include' for playbook includes. You should use 'import_playbook' instead. This feature will be removed in version 2.8. Deprecation warnings can be
disabled by setting deprecation_warnings=False in ansible.cfg.
[DEPRECATION WARNING]: Instead of sudo/sudo_user, use become/become_user and make sure become_method is 'sudo' (default). This feature will be removed in version 2.9.
Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.

PLAY [Setup Redis Server] ******************************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************
ok: [172.28.128.16]

TASK [Ensure python3 is installed] *********************************************************************************************************************************************
ok: [172.28.128.16]

TASK [Ensure python-pip is installed] ******************************************************************************************************************************************
changed: [172.28.128.16]

TASK [Ensure that the ~/.envs directory exists] ********************************************************************************************************************************
changed: [172.28.128.16]

TASK [Copy requirements.txt file to redis server] ******************************************************************************************************************************
changed: [172.28.128.16]

TASK [Install virtualenv via pip] **********************************************************************************************************************************************
changed: [172.28.128.16]

TASK [Create python 3.4 virtual environment] ***********************************************************************************************************************************
changed: [172.28.128.16]

TASK [Copy redis test script] **************************************************************************************************************************************************
changed: [172.28.128.16]

PLAY [Install Redis] ***********************************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************
ok: [172.28.128.16]

TASK [debug] *******************************************************************************************************************************************************************
ok: [172.28.128.16] => {
    "hostvars[inventory_hostname]['ansible_eth1']['ipv4']": {
        "address": "172.28.128.16",
        "broadcast": "172.28.128.255",
        "netmask": "255.255.255.0",
        "network": "172.28.128.0"
    }
}

TASK [Ensure Redis is present] *************************************************************************************************************************************************
changed: [172.28.128.16]

TASK [Ensure Redis is started] *************************************************************************************************************************************************
ok: [172.28.128.16]

TASK [Ensure Redis Configuration] **********************************************************************************************************************************************
changed: [172.28.128.16]

RUNNING HANDLER [Redis Restart] ************************************************************************************************************************************************
changed: [172.28.128.16]

PLAY [Install Redis] ***********************************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************
ok: [172.28.128.16]

TASK [Run a redis test script] *************************************************************************************************************************************************
changed: [172.28.128.16]

TASK [debug] *******************************************************************************************************************************************************************
ok: [172.28.128.16] => {
    "output['stdout']": "last_updated_at: {} b'2018-11-06 23:50:52.848373'"
}

TASK [debug] *******************************************************************************************************************************************************************
ok: [172.28.128.16] => {
    "output['stderr']": ""
}

PLAY RECAP *********************************************************************************************************************************************************************
172.28.128.16              : ok=18   changed=10   unreachable=0    failed=0
```
