# KubernetesSecretProviderSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the config provider. | 
**secret_ref** | [**KubernetesSecretProviderSpecSecretRef**](KubernetesSecretProviderSpecSecretRef.md) |  | 

## Example

```python
from flightctl.models.kubernetes_secret_provider_spec import KubernetesSecretProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesSecretProviderSpec from a JSON string
kubernetes_secret_provider_spec_instance = KubernetesSecretProviderSpec.from_json(json)
# print the JSON string representation of the object
print(KubernetesSecretProviderSpec.to_json())

# convert the object into a dict
kubernetes_secret_provider_spec_dict = kubernetes_secret_provider_spec_instance.to_dict()
# create an instance of KubernetesSecretProviderSpec from a dict
kubernetes_secret_provider_spec_from_dict = KubernetesSecretProviderSpec.from_dict(kubernetes_secret_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


