# DeviceOsStatus

Current status of the device OS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | Version of the OS image. | 
**image_digest** | **str** | The digest of the OS image (e.g. sha256:a0...). | 
**delta_size** | **str** | Size of the control-plane generated OS delta image in IEC units (e.g. \&quot;245.3 MiB\&quot;, \&quot;1 GiB\&quot;). Absent when no delta image was generated or its size is unknown. | [optional]
**last_delta** | [**DeviceDeltaApplyStatus**](DeviceDeltaApplyStatus.md) |  | [optional]

## Example

```python
from flightctl.models.device_os_status import DeviceOsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceOsStatus from a JSON string
device_os_status_instance = DeviceOsStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceOsStatus.to_json())

# convert the object into a dict
device_os_status_dict = device_os_status_instance.to_dict()
# create an instance of DeviceOsStatus from a dict
device_os_status_from_dict = DeviceOsStatus.from_dict(device_os_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


