# HelmApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The application name must be 1–253 characters long, start with a letter or number, and contain no whitespace. | [optional] 
**app_type** | [**AppType**](AppType.md) |  | 
**image** | **str** | Reference to the chart for this helm application. | 
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


