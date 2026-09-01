# ImageOrCatalogItemRefSpec

Either a specific OCI image reference, or a reference to a catalog item version that can be resolved to an OCI image ref.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | Reference to an OCI image or artifact with tag. | [optional] 
**catalog_item_ref** | [**CatalogItemRefSpec**](CatalogItemRefSpec.md) |  | [optional] 

## Example

```python
from flightctl.models.image_or_catalog_item_ref_spec import ImageOrCatalogItemRefSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ImageOrCatalogItemRefSpec from a JSON string
image_or_catalog_item_ref_spec_instance = ImageOrCatalogItemRefSpec.from_json(json)
# print the JSON string representation of the object
print(ImageOrCatalogItemRefSpec.to_json())

# convert the object into a dict
image_or_catalog_item_ref_spec_dict = image_or_catalog_item_ref_spec_instance.to_dict()
# create an instance of ImageOrCatalogItemRefSpec from a dict
image_or_catalog_item_ref_spec_from_dict = ImageOrCatalogItemRefSpec.from_dict(image_or_catalog_item_ref_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


