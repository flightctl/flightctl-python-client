# DeviceSystemInfo

System information collected from the device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | The Architecture reported by the device. | 
**boot_id** | **str** | Boot ID reported by the device. | 
**operating_system** | **str** | The Operating System reported by the device. | 
**agent_version** | **str** | The Agent version. | 
**bootc_version** | **str** | Version reported by &#x60;bootc --version&#x60;. Absent when bootc is not installed or the version command fails. | [optional]
**oci_delta_version** | **str** | Version reported by &#x60;oci-delta --version&#x60;, or from Go module build information when that flag is unsupported. Absent when oci-delta is not installed or its version cannot be determined. | [optional]
**delta_eligible** | **bool** | Whether this device can consume OCI deltas. True when the oci-delta binary is present. False when it is not. Omitted when an older agent does not report the field. | [optional]
**custom_info** | **Dict[str, str]** | User-defined information about the device. | [optional] 
**gpus** | [**List[DeviceGpu]**](DeviceGpu.md) | List of GPU devices discovered on the device. | [optional]
**kvm** | [**DeviceKvm**](DeviceKvm.md) |  | [optional]
**os_mode** | [**OsModeType**](OsModeType.md) |  | [optional]

## Example

```python
from flightctl.models.device_system_info import DeviceSystemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSystemInfo from a JSON string
device_system_info_instance = DeviceSystemInfo.from_json(json)
# print the JSON string representation of the object
print(DeviceSystemInfo.to_json())

# convert the object into a dict
device_system_info_dict = device_system_info_instance.to_dict()
# create an instance of DeviceSystemInfo from a dict
device_system_info_from_dict = DeviceSystemInfo.from_dict(device_system_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


