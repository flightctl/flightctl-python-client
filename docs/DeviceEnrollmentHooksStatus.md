# DeviceEnrollmentHooksStatus

Enrollment hooks state for a device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot** | [**EnrollmentHookSnapshot**](EnrollmentHookSnapshot.md) |  | [optional]

## Example

```python
from flightctl.models.device_enrollment_hooks_status import DeviceEnrollmentHooksStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceEnrollmentHooksStatus from a JSON string
device_enrollment_hooks_status_instance = DeviceEnrollmentHooksStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceEnrollmentHooksStatus.to_json())

# convert the object into a dict
device_enrollment_hooks_status_dict = device_enrollment_hooks_status_instance.to_dict()
# create an instance of DeviceEnrollmentHooksStatus from a dict
device_enrollment_hooks_status_from_dict = DeviceEnrollmentHooksStatus.from_dict(device_enrollment_hooks_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
