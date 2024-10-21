class AzureAuthenticator:
    """
    A class to handle Azure authentication.

    Attributes:
        subscription_id (str): The subscription ID for Azure.
    """

    def __init__(self, subscription_id):
        """
        Initializes the AzureAuthenticator with the given subscription ID.

        Args:
            subscription_id (str): The subscription ID for Azure.
        """
        self.subscription_id = subscription_id

    def authenticate_with_ad(self):
        """
        Authenticates with Azure AD using DefaultAzureCredential.

        Returns:
            DefaultAzureCredential: The credential for Azure AD authentication.
        """
        from azure.identity import DefaultAzureCredential
        credential = DefaultAzureCredential()
        return credential

    def authenticate_with_service_principal(self, tenant_id, client_id, client_secret):
        """
        Authenticates with Azure AD using a service principal.

        Args:
            tenant_id (str): The tenant ID for Azure AD.
            client_id (str): The client ID for Azure AD.
            client_secret (str): The client secret for Azure AD.

        Returns:
            ClientSecretCredential: The credential for service principal authentication.
        """
        from azure.identity import ClientSecretCredential
        credential = ClientSecretCredential(tenant_id, client_id, client_secret)
        return credential

    def get_resource_client(self, credential):
        """
        Returns a ResourceManagementClient using the provided credential.

        Args:
            credential (DefaultAzureCredential or ClientSecretCredential): The credential for Azure authentication.

        Returns:
            ResourceManagementClient: The client for managing Azure resources.
        """
        from azure.mgmt.resource import ResourceManagementClient
        resource_client = ResourceManagementClient(credential, self.subscription_id)
        return resource_client