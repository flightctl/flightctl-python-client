# RenderedApplicationSpec

RenderedApplicationSpec describes the rendered and self-contained specification of an application.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env_vars** | **Dict[str, str]** | Environment variable key-value pairs, injected during runtime. | [optional] 
**name** | **str** | An application name. | [optional] 
**image** | **str** | Reference to the container image for the application package. | 

## Example

```python
from flightctl.models.rendered_application_spec import RenderedApplicationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of RenderedApplicationSpec from a JSON string
rendered_application_spec_instance = RenderedApplicationSpec.from_json(json)
# print the JSON string representation of the object
print(RenderedApplicationSpec.to_json())

# convert the object into a dict
rendered_application_spec_dict = rendered_application_spec_instance.to_dict()
# create an instance of RenderedApplicationSpec from a dict
rendered_application_spec_from_dict = RenderedApplicationSpec.from_dict(rendered_application_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


