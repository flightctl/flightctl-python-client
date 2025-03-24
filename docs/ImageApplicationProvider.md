# ImageApplicationProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | Reference to the container image for the application package. | 

## Example

```python
from flightctl.models.image_application_provider import ImageApplicationProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ImageApplicationProvider from a JSON string
image_application_provider_instance = ImageApplicationProvider.from_json(json)
# print the JSON string representation of the object
print(ImageApplicationProvider.to_json())

# convert the object into a dict
image_application_provider_dict = image_application_provider_instance.to_dict()
# create an instance of ImageApplicationProvider from a dict
image_application_provider_from_dict = ImageApplicationProvider.from_dict(image_application_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


