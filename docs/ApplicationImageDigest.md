# ApplicationImageDigest

An image reference and its known registry image digest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | Image reference as it appears in the rendered application spec. |
**digest** | **str** | Registry digest associated with this image. If the runtime identifies a platform-specific image, this may differ from the digest in the image reference. Omitted when unavailable. | [optional]

## Example

```python
from flightctl.models.application_image_digest import ApplicationImageDigest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationImageDigest from a JSON string
application_image_digest_instance = ApplicationImageDigest.from_json(json)
# print the JSON string representation of the object
print(ApplicationImageDigest.to_json())

# convert the object into a dict
application_image_digest_dict = application_image_digest_instance.to_dict()
# create an instance of ApplicationImageDigest from a dict
application_image_digest_from_dict = ApplicationImageDigest.from_dict(application_image_digest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
