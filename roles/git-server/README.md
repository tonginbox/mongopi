Git Host
=========

Installation of Git Host for remote repository of Git SCM. This install only bare minimum to make the Git Host accessible via SSH, no http interface provided.

Requirements
------------

Raspberry Pi 3 B+ with Ubuntu Server [link](https://www.ubuntu.com/download/iot/raspberry-pi-2-3)

Role Variables
--------------
There is a single variable the director location of the root repository of the git.

      # file roles/git-server/vars/main.yml
      repo_root: /repo


Dependencies
------------

No dependencies

Example Playbook
----------------

    # file git-server.yml
    - hosts: git-server
      gather_facts: true
      become: yes
      become_method: sudo

      vars_files:
        - group_vars/common.yml

      roles:
        - roles/common
        - roles/git-server

License
-------

BSD

Author Information
------------------

tonginbox@gmail.com
