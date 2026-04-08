# CatalogItemSpec

CatalogItemSpec defines the configuration for a catalog item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**CatalogItemCategory**](CatalogItemCategory.md) |  | [optional] [default to CatalogItemCategory.NUMBER_CatalogItemCategoryApplication]
**type** | [**CatalogItemType**](CatalogItemType.md) |  | 
**artifacts** | [**List[CatalogItemArtifact]**](CatalogItemArtifact.md) | Artifact definitions for this catalog item. Defined once; version references resolve each artifact independently. Type must be unique within the list. | 
**versions** | [**List[CatalogItemVersion]**](CatalogItemVersion.md) | Available versions using Cincinnati model. Use replaces for primary edge, skips when stable channel skips intermediate versions. | 
**defaults** | [**CatalogItemConfigurable**](CatalogItemConfigurable.md) |  | [optional] 
**display_name** | **str** | Human-readable display name shown in catalog listings. | [optional] 
**short_description** | **str** | A brief one-line description of the catalog item. | [optional] 
**icon** | **str** | URL or data URI of the catalog item icon for display in UI. | [optional] 
**deprecation** | [**CatalogItemDeprecation**](CatalogItemDeprecation.md) |  | [optional] 
**provider** | **str** | Provider or publisher of the catalog item (company or team name). | [optional] 
**support** | **str** | Link to support resources or documentation for getting help. | [optional] 
**homepage** | **str** | The homepage URL for the catalog item project. | [optional] 
**documentation_url** | **str** | Link to external documentation. | [optional] 

## Example

```python
from flightctl.v1alpha1.models.catalog_item_spec import CatalogItemSpec

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogItemSpec from a JSON string
catalog_item_spec_instance = CatalogItemSpec.from_json(json)
# print the JSON string representation of the object
print(CatalogItemSpec.to_json())

# convert the object into a dict
catalog_item_spec_dict = catalog_item_spec_instance.to_dict()
# create an instance of CatalogItemSpec from a dict
catalog_item_spec_from_dict = CatalogItemSpec.from_dict(catalog_item_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


