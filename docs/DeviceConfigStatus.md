# DeviceConfigStatus

Current status of the device config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rendered_version** | **str** | Rendered version of the device config. | 

## Example

```python
from flightctl.models.device_config_status import DeviceConfigStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceConfigStatus from a JSON string
device_config_status_instance = DeviceConfigStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceConfigStatus.to_json())

# convert the object into a dict
device_config_status_dict = device_config_status_instance.to_dict()
# create an instance of DeviceConfigStatus from a dict
device_config_status_from_dict = DeviceConfigStatus.from_dict(device_config_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


