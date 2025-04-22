# AbsolutePath

Represents an absolute file path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The absolute path to a file on the system. Note that any existing file will be overwritten. | [optional] 

## Example

```python
from flightctl.models.absolute_path import AbsolutePath

# TODO update the JSON string below
json = "{}"
# create an instance of AbsolutePath from a JSON string
absolute_path_instance = AbsolutePath.from_json(json)
# print the JSON string representation of the object
print(AbsolutePath.to_json())

# convert the object into a dict
absolute_path_dict = absolute_path_instance.to_dict()
# create an instance of AbsolutePath from a dict
absolute_path_from_dict = AbsolutePath.from_dict(absolute_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


