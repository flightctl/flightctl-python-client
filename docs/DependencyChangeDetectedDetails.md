# DependencyChangeDetectedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. | 
**resource_key** | **str** | The resource key identifying the dependency that changed (e.g. \&quot;git:my-repo/main\&quot;). | 
**fingerprint** | **str** | The new fingerprint (e.g. commit SHA) of the changed dependency. | 

## Example

```python
from flightctl.models.dependency_change_detected_details import DependencyChangeDetectedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DependencyChangeDetectedDetails from a JSON string
dependency_change_detected_details_instance = DependencyChangeDetectedDetails.from_json(json)
# print the JSON string representation of the object
print(DependencyChangeDetectedDetails.to_json())

# convert the object into a dict
dependency_change_detected_details_dict = dependency_change_detected_details_instance.to_dict()
# create an instance of DependencyChangeDetectedDetails from a dict
dependency_change_detected_details_from_dict = DependencyChangeDetectedDetails.from_dict(dependency_change_detected_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


