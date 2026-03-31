# QuadletApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The application name must be 1–253 characters long, start with a letter or number, and contain no whitespace. | [optional] 
**app_type** | [**AppType**](AppType.md) |  | 
**env_vars** | **Dict[str, str]** | Environment variable key-value pairs, injected during runtime. The key and value each must be between 1 and 253 characters. | [optional] 
**run_as** | **str** | The username of the system user this application should be run under. This is not the same as the user within any containers of the application (if applicable). Defaults to the user that the agent runs as (generally root) if not specified. | [optional] 
**volumes** | [**List[ApplicationVolume]**](ApplicationVolume.md) | List of application volumes. | [optional] 
**image** | **str** | Reference to the OCI image or artifact for the application package. | 
**inline** | [**List[ApplicationContent]**](ApplicationContent.md) | A list of application content. | 

## Example

```python
from flightctl.models.quadlet_application import QuadletApplication

# TODO update the JSON string below
json = "{}"
# create an instance of QuadletApplication from a JSON string
quadlet_application_instance = QuadletApplication.from_json(json)
# print the JSON string representation of the object
print(QuadletApplication.to_json())

# convert the object into a dict
quadlet_application_dict = quadlet_application_instance.to_dict()
# create an instance of QuadletApplication from a dict
quadlet_application_from_dict = QuadletApplication.from_dict(quadlet_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


