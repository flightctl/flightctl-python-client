# LabelSyncProvenanceItem

Current owning LabelSyncMapping names for one exact label key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Exact label key. |
**owners** | **List[str]** | Names of current owning LabelSyncMapping resources. An empty array means the key has no current mapping owner. |

## Example

```python
from flightctl.models.label_sync_provenance_item import LabelSyncProvenanceItem

# TODO update the JSON string below
json = "{}"
# create an instance of LabelSyncProvenanceItem from a JSON string
label_sync_provenance_item_instance = LabelSyncProvenanceItem.from_json(json)
# print the JSON string representation of the object
print(LabelSyncProvenanceItem.to_json())

# convert the object into a dict
label_sync_provenance_item_dict = label_sync_provenance_item_instance.to_dict()
# create an instance of LabelSyncProvenanceItem from a dict
label_sync_provenance_item_from_dict = LabelSyncProvenanceItem.from_dict(label_sync_provenance_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
