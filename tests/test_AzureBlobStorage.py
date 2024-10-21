import unittest
from unittest.mock import patch, mock_open, MagicMock
from AzureStorage.AzureBlobStorage  import AzureBlobStorage
from config import storage_account_name, container_name

class TestAzureBlobStorage(unittest.TestCase):

    @patch('AzureBlobStorage.BlobServiceClient')
    def file_uploads_successfully(self, MockBlobServiceClient):
        mock_blob_service_client = MockBlobServiceClient.return_value
        mock_container_client = mock_blob_service_client.get_container_client.return_value
        mock_blob_client = mock_container_client.get_blob_client.return_value

        azure_blob_storage = AzureBlobStorage(storage_account_name, container_name)
        with patch('builtins.open', mock_open(read_data="data")) as mock_file:
            azure_blob_storage.upload_file("file.txt", "blob-name.txt")

        mock_blob_client.upload_blob.assert_called_once()
        mock_file.assert_called_once_with("file.txt", "rb")

    @patch('AzureBlobStorage.BlobServiceClient')
    def file_upload_fails(self, MockBlobServiceClient):
        mock_blob_service_client = MockBlobServiceClient.return_value
        mock_container_client = mock_blob_service_client.get_container_client.return_value
        mock_blob_client = mock_container_client.get_blob_client.return_value
        mock_blob_client.upload_blob.side_effect = Exception("Upload failed")

        azure_blob_storage = AzureBlobStorage(storage_account_name, container_name)
        with patch('builtins.open', mock_open(read_data="data")):
            with self.assertRaises(Exception):
                azure_blob_storage.upload_file("path/to/local/file.txt", "blob-name.txt")

    @patch('AzureBlobStorage.BlobServiceClient')
    def file_downloads_successfully(self, MockBlobServiceClient):
        mock_blob_service_client = MockBlobServiceClient.return_value
        mock_container_client = mock_blob_service_client.get_container_client.return_value
        mock_blob_client = mock_container_client.get_blob_client.return_value
        mock_blob_client.download_blob.return_value.readall.return_value = b"data"

        azure_blob_storage = AzureBlobStorage(storage_account_name, container_name)
        with patch('builtins.open', mock_open()) as mock_file:
            azure_blob_storage.download_file("blob-name.txt", "path/to/download/file.txt")

        mock_blob_client.download_blob.assert_called_once()
        mock_file().write.assert_called_once_with(b"data")

    @patch('AzureBlobStorage.BlobServiceClient')
    def file_download_fails(self, MockBlobServiceClient):
        mock_blob_service_client = MockBlobServiceClient.return_value
        mock_container_client = mock_blob_service_client.get_container_client.return_value
        mock_blob_client = mock_container_client.get_blob_client.return_value
        mock_blob_client.download_blob.side_effect = Exception("Download failed")

        azure_blob_storage = AzureBlobStorage(storage_account_name, container_name)
        with self.assertRaises(Exception):
            azure_blob_storage.download_file("blob-name.txt", "path/to/download/file.txt")

if __name__ == '__main__':
    unittest.main()