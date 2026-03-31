# CatalogSpec

CatalogSpec describes the configuration of a catalog. Catalogs are containers for locally-managed CatalogItems.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Human-readable display name shown in catalog listings. | [optional] 
**short_description** | **str** | A brief one-line description of the catalog. | [optional] 
**icon** | **str** | URL or data URI of the catalog icon for display in UI. | [optional] 
**provider** | **str** | Provider or publisher of the catalog (company or team name). | [optional] 
**support** | **str** | Link to support resources or documentation for getting help. | [optional] 

## Example

```python
from flightctl.v1alpha1.models.catalog_spec import CatalogSpec

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogSpec from a JSON string
catalog_spec_instance = CatalogSpec.from_json(json)
# print the JSON string representation of the object
print(CatalogSpec.to_json())

# convert the object into a dict
catalog_spec_dict = catalog_spec_instance.to_dict()
# create an instance of CatalogSpec from a dict
catalog_spec_from_dict = CatalogSpec.from_dict(catalog_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


