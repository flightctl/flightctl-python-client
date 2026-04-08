# CatalogItem

CatalogItem represents an application template from a catalog. It provides default configuration values that can be customized when adding the application to a fleet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | [**ApiVersion**](ApiVersion.md) |  | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. | 
**metadata** | [**CatalogItemMeta**](CatalogItemMeta.md) |  | 
**spec** | [**CatalogItemSpec**](CatalogItemSpec.md) |  | 

## Example

```python
from flightctl.v1alpha1.models.catalog_item import CatalogItem

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogItem from a JSON string
catalog_item_instance = CatalogItem.from_json(json)
# print the JSON string representation of the object
print(CatalogItem.to_json())

# convert the object into a dict
catalog_item_dict = catalog_item_instance.to_dict()
# create an instance of CatalogItem from a dict
catalog_item_from_dict = CatalogItem.from_dict(catalog_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


