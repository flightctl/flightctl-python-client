# DeviceOSSpec

DeviceOSSpec describes the target OS for the device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | The target OS image name or URL. | 

## Example

```python
from flightctl.models.device_os_spec import DeviceOSSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceOSSpec from a JSON string
device_os_spec_instance = DeviceOSSpec.from_json(json)
# print the JSON string representation of the object
print(DeviceOSSpec.to_json())

# convert the object into a dict
device_os_spec_dict = device_os_spec_instance.to_dict()
# create an instance of DeviceOSSpec from a dict
device_os_spec_from_dict = DeviceOSSpec.from_dict(device_os_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


