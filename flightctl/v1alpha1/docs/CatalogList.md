# CatalogList

CatalogList is a list of Catalogs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | [**ApiVersion**](ApiVersion.md) |  | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**metadata** | [**ListMeta**](ListMeta.md) |  | 
**items** | [**List[Catalog]**](Catalog.md) | List of Catalogs. | 

## Example

```python
from flightctl.v1alpha1.models.catalog_list import CatalogList

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogList from a JSON string
catalog_list_instance = CatalogList.from_json(json)
# print the JSON string representation of the object
print(CatalogList.to_json())

# convert the object into a dict
catalog_list_dict = catalog_list_instance.to_dict()
# create an instance of CatalogList from a dict
catalog_list_from_dict = CatalogList.from_dict(catalog_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


