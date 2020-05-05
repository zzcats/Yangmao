from azure.storage.blob import BlobServiceClient
from constants.key_constants import KeyConstants


class StorageClient:
    def __init__(self, connectstring, container):
        self.blob_service = BlobServiceClient.from_connection_string(connectstring)
        self.container_client = self.blob_service.get_container_client(container)

    def upload_file(self, local_path, blob_name):
        #self.file_service.create_file_from_stream("picture",None,"tmp","",1)
        blob_client = self.container_client.get_blob_client(blob_name)
        with open(local_path, "rb") as data:
            blob_client.upload_blob(data, blob_type="BlockBlob")


