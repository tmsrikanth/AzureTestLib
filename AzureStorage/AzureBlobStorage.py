from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from config import storage_account_name, container_name

class AzureBlobStorage:
    """
    A class to interact with Azure Blob Storage.

    Attributes:
        storage_account_name (str): The name of the Azure Storage account.
        container_name (str): The name of the container in Azure Storage.
        credential (DefaultAzureCredential): The credential for Azure AD authentication.
        blob_service_client (BlobServiceClient): The client for Azure Blob Storage.
        container_client (ContainerClient): The client for the container in Azure Blob Storage.
    """

    def __init__(self, storage_account_name, container_name):
        """
        Initializes the AzureBlobStorage with the storage account and container names.

        Args:
            storage_account_name (str): The name of the Azure Storage account.
            container_name (str): The name of the container in Azure Storage.
        """
        self.storage_account_name = storage_account_name
        self.container_name = container_name
        self.credential = DefaultAzureCredential()
        self.blob_service_client = BlobServiceClient(
            account_url=f"https://{storage_account_name}.blob.core.windows.net",
            credential=self.credential
        )
        self.container_client = self.blob_service_client.get_container_client(container_name)

    def upload_file(self, file_path, blob_name):
        """
        Uploads a file to the specified blob in Azure Blob Storage.

        Args:
            file_path (str): The local path to the file to upload.
            blob_name (str): The name of the blob in Azure Blob Storage.

        Raises:
            Exception: If there is an error uploading the file.
        """
        try:
            blob_client = self.container_client.get_blob_client(blob_name)
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data)
            print(f"File {file_path} uploaded to blob {blob_name}.")
        except Exception as e:
            print(f"Failed to upload file {file_path} to blob {blob_name}: {e}")

    def download_file(self, blob_name, download_path):
        """
        Downloads a blob from Azure Blob Storage to the specified local path.

        Args:
            blob_name (str): The name of the blob in Azure Blob Storage.
            download_path (str): The local path to save the downloaded file.

        Raises:
            Exception: If there is an error downloading the file.
        """
        try:
            blob_client = self.container_client.get_blob_client(blob_name)
            with open(download_path, "wb") as download_file:
                download_file.write(blob_client.download_blob().readall())
            print(f"Blob {blob_name} downloaded to {download_path}.")
        except Exception as e:
            print(f"Failed to download blob {blob_name} to {download_path}: {e}")

# Example usage
if __name__ == "__main__":
    azure_blob_storage = AzureBlobStorage(storage_account_name, container_name)
    azure_blob_storage.upload_file("path/to/local/file.txt", "blob-name.txt")
    azure_blob_storage.download_file("blob-name.txt", "path/to/download/file.txt")