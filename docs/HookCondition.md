# HookCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The absolute path to a file or directory that must have changed as condition for the action to be performed. | 
**op** | [**List[FileOperation]**](FileOperation.md) | The operation(s) on files at or below the path that satisfy the path condition. | 

## Example

```python
from flightctl.models.hook_condition import HookCondition

# TODO update the JSON string below
json = "{}"
# create an instance of HookCondition from a JSON string
hook_condition_instance = HookCondition.from_json(json)
# print the JSON string representation of the object
print(HookCondition.to_json())

# convert the object into a dict
hook_condition_dict = hook_condition_instance.to_dict()
# create an instance of HookCondition from a dict
hook_condition_from_dict = HookCondition.from_dict(hook_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


