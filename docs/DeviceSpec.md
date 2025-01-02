# DeviceSpec

DeviceSpec describes a device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_policy** | [**DeviceUpdatePolicySpec**](DeviceUpdatePolicySpec.md) |  | [optional] 
**os** | [**DeviceOSSpec**](DeviceOSSpec.md) |  | [optional] 
**config** | [**List[ConfigProviderSpec]**](ConfigProviderSpec.md) | List of config providers. | [optional] 
**applications** | [**List[ApplicationSpec]**](ApplicationSpec.md) | List of applications. | [optional] 
**systemd** | [**DeviceSpecSystemd**](DeviceSpecSystemd.md) |  | [optional] 
**resources** | [**List[ResourceMonitor]**](ResourceMonitor.md) | Array of resource monitor configurations. | [optional] 

## Example

```python
from flightctl.models.device_spec import DeviceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSpec from a JSON string
device_spec_instance = DeviceSpec.from_json(json)
# print the JSON string representation of the object
print(DeviceSpec.to_json())

# convert the object into a dict
device_spec_dict = device_spec_instance.to_dict()
# create an instance of DeviceSpec from a dict
device_spec_from_dict = DeviceSpec.from_dict(device_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


