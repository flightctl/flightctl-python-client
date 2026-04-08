# ImageBuildDestination

ImageBuildDestination specifies the destination for the built image.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | The name of the Repository resource of type OCI to push the built image to. | 
**image_name** | **str** | The name of the output image. | 
**image_tag** | **str** | The tag of the output image. | 

## Example

```python
from flightctl.imagebuilder.models.image_build_destination import ImageBuildDestination

# TODO update the JSON string below
json = "{}"
# create an instance of ImageBuildDestination from a JSON string
image_build_destination_instance = ImageBuildDestination.from_json(json)
# print the JSON string representation of the object
print(ImageBuildDestination.to_json())

# convert the object into a dict
image_build_destination_dict = image_build_destination_instance.to_dict()
# create an instance of ImageBuildDestination from a dict
image_build_destination_from_dict = ImageBuildDestination.from_dict(image_build_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


