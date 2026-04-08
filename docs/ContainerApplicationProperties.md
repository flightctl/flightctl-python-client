# ContainerApplicationProperties

Properties for container application deployments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ports** | **List[str]** | Port mappings. | [optional] 
**resources** | [**ApplicationResources**](ApplicationResources.md) |  | [optional] 

## Example

```python
from flightctl.models.container_application_properties import ContainerApplicationProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerApplicationProperties from a JSON string
container_application_properties_instance = ContainerApplicationProperties.from_json(json)
# print the JSON string representation of the object
print(ContainerApplicationProperties.to_json())

# convert the object into a dict
container_application_properties_dict = container_application_properties_instance.to_dict()
# create an instance of ContainerApplicationProperties from a dict
container_application_properties_from_dict = ContainerApplicationProperties.from_dict(container_application_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


