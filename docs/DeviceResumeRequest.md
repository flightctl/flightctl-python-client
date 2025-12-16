# DeviceResumeRequest

Request to resume devices based on label selector and/or field selector. At least one selector must be provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_selector** | **str** | A selector to restrict the list of devices to resume by their labels. Uses the same format as Kubernetes label selectors (e.g., \&quot;key1&#x3D;value1,key2!&#x3D;value2\&quot;). | [optional] 
**field_selector** | **str** | A selector to restrict the list of devices to resume by their fields. Uses the same format as Kubernetes field selectors (e.g., \&quot;metadata.name&#x3D;device1,status.phase!&#x3D;Pending\&quot;). | [optional] 

## Example

```python
from flightctl.models.device_resume_request import DeviceResumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceResumeRequest from a JSON string
device_resume_request_instance = DeviceResumeRequest.from_json(json)
# print the JSON string representation of the object
print(DeviceResumeRequest.to_json())

# convert the object into a dict
device_resume_request_dict = device_resume_request_instance.to_dict()
# create an instance of DeviceResumeRequest from a dict
device_resume_request_from_dict = DeviceResumeRequest.from_dict(device_resume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


