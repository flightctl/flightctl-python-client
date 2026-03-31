# ApplicationProviderSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The application name must be 1–253 characters long, start with a letter or number, and contain no whitespace. | [optional] 
**app_type** | [**AppType**](AppType.md) |  | 
**env_vars** | **Dict[str, str]** | Environment variable key-value pairs, injected during runtime. The key and value each must be between 1 and 253 characters. | [optional] 
**volumes** | [**List[ApplicationVolume]**](ApplicationVolume.md) | List of application volumes. | [optional] 
**image** | **str** | Reference to the chart for this helm application. | 
**inline** | [**List[ApplicationContent]**](ApplicationContent.md) | A list of application content. | 
**run_as** | **str** | The username of the system user this application should be run under. This is not the same as the user within any containers of the application (if applicable). Defaults to the user that the agent runs as (generally root) if not specified. | [optional] 
**ports** | **List[str]** | Port mappings. | [optional] 
**resources** | [**ApplicationResources**](ApplicationResources.md) |  | [optional] 
**namespace** | **str** | The target namespace for the application deployment. | [optional] 
**values** | **Dict[str, object]** | Configuration values for the application. Supports arbitrarily nested structures. | [optional] 
**values_files** | **List[str]** | List of values files to apply during deployment. Files are relative paths and applied in array order before user-provided values. | [optional] 

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


