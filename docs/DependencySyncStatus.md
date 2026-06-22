# DependencySyncStatus

DependencySyncStatus represents the synchronization fingerprints for external dependencies of a device, captured at render time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_refs** | [**List[DependencySyncConfigRefStatus]**](DependencySyncConfigRefStatus.md) | Per-config-provider fingerprint and last update time, set when the device renders. | [optional] 

## Example

```python
from flightctl.models.dependency_sync_status import DependencySyncStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DependencySyncStatus from a JSON string
dependency_sync_status_instance = DependencySyncStatus.from_json(json)
# print the JSON string representation of the object
print(DependencySyncStatus.to_json())

# convert the object into a dict
dependency_sync_status_dict = dependency_sync_status_instance.to_dict()
# create an instance of DependencySyncStatus from a dict
dependency_sync_status_from_dict = DependencySyncStatus.from_dict(dependency_sync_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


