# FleetRolloutBatchCompletedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. | 
**template_version** | **str** | The name of the TemplateVersion that this batch is rolling out to. | 
**batch** | **str** | The batch within the fleet rollout. | 
**success_percentage** | **int** | The success percentage of the batch. | 
**total** | **int** | The total number of devices in the batch. | 
**successful** | **int** | The number of successful devices in the batch. | 
**failed** | **int** | The number of failed devices in the batch. | 
**timed_out** | **int** | The number of timed out devices in the batch. | 

## Example

```python
from flightctl.models.fleet_rollout_batch_completed_details import FleetRolloutBatchCompletedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FleetRolloutBatchCompletedDetails from a JSON string
fleet_rollout_batch_completed_details_instance = FleetRolloutBatchCompletedDetails.from_json(json)
# print the JSON string representation of the object
print(FleetRolloutBatchCompletedDetails.to_json())

# convert the object into a dict
fleet_rollout_batch_completed_details_dict = fleet_rollout_batch_completed_details_instance.to_dict()
# create an instance of FleetRolloutBatchCompletedDetails from a dict
fleet_rollout_batch_completed_details_from_dict = FleetRolloutBatchCompletedDetails.from_dict(fleet_rollout_batch_completed_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


