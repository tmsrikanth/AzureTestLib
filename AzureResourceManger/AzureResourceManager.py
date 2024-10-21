from azure.mgmt.resource import ResourceManagementClient
from azure.identity import DefaultAzureCredential
from config import subscription_id

class ResourceManager:
    """
    A class to manage Azure resource groups.

    Attributes:
        credential (DefaultAzureCredential): The credential for Azure authentication.
        client (ResourceManagementClient): The client for managing Azure resources.
    """

    def __init__(self, credential=None):
        """
        Initializes the ResourceManager with the given credential.

        Args:
            credential (DefaultAzureCredential, optional): The credential for Azure authentication. Defaults to None.
        """
        self.credential = credential or DefaultAzureCredential()
        self.client = ResourceManagementClient(self.credential, subscription_id)

    def create_resource_group(self, resource_group_name, location):
        """
        Creates a resource group in the specified location.

        Args:
            resource_group_name (str): The name of the resource group.
            location (str): The location for the resource group.

        Returns:
            ResourceGroup: The created resource group.
        """
        resource_group_params = {"location": location}
        resource_group = self.client.resource_groups.create_or_update(resource_group_name, resource_group_params)
        return resource_group

    def delete_resource_group(self, resource_group_name):
        """
        Deletes the specified resource group.

        Args:
            resource_group_name (str): The name of the resource group to delete.

        Returns:
            str: A message indicating the resource group was deleted.
        """
        delete_async_operation = self.client.resource_groups.begin_delete(resource_group_name)
        delete_async_operation.wait()
        return f"Resource group '{resource_group_name}' deleted."

    def list_resource_groups(self):
        """
        Lists all resource groups in the subscription.

        Returns:
            list: A list of resource groups.
        """
        resource_groups = self.client.resource_groups.list()
        return list(resource_groups)