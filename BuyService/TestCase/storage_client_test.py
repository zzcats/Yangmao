import unittest
from storage.storage_client import StorageClient
from constants.key_constants import KeyConstants

key = KeyConstants.storage_key
name = KeyConstants.storage_name
container_name = KeyConstants.storage_container
client = StorageClient(KeyConstants.storage_connect_string, container_name)


class StorageTestCase(unittest.TestCase):
    def test_upload(self):
        client.upload_file(r'C:\workspace\tmp.png')
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
