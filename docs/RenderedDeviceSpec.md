# RenderedDeviceSpec

RenderedDeviceSpec describes the rendered and self-contained specification of a Device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rendered_version** | **str** | Version of the rendered device spec. | 
**update_policy** | [**DeviceUpdatePolicySpec**](DeviceUpdatePolicySpec.md) |  | [optional] 
**os** | [**DeviceOSSpec**](DeviceOSSpec.md) |  | [optional] 
**config** | **str** | The configuration to apply, in Ignition format. | [optional] 
**applications** | [**List[RenderedApplicationSpec]**](RenderedApplicationSpec.md) | The list of applications to deploy. | [optional] 
**systemd** | [**RenderedDeviceSpecSystemd**](RenderedDeviceSpecSystemd.md) |  | [optional] 
**resources** | [**List[ResourceMonitor]**](ResourceMonitor.md) | Array of resource monitor configurations. | [optional] 
**console** | [**DeviceConsole**](DeviceConsole.md) |  | [optional] 
**decommission** | [**DeviceDecommission**](DeviceDecommission.md) |  | [optional] 

## Example

```python
from flightctl.models.rendered_device_spec import RenderedDeviceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of RenderedDeviceSpec from a JSON string
rendered_device_spec_instance = RenderedDeviceSpec.from_json(json)
# print the JSON string representation of the object
print(RenderedDeviceSpec.to_json())

# convert the object into a dict
rendered_device_spec_dict = rendered_device_spec_instance.to_dict()
# create an instance of RenderedDeviceSpec from a dict
rendered_device_spec_from_dict = RenderedDeviceSpec.from_dict(rendered_device_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


