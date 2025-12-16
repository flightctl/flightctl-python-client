# K8sProviderSpec

K8sProviderSpec describes a Kubernetes/OpenShift provider configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** | The type of authentication provider. | 
**display_name** | **str** | Human-readable display name for the provider. | [optional] 
**api_url** | **str** | The internal Kubernetes API URL. | 
**rbac_ns** | **str** | The RBAC namespace for permissions. | [optional] 
**enabled** | **bool** | Whether this K8s provider is enabled. | [optional] [default to True]
**organization_assignment** | [**AuthOrganizationAssignment**](AuthOrganizationAssignment.md) |  | 
**role_assignment** | [**AuthRoleAssignment**](AuthRoleAssignment.md) |  | 
**role_suffix** | **str** | Optional suffix to strip from ClusterRole names when normalizing role names. Used for multi-release deployments where ClusterRoles have namespace-specific names (e.g., flightctl-admin-&lt;namespace&gt;). | [optional] 

## Example

```python
from flightctl.models.k8s_provider_spec import K8sProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of K8sProviderSpec from a JSON string
k8s_provider_spec_instance = K8sProviderSpec.from_json(json)
# print the JSON string representation of the object
print(K8sProviderSpec.to_json())

# convert the object into a dict
k8s_provider_spec_dict = k8s_provider_spec_instance.to_dict()
# create an instance of K8sProviderSpec from a dict
k8s_provider_spec_from_dict = K8sProviderSpec.from_dict(k8s_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


