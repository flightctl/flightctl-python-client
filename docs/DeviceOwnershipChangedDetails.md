# DeviceOwnershipChangedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. | 
**previous_owner** | **str** | The previous owner fleet (null if none). | [optional] 
**new_owner** | **str** | The new owner fleet (null if removed). | [optional] 

## Example

```python
from flightctl.models.device_ownership_changed_details import DeviceOwnershipChangedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceOwnershipChangedDetails from a JSON string
device_ownership_changed_details_instance = DeviceOwnershipChangedDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceOwnershipChangedDetails.to_json())

# convert the object into a dict
device_ownership_changed_details_dict = device_ownership_changed_details_instance.to_dict()
# create an instance of DeviceOwnershipChangedDetails from a dict
device_ownership_changed_details_from_dict = DeviceOwnershipChangedDetails.from_dict(device_ownership_changed_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


