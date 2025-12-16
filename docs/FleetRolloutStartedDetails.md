# FleetRolloutStartedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. | 
**template_version** | **str** | The name of the TemplateVersion that is rolling out. | 
**rollout_strategy** | **str** | Rollout strategy type. | 

## Example

```python
from flightctl.models.fleet_rollout_started_details import FleetRolloutStartedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FleetRolloutStartedDetails from a JSON string
fleet_rollout_started_details_instance = FleetRolloutStartedDetails.from_json(json)
# print the JSON string representation of the object
print(FleetRolloutStartedDetails.to_json())

# convert the object into a dict
fleet_rollout_started_details_dict = fleet_rollout_started_details_instance.to_dict()
# create an instance of FleetRolloutStartedDetails from a dict
fleet_rollout_started_details_from_dict = FleetRolloutStartedDetails.from_dict(fleet_rollout_started_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


