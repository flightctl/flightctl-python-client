# LabelSyncProvenanceList

Current LabelSyncMapping ownership grouped by exact label key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[LabelSyncProvenanceItem]**](LabelSyncProvenanceItem.md) | For organization queries, one item per supplied key in request order, including duplicates. For Device queries, one item per currently owned key, sorted by key. |

## Example

```python
from flightctl.models.label_sync_provenance_list import LabelSyncProvenanceList

# TODO update the JSON string below
json = "{}"
# create an instance of LabelSyncProvenanceList from a JSON string
label_sync_provenance_list_instance = LabelSyncProvenanceList.from_json(json)
# print the JSON string representation of the object
print(LabelSyncProvenanceList.to_json())

# convert the object into a dict
label_sync_provenance_list_dict = label_sync_provenance_list_instance.to_dict()
# create an instance of LabelSyncProvenanceList from a dict
label_sync_provenance_list_from_dict = LabelSyncProvenanceList.from_dict(label_sync_provenance_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
