# ImageApplicationProviderSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volumes** | [**List[ApplicationVolume]**](ApplicationVolume.md) | List of application volumes. | [optional] 
**image** | **str** | Reference to the container image for the application package. | 

## Example

```python
from flightctl.models.image_application_provider_spec import ImageApplicationProviderSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ImageApplicationProviderSpec from a JSON string
image_application_provider_spec_instance = ImageApplicationProviderSpec.from_json(json)
# print the JSON string representation of the object
print(ImageApplicationProviderSpec.to_json())

# convert the object into a dict
image_application_provider_spec_dict = image_application_provider_spec_instance.to_dict()
# create an instance of ImageApplicationProviderSpec from a dict
image_application_provider_spec_from_dict = ImageApplicationProviderSpec.from_dict(image_application_provider_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


