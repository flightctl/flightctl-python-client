# HookConditionPathOp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The absolute path to a file or directory that must have changed as condition for the action to be performed. | 
**op** | [**List[FileOperation]**](FileOperation.md) | The operation(s) on files at or below the path that satisfy the path condition. | 

## Example

```python
from flightctl.models.hook_condition_path_op import HookConditionPathOp

# TODO update the JSON string below
json = "{}"
# create an instance of HookConditionPathOp from a JSON string
hook_condition_path_op_instance = HookConditionPathOp.from_json(json)
# print the JSON string representation of the object
print(HookConditionPathOp.to_json())

# convert the object into a dict
hook_condition_path_op_dict = hook_condition_path_op_instance.to_dict()
# create an instance of HookConditionPathOp from a dict
hook_condition_path_op_from_dict = HookConditionPathOp.from_dict(hook_condition_path_op_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


