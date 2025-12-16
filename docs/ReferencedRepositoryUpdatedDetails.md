# ReferencedRepositoryUpdatedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. | 
**repository** | **str** | The name of the repository that was updated. | 

## Example

```python
from flightctl.models.referenced_repository_updated_details import ReferencedRepositoryUpdatedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedRepositoryUpdatedDetails from a JSON string
referenced_repository_updated_details_instance = ReferencedRepositoryUpdatedDetails.from_json(json)
# print the JSON string representation of the object
print(ReferencedRepositoryUpdatedDetails.to_json())

# convert the object into a dict
referenced_repository_updated_details_dict = referenced_repository_updated_details_instance.to_dict()
# create an instance of ReferencedRepositoryUpdatedDetails from a dict
referenced_repository_updated_details_from_dict = ReferencedRepositoryUpdatedDetails.from_dict(referenced_repository_updated_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


