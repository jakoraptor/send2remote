#!/usr/bin/python3
"""Perform tasks against a remote host."""
from cortexutils.responder import Responder
from client import RemoteClient
from os import walk, path
from typing import List

local_file_directory = "/tmp/bloops/"


class SendToSift(Responder):
    def __init__(self):
        Responder.__init__(self)
        self.host = self.get_param("config.host", "192.168.135.133", "no host provided")
        self.username = self.get_param('config.username', None, 'Remote host username is missing')
        # self.password = self.get_param('config.password', None, None)
        self.ssh_key_filepath = self.get_param('config.ssh_key_filepath', None, 'Location of local SSH key required')
        self.remote_path = self.get_param('config.remote_path', '/home/sansforensics/suspect', 'Remote path location required')

    def run(self):
        Responder.run(self)
        if self.data_type == "file":
            """Initialise remote host client and execute actions."""
            remote = RemoteClient(self.host, self.username, self.ssh_key_filepath, self.remote_path)
            upload_files_to_remote(remote)
        else:
            self.error("invalid data type!")


def upload_files_to_remote(remote) -> object:
    """Upload bloops to remote via SCP"""
    local_files = fetch_local_files(local_file_directory)
    remote.bulk_upload(local_files)


def fetch_local_files(local_file_dir: str) -> List[str]:
    """Create list of file paths."""
    local_files = walk(local_file_dir)
    basedir = path.abspath(path.dirname(__file__))
    for root, dirs, files in local_files:
        return [f"{basedir}/{root}/{file}" for file in files]


if __name__ == "__main__":
    SendToSift().run()
