# DeviceMultipleOwnersResolvedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. | 
**resolution_type** | **str** | How the conflict was resolved. | 
**assigned_owner** | **str** | The fleet assigned as owner (null if no owner). | [optional] 
**previous_matching_fleets** | **List[str]** | List of fleets that previously matched the device. | [optional] 

## Example

```python
from flightctl.models.device_multiple_owners_resolved_details import DeviceMultipleOwnersResolvedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceMultipleOwnersResolvedDetails from a JSON string
device_multiple_owners_resolved_details_instance = DeviceMultipleOwnersResolvedDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceMultipleOwnersResolvedDetails.to_json())

# convert the object into a dict
device_multiple_owners_resolved_details_dict = device_multiple_owners_resolved_details_instance.to_dict()
# create an instance of DeviceMultipleOwnersResolvedDetails from a dict
device_multiple_owners_resolved_details_from_dict = DeviceMultipleOwnersResolvedDetails.from_dict(device_multiple_owners_resolved_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


