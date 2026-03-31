# PatchRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | A JSON Pointer path. | 
**value** | **object** | The value to add or replace. | [optional] 
**op** | **str** | The operation to perform. | 

## Example

```python
from flightctl.v1alpha1.models.patch_request_inner import PatchRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of PatchRequestInner from a JSON string
patch_request_inner_instance = PatchRequestInner.from_json(json)
# print the JSON string representation of the object
print(PatchRequestInner.to_json())

# convert the object into a dict
patch_request_inner_dict = patch_request_inner_instance.to_dict()
# create an instance of PatchRequestInner from a dict
patch_request_inner_from_dict = PatchRequestInner.from_dict(patch_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


