# NewCatalogItemTarget

Publish target that creates a new CatalogItem. Rejected immediately if a CatalogItem with the given catalogItemName already exists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Discriminator for the target type. | 
**catalog_name** | **str** | Name of the parent Catalog resource. | 
**catalog_item_name** | **str** | Name of the CatalogItem to create. | 
**version** | **str** | Semver version string for the new CatalogItem version entry. | 
**readme** | **str** | Optional item-level readme for the new CatalogItem. Markdown is supported. | [optional] 
**display_name** | **str** | Optional human-readable display name for the new CatalogItem. | [optional] 

## Example

```python
from flightctl.imagebuilder.models.new_catalog_item_target import NewCatalogItemTarget

# TODO update the JSON string below
json = "{}"
# create an instance of NewCatalogItemTarget from a JSON string
new_catalog_item_target_instance = NewCatalogItemTarget.from_json(json)
# print the JSON string representation of the object
print(NewCatalogItemTarget.to_json())

# convert the object into a dict
new_catalog_item_target_dict = new_catalog_item_target_instance.to_dict()
# create an instance of NewCatalogItemTarget from a dict
new_catalog_item_target_from_dict = NewCatalogItemTarget.from_dict(new_catalog_item_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


