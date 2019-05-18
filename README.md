# Ansible Playbook Install MongoDb on Ubuntu Raspberry Pi 3
This is an ansible playbook to install MongoDb 4.0.x to Ubuntu Raspberry Pi 3 Operating System.

**Note** Raspbian is not supported.

## Installation platform
Ubuntu Raspberry Pi version below 
```
$ uname -srv
Linux 4.15.0-1031-raspi2 #33-Ubuntu SMP PREEMPT Wed Jan 16 09:52:45 UTC 2019
```
[link](https://www.ubuntu.com/download/iot/raspberry-pi-2-3) to download the image


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
---
Readme in Thai Language

โครงการนี้ใช้เครื่องมือ Ansible สำหรับติดตั้ง MongoDb บน Raspberry Pi 3 บนระบบปฏิบัติการ Ubuntu

โครงการนี้ใช้ไม่ได้กับระบบปฏิบัติการ Raspbian

## ระบบปฏิบัติการ

Ubuntu Raspberry Pi เวอร์ชั่น
```
$ uname -srv
Linux 4.15.0-1031-raspi2 #33-Ubuntu SMP PREEMPT Wed Jan 16 09:52:45 UTC 2019
```
[ตามลิ้ง](https://www.ubuntu.com/download/iot/raspberry-pi-2-3) สำหรับดาวน์โหลดระบบปฏิบัติการ

## ชั้นตอน

1. สร้างไฟล์ชื่อ ```'hosts'``` ตัวอย่างข้อมูลในไฟล์ เปลี่ยน IP address และ รหัสผ่าน ให้เป็นของเครื่องที่ต้องการติดตั้ง
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
2. สังติดตั้งใช้ playbook
```
ansible-playbook -i hosts site.yml
```