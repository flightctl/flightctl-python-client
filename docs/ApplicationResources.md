# ApplicationResources

Resource constraints for the application.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | [**ApplicationResourceLimits**](ApplicationResourceLimits.md) |  | [optional] 

## Example

```python
from flightctl.models.application_resources import ApplicationResources

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationResources from a JSON string
application_resources_instance = ApplicationResources.from_json(json)
# print the JSON string representation of the object
print(ApplicationResources.to_json())

# convert the object into a dict
application_resources_dict = application_resources_instance.to_dict()
# create an instance of ApplicationResources from a dict
application_resources_from_dict = ApplicationResources.from_dict(application_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


