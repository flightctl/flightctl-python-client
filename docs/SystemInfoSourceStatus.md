# SystemInfoSourceStatus

Collection status for a single system information source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**SystemInfoSourceStatusType**](SystemInfoSourceStatusType.md) |  |
**last_transition_time** | **datetime** | The last time the collection status of this source changed. |
**message** | **str** | Human readable message providing details about the source status. | [optional]

## Example

```python
from flightctl.models.system_info_source_status import SystemInfoSourceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SystemInfoSourceStatus from a JSON string
system_info_source_status_instance = SystemInfoSourceStatus.from_json(json)
# print the JSON string representation of the object
print(SystemInfoSourceStatus.to_json())

# convert the object into a dict
system_info_source_status_dict = system_info_source_status_instance.to_dict()
# create an instance of SystemInfoSourceStatus from a dict
system_info_source_status_from_dict = SystemInfoSourceStatus.from_dict(system_info_source_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
