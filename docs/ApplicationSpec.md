# ApplicationSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env_vars** | **Dict[str, str]** | Environment variable key-value pairs, injected during runtime. | [optional] 
**name** | **str** | The name of the application. | [optional] 
**image** | **str** | Reference to the container image for the application package. | 

## Example

```python
from flightctl.models.application_spec import ApplicationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationSpec from a JSON string
application_spec_instance = ApplicationSpec.from_json(json)
# print the JSON string representation of the object
print(ApplicationSpec.to_json())

# convert the object into a dict
application_spec_dict = application_spec_instance.to_dict()
# create an instance of ApplicationSpec from a dict
application_spec_from_dict = ApplicationSpec.from_dict(application_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


