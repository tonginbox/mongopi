# Ansible Playbook install mongodb, git host on Ubuntu Raspberry Pi 3
[[ภาษาไทย/thai](#ภาษาไทย)]

This is an ansible playbook to install MongoDb 4.1.x (unstable) and Git Host to Ubuntu Raspberry Pi 3 Operating System.

**Note** Raspbian is not supported.

## Target platform
Ubuntu Raspberry Pi version download link below 
```
$ uname -srv
Linux 4.15.0-1031-raspi2 #33-Ubuntu SMP PREEMPT Wed Jan 16 09:52:45 UTC 2019
```
[link](https://www.ubuntu.com/download/iot/raspberry-pi-2-3) to download the image

## Prerequisite
Install ansible control node, [instruction](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#control-node-requirements), for Widnows 10, it can be used by [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

## Step install MongoDb
1. make a hosts file to target your raspberry, see sample below, make sure hostname is under the section name ```[mongo-pi]```
    ```
    raspberry-pi01 ansible_host=<your RPi IP 192.168.1.100>

    [mongo-pi]
    raspberry-pi01

    [all:vars]
    ansible_python_interpreter=/usr/bin/python3
    ansible_connection=ssh
    ansible_user=ubuntu
    ansible_ssh_pass=<change to your raspberry password>
    ```
1. Run the playbook to install MongoDb
    ```
    ansible-playbook -i hosts mongo-pi.yml
    ```
1. More details [link](roles/mongodb/README.md)

## Step install Git Host
1. make a hosts file to target your raspberry, see sample below, make sure hostname is under the section name ```[git-server]```
    ```
    raspberry-pi01 ansible_host=<your RPi IP 192.168.1.100>

    [git-server]
    raspberry-pi01

    [all:vars]
    ansible_python_interpreter=/usr/bin/python3
    ansible_connection=ssh
    ansible_user=ubuntu
    ansible_ssh_pass=<change to your raspberry password>
    ```
1. Run the playbook to install MongoDb
    ```
    ansible-playbook -i hosts git-server.yml
    ```
1. More details [link](roles/git-server/README.md)

---

### ภาษาไทย

โครงการนี้ใช้เครื่องมือ Ansible สำหรับติดตั้ง MongoDb, Git Host บน Raspberry Pi 3 บนระบบปฏิบัติการ Ubuntu

โครงการนี้ใช้ไม่ได้กับระบบปฏิบัติการ Raspbian

## ระบบปฏิบัติการที่รองรับ

Ubuntu Raspberry Pi เวอร์ชั่น
```
$ uname -srv
Linux 4.15.0-1031-raspi2 #33-Ubuntu SMP PREEMPT Wed Jan 16 09:52:45 UTC 2019
```
[ตามลิ้ง](https://www.ubuntu.com/download/iot/raspberry-pi-2-3) สำหรับดาวน์โหลดระบบปฏิบัติการ

## เตรียมก่อนใช้

ติดตั้ง ansible control node [ขั้นตอนติดตั้ง](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#control-node-requirements), สำหรับ MS Windows สามารถติดตั้งใน [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

## ขั้นตอนติดตั้ง MongoDb

1. สร้างไฟล์ชื่อ ```'hosts'``` ดูตัวอย่างข้อมูลในไฟล์ด้านล่าง เปลี่ยน IP address และ รหัสผ่าน ให้เป็นของเครื่องที่ต้องการติดตั้ง ต้องใส่ชื่อเครื่องใต้ กลุ่ม ```[mongo-pi]```
    ```
    raspberry-pi01 ansible_host=<your RPi IP 192.168.1.100>

    [mongo-pi]
    raspberry-pi01

    [all:vars]
    ansible_python_interpreter=/usr/bin/python3
    ansible_connection=ssh
    ansible_user=ubuntu
    ansible_ssh_pass=<change to your raspberry password>
    ```
1. สั่งติดตั้งใช้ playbook เพื่อติดตั้ง MongoDb
    ```
    ansible-playbook -i hosts mongo-pi.yml
    ```
1. รายละเอียดเพิ่มเติม [ลิ้ง](roles/mongodb/README.md)

## ขั้นตอนติดตั้ง Git Host

1. สร้างไฟล์ชื่อ ```'hosts'``` ดูตัวอย่างข้อมูลในไฟล์ด้านล่าง เปลี่ยน IP address และ รหัสผ่าน ให้เป็นของเครื่องที่ต้องการติดตั้ง ต้องใส่ชื่อเครื่องใต้ กลุ่ม ```[git-server]```
    ```
    raspberry-pi01 ansible_host=<your RPi IP 192.168.1.100>

    [git-server]
    raspberry-pi01

    [all:vars]
    ansible_python_interpreter=/usr/bin/python3
    ansible_connection=ssh
    ansible_user=ubuntu
    ansible_ssh_pass=<change to your raspberry password>
    ```
1. สั่งติดตั้งใช้ playbook เพื่อติดตั้ง Git Host
    ```
    ansible-playbook -i hosts git-server.yml
    ```
1. รายละเอียดเพิ่มเติม [ลิ้ง](roles/git-server/README.md)

---
[![Analytics](https://ga-beacon.appspot.com/UA-140393747-1/welcome-page)](https://github.com/igrigorik/ga-beacon)
