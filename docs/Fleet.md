# Fleet

Fleet represents a set of devices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  | 
**spec** | [**FleetSpec**](FleetSpec.md) |  | 
**status** | [**FleetStatus**](FleetStatus.md) |  | [optional] 

## Example

```python
from flightctl.models.fleet import Fleet

# TODO update the JSON string below
json = "{}"
# create an instance of Fleet from a JSON string
fleet_instance = Fleet.from_json(json)
# print the JSON string representation of the object
print(Fleet.to_json())

# convert the object into a dict
fleet_dict = fleet_instance.to_dict()
# create an instance of Fleet from a dict
fleet_from_dict = Fleet.from_dict(fleet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


