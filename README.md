# send2sift
cortex analyzer to send a file from the hive to another server, in this case sift workstation. (Any other OS could be used in theory but analyser tested only to Sift)

credit to https://github.com/hackersandslackers/paramiko-tutorial for the bulk of the scripting

## Usage

* first, set up your VMs, you will need a working Hive VM as per https://github.com/TheHive-Project/TheHiveDocs/blob/master/training-material.md 
* you will also need another machine to send the files to, i.e. sift workstation: https://digital-forensics.sans.org/community/downloads
* clone the files to the analyzer directory in the hive, i.e. <code>/opt/Cortex-Analyzers/analyzers</code>
* cortex needs to be able to connect to the sift box over ssh, so make sure cortex has shared it's public key with sift. https://www.ssh.com/ssh/keygen/
* configure analyzer in cortex
* test analyzer 
