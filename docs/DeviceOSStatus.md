# DeviceOSStatus

Current status of the device OS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | Version of the OS image. | 
**image_digest** | **str** | The digest of the OS image (e.g. sha256:a0...). | 

## Example

```python
from flightctl.models.device_os_status import DeviceOSStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceOSStatus from a JSON string
device_os_status_instance = DeviceOSStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceOSStatus.to_json())

# convert the object into a dict
device_os_status_dict = device_os_status_instance.to_dict()
# create an instance of DeviceOSStatus from a dict
device_os_status_from_dict = DeviceOSStatus.from_dict(device_os_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


