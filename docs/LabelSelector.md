# LabelSelector

A label selector is a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. Empty/null label selectors match nothing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_labels** | **Dict[str, str]** | A map of {key,value} pairs. | [optional] 
**match_expressions** | [**List[MatchExpression]**](MatchExpression.md) | A list of match expressions. | [optional] 

## Example

```python
from flightctl.models.label_selector import LabelSelector

# TODO update the JSON string below
json = "{}"
# create an instance of LabelSelector from a JSON string
label_selector_instance = LabelSelector.from_json(json)
# print the JSON string representation of the object
print(LabelSelector.to_json())

# convert the object into a dict
label_selector_dict = label_selector_instance.to_dict()
# create an instance of LabelSelector from a dict
label_selector_from_dict = LabelSelector.from_dict(label_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


