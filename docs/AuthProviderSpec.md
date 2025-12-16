# AuthProviderSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** | The type of authentication provider. | 
**display_name** | **str** | Human-readable display name for the provider. | [optional] 
**issuer** | **str** | The OAuth2 issuer identifier (used for issuer identification in tokens). | 
**client_id** | **str** | The OAuth2 client ID. | 
**client_secret** | **str** | The OAuth2 client secret. | 
**enabled** | **bool** | Whether this K8s provider is enabled. | [optional] [default to True]
**scopes** | **List[str]** | List of OAuth2 scopes to request. | 
**organization_assignment** | [**AuthOrganizationAssignment**](AuthOrganizationAssignment.md) |  | 
**username_claim** | **List[str]** | JSON path to the username claim in the userinfo response as an array of path segments (e.g., [\&quot;preferred_username\&quot;], [\&quot;email\&quot;], [\&quot;sub\&quot;]). | [optional] [default to [preferred_username]]
**role_assignment** | [**AuthRoleAssignment**](AuthRoleAssignment.md) |  | 
**authorization_url** | **str** | The OAuth2 authorization endpoint URL. | 
**token_url** | **str** | The OAuth2 token endpoint URL. | 
**userinfo_url** | **str** | The OAuth2 userinfo endpoint URL. | 
**introspection** | [**OAuth2Introspection**](OAuth2Introspection.md) |  | [optional] 
**cluster_control_plane_url** | **str** | The OpenShift cluster control plane URL. | [optional] 
**project_label_filter** | **str** | If specified, only projects with this label will be considered. The label selector should be in the format &#39;key&#39; or &#39;key&#x3D;value&#39;. If only the key is provided, any project with that label (regardless of value) will be included. This enables server-side filtering for better performance. | [optional] 
**role_suffix** | **str** | Optional suffix to strip from ClusterRole names when normalizing role names. Used for multi-release deployments where ClusterRoles have namespace-specific names (e.g., flightctl-admin-&lt;namespace&gt;). | [optional] 
**api_url** | **str** | The internal Kubernetes API URL. | 
**rbac_ns** | **str** | The RBAC namespace for permissions. | [optional] 

## Example

```python
from flightctl.models.auth_provider_spec import AuthProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of AuthProviderSpec from a JSON string
auth_provider_spec_instance = AuthProviderSpec.from_json(json)
# print the JSON string representation of the object
print(AuthProviderSpec.to_json())

# convert the object into a dict
auth_provider_spec_dict = auth_provider_spec_instance.to_dict()
# create an instance of AuthProviderSpec from a dict
auth_provider_spec_from_dict = AuthProviderSpec.from_dict(auth_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


