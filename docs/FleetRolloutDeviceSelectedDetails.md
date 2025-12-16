# FleetRolloutDeviceSelectedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. | 
**fleet_name** | **str** | The name of the fleet that the device is being selected for. | 
**template_version** | **str** | The name of the TemplateVersion that the device is being selected to render. | 

## Example

```python
from flightctl.models.fleet_rollout_device_selected_details import FleetRolloutDeviceSelectedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FleetRolloutDeviceSelectedDetails from a JSON string
fleet_rollout_device_selected_details_instance = FleetRolloutDeviceSelectedDetails.from_json(json)
# print the JSON string representation of the object
print(FleetRolloutDeviceSelectedDetails.to_json())

# convert the object into a dict
fleet_rollout_device_selected_details_dict = fleet_rollout_device_selected_details_instance.to_dict()
# create an instance of FleetRolloutDeviceSelectedDetails from a dict
fleet_rollout_device_selected_details_from_dict = FleetRolloutDeviceSelectedDetails.from_dict(fleet_rollout_device_selected_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


