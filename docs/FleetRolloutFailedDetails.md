# FleetRolloutFailedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. | 
**template_version** | **str** | The name of the TemplateVersion that this fleet rollout failed for. | 

## Example

```python
from flightctl.models.fleet_rollout_failed_details import FleetRolloutFailedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FleetRolloutFailedDetails from a JSON string
fleet_rollout_failed_details_instance = FleetRolloutFailedDetails.from_json(json)
# print the JSON string representation of the object
print(FleetRolloutFailedDetails.to_json())

# convert the object into a dict
fleet_rollout_failed_details_dict = fleet_rollout_failed_details_instance.to_dict()
# create an instance of FleetRolloutFailedDetails from a dict
fleet_rollout_failed_details_from_dict = FleetRolloutFailedDetails.from_dict(fleet_rollout_failed_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


