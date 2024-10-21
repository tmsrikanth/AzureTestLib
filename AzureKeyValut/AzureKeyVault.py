from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from config import key_vault_name, secret_name

class AzureKeyVault:
    """
    A class to interact with Azure Key Vault.

    Attributes:
        key_vault_name (str): The name of the Azure Key Vault.
        credential (DefaultAzureCredential): The credential for Azure AD authentication.
        client (SecretClient): The client for Azure Key Vault.
    """

    def __init__(self, key_vault_name):
        """
        Initializes the AzureKeyVault with the key vault name.

        Args:
            key_vault_name (str): The name of the Azure Key Vault.
        """
        self.key_vault_name = key_vault_name
        self.credential = DefaultAzureCredential()
        self.client = SecretClient(vault_url=f"https://{key_vault_name}.vault.azure.net/", credential=self.credential)

    def get_secret(self, secret_name):
        """
        Retrieves the value of the specified secret from Azure Key Vault.

        Args:
            secret_name (str): The name of the secret in Azure Key Vault.

        Returns:
            str: The value of the secret.

        Raises:
            Exception: If there is an error retrieving the secret.
        """
        try:
            secret = self.client.get_secret(secret_name)
            return secret.value
        except Exception as e:
            print(f"Failed to retrieve secret {secret_name}: {e}")

# Example usage
if __name__ == "__main__":
    key_vault = AzureKeyVault(key_vault_name)
    secret_value = key_vault.get_secret(secret_name)
    if secret_value:
        print(f"The value of the secret '{secret_name}' is: {secret_value}")