# DeviceDeltaApplyStatus

Agent-reported result for delta apply attempts for this update target. For an application with multiple image targets, the outcome is aggregated across image targets. The lastDelta field is omitted until the agent reports an outcome; server-side delta preparation is reported separately.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcome** | [**DeviceDeltaApplyOutcomeType**](DeviceDeltaApplyOutcomeType.md) |  |
**fallback_reason** | **str** | Set when one or more delta attempts failed and the agent attempted a full image pull. For an application with multiple image targets, this reports one representative failure reason. | [optional]

## Example

```python
from flightctl.models.device_delta_apply_status import DeviceDeltaApplyStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDeltaApplyStatus from a JSON string
device_delta_apply_status_instance = DeviceDeltaApplyStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceDeltaApplyStatus.to_json())

# convert the object into a dict
device_delta_apply_status_dict = device_delta_apply_status_instance.to_dict()
# create an instance of DeviceDeltaApplyStatus from a dict
device_delta_apply_status_from_dict = DeviceDeltaApplyStatus.from_dict(device_delta_apply_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
