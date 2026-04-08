# LateBinding

Late binding configuration - device binds at first boot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of binding. | 

## Example

```python
from flightctl.imagebuilder.models.late_binding import LateBinding

# TODO update the JSON string below
json = "{}"
# create an instance of LateBinding from a JSON string
late_binding_instance = LateBinding.from_json(json)
# print the JSON string representation of the object
print(LateBinding.to_json())

# convert the object into a dict
late_binding_dict = late_binding_instance.to_dict()
# create an instance of LateBinding from a dict
late_binding_from_dict = LateBinding.from_dict(late_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


