# ApplicationResourceLimits

Resource limits for the application.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **str** | CPU limit in cores. Format restricted based on application type. | [optional] 
**memory** | **str** | Memory limit with optional unit. Format restricted based on application type. | [optional] 

## Example

```python
from flightctl.models.application_resource_limits import ApplicationResourceLimits

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationResourceLimits from a JSON string
application_resource_limits_instance = ApplicationResourceLimits.from_json(json)
# print the JSON string representation of the object
print(ApplicationResourceLimits.to_json())

# convert the object into a dict
application_resource_limits_dict = application_resource_limits_instance.to_dict()
# create an instance of ApplicationResourceLimits from a dict
application_resource_limits_from_dict = ApplicationResourceLimits.from_dict(application_resource_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


