# DeviceApplicationStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human readable name of the application. | 
**ready** | **str** | The number of containers which are ready in the application. | 
**restarts** | **int** | Number of restarts observed for the application. | 
**status** | [**ApplicationStatusType**](ApplicationStatusType.md) |  | 
**volumes** | [**List[ApplicationVolumeStatus]**](ApplicationVolumeStatus.md) | Status of volumes used by this application. | [optional] 

## Example

```python
from flightctl.models.device_application_status import DeviceApplicationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceApplicationStatus from a JSON string
device_application_status_instance = DeviceApplicationStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceApplicationStatus.to_json())

# convert the object into a dict
device_application_status_dict = device_application_status_instance.to_dict()
# create an instance of DeviceApplicationStatus from a dict
device_application_status_from_dict = DeviceApplicationStatus.from_dict(device_application_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


