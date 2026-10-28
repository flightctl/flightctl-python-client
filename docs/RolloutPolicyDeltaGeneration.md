# RolloutPolicyDeltaGeneration

Controls OS delta generation for this fleet rollout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generate_delta** | **bool** | When false, skip control-plane OS delta generation for this fleet. Omitted means true. | [optional]
**max_wait_for_delta** | **str** | How long a prepare may wait before periodic resume. Omitted uses DeltaGeneration.maxWaitForDelta. Ignored when generateDelta is false. 0s still generates then resumes immediately. | [optional]
**delta_generation_timeout** | **str** | Context deadline for each generation job. Omitted uses DeltaGeneration.timeout. | [optional]

## Example

```python
from flightctl.models.rollout_policy_delta_generation import RolloutPolicyDeltaGeneration

# TODO update the JSON string below
json = "{}"
# create an instance of RolloutPolicyDeltaGeneration from a JSON string
rollout_policy_delta_generation_instance = RolloutPolicyDeltaGeneration.from_json(json)
# print the JSON string representation of the object
print(RolloutPolicyDeltaGeneration.to_json())

# convert the object into a dict
rollout_policy_delta_generation_dict = rollout_policy_delta_generation_instance.to_dict()
# create an instance of RolloutPolicyDeltaGeneration from a dict
rollout_policy_delta_generation_from_dict = RolloutPolicyDeltaGeneration.from_dict(rollout_policy_delta_generation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
