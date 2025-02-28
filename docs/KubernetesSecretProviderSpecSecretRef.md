# KubernetesSecretProviderSpecSecretRef

The reference to a Kubernetes secret.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the secret. | 
**namespace** | **str** | The namespace of the secret. | 
**mount_path** | **str** | Path in the device&#39;s file system at which the secret should be mounted. | 

## Example

```python
from flightctl.models.kubernetes_secret_provider_spec_secret_ref import KubernetesSecretProviderSpecSecretRef

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesSecretProviderSpecSecretRef from a JSON string
kubernetes_secret_provider_spec_secret_ref_instance = KubernetesSecretProviderSpecSecretRef.from_json(json)
# print the JSON string representation of the object
print(KubernetesSecretProviderSpecSecretRef.to_json())

# convert the object into a dict
kubernetes_secret_provider_spec_secret_ref_dict = kubernetes_secret_provider_spec_secret_ref_instance.to_dict()
# create an instance of KubernetesSecretProviderSpecSecretRef from a dict
kubernetes_secret_provider_spec_secret_ref_from_dict = KubernetesSecretProviderSpecSecretRef.from_dict(kubernetes_secret_provider_spec_secret_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


