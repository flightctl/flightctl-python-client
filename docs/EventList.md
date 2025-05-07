# EventList

EventList is a list of Events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**metadata** | [**ListMeta**](ListMeta.md) |  | 
**items** | [**List[Event]**](Event.md) | List of Events. | 

## Example

```python
from flightctl.models.event_list import EventList

# TODO update the JSON string below
json = "{}"
# create an instance of EventList from a JSON string
event_list_instance = EventList.from_json(json)
# print the JSON string representation of the object
print(EventList.to_json())

# convert the object into a dict
event_list_dict = event_list_instance.to_dict()
# create an instance of EventList from a dict
event_list_from_dict = EventList.from_dict(event_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


