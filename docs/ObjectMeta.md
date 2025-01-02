# ObjectMeta

ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_timestamp** | **datetime** | The time the object was created. | [optional] 
**deletion_timestamp** | **datetime** | The time the object will be deleted. | [optional] 
**name** | **str** | The name of the object. | [optional] 
**labels** | **Dict[str, str]** | Map of string keys and values that can be used to organize and categorize (scope and select) objects. | [optional] 
**generation** | **int** | A sequence number representing a specific generation of the desired state. Populated by the system. Read-only. | [optional] 
**owner** | **str** | A resource that owns this resource, in \&quot;kind/name\&quot; format. | [optional] 
**annotations** | **Dict[str, str]** | Properties set by the service. | [optional] 
**resource_version** | **str** | An opaque string that identifies the server&#39;s internal version of an object. | [optional] 

## Example

```python
from flightctl.models.object_meta import ObjectMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectMeta from a JSON string
object_meta_instance = ObjectMeta.from_json(json)
# print the JSON string representation of the object
print(ObjectMeta.to_json())

# convert the object into a dict
object_meta_dict = object_meta_instance.to_dict()
# create an instance of ObjectMeta from a dict
object_meta_from_dict = ObjectMeta.from_dict(object_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


