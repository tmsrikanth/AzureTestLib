from azure.mgmt.resource import ResourceManagementClient
from azure.identity import DefaultAzureCredential
from config import subscription_id

class ResourceManager:
    def __init__(self, credential=None):
        self.credential = credential or DefaultAzureCredential()
        self.client = ResourceManagementClient(self.credential, subscription_id)

    def create_resource_group(self, resource_group_name, location):
        resource_group_params = {"location": location}
        resource_group = self.client.resource_groups.create_or_update(resource_group_name, resource_group_params)
        return resource_group

    def delete_resource_group(self, resource_group_name):
        delete_async_operation = self.client.resource_groups.begin_delete(resource_group_name)
        delete_async_operation.wait()
        return f"Resource group '{resource_group_name}' deleted."

    def list_resource_groups(self):
        resource_groups = self.client.resource_groups.list()
        return list(resource_groups)

# Example usage
if __name__ == "__main__":
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