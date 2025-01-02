# ResourceSync

ResourceSync represents a reference to one or more files in a repository to sync to resource definitions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  | 
**spec** | [**ResourceSyncSpec**](ResourceSyncSpec.md) |  | 
**status** | [**ResourceSyncStatus**](ResourceSyncStatus.md) |  | [optional] 

## Example

```python
from flightctl.models.resource_sync import ResourceSync

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSync from a JSON string
resource_sync_instance = ResourceSync.from_json(json)
# print the JSON string representation of the object
print(ResourceSync.to_json())

# convert the object into a dict
resource_sync_dict = resource_sync_instance.to_dict()
# create an instance of ResourceSync from a dict
resource_sync_from_dict = ResourceSync.from_dict(resource_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


