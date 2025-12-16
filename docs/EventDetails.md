# EventDetails

Event-specific details, structured based on event type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. | 
**updated_fields** | **List[str]** | List of fields that were updated in the resource. | 
**previous_owner** | **str** | The previous owner fleet (null if none). | [optional] 
**new_owner** | **str** | The new owner fleet (null if removed). | [optional] 
**matching_fleets** | **List[str]** | List of fleet names that match the device. | 
**resolution_type** | **str** | How the conflict was resolved. | 
**assigned_owner** | **str** | The fleet assigned as owner (null if no owner). | [optional] 
**previous_matching_fleets** | **List[str]** | List of fleets that previously matched the device. | [optional] 
**error_message** | **str** | The error message describing the permanent failure. | 
**retry_count** | **int** | Number of times the task was retried before being marked as permanently failed. | 
**original_event** | [**Event**](Event.md) |  | 
**commit_hash** | **str** | Hash of the last commit. | 
**change_count** | **int** | Number of changes introduced by this ResourceSync update. | 
**error_count** | **int** | Number of errors encountered by this ResourceSync update. | 
**repository** | **str** | The name of the repository that was updated. | 
**template_version** | **str** | The name of the TemplateVersion that the device is being selected to render. | 
**rollout_strategy** | **str** | Rollout strategy type. | 
**batch** | **str** | The batch within the fleet rollout. | 
**success_percentage** | **int** | The success percentage of the batch. | 
**total** | **int** | The total number of devices in the batch. | 
**successful** | **int** | The number of successful devices in the batch. | 
**failed** | **int** | The number of failed devices in the batch. | 
**timed_out** | **int** | The number of timed out devices in the batch. | 
**fleet_name** | **str** | The name of the fleet that the device is being selected for. | 

## Example

```python
from flightctl.models.event_details import EventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EventDetails from a JSON string
event_details_instance = EventDetails.from_json(json)
# print the JSON string representation of the object
print(EventDetails.to_json())

# convert the object into a dict
event_details_dict = event_details_instance.to_dict()
# create an instance of EventDetails from a dict
event_details_from_dict = EventDetails.from_dict(event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


