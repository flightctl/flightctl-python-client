# FleetList

FleetList is a list of Fleets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**metadata** | [**ListMeta**](ListMeta.md) |  | 
**items** | [**List[Fleet]**](Fleet.md) | List of Fleets. | 

## Example

```python
from flightctl.models.fleet_list import FleetList

# TODO update the JSON string below
json = "{}"
# create an instance of FleetList from a JSON string
fleet_list_instance = FleetList.from_json(json)
# print the JSON string representation of the object
print(FleetList.to_json())

# convert the object into a dict
fleet_list_dict = fleet_list_instance.to_dict()
# create an instance of FleetList from a dict
fleet_list_from_dict = FleetList.from_dict(fleet_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


