# DeviceApplicationStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human readable name of the application. | 
**ready** | **str** | The number of containers which are ready in the application. | 
**restarts** | **int** | Number of restarts observed for the application. | 
**status** | [**ApplicationStatusType**](ApplicationStatusType.md) |  | 
**embedded** | **bool** | Whether the application is embedded in the bootc image. | 
**app_type** | [**AppType**](AppType.md) |  | 
**run_as** | **str** | The username of the system user this application is runing under. If blank, the application is run as the same user as the agent (generally root). | [optional] 
**volumes** | [**List[ApplicationVolumeStatus]**](ApplicationVolumeStatus.md) | Status of volumes used by this application. | [optional] 
**last_delta** | [**DeviceDeltaApplyStatus**](DeviceDeltaApplyStatus.md) |  | [optional]
**image_digests** | [**List[ApplicationImageDigest]**](ApplicationImageDigest.md) | Image references this application uses and the registry digest associated with each image. image is the ref from the current rendered spec (tag or digest). For a multi-platform index, digest is the platform-specific manifest selected by the runtime when available; if the runtime exposes only an opaque ID, an immutable image reference&#39;s digest may be reported. digest is omitted when no registry digest is known. | [optional]
**delta_size** | **str** | Expected total size of control-plane generated delta images for this application update in IEC units (e.g. \&quot;245.3 MiB\&quot;, \&quot;1 GiB\&quot;). Computed as the sum of generated delta image sizes across the application. Absent when no delta image was generated or any generated delta image size is unknown. Full image sizes are not included. | [optional]

## Example

```python
from flightctl.models.device_application_status import DeviceApplicationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceApplicationStatus from a JSON string
device_application_status_instance = DeviceApplicationStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceApplicationStatus.to_json())

# convert the object into a dict
device_application_status_dict = device_application_status_instance.to_dict()
# create an instance of DeviceApplicationStatus from a dict
device_application_status_from_dict = DeviceApplicationStatus.from_dict(device_application_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


