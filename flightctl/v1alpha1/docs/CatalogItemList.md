# CatalogItemList

CatalogItemList is a list of CatalogItems.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | [**ApiVersion**](ApiVersion.md) |  | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**metadata** | [**ListMeta**](ListMeta.md) |  | 
**items** | [**List[CatalogItem]**](CatalogItem.md) | List of CatalogItems. | 

## Example

```python
from flightctl.v1alpha1.models.catalog_item_list import CatalogItemList

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogItemList from a JSON string
catalog_item_list_instance = CatalogItemList.from_json(json)
# print the JSON string representation of the object
print(CatalogItemList.to_json())

# convert the object into a dict
catalog_item_list_dict = catalog_item_list_instance.to_dict()
# create an instance of CatalogItemList from a dict
catalog_item_list_from_dict = CatalogItemList.from_dict(catalog_item_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


