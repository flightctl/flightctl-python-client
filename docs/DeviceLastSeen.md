# DeviceLastSeen

DeviceLastSeen represents the last seen timestamp of a device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_seen** | **datetime** | The last time the device was seen by the service. | 

## Example

```python
from flightctl.models.device_last_seen import DeviceLastSeen

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceLastSeen from a JSON string
device_last_seen_instance = DeviceLastSeen.from_json(json)
# print the JSON string representation of the object
print(DeviceLastSeen.to_json())

# convert the object into a dict
device_last_seen_dict = device_last_seen_instance.to_dict()
# create an instance of DeviceLastSeen from a dict
device_last_seen_from_dict = DeviceLastSeen.from_dict(device_last_seen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


