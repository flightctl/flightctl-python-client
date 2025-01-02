# TemplateVersionSpec

TemplateVersionSpec describes a version of a device template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fleet** | **str** | The fleet whose template this refers to. | 

## Example

```python
from flightctl.models.template_version_spec import TemplateVersionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateVersionSpec from a JSON string
template_version_spec_instance = TemplateVersionSpec.from_json(json)
# print the JSON string representation of the object
print(TemplateVersionSpec.to_json())

# convert the object into a dict
template_version_spec_dict = template_version_spec_instance.to_dict()
# create an instance of TemplateVersionSpec from a dict
template_version_spec_from_dict = TemplateVersionSpec.from_dict(template_version_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


