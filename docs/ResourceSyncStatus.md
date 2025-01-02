# ResourceSyncStatus

ResourceSyncStatus represents information about the status of a ResourceSync.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**observed_commit** | **str** | The last commit hash that was synced. | [optional] 
**observed_generation** | **int** | The last generation that was synced. | [optional] 
**conditions** | [**List[Condition]**](Condition.md) | Current state of a resourcesync. | 

## Example

```python
from flightctl.models.resource_sync_status import ResourceSyncStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSyncStatus from a JSON string
resource_sync_status_instance = ResourceSyncStatus.from_json(json)
# print the JSON string representation of the object
print(ResourceSyncStatus.to_json())

# convert the object into a dict
resource_sync_status_dict = resource_sync_status_instance.to_dict()
# create an instance of ResourceSyncStatus from a dict
resource_sync_status_from_dict = ResourceSyncStatus.from_dict(resource_sync_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


