# CatalogItemRefSpec

A reference to a catalog item, along with its configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog** | **str** | The catalog name that the item is part of. | 
**item** | **str** | The name of the catalog item itself. | 
**version** | **str** | A valid version that currently exists in the catalog item. | 
**channel** | **str** | An optional update channel which will be used to provide update cues when available. | [optional] 

## Example

```python
from flightctl.models.catalog_item_ref_spec import CatalogItemRefSpec

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogItemRefSpec from a JSON string
catalog_item_ref_spec_instance = CatalogItemRefSpec.from_json(json)
# print the JSON string representation of the object
print(CatalogItemRefSpec.to_json())

# convert the object into a dict
catalog_item_ref_spec_dict = catalog_item_ref_spec_instance.to_dict()
# create an instance of CatalogItemRefSpec from a dict
catalog_item_ref_spec_from_dict = CatalogItemRefSpec.from_dict(catalog_item_ref_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


