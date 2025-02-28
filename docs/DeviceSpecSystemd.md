# DeviceSpecSystemd

The systemd services to monitor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_patterns** | **List[str]** | A list of match patterns. | [optional] 

## Example

```python
from flightctl.models.device_spec_systemd import DeviceSpecSystemd

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSpecSystemd from a JSON string
device_spec_systemd_instance = DeviceSpecSystemd.from_json(json)
# print the JSON string representation of the object
print(DeviceSpecSystemd.to_json())

# convert the object into a dict
device_spec_systemd_dict = device_spec_systemd_instance.to_dict()
# create an instance of DeviceSpecSystemd from a dict
device_spec_systemd_from_dict = DeviceSpecSystemd.from_dict(device_spec_systemd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


