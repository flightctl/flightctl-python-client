# ImageBuildNewVersionRequest

Request body for the newversion subresource endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the new ImageBuild resource. | 
**source_image_tag** | **str** | Override for spec.source.imageTag. If omitted, the parent&#39;s tag is used. | [optional] 
**destination_image_tag** | **str** | Override for spec.destination.imageTag. If omitted, the parent&#39;s tag is used. | [optional] 

## Example

```python
from flightctl.imagebuilder.models.image_build_new_version_request import ImageBuildNewVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageBuildNewVersionRequest from a JSON string
image_build_new_version_request_instance = ImageBuildNewVersionRequest.from_json(json)
# print the JSON string representation of the object
print(ImageBuildNewVersionRequest.to_json())

# convert the object into a dict
image_build_new_version_request_dict = image_build_new_version_request_instance.to_dict()
# create an instance of ImageBuildNewVersionRequest from a dict
image_build_new_version_request_from_dict = ImageBuildNewVersionRequest.from_dict(image_build_new_version_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


