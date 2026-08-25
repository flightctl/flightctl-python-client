# HelmApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The application name must be 1–253 characters long, start with a letter or number, and contain no whitespace. | [optional] 
**app_type** | [**AppType**](AppType.md) |  | 
**annotations** | **Dict[str, str]** | Arbitrary metadata annotations. Used internally by the control plane (e.g., flightctl.io/workload-type) when transforming application types at render time. | [optional] [readonly] 
**desired_state** | [**ApplicationDesiredState**](ApplicationDesiredState.md) | Desired lifecycle state for this application, as most recently set by the stop/start device APIs. Read-only: cannot be set directly by apply; only present in the rendered application spec delivered to the agent. | [optional] [readonly] 
**restart_generation** | **int** | Counter incremented by the restart device API each time the application is restarted. Read-only: cannot be set directly by apply; only present in the rendered application spec delivered to the agent. | [optional] [readonly] 
**image** | **str** | Reference to an OCI image or artifact with tag. | 
**catalog_item_ref** | [**CatalogItemRefSpec**](CatalogItemRefSpec.md) |  | 
**namespace** | **str** | The target namespace for the application deployment. | [optional] 
**values** | **Dict[str, object]** | Configuration values for the application. Supports arbitrarily nested structures. | [optional] 
**values_files** | **List[str]** | List of values files to apply during deployment. Files are relative paths and applied in array order before user-provided values. | [optional] 

## Example

```python
from flightctl.models.helm_application import HelmApplication

# TODO update the JSON string below
json = "{}"
# create an instance of HelmApplication from a JSON string
helm_application_instance = HelmApplication.from_json(json)
# print the JSON string representation of the object
print(HelmApplication.to_json())

# convert the object into a dict
helm_application_dict = helm_application_instance.to_dict()
# create an instance of HelmApplication from a dict
helm_application_from_dict = HelmApplication.from_dict(helm_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


