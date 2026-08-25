# ComposeApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The application name must be 1–253 characters long, start with a letter or number, and contain no whitespace. | [optional] 
**app_type** | [**AppType**](AppType.md) |  | 
**annotations** | **Dict[str, str]** | Arbitrary metadata annotations. Used internally by the control plane (e.g., flightctl.io/workload-type) when transforming application types at render time. | [optional] [readonly] 
**desired_state** | [**ApplicationDesiredState**](ApplicationDesiredState.md) | Desired lifecycle state for this application, as most recently set by the stop/start device APIs. Read-only: cannot be set directly by apply; only present in the rendered application spec delivered to the agent. | [optional] [readonly] 
**restart_generation** | **int** | Counter incremented by the restart device API each time the application is restarted. Read-only: cannot be set directly by apply; only present in the rendered application spec delivered to the agent. | [optional] [readonly] 
**env_vars** | **Dict[str, str]** | Environment variable key-value pairs, injected during runtime. The key and value each must be between 1 and 253 characters. | [optional] 
**volumes** | [**List[ApplicationVolume]**](ApplicationVolume.md) | List of application volumes. | [optional] 
**image** | **str** | Reference to an OCI image or artifact with tag. | 
**catalog_item_ref** | [**CatalogItemRefSpec**](CatalogItemRefSpec.md) |  | 
**inline** | [**List[ApplicationContent]**](ApplicationContent.md) | A list of application content. | 

## Example

```python
from flightctl.models.compose_application import ComposeApplication

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeApplication from a JSON string
compose_application_instance = ComposeApplication.from_json(json)
# print the JSON string representation of the object
print(ComposeApplication.to_json())

# convert the object into a dict
compose_application_dict = compose_application_instance.to_dict()
# create an instance of ComposeApplication from a dict
compose_application_from_dict = ComposeApplication.from_dict(compose_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


