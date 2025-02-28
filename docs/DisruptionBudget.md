# DisruptionBudget

DisruptionBudget defines the level of allowed disruption when rollout is in progress.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **List[str]** | List of label keys to perform grouping for the disruption budget. | [optional] 
**min_available** | **int** | The maximum number of unavailable devices allowed during rollout. | [optional] 
**max_unavailable** | **int** | The minimum number of required available devices during rollout. | [optional] 

## Example

```python
from flightctl.models.disruption_budget import DisruptionBudget

# TODO update the JSON string below
json = "{}"
# create an instance of DisruptionBudget from a JSON string
disruption_budget_instance = DisruptionBudget.from_json(json)
# print the JSON string representation of the object
print(DisruptionBudget.to_json())

# convert the object into a dict
disruption_budget_dict = disruption_budget_instance.to_dict()
# create an instance of DisruptionBudget from a dict
disruption_budget_from_dict = DisruptionBudget.from_dict(disruption_budget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


