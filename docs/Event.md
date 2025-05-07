# Event


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  | 
**involved_object** | [**ObjectReference**](ObjectReference.md) |  | 
**reason** | **str** | A short, machine-readable string that describes the reason for the event. | 
**message** | **str** | A human-readable description of the status of this operation. | 
**details** | [**EventDetails**](EventDetails.md) |  | [optional] 
**type** | **str** | The type of the event. One of Normal, Warning. | 
**source** | [**EventSource**](EventSource.md) |  | 
**actor** | **str** | The name of the user or service that triggered the event. The value will be prefixed by either user: (for human users) or service: (for automated services). | 

## Example

```python
from flightctl.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


