# FileSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The absolute path to the file on the device. Note that any existing file will be overwritten. | 
**content** | **str** | The plain text (UTF-8) or base64-encoded content of the file. | 
**content_encoding** | **str** | How the contents are encoded. Must be either \&quot;plain\&quot; or \&quot;base64\&quot;. Defaults to \&quot;plain\&quot;. | [optional] 
**mode** | **int** | The file&#39;s permission mode. You may specify the more familiar octal with a leading zero (e.g., 0644) or as a decimal without a leading zero (e.g., 420). Setuid/setgid/sticky bits are supported. If not specified, the permission mode for files defaults to 0644. | [optional] 
**user** | **str** | The file&#39;s owner, specified either as a name or numeric ID. Defaults to \&quot;root\&quot;. | [optional] 
**group** | **str** | The file&#39;s group, specified either as a name or numeric ID. Defaults to \&quot;root\&quot;. | [optional] 

## Example

```python
from flightctl.models.file_spec import FileSpec

# TODO update the JSON string below
json = "{}"
# create an instance of FileSpec from a JSON string
file_spec_instance = FileSpec.from_json(json)
# print the JSON string representation of the object
print(FileSpec.to_json())

# convert the object into a dict
file_spec_dict = file_spec_instance.to_dict()
# create an instance of FileSpec from a dict
file_spec_from_dict = FileSpec.from_dict(file_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


