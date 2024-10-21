import unittest
from unittest.mock import patch
from azure.identity import DefaultAzureCredential, ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
from AzureAuthenticate.AzureAuthenticator import AzureAuthenticator

class TestAzureAuthenticator(unittest.TestCase):
    def setUp(self):
        self.subscription_id = "your-subscription-id"
        self.authenticator = AzureAuthenticator(self.subscription_id)

    @patch('azure.identity.DefaultAzureCredential')
    def test_authenticate_with_ad(self, mock_default_credential):
        credential = self.authenticator.authenticate_with_ad()
        self.assertIsInstance(credential, DefaultAzureCredential)
        mock_default_credential.assert_called_once()

    @patch('azure.identity.ClientSecretCredential')
    def test_authenticate_with_service_principal(self, mock_client_secret_credential):
        tenant_id = "your-tenant-id"
        client_id = "your-client-id"
        client_secret = "your-client-secret"
        credential = self.authenticator.authenticate_with_service_principal(tenant_id, client_id, client_secret)
        self.assertIsInstance(credential, ClientSecretCredential)
        mock_client_secret_credential.assert_called_once_with(tenant_id, client_id, client_secret)

    @patch('azure.mgmt.resource.ResourceManagementClient')
    def test_get_resource_client(self, mock_resource_client):
        credential = DefaultAzureCredential()
        resource_client = self.authenticator.get_resource_client(credential)
        self.assertIsInstance(resource_client, ResourceManagementClient)
        mock_resource_client.assert_called_once_with(credential, self.subscription_id)

if __name__ == '__main__':
    unittest.main()
