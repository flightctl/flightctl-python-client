# CatalogItemArtifact

An artifact reference. The type field is the discriminator and must be unique within the artifacts list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CatalogItemArtifactType**](CatalogItemArtifactType.md) |  | 
**name** | **str** | Optional human-readable display name for this artifact. | [optional] 
**uri** | **str** | Artifact URI without version qualifier. The version reference (tag or digest) is applied at resolution time. | 

## Example

```python
from flightctl.v1alpha1.models.catalog_item_artifact import CatalogItemArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogItemArtifact from a JSON string
catalog_item_artifact_instance = CatalogItemArtifact.from_json(json)
# print the JSON string representation of the object
print(CatalogItemArtifact.to_json())

# convert the object into a dict
catalog_item_artifact_dict = catalog_item_artifact_instance.to_dict()
# create an instance of CatalogItemArtifact from a dict
catalog_item_artifact_from_dict = CatalogItemArtifact.from_dict(catalog_item_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


