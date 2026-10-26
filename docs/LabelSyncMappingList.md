# LabelSyncMappingList

LabelSyncMappingList is a list of LabelSyncMapping resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | [**ApiVersion**](ApiVersion.md) |  |
**kind** | **str** | Kind is a string value representing the REST resource this object represents. |
**metadata** | [**ListMeta**](ListMeta.md) |  |
**items** | [**List[LabelSyncMapping]**](LabelSyncMapping.md) | List of LabelSyncMapping resources. |

## Example

```python
from flightctl.models.label_sync_mapping_list import LabelSyncMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of LabelSyncMappingList from a JSON string
label_sync_mapping_list_instance = LabelSyncMappingList.from_json(json)
# print the JSON string representation of the object
print(LabelSyncMappingList.to_json())

# convert the object into a dict
label_sync_mapping_list_dict = label_sync_mapping_list_instance.to_dict()
# create an instance of LabelSyncMappingList from a dict
label_sync_mapping_list_from_dict = LabelSyncMappingList.from_dict(label_sync_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
