# LabelSyncMappingStatus

Current propagation state for a label synchronization mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[Condition]**](Condition.md) | The Ready condition reports Pending, Degraded, or Success state. | [optional]

## Example

```python
from flightctl.models.label_sync_mapping_status import LabelSyncMappingStatus

# TODO update the JSON string below
json = "{}"
# create an instance of LabelSyncMappingStatus from a JSON string
label_sync_mapping_status_instance = LabelSyncMappingStatus.from_json(json)
# print the JSON string representation of the object
print(LabelSyncMappingStatus.to_json())

# convert the object into a dict
label_sync_mapping_status_dict = label_sync_mapping_status_instance.to_dict()
# create an instance of LabelSyncMappingStatus from a dict
label_sync_mapping_status_from_dict = LabelSyncMappingStatus.from_dict(label_sync_mapping_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
