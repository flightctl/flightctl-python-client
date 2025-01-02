# HookAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_if** | [**List[HookCondition]**](HookCondition.md) | Conditions that must be met for the action to be executed. | [optional] 
**timeout** | **str** | The maximum duration allowed for the action to complete. The duration should be specified as a positive integer followed by a time unit. Supported time units are &#39;s&#39; for seconds, &#39;m&#39; for minutes, and &#39;h&#39; for hours. | [optional] 
**run** | **str** | The command to be executed, including any arguments using standard shell syntax. This field supports multiple commands piped together, as if they were executed under a bash -c context. | 
**env_vars** | **Dict[str, str]** | Environment variable key-value pairs, injected during runtime. | [optional] 
**work_dir** | **str** | The working directory to be used when running the command. | [optional] 

## Example

```python
from flightctl.models.hook_action import HookAction

# TODO update the JSON string below
json = "{}"
# create an instance of HookAction from a JSON string
hook_action_instance = HookAction.from_json(json)
# print the JSON string representation of the object
print(HookAction.to_json())

# convert the object into a dict
hook_action_dict = hook_action_instance.to_dict()
# create an instance of HookAction from a dict
hook_action_from_dict = HookAction.from_dict(hook_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


