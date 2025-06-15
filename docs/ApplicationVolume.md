# ApplicationVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name of the volume used within the application. | 
**image** | [**ImageVolumeSource**](ImageVolumeSource.md) |  | 

## Example

```python
from flightctl.models.application_volume import ApplicationVolume

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationVolume from a JSON string
application_volume_instance = ApplicationVolume.from_json(json)
# print the JSON string representation of the object
print(ApplicationVolume.to_json())

# convert the object into a dict
application_volume_dict = application_volume_instance.to_dict()
# create an instance of ApplicationVolume from a dict
application_volume_from_dict = ApplicationVolume.from_dict(application_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


