# AzurePythonConnectors

## Overview

AzurePythonConnectors is a Python package designed to facilitate connections to various Azure services, including Azure SQL Database, Azure Resource Manager, Azure Key Vault, and Azure Blob Storage. This package leverages Azure AD authentication for secure access to these services.

## Features

- **Azure SQL Database**: Connect and execute queries using Azure AD authentication.
- **Azure Resource Manager**: Manage Azure resource groups.
- **Azure Key Vault**: Access secrets stored in Azure Key Vault.
- **Azure Blob Storage**: Interact with Azure Blob Storage.

## Installation

### Using `setup.py`

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/AzurePythonConnectors.git
   cd AzurePythonConnectors
   

2. Install the package:
   ```sh
Install the package:
```markdown
pip install .
```

Using Poetry
Install Poetry:  

```markdown
curl -sSL https\://install.python-poetry.org | python3 -
```
Install the dependencies and package:

```markdown
poetry install
```
### Azure SQL Client
```markdown

from AzureSQL.AzureSQLClient import AzureSQLClient

server = 'your-server-name.database.windows.net'
database = 'your-database-name'
azure_sql_client = AzureSQLClient(server, database)

try:
    azure_sql_client.connect()
    query = "SELECT TOP 10 * FROM your_table_name"
    results = azure_sql_client.execute_query(query)
    for row in results:
        print(row)
finally:
    azure_sql_client.close()
```

### Azure Resource Manage
```markdown

from AzureResourceManger.AzureResourceManager import ResourceManager

resource_manager = ResourceManager()

# Create a resource group
resource_group_name = "myResourceGroup"
location = "eastus"
resource_group = resource_manager.create_resource_group(resource_group_name, location)
print(f"Resource Group '{resource_group_name}' created in location '{location}'")

# List resource groups
resource_groups = resource_manager.list_resource_groups()
for rg in resource_groups:
    print(f"Resource Group: {rg.name}, Location: {rg.location}")

# Delete the resource group
delete_message = resource_manager.delete_resource_group(resource_group_name)
print(delete_message)
```

### Azure Service Factory
```markdown
from ClientFactory.AzureServiceFactory import AzureServiceFactory

# Using DefaultAzureCredential
factory_default = AzureServiceFactory(auth_method="default")

# Get Resource Management Client
resource_client_default = factory_default.get_client("resource")
print(f"Resource Management Client (Default): {resource_client_default}")

# Get Secret Client with vault_url
secret_client_default = factory_default.get_client("key_vault", vault_url="https://your-key-vault-name.vault.azure.net/")
print(f"Secret Client (Default): {secret_client_default}")

# Get Blob Service Client with account_url
blob_service_client_default = factory_default.get_client("blob_storage", account_url="https://your-storage-account-name.blob.core.windows.net")
print(f"Blob Service Client (Default): {blob_service_client_default}")
```

### Azure Authenticator
```markdown
from AzureAuthenticate.AzureAuthenticator import AzureAuthenticator

subscription_id = "your-subscription-id"
authenticator = AzureAuthenticator(subscription_id)

# Authenticate with Azure AD
credential = authenticator.authenticate_with_ad()
resource_client = authenticator.get_resource_client(credential)
print(f"Resource Management Client: {resource_client}")
```

### Configuration
```markdown
subscription_id = "your-subscription-id"
tenant_id = "your-tenant-id"
client_id = "your-client-id"
client_secret = "your-client-secret"
key_vault_name = "your-key-vault-name"
secret_name = "your-secret-name"
storage_account_name = "your-storage-account-name"
container_name = "your-container-name"
```
## License
This`README.md` provides an overview of the project, installation instructions, usage examples, configuration details, and license information.