from azure.identity import DefaultAzureCredential, ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobServiceClient
from config import subscription_id, tenant_id, client_id, client_secret

class AzureServiceFactory:
    def __init__(self, auth_method="default"):
        if auth_method == "default":
            self.credential = DefaultAzureCredential()
        elif auth_method == "service_principal":
            self.credential = ClientSecretCredential(tenant_id, client_id, client_secret)
        else:
            raise ValueError(f"Unknown authentication method: {auth_method}")

    def get_client(self, service_type, **kwargs):
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

# Example usage
if __name__ == "__main__":
    # Using DefaultAzureCredential
    factory_default = AzureServiceFactory(auth_method="default")

    # Get Resource Management Client
    resource_client_default = factory_default.get_client("resource")
    print(f"Resource Management Client (Default): {resource_client_default}")
    # Define the resource group parameters
    resource_group_name = "myResourceGroup"
    location = "eastus"  # Default region

    # Create the resource group
    resource_group_params = {"location": location}
    resource_group = resource_client_default .resource_groups.create_or_update(resource_group_name, resource_group_params)

    # Get Secret Client with vault_url
    secret_client_default = factory_default.get_client("key_vault", vault_url="https://your-key-vault-name.vault.azure.net/")
    print(f"Secret Client (Default): {secret_client_default}")

    # Get Blob Service Client with account_url
    blob_service_client_default = factory_default.get_client("blob_storage", account_url="https://your-storage-account-name.blob.core.windows.net")
    print(f"Blob Service Client (Default): {blob_service_client_default}")