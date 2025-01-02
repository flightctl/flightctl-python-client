# HookActionRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run** | **str** | The command to be executed, including any arguments using standard shell syntax. This field supports multiple commands piped together, as if they were executed under a bash -c context. | 
**env_vars** | **Dict[str, str]** | Environment variable key-value pairs, injected during runtime. | [optional] 
**work_dir** | **str** | The working directory to be used when running the command. | [optional] 

## Example

```python
from flightctl.models.hook_action_run import HookActionRun

# TODO update the JSON string below
json = "{}"
# create an instance of HookActionRun from a JSON string
hook_action_run_instance = HookActionRun.from_json(json)
# print the JSON string representation of the object
print(HookActionRun.to_json())

# convert the object into a dict
hook_action_run_dict = hook_action_run_instance.to_dict()
# create an instance of HookActionRun from a dict
hook_action_run_from_dict = HookActionRun.from_dict(hook_action_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


