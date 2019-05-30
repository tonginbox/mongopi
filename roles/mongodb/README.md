MongoDb
=========

Installation of MongoDb to Ubuntu ARM on Raspberry Pi

Requirements
------------

Raspberry Pi 3 B+ with Ubuntu Server [link](https://www.ubuntu.com/download/iot/raspberry-pi-2-3)

Role Variables
--------------
There is a single variable to initilize swap in MB.

      # file roles/mongodb/vars/main.yml
      swap_size: 1024


Dependencies
------------

No dependencies

Example Playbook
----------------


    - hosts: mongo-pi
      gather_facts: true
      become: yes
      become_method: sudo

      vars_files:
        - group_vars/common.yml

      roles:
        - roles/common
        - roles/mongodb

License
-------

BSD

Author Information
------------------

tonginbox@gmail.com
