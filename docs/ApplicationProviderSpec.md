# ApplicationProviderSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env_vars** | **Dict[str, str]** | Environment variable key-value pairs, injected during runtime. The key and value each must be between 1 and 253 characters. | [optional] 
**name** | **str** | The application name must be 1–253 characters long, start with a letter or number, and contain no whitespace. | [optional] 
**app_type** | [**AppType**](AppType.md) |  | [optional] 
**image** | **str** | Reference to the container image for the application package. | 
**inline** | [**List[ApplicationContent]**](ApplicationContent.md) | A list of application content. | 

## Example

```python
from flightctl.models.application_provider_spec import ApplicationProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationProviderSpec from a JSON string
application_provider_spec_instance = ApplicationProviderSpec.from_json(json)
# print the JSON string representation of the object
print(ApplicationProviderSpec.to_json())

# convert the object into a dict
application_provider_spec_dict = application_provider_spec_instance.to_dict()
# create an instance of ApplicationProviderSpec from a dict
application_provider_spec_from_dict = ApplicationProviderSpec.from_dict(application_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


