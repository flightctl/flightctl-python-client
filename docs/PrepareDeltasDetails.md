# PrepareDeltasDetails

Structured details for PrepareDeltas events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. |
**template_version** | **str** | Fleet only. The TemplateVersion this prepare is for. Required when involvedObject.kind is Fleet; omitted for Device. | [optional]
**generation** | **int** | Device only. The desired spec generation this prepare is for. Required when involvedObject.kind is Device; omitted for Fleet. | [optional]
**resource_version** | **str** | The resource version of the involved Fleet or Device when this prepare event was created. Used to ignore stale prepare events. May be omitted for retained events created before this field was introduced. | [optional]

## Example

```python
from flightctl.models.prepare_deltas_details import PrepareDeltasDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareDeltasDetails from a JSON string
prepare_deltas_details_instance = PrepareDeltasDetails.from_json(json)
# print the JSON string representation of the object
print(PrepareDeltasDetails.to_json())

# convert the object into a dict
prepare_deltas_details_dict = prepare_deltas_details_instance.to_dict()
# create an instance of PrepareDeltasDetails from a dict
prepare_deltas_details_from_dict = PrepareDeltasDetails.from_dict(prepare_deltas_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
