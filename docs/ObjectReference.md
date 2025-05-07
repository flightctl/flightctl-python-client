# ObjectReference

A reference to a resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**name** | **str** | The name of the referenced object. | 

## Example

```python
from flightctl.models.object_reference import ObjectReference

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectReference from a JSON string
object_reference_instance = ObjectReference.from_json(json)
# print the JSON string representation of the object
print(ObjectReference.to_json())

# convert the object into a dict
object_reference_dict = object_reference_instance.to_dict()
# create an instance of ObjectReference from a dict
object_reference_from_dict = ObjectReference.from_dict(object_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


