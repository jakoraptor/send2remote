#!/usr/bin/python3
from cortexutils.analyzer import Analyzer
from client import RemoteClient
from os.path import basename
from paramiko.ssh_exception import NoValidConnectionsError, SSHException
from scp import SCPException
from datetime import datetime


class SendToServer(Analyzer):
    def __init__(self):
        Analyzer.__init__(self)
        self.host = self.get_param("config.host", None, "no host provided")
        self.username = self.get_param('config.username', None, 'Remote host username is missing')
        self.passphrase = self.get_param('config.passphrase', None, None)
        self.ssh_key_filepath = self.get_param('config.ssh_key_filepath', None, 'Location of local SSH key required')
        self.remote_path = self.get_param('config.remote_path', None, 'Remote path location required')

    def run(self):
        Analyzer.run(self)
        try:
            if self.data_type == "file":
                """Initialise remote host client and execute actions."""
                filepath = self.get_param('file', None, 'file is missing')
                filename = self.get_param('filename', basename(filepath)).replace(" ", "_")
                remote = RemoteClient(self.host, self.username, self.passphrase, self.ssh_key_filepath, self.remote_path)
                remote.scp.put(filepath, remote_path=f'{self.remote_path}/{filename}_{datetime.now()}')
                self.report({'success': 'file transferred!'})
            else:
                self.error("invalid data type!")
        except (NoValidConnectionsError, SSHException) as e:
            print('SSH Connection refused: Check config in cortex.', e)
        except FileNotFoundError as e:
            print('SSH key not found: Check config in cortex.', e)
        except PermissionError as e:
            print('SSH key incorrect permissions: ensure cortex user can read key specified in Cortex config.', e)
        except SCPException as e:
            print('Remote directory does not exist: Check config in cortex.', e)
            
            
if __name__ == "__main__":
    SendToServer().run()