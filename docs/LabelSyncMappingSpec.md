# LabelSyncMappingSpec

Desired state for a label synchronization mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | Immutable resource type evaluated by the mapping. |
**key** | **str** | Complete destination label key for scalar mode. Omitted or null selects map mode; no prefix is added. | [optional]
**expression** | **str** | CEL expression evaluated for the selected resource type. |

## Example

```python
from flightctl.models.label_sync_mapping_spec import LabelSyncMappingSpec

# TODO update the JSON string below
json = "{}"
# create an instance of LabelSyncMappingSpec from a JSON string
label_sync_mapping_spec_instance = LabelSyncMappingSpec.from_json(json)
# print the JSON string representation of the object
print(LabelSyncMappingSpec.to_json())

# convert the object into a dict
label_sync_mapping_spec_dict = label_sync_mapping_spec_instance.to_dict()
# create an instance of LabelSyncMappingSpec from a dict
label_sync_mapping_spec_from_dict = LabelSyncMappingSpec.from_dict(label_sync_mapping_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
