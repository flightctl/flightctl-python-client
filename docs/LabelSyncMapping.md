# LabelSyncMapping

LabelSyncMapping defines an organization-scoped device label mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | [**ApiVersion**](ApiVersion.md) |  |
**kind** | **str** | Kind is a string value representing this resource type. |
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  |
**spec** | [**LabelSyncMappingSpec**](LabelSyncMappingSpec.md) |  |
**status** | [**LabelSyncMappingStatus**](LabelSyncMappingStatus.md) |  | [optional]

## Example

```python
from flightctl.models.label_sync_mapping import LabelSyncMapping

# TODO update the JSON string below
json = "{}"
# create an instance of LabelSyncMapping from a JSON string
label_sync_mapping_instance = LabelSyncMapping.from_json(json)
# print the JSON string representation of the object
print(LabelSyncMapping.to_json())

# convert the object into a dict
label_sync_mapping_dict = label_sync_mapping_instance.to_dict()
# create an instance of LabelSyncMapping from a dict
label_sync_mapping_from_dict = LabelSyncMapping.from_dict(label_sync_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
