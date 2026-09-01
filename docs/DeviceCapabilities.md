# DeviceCapabilities

Capabilities reported by the device agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**os_mode** | [**OsModeType**](OsModeType.md) |  | [optional] 

## Example

```python
from flightctl.models.device_capabilities import DeviceCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceCapabilities from a JSON string
device_capabilities_instance = DeviceCapabilities.from_json(json)
# print the JSON string representation of the object
print(DeviceCapabilities.to_json())

# convert the object into a dict
device_capabilities_dict = device_capabilities_instance.to_dict()
# create an instance of DeviceCapabilities from a dict
device_capabilities_from_dict = DeviceCapabilities.from_dict(device_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


