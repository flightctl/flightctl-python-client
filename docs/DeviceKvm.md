# DeviceKvm

KVM virtualization information reported by the device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether KVM virtualization is active and available on the device. | [optional]

## Example

```python
from flightctl.models.device_kvm import DeviceKvm

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceKvm from a JSON string
device_kvm_instance = DeviceKvm.from_json(json)
# print the JSON string representation of the object
print(DeviceKvm.to_json())

# convert the object into a dict
device_kvm_dict = device_kvm_instance.to_dict()
# create an instance of DeviceKvm from a dict
device_kvm_from_dict = DeviceKvm.from_dict(device_kvm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
