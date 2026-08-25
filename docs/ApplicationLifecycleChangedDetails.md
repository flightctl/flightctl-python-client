# ApplicationLifecycleChangedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. | 
**app_name** | **str** | The name of the application whose device-level lifecycle override changed. | 
**action** | **str** | The lifecycle action that was requested. | 

## Example

```python
from flightctl.models.application_lifecycle_changed_details import ApplicationLifecycleChangedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationLifecycleChangedDetails from a JSON string
application_lifecycle_changed_details_instance = ApplicationLifecycleChangedDetails.from_json(json)
# print the JSON string representation of the object
print(ApplicationLifecycleChangedDetails.to_json())

# convert the object into a dict
application_lifecycle_changed_details_dict = application_lifecycle_changed_details_instance.to_dict()
# create an instance of ApplicationLifecycleChangedDetails from a dict
application_lifecycle_changed_details_from_dict = ApplicationLifecycleChangedDetails.from_dict(application_lifecycle_changed_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


