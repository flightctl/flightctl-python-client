# CatalogItemConfigurable

Configuration fields that can be specified at item level (as defaults) and overridden at version level. Version-level values fully replace item-level values (not merged).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **Dict[str, object]** | Configuration values (envVars, ports, volumes, resources, etc.). | [optional] 
**config_schema** | **Dict[str, object]** | JSON Schema defining configurable parameters and their validation. | [optional] 
**readme** | **str** | Detailed documentation, preferably in markdown format. | [optional] 

## Example

```python
from flightctl.v1alpha1.models.catalog_item_configurable import CatalogItemConfigurable

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogItemConfigurable from a JSON string
catalog_item_configurable_instance = CatalogItemConfigurable.from_json(json)
# print the JSON string representation of the object
print(CatalogItemConfigurable.to_json())

# convert the object into a dict
catalog_item_configurable_dict = catalog_item_configurable_instance.to_dict()
# create an instance of CatalogItemConfigurable from a dict
catalog_item_configurable_from_dict = CatalogItemConfigurable.from_dict(catalog_item_configurable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


