from azure.identity import DefaultAzureCredential, ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobServiceClient
from config import subscription_id, tenant_id, client_id, client_secret

class AzureServiceFactory:
    """
    A factory class to create Azure service clients.

    Attributes:
        credential (DefaultAzureCredential or ClientSecretCredential): The credential for Azure authentication.
    """

    def __init__(self, auth_method="default"):
        """
        Initializes the AzureServiceFactory with the specified authentication method.

        Args:
            auth_method (str, optional): The authentication method ("default" or "service_principal"). Defaults to "default".

        Raises:
            ValueError: If an unknown authentication method is provided.
        """
        if auth_method == "default":
            self.credential = DefaultAzureCredential()
        elif auth_method == "service_principal":
            self.credential = ClientSecretCredential(tenant_id, client_id, client_secret)
        else:
            raise ValueError(f"Unknown authentication method: {auth_method}")

    def get_client(self, service_type, **kwargs):
        """
        Returns a client for the specified Azure service.

        Args:
            service_type (str): The type of Azure service ("resource", "key_vault", or "blob_storage").
            **kwargs: Additional arguments required for the service client.

        Returns:
            object: The Azure service client.

        Raises:
            ValueError: If an unknown service type is provided or required arguments are missing.
        """
        if service_type == "resource":
            return ResourceManagementClient(self.credential, subscription_id)
        elif service_type == "key_vault":
            vault_url = kwargs.get("vault_url")
            if not vault_url:
                raise ValueError("vault_url is required for key_vault service")
            return SecretClient(vault_url=vault_url, credential=self.credential)
        elif service_type == "blob_storage":
            account_url = kwargs.get("account_url")
            if not account_url:
                raise ValueError("account_url is required for blob_storage service")
            return BlobServiceClient(account_url=account_url, credential=self.credential)
        else:
            raise ValueError(f"Unknown service type: {service_type}")