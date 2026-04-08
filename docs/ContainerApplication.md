# ContainerApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The application name must be 1–253 characters long, start with a letter or number, and contain no whitespace. | [optional] 
**app_type** | [**AppType**](AppType.md) |  | 
**env_vars** | **Dict[str, str]** | Environment variable key-value pairs, injected during runtime. The key and value each must be between 1 and 253 characters. | [optional] 
**run_as** | **str** | The username of the system user this application should be run under. This is not the same as the user within any containers of the application (if applicable). Defaults to the user that the agent runs as (generally root) if not specified. | [optional] 
**volumes** | [**List[ApplicationVolume]**](ApplicationVolume.md) | List of application volumes. | [optional] 
**image** | **str** | Reference to the image for this container. | 
**ports** | **List[str]** | Port mappings. | [optional] 
**resources** | [**ApplicationResources**](ApplicationResources.md) |  | [optional] 

## Example

```python
from flightctl.models.container_application import ContainerApplication

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerApplication from a JSON string
container_application_instance = ContainerApplication.from_json(json)
# print the JSON string representation of the object
print(ContainerApplication.to_json())

# convert the object into a dict
container_application_dict = container_application_instance.to_dict()
# create an instance of ContainerApplication from a dict
container_application_from_dict = ContainerApplication.from_dict(container_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


