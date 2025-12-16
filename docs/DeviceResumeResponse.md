# DeviceResumeResponse

Response from resuming devices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resumed_devices** | **int** | Number of devices that were successfully resumed. | 

## Example

```python
from flightctl.models.device_resume_response import DeviceResumeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceResumeResponse from a JSON string
device_resume_response_instance = DeviceResumeResponse.from_json(json)
# print the JSON string representation of the object
print(DeviceResumeResponse.to_json())

# convert the object into a dict
device_resume_response_dict = device_resume_response_instance.to_dict()
# create an instance of DeviceResumeResponse from a dict
device_resume_response_from_dict = DeviceResumeResponse.from_dict(device_resume_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


