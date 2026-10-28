# DeltaGenerationProgressDetails

Structured details for DeltaGenerationProgress events. One event when a pair enters a phase or becomes terminal, fanned out to each waiting Fleet or standalone Device. Not a percent heartbeat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. |
**image_repository** | **str** | Image repository (host/namespace/name) for this pair. |
**source_digest** | **str** | Current image digest. |
**target_digest** | **str** | Target image digest. |
**generation_status** | **str** | Generation row status for this pair. |
**phase** | [**DeltaGenerationPhase**](DeltaGenerationPhase.md) |  | [optional]
**template_version** | **str** | Fleet only. The TemplateVersion this prepare is for. | [optional]
**generation** | **int** | Device only. The desired spec generation this prepare is for. | [optional]

## Example

```python
from flightctl.models.delta_generation_progress_details import DeltaGenerationProgressDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DeltaGenerationProgressDetails from a JSON string
delta_generation_progress_details_instance = DeltaGenerationProgressDetails.from_json(json)
# print the JSON string representation of the object
print(DeltaGenerationProgressDetails.to_json())

# convert the object into a dict
delta_generation_progress_details_dict = delta_generation_progress_details_instance.to_dict()
# create an instance of DeltaGenerationProgressDetails from a dict
delta_generation_progress_details_from_dict = DeltaGenerationProgressDetails.from_dict(delta_generation_progress_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
