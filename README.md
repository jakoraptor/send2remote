# send2remote
cortex analyzer to send a file from the hive to a dedicated malware analysis box for extended manual analysis

credit to https://github.com/hackersandslackers/paramiko-tutorial for the bulk of the scripting

## Usage

* first, set up your VMs, you will need a working Hive VM as per https://github.com/TheHive-Project/TheHiveDocs/blob/master/training-material.md 
* you will also need another machine to send the files to, i.e. sift workstation: https://digital-forensics.sans.org/community/downloads
* clone the files to the analyzer directory in the hive, i.e. <code>/opt/Cortex-Analyzers/analyzers</code>
* make the send2remote.py file executable - <code>chmod +x send2remote.py</code>
* cortex needs to be able to connect to the sift box over ssh, so make sure cortex has shared it's public key with sift. https://www.ssh.com/ssh/keygen/
* make sure the local ssh key you just created is owned/readable by cortex user - <code>chown -R cortex:cortex cortex</code>
* configure analyzer in cortex using gui
* (optional) test analyzer works from within cortex gui
