# EarlyBinding

Early binding configuration - embeds certificate in the image.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of binding. | 

## Example

```python
from flightctl.imagebuilder.models.early_binding import EarlyBinding

# TODO update the JSON string below
json = "{}"
# create an instance of EarlyBinding from a JSON string
early_binding_instance = EarlyBinding.from_json(json)
# print the JSON string representation of the object
print(EarlyBinding.to_json())

# convert the object into a dict
early_binding_dict = early_binding_instance.to_dict()
# create an instance of EarlyBinding from a dict
early_binding_from_dict = EarlyBinding.from_dict(early_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


