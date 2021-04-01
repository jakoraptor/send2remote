#!/usr/bin/python3
from cortexutils.analyzer import Analyzer
from client import RemoteClient
from os.path import basename


class SendToSift(Analyzer):
    def __init__(self):
        Analyzer.__init__(self)
        self.host = self.get_param("config.host", None, "no host provided")
        self.username = self.get_param('config.username', None, 'Remote host username is missing')
        # self.password = self.get_param('config.password', None, None)
        self.ssh_key_filepath = self.get_param('config.ssh_key_filepath', None, 'Location of local SSH key required')
        self.remote_path = self.get_param('config.remote_path', None, 'Remote path location required')

    def run(self):
        Analyzer.run(self)
        if self.data_type == "file":
            """Initialise remote host client and execute actions."""
            filepath = self.get_param('file', None, 'file is missing')
            filename = self.get_param('filename' basename(filepath))
            remote = RemoteClient(self.host, self.username, self.ssh_key_filepath, self.remote_path)
            remote.scp.put(filepath, remote_path=self.remote_path + '/' + filename)
        else:
            self.error("invalid data type!")


if __name__ == "__main__":
    SendToSift().run()
