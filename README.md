# send2sift
cortex analyzer to send a file from the hive to another server

credit to https://github.com/hackersandslackers/paramiko-tutorial for the bulk of the scripting

## Usage

* clone the files to the analyzer directory in the hive, i.e. <code>/opt/Cortex-Analyzers/analyzers/Send2Sift</code>
* cortex needs to be able to connect to the chosen server over ssh, so make sure cortex has a public key on said box.
* configure analyzer in cortex
* test analyzer in test case in the hive
