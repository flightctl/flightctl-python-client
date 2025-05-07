# ResourceUpdatedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_fields** | **List[str]** | List of fields that were updated in the resource. | 
**previous_owner** | **str** | The previous owner (if applicable). | [optional] 
**new_owner** | **str** | The new owner (if applicable). | [optional] 

## Example

```python
from flightctl.models.resource_updated_details import ResourceUpdatedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceUpdatedDetails from a JSON string
resource_updated_details_instance = ResourceUpdatedDetails.from_json(json)
# print the JSON string representation of the object
print(ResourceUpdatedDetails.to_json())

# convert the object into a dict
resource_updated_details_dict = resource_updated_details_instance.to_dict()
# create an instance of ResourceUpdatedDetails from a dict
resource_updated_details_from_dict = ResourceUpdatedDetails.from_dict(resource_updated_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


