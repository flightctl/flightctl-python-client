# ResourceSyncSpec

ResourceSyncSpec describes the file(s) to sync from a repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | The name of the repository resource to use as the sync source. | 
**target_revision** | **str** | The desired revision in the repository. | 
**path** | **str** | The path of a file or directory in the repository. If a directory, the directory should contain only resource definitions with no subdirectories. Each file should contain the definition of one or more resources. | 

## Example

```python
from flightctl.models.resource_sync_spec import ResourceSyncSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSyncSpec from a JSON string
resource_sync_spec_instance = ResourceSyncSpec.from_json(json)
# print the JSON string representation of the object
print(ResourceSyncSpec.to_json())

# convert the object into a dict
resource_sync_spec_dict = resource_sync_spec_instance.to_dict()
# create an instance of ResourceSyncSpec from a dict
resource_sync_spec_from_dict = ResourceSyncSpec.from_dict(resource_sync_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


