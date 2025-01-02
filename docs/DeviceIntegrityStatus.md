# DeviceIntegrityStatus

Status of device integrity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**DeviceIntegrityStatusSummary**](DeviceIntegrityStatusSummary.md) |  | 

## Example

```python
from flightctl.models.device_integrity_status import DeviceIntegrityStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceIntegrityStatus from a JSON string
device_integrity_status_instance = DeviceIntegrityStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceIntegrityStatus.to_json())

# convert the object into a dict
device_integrity_status_dict = device_integrity_status_instance.to_dict()
# create an instance of DeviceIntegrityStatus from a dict
device_integrity_status_from_dict = DeviceIntegrityStatus.from_dict(device_integrity_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


