# DependencySyncConfigRefStatus

DependencySyncConfigRefStatus represents the rendered fingerprint for a single config provider's external dependency.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_provider_name** | **str** | The name of the config provider (e.g. the git or HTTP config source name). | 
**fingerprint** | **str** | The fingerprint of the rendered content (e.g. git commit SHA, sha256 of HTTP body, K8s secret ResourceVersion). | [optional] 
**last_updated_at** | **datetime** | The last time the fingerprint changed (i.e. the dependency content was updated). | [optional] 

## Example

```python
from flightctl.models.dependency_sync_config_ref_status import DependencySyncConfigRefStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DependencySyncConfigRefStatus from a JSON string
dependency_sync_config_ref_status_instance = DependencySyncConfigRefStatus.from_json(json)
# print the JSON string representation of the object
print(DependencySyncConfigRefStatus.to_json())

# convert the object into a dict
dependency_sync_config_ref_status_dict = dependency_sync_config_ref_status_instance.to_dict()
# create an instance of DependencySyncConfigRefStatus from a dict
dependency_sync_config_ref_status_from_dict = DependencySyncConfigRefStatus.from_dict(dependency_sync_config_ref_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


