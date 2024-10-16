from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from config import key_vault_name, secret_name

class AzureKeyVault:
    def __init__(self, key_vault_name):
        self.key_vault_name = key_vault_name
        self.credential = DefaultAzureCredential()
        self.client = SecretClient(vault_url=f"https://{key_vault_name}.vault.azure.net/", credential=self.credential)

    def get_secret(self, secret_name):
        secret = self.client.get_secret(secret_name)
        return secret.value

# Example usage
if __name__ == "__main__":
    key_vault = AzureKeyVault(key_vault_name)
    secret_value = key_vault.get_secret(secret_name)
    print(f"The value of the secret '{secret_name}' is: {secret_value}")