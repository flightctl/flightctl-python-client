# FleetRolloutBatchDispatchedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. | 
**template_version** | **str** | The name of the TemplateVersion that this batch is rolling out to. | 
**batch** | **str** | The batch within the fleet rollout. | 

## Example

```python
from flightctl.models.fleet_rollout_batch_dispatched_details import FleetRolloutBatchDispatchedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FleetRolloutBatchDispatchedDetails from a JSON string
fleet_rollout_batch_dispatched_details_instance = FleetRolloutBatchDispatchedDetails.from_json(json)
# print the JSON string representation of the object
print(FleetRolloutBatchDispatchedDetails.to_json())

# convert the object into a dict
fleet_rollout_batch_dispatched_details_dict = fleet_rollout_batch_dispatched_details_instance.to_dict()
# create an instance of FleetRolloutBatchDispatchedDetails from a dict
fleet_rollout_batch_dispatched_details_from_dict = FleetRolloutBatchDispatchedDetails.from_dict(fleet_rollout_batch_dispatched_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


