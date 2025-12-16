# DeviceMultipleOwnersDetectedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. | 
**matching_fleets** | **List[str]** | List of fleet names that match the device. | 

## Example

```python
from flightctl.models.device_multiple_owners_detected_details import DeviceMultipleOwnersDetectedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceMultipleOwnersDetectedDetails from a JSON string
device_multiple_owners_detected_details_instance = DeviceMultipleOwnersDetectedDetails.from_json(json)
# print the JSON string representation of the object
print(DeviceMultipleOwnersDetectedDetails.to_json())

# convert the object into a dict
device_multiple_owners_detected_details_dict = device_multiple_owners_detected_details_instance.to_dict()
# create an instance of DeviceMultipleOwnersDetectedDetails from a dict
device_multiple_owners_detected_details_from_dict = DeviceMultipleOwnersDetectedDetails.from_dict(device_multiple_owners_detected_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


