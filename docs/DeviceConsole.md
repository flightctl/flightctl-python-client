# DeviceConsole

DeviceConsole represents the console connection information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_metadata** | **str** | Additional session metadata in the form of key&#x3D;value pairs, can be used to initialize the type of terminal, console to be used, etc. | 
**session_id** | **str** | The session ID for the console connection. | 

## Example

```python
from flightctl.models.device_console import DeviceConsole

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceConsole from a JSON string
device_console_instance = DeviceConsole.from_json(json)
# print the JSON string representation of the object
print(DeviceConsole.to_json())

# convert the object into a dict
device_console_dict = device_console_instance.to_dict()
# create an instance of DeviceConsole from a dict
device_console_from_dict = DeviceConsole.from_dict(device_console_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


