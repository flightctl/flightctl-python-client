# MatchExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The label key that the selector applies to. | 
**operator** | **str** | The operation to apply when matching. | 
**values** | **List[str]** | The list of values to match. | [optional] 

## Example

```python
from flightctl.models.match_expression import MatchExpression

# TODO update the JSON string below
json = "{}"
# create an instance of MatchExpression from a JSON string
match_expression_instance = MatchExpression.from_json(json)
# print the JSON string representation of the object
print(MatchExpression.to_json())

# convert the object into a dict
match_expression_dict = match_expression_instance.to_dict()
# create an instance of MatchExpression from a dict
match_expression_from_dict = MatchExpression.from_dict(match_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


