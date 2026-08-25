# CatalogItemDeployment

CatalogItemDeployment represents a specific deployment of a catalog item to a fleet or device. A catalog item associated to a fleet that has no devices is still considered a deployment. A deployment is only associated with the fleet and not the individual devices in cases where a device is using a catalog item deployment that came from a device spec template on a fleet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | [**ApiVersion**](ApiVersion.md) |  | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. | 
**deployed_to** | [**CatalogItemDeploymentDeployedTo**](CatalogItemDeploymentDeployedTo.md) |  | [optional] 
**catalog** | **str** | The catalog of the catalogItem. | 
**catalog_item** | **str** | The catalogItem that this deployment corresponds to. | 
**version** | **str** | The version of the catalog item that is deployed. | 
**channel** | **str** | The channel, if any, that is intended to be tracked for the catalog item. | [optional] 
**application_name** | **str** | For catalog items in the &#39;application&#39; category, the name of the application on the device that the deployment is associated with. Required for application catalog items. | [optional] 

## Example

```python
from flightctl.v1alpha1.models.catalog_item_deployment import CatalogItemDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogItemDeployment from a JSON string
catalog_item_deployment_instance = CatalogItemDeployment.from_json(json)
# print the JSON string representation of the object
print(CatalogItemDeployment.to_json())

# convert the object into a dict
catalog_item_deployment_dict = catalog_item_deployment_instance.to_dict()
# create an instance of CatalogItemDeployment from a dict
catalog_item_deployment_from_dict = CatalogItemDeployment.from_dict(catalog_item_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


