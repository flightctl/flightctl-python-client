# ApplicationProviderBase

Common properties for all application types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The application name must be 1–253 characters long, start with a letter or number, and contain no whitespace. | [optional] 
**app_type** | [**AppType**](AppType.md) |  | 
**annotations** | **Dict[str, str]** | Arbitrary metadata annotations. Used internally by the control plane (e.g., flightctl.io/workload-type) when transforming application types at render time. | [optional] [readonly] 
**desired_state** | [**ApplicationDesiredState**](ApplicationDesiredState.md) | Desired lifecycle state for this application, as most recently set by the stop/start device APIs. Read-only: cannot be set directly by apply; only present in the rendered application spec delivered to the agent. | [optional] [readonly] 
**restart_generation** | **int** | Counter incremented by the restart device API each time the application is restarted. Read-only: cannot be set directly by apply; only present in the rendered application spec delivered to the agent. | [optional] [readonly] 

## Example

```python
from flightctl.models.application_provider_base import ApplicationProviderBase

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationProviderBase from a JSON string
application_provider_base_instance = ApplicationProviderBase.from_json(json)
# print the JSON string representation of the object
print(ApplicationProviderBase.to_json())

# convert the object into a dict
application_provider_base_dict = application_provider_base_instance.to_dict()
# create an instance of ApplicationProviderBase from a dict
application_provider_base_from_dict = ApplicationProviderBase.from_dict(application_provider_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


