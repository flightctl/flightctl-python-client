# ApplicationVolumeStatus

Status of a volume used by an application.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the volume. | 
**reference** | **str** | Reference to the deployed OCI-compliant image or artifact backing the volume. | 

## Example

```python
from flightctl.models.application_volume_status import ApplicationVolumeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationVolumeStatus from a JSON string
application_volume_status_instance = ApplicationVolumeStatus.from_json(json)
# print the JSON string representation of the object
print(ApplicationVolumeStatus.to_json())

# convert the object into a dict
application_volume_status_dict = application_volume_status_instance.to_dict()
# create an instance of ApplicationVolumeStatus from a dict
application_volume_status_from_dict = ApplicationVolumeStatus.from_dict(application_volume_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


