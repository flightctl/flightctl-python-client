# DependencySyncProbeFailedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. | 
**resource_key** | **str** | The resource key identifying the dependency that failed (e.g. \&quot;git:my-repo/main\&quot;). | 
**error** | **str** | The error message from the failed probe. | 

## Example

```python
from flightctl.models.dependency_sync_probe_failed_details import DependencySyncProbeFailedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DependencySyncProbeFailedDetails from a JSON string
dependency_sync_probe_failed_details_instance = DependencySyncProbeFailedDetails.from_json(json)
# print the JSON string representation of the object
print(DependencySyncProbeFailedDetails.to_json())

# convert the object into a dict
dependency_sync_probe_failed_details_dict = dependency_sync_probe_failed_details_instance.to_dict()
# create an instance of DependencySyncProbeFailedDetails from a dict
dependency_sync_probe_failed_details_from_dict = DependencySyncProbeFailedDetails.from_dict(dependency_sync_probe_failed_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


