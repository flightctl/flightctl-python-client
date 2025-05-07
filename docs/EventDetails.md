# EventDetails

Event-specific details, structured based on event type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_fields** | **List[str]** | List of fields that were updated in the resource. | 
**previous_owner** | **str** | The previous owner (if applicable). | [optional] 
**new_owner** | **str** | The new owner (if applicable). | [optional] 

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


