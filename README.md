# Ansible Play Install MongoDb on Ubuntu Raspberry Pi 3
This is an ansible playbook to install MongoDb 4.0.x to Ubuntu Raspberry Pi 3 Operating System.
## Installation platform
Ubuntu Raspberry Pi version below 
```
Linux 4.15.0-1031-raspi2 #33-Ubuntu SMP PREEMPT Wed Jan 16 09:52:45 UTC 2019
```
[link](https://www.ubuntu.com/download/iot/raspberry-pi-2-3) to download the image

**Note** Raspbian is not supported.

## Steps
1. Make hosts file to target a raspberry, see sample below
```
raspberry-pi01 ansible_host=192.168.1.100

[mongo-pi]
raspberry-pi01

[all:vars]
ansible_python_interpreter=/usr/bin/python3
ansible_connection=ssh
ansible_user=ubuntu
ansible_ssh_pass=<change to your raspberry password>
```
2. Run the playbook
```
ansible-playbook -i hosts site.yml
```
