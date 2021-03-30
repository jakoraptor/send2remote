#!/usr/bin/python3
from typing import List
from paramiko import SSHClient, AutoAddPolicy, RSAKey
from paramiko.auth_handler import AuthenticationException, SSHException
from scp import SCPClient, SCPException
from log import LOGGER


class RemoteClient:
    """Client to interact with a remote host via SSH & SCP."""

    def __init__(
            self,
            host: str,
            user: str,
            # password: str,
            ssh_key_filepath: str,
            remote_path: str,
    ):
        self.host = host
        self.user = user
        # self.password = password
        self.ssh_key_filepath = ssh_key_filepath
        self.remote_path = remote_path
        self.client = None

    @property
    def connection(self):
        """Open Connection to remote host."""
        try:
            client = SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(AutoAddPolicy())
            client.connect(
                self.host,
                username=self.user,
                # password=self.password,
                key_filename=self.ssh_key_filepath,
                timeout=5000,
            )
            return client
        except AuthenticationException as e:
            LOGGER.error(f"Authentication failed: did you remember to create an SSH key? {e}")
            raise e

    @property
    def scp(self) -> SCPClient:
        conn = self.connection
        return SCPClient(conn.get_transport())

    def _get_ssh_key(self):
        """Fetch locally stored SSH key."""
        try:
            self.ssh_key = RSAKey.from_private_key_file(self.ssh_key_filepath)
            LOGGER.info(f"Found SSH key at self {self.ssh_key_filepath}")
            return self.ssh_key
        except SSHException as e:
            LOGGER.error(e)

    def disconnect(self):
        """Close ssh connection."""
        if self.client:
            self.client.close()
        if self.scp:
            self.scp.close()

    def bulk_upload(self, files):
        """"
        Upload multiple bloops to a remote directory.

        :param files: List of local bloops to be uploaded.
        :type files: List[str]
        """
        try:
            self.scp.put(files, remote_path=self.remote_path)
            LOGGER.info(f"Finished uploading {len(files)} files to {self.remote_path} on {self.host}")
        except SCPException as e:
            raise e
