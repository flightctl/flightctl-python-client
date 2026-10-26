# DeltaGenerationStatus

Pair counts (completed/total) for a prepare in flight. Per-pair phase is one DeltaGenerationProgress event per step, not a percent heartbeat. Condition messages carry the same completed/total counts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **int** | Number of joined generation pairs that are already terminal. |
**total** | **int** | Number of unique generation pairs in this prepare. |
**last_updated** | **datetime** | Time of the last completed/total write for this prepare. | [optional]

## Example

```python
from flightctl.models.delta_generation_status import DeltaGenerationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeltaGenerationStatus from a JSON string
delta_generation_status_instance = DeltaGenerationStatus.from_json(json)
# print the JSON string representation of the object
print(DeltaGenerationStatus.to_json())

# convert the object into a dict
delta_generation_status_dict = delta_generation_status_instance.to_dict()
# create an instance of DeltaGenerationStatus from a dict
delta_generation_status_from_dict = DeltaGenerationStatus.from_dict(delta_generation_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
