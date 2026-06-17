# ExistingCatalogItemTarget

Publish target that appends a version to an existing CatalogItem. Rejected immediately if the CatalogItem does not exist.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Discriminator for the target type. | 
**catalog_name** | **str** | Name of the parent Catalog resource. | 
**catalog_item_name** | **str** | Name of the CatalogItem to update. | 
**version** | **str** | Semver version string for the new CatalogItem version entry. | 
**readme** | **str** | Optional version-level readme for this version entry. Markdown is supported. | [optional] 
**replaces** | **str** | The single version this one replaces, defining the primary upgrade edge. | [optional] 
**skips** | **List[str]** | Additional versions that can upgrade directly to this one. | [optional] 
**skip_range** | **str** | Semver range of versions that can upgrade directly to this one (e.g. \&quot;&gt;&#x3D;1.0.0 &lt;1.3.0\&quot;). | [optional] 

## Example

```python
from flightctl.imagebuilder.models.existing_catalog_item_target import ExistingCatalogItemTarget

# TODO update the JSON string below
json = "{}"
# create an instance of ExistingCatalogItemTarget from a JSON string
existing_catalog_item_target_instance = ExistingCatalogItemTarget.from_json(json)
# print the JSON string representation of the object
print(ExistingCatalogItemTarget.to_json())

# convert the object into a dict
existing_catalog_item_target_dict = existing_catalog_item_target_instance.to_dict()
# create an instance of ExistingCatalogItemTarget from a dict
existing_catalog_item_target_from_dict = ExistingCatalogItemTarget.from_dict(existing_catalog_item_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


