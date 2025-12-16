# OpenShiftProviderSpec

OpenShiftProviderSpec describes an OpenShift OAuth provider configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** | The type of authentication provider. | 
**display_name** | **str** | Human-readable display name for the provider. | [optional] 
**issuer** | **str** | The OAuth2 issuer identifier (used for issuer identification in tokens). | [optional] 
**authorization_url** | **str** | The OAuth2 authorization endpoint URL. | [optional] 
**token_url** | **str** | The OAuth2 token endpoint URL. | [optional] 
**client_id** | **str** | The OAuth2 client ID. | [optional] 
**client_secret** | **str** | The OAuth2 client secret. | [optional] 
**enabled** | **bool** | Whether this OpenShift provider is enabled. | [optional] [default to True]
**scopes** | **List[str]** | List of OAuth2 scopes to request. | [optional] 
**cluster_control_plane_url** | **str** | The OpenShift cluster control plane URL. | [optional] 
**project_label_filter** | **str** | If specified, only projects with this label will be considered. The label selector should be in the format &#39;key&#39; or &#39;key&#x3D;value&#39;. If only the key is provided, any project with that label (regardless of value) will be included. This enables server-side filtering for better performance. | [optional] 
**role_suffix** | **str** | Optional suffix to strip from ClusterRole names when normalizing role names. Used for multi-release deployments where ClusterRoles have namespace-specific names (e.g., flightctl-admin-&lt;namespace&gt;). | [optional] 

## Example

```python
from flightctl.models.open_shift_provider_spec import OpenShiftProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of OpenShiftProviderSpec from a JSON string
open_shift_provider_spec_instance = OpenShiftProviderSpec.from_json(json)
# print the JSON string representation of the object
print(OpenShiftProviderSpec.to_json())

# convert the object into a dict
open_shift_provider_spec_dict = open_shift_provider_spec_instance.to_dict()
# create an instance of OpenShiftProviderSpec from a dict
open_shift_provider_spec_from_dict = OpenShiftProviderSpec.from_dict(open_shift_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


