# ImageDeltaHint

A control-plane-generated delta hint for a nested image within an application. Present only in rendered application specs delivered to the agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_image** | **str** | The target image reference this delta applies to. |
**target_digest** | **str** | The content digest of the target image. |
**delta_image** | **str** | Reference to the delta artifact for this nested image. |

## Example

```python
from flightctl.models.image_delta_hint import ImageDeltaHint

# TODO update the JSON string below
json = "{}"
# create an instance of ImageDeltaHint from a JSON string
image_delta_hint_instance = ImageDeltaHint.from_json(json)
# print the JSON string representation of the object
print(ImageDeltaHint.to_json())

# convert the object into a dict
image_delta_hint_dict = image_delta_hint_instance.to_dict()
# create an instance of ImageDeltaHint from a dict
image_delta_hint_from_dict = ImageDeltaHint.from_dict(image_delta_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
