# CatalogItemDeprecation

Deprecation information for a catalog item or version. Presence indicates deprecated status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Required message explaining why this is deprecated and what to do instead. | 
**replacement** | **str** | Optional name of the replacement catalog item (item-level only). | [optional] 

## Example

```python
from flightctl.v1alpha1.models.catalog_item_deprecation import CatalogItemDeprecation

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogItemDeprecation from a JSON string
catalog_item_deprecation_instance = CatalogItemDeprecation.from_json(json)
# print the JSON string representation of the object
print(CatalogItemDeprecation.to_json())

# convert the object into a dict
catalog_item_deprecation_dict = catalog_item_deprecation_instance.to_dict()
# create an instance of CatalogItemDeprecation from a dict
catalog_item_deprecation_from_dict = CatalogItemDeprecation.from_dict(catalog_item_deprecation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


