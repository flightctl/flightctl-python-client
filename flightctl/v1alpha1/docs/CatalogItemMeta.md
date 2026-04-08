# CatalogItemMeta

Metadata for CatalogItem resources. Extends ObjectMeta with catalog scoping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_timestamp** | **datetime** | The time the object was created. | [optional] 
**deletion_timestamp** | **datetime** | The time the object will be deleted. | [optional] 
**name** | **str** | The name of the object. | [optional] 
**labels** | **Dict[str, str]** | Map of string keys and values that can be used to organize and categorize (scope and select) objects. | [optional] 
**generation** | **int** | A sequence number representing a specific generation of the desired state. Populated by the system. Read-only. | [optional] 
**owner** | **str** | A resource that owns this resource, in \&quot;kind/name\&quot; format. | [optional] 
**annotations** | **Dict[str, str]** | Properties set by the service. | [optional] 
**resource_version** | **str** | An opaque string that identifies the server&#39;s internal version of an object. | [optional] 
**catalog** | **str** | The catalog this item belongs to. Similar to namespace in Kubernetes. | 

## Example

```python
from flightctl.v1alpha1.models.catalog_item_meta import CatalogItemMeta

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogItemMeta from a JSON string
catalog_item_meta_instance = CatalogItemMeta.from_json(json)
# print the JSON string representation of the object
print(CatalogItemMeta.to_json())

# convert the object into a dict
catalog_item_meta_dict = catalog_item_meta_instance.to_dict()
# create an instance of CatalogItemMeta from a dict
catalog_item_meta_from_dict = CatalogItemMeta.from_dict(catalog_item_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


