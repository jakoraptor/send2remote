#!/usr/bin/python3
"""Perform tasks against a remote host."""
from cortexutils.analyzer import Analyzer
from client import RemoteClient
from os import walk, path
from typing import List


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
            remote = RemoteClient(self.host, self.username, self.ssh_key_filepath, self.remote_path)
            remote.bulkupload(filepath)
        else:
            self.error("invalid data type!")

if __name__ == "__main__":
    SendToSift().run()
