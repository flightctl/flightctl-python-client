# DeviceFeatures

Device feature requirements declared by a catalog item version. Each field names a device feature that a target device must provide with a matching value for this version to be considered compatible.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_present** | [**DeviceFeatureBoolean**](DeviceFeatureBoolean.md) | Whether the target device is required to have a GPU present. | [optional]
**kvm_enabled** | [**DeviceFeatureBoolean**](DeviceFeatureBoolean.md) | Whether the target device is required to have KVM enabled. | [optional]
**os_mode** | [**OsModeType**](OsModeType.md) | The OS management mode the target device is required to run. | [optional]

## Example

```python
from flightctl.v1alpha1.models.device_features import DeviceFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceFeatures from a JSON string
device_features_instance = DeviceFeatures.from_json(json)
# print the JSON string representation of the object
print(DeviceFeatures.to_json())

# convert the object into a dict
device_features_dict = device_features_instance.to_dict()
# create an instance of DeviceFeatures from a dict
device_features_from_dict = DeviceFeatures.from_dict(device_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
