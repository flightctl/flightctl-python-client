# FleetSpecTemplate

The template for the devices in the fleet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  | [optional] 
**spec** | [**DeviceSpec**](DeviceSpec.md) |  | 

## Example

```python
from flightctl.models.fleet_spec_template import FleetSpecTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of FleetSpecTemplate from a JSON string
fleet_spec_template_instance = FleetSpecTemplate.from_json(json)
# print the JSON string representation of the object
print(FleetSpecTemplate.to_json())

# convert the object into a dict
fleet_spec_template_dict = fleet_spec_template_instance.to_dict()
# create an instance of FleetSpecTemplate from a dict
fleet_spec_template_from_dict = FleetSpecTemplate.from_dict(fleet_spec_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


