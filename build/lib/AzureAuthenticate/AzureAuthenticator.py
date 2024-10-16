class AzureAuthenticator:
    def __init__(self, subscription_id):
        self.subscription_id = subscription_id

    def authenticate_with_ad(self):
        from azure.identity import DefaultAzureCredential
        # Use DefaultAzureCredential for Azure AD authentication
        credential = DefaultAzureCredential()
        return credential

    def authenticate_with_service_principal(self, tenant_id, client_id, client_secret):
        from azure.identity import ClientSecretCredential
        # Use ClientSecretCredential for Service Principal authentication
        credential = ClientSecretCredential(tenant_id, client_id, client_secret)
        return credential

    def get_resource_client(self, credential):
        from azure.mgmt.resource import ResourceManagementClient
        # Create a ResourceManagementClient using the provided credential
        resource_client = ResourceManagementClient(credential, self.subscription_id)
        return resource_client