# RelativePath

Represents a relative file path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | A relative file path on the system. Note that any existing file will be overwritten. | [optional] 

## Example

```python
from flightctl.models.relative_path import RelativePath

# TODO update the JSON string below
json = "{}"
# create an instance of RelativePath from a JSON string
relative_path_instance = RelativePath.from_json(json)
# print the JSON string representation of the object
print(RelativePath.to_json())

# convert the object into a dict
relative_path_dict = relative_path_instance.to_dict()
# create an instance of RelativePath from a dict
relative_path_from_dict = RelativePath.from_dict(relative_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


