# ResourceSyncCompletedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. | 
**commit_hash** | **str** | Hash of the last commit. | 
**change_count** | **int** | Number of changes introduced by this ResourceSync update. | 
**error_count** | **int** | Number of errors encountered by this ResourceSync update. | 

## Example

```python
from flightctl.models.resource_sync_completed_details import ResourceSyncCompletedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSyncCompletedDetails from a JSON string
resource_sync_completed_details_instance = ResourceSyncCompletedDetails.from_json(json)
# print the JSON string representation of the object
print(ResourceSyncCompletedDetails.to_json())

# convert the object into a dict
resource_sync_completed_details_dict = resource_sync_completed_details_instance.to_dict()
# create an instance of ResourceSyncCompletedDetails from a dict
resource_sync_completed_details_from_dict = ResourceSyncCompletedDetails.from_dict(resource_sync_completed_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


