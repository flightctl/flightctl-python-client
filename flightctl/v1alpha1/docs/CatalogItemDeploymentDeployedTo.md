# CatalogItemDeploymentDeployedTo

The device or fleet that this deployment pertains to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_kind** | **str** | Either a Device or Fleet. | [optional] 
**resource_name** | **str** | The name of the device or fleet. | [optional] 

## Example

```python
from flightctl.v1alpha1.models.catalog_item_deployment_deployed_to import CatalogItemDeploymentDeployedTo

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogItemDeploymentDeployedTo from a JSON string
catalog_item_deployment_deployed_to_instance = CatalogItemDeploymentDeployedTo.from_json(json)
# print the JSON string representation of the object
print(CatalogItemDeploymentDeployedTo.to_json())

# convert the object into a dict
catalog_item_deployment_deployed_to_dict = catalog_item_deployment_deployed_to_instance.to_dict()
# create an instance of CatalogItemDeploymentDeployedTo from a dict
catalog_item_deployment_deployed_to_from_dict = CatalogItemDeploymentDeployedTo.from_dict(catalog_item_deployment_deployed_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


