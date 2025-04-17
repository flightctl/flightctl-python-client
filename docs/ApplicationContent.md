# ApplicationContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The plain text (UTF-8) or base64-encoded content of the file. | [optional] 
**content_encoding** | [**EncodingType**](EncodingType.md) |  | [optional] 
**path** | **str** | A relative file path on the system. Note that any existing file will be overwritten. | 

## Example

```python
from flightctl.models.application_content import ApplicationContent

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationContent from a JSON string
application_content_instance = ApplicationContent.from_json(json)
# print the JSON string representation of the object
print(ApplicationContent.to_json())

# convert the object into a dict
application_content_dict = application_content_instance.to_dict()
# create an instance of ApplicationContent from a dict
application_content_from_dict = ApplicationContent.from_dict(application_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


