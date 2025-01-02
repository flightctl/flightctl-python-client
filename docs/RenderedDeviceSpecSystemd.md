# RenderedDeviceSpecSystemd

The systemd services to monitor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_patterns** | **List[str]** | A list of match patterns. | [optional] 

## Example

```python
from flightctl.models.rendered_device_spec_systemd import RenderedDeviceSpecSystemd

# TODO update the JSON string below
json = "{}"
# create an instance of RenderedDeviceSpecSystemd from a JSON string
rendered_device_spec_systemd_instance = RenderedDeviceSpecSystemd.from_json(json)
# print the JSON string representation of the object
print(RenderedDeviceSpecSystemd.to_json())

# convert the object into a dict
rendered_device_spec_systemd_dict = rendered_device_spec_systemd_instance.to_dict()
# create an instance of RenderedDeviceSpecSystemd from a dict
rendered_device_spec_systemd_from_dict = RenderedDeviceSpecSystemd.from_dict(rendered_device_spec_systemd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


