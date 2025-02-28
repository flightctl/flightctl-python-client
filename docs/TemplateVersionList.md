# TemplateVersionList

TemplateVersionList is a list of TemplateVersions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**metadata** | [**ListMeta**](ListMeta.md) |  | 
**items** | [**List[TemplateVersion]**](TemplateVersion.md) | List of TemplateVersions. | 

## Example

```python
from flightctl.models.template_version_list import TemplateVersionList

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateVersionList from a JSON string
template_version_list_instance = TemplateVersionList.from_json(json)
# print the JSON string representation of the object
print(TemplateVersionList.to_json())

# convert the object into a dict
template_version_list_dict = template_version_list_instance.to_dict()
# create an instance of TemplateVersionList from a dict
template_version_list_from_dict = TemplateVersionList.from_dict(template_version_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


