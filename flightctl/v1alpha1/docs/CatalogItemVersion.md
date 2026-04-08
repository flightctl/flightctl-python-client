# CatalogItemVersion

A version of a catalog item following the Cincinnati model where versions are nodes in an upgrade graph and channels are labels on those nodes. Upgrade edges are defined by replaces (single), skips (multiple), or skipRange (semver range). Includes CatalogItemConfigurable fields that override item-level defaults. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **Dict[str, object]** | Configuration values (envVars, ports, volumes, resources, etc.). | [optional] 
**config_schema** | **Dict[str, object]** | JSON Schema defining configurable parameters and their validation. | [optional] 
**readme** | **str** | Detailed documentation, preferably in markdown format. | [optional] 
**version** | **str** | Semantic version identifier (e.g., 1.2.3, v2.0.0-rc1). Required for version ordering and upgrade graph. | 
**references** | **Dict[str, str]** | Map of artifact type to image tag or digest. Keys must match a type in spec.artifacts. Only keyed artifacts are available for this version. | 
**channels** | **List[str]** | Channels this version belongs to. | 
**replaces** | **str** | The single version this one replaces, defining the primary upgrade edge. | [optional] 
**skips** | **List[str]** | Additional versions that can upgrade directly to this one. Use when stable channel skips intermediate fast-only versions. | [optional] 
**skip_range** | **str** | Semver range of versions that can upgrade directly to this one. Use for z-stream updates or hotfixes. | [optional] 
**deprecation** | [**CatalogItemDeprecation**](CatalogItemDeprecation.md) |  | [optional] 

## Example

```python
from flightctl.v1alpha1.models.catalog_item_version import CatalogItemVersion

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogItemVersion from a JSON string
catalog_item_version_instance = CatalogItemVersion.from_json(json)
# print the JSON string representation of the object
print(CatalogItemVersion.to_json())

# convert the object into a dict
catalog_item_version_dict = catalog_item_version_instance.to_dict()
# create an instance of CatalogItemVersion from a dict
catalog_item_version_from_dict = CatalogItemVersion.from_dict(catalog_item_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


