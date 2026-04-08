# CatalogStatus

CatalogStatus represents the current status of a catalog source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[Condition]**](Condition.md) | Current state of the catalog source. | 

## Example

```python
from flightctl.v1alpha1.models.catalog_status import CatalogStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogStatus from a JSON string
catalog_status_instance = CatalogStatus.from_json(json)
# print the JSON string representation of the object
print(CatalogStatus.to_json())

# convert the object into a dict
catalog_status_dict = catalog_status_instance.to_dict()
# create an instance of CatalogStatus from a dict
catalog_status_from_dict = CatalogStatus.from_dict(catalog_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


