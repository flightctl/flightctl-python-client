# TemplateVersion

TemplateVersion represents a version of a template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | [**ApiVersion**](ApiVersion.md) |  | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  | 
**spec** | [**TemplateVersionSpec**](TemplateVersionSpec.md) |  | 
**status** | [**TemplateVersionStatus**](TemplateVersionStatus.md) |  | [optional] 

## Example

```python
from flightctl.models.template_version import TemplateVersion

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateVersion from a JSON string
template_version_instance = TemplateVersion.from_json(json)
# print the JSON string representation of the object
print(TemplateVersion.to_json())

# convert the object into a dict
template_version_dict = template_version_instance.to_dict()
# create an instance of TemplateVersion from a dict
template_version_from_dict = TemplateVersion.from_dict(template_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


