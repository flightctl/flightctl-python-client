# ArtifactPromotionStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | Artifact format. \&quot;container\&quot; for the ImageBuild artifact; one of the exportFormats values for additional artifacts. | 
**ready** | **bool** | True when at least one successful artifact of this format is available. | 
**published** | **bool** | True when this format&#39;s artifact reference has been successfully written to the CatalogItemVersion. For the initial publish, all formats are published atomically. For amendments, formats added via PATCH/PUT start as published&#x3D;false and transition to published&#x3D;true when their CatalogItem patch succeeds. | 
**resolved_export** | **str** | Name of the ImageExport resource that will be (or was) used for this format. Absent for the container artifact and for formats not yet ready. | [optional] 

## Example

```python
from flightctl.imagebuilder.models.artifact_promotion_status import ArtifactPromotionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactPromotionStatus from a JSON string
artifact_promotion_status_instance = ArtifactPromotionStatus.from_json(json)
# print the JSON string representation of the object
print(ArtifactPromotionStatus.to_json())

# convert the object into a dict
artifact_promotion_status_dict = artifact_promotion_status_instance.to_dict()
# create an instance of ArtifactPromotionStatus from a dict
artifact_promotion_status_from_dict = ArtifactPromotionStatus.from_dict(artifact_promotion_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


