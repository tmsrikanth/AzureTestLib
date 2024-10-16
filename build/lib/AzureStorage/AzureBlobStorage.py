from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from config import storage_account_name, container_name

class AzureBlobStorage:
    def __init__(self, storage_account_name, container_name):
        self.storage_account_name = storage_account_name
        self.container_name = container_name
        self.credential = DefaultAzureCredential()
        self.blob_service_client = BlobServiceClient(
            account_url=f"https://{storage_account_name}.blob.core.windows.net",
            credential=self.credential
        )
        self.container_client = self.blob_service_client.get_container_client(container_name)

    def upload_file(self, file_path, blob_name):
        blob_client = self.container_client.get_blob_client(blob_name)
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
        print(f"File {file_path} uploaded to blob {blob_name}.")

    def download_file(self, blob_name, download_path):
        blob_client = self.container_client.get_blob_client(blob_name)
        with open(download_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())
        print(f"Blob {blob_name} downloaded to {download_path}.")

# Example usage
if __name__ == "__main__":
    azure_blob_storage = AzureBlobStorage(storage_account_name, container_name)
    azure_blob_storage.upload_file("path/to/local/file.txt", "blob-name.txt")
    azure_blob_storage.download_file("blob-name.txt", "path/to/download/file.txt")