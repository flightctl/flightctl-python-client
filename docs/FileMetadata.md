# FileMetadata

File metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **int** | The file&#39;s permission mode. You may specify the more familiar octal with a leading zero (e.g., 0644) or as a decimal without a leading zero (e.g., 420). Setuid/setgid/sticky bits are supported. If not specified, the permission mode for files defaults to 0644. | [optional] 
**user** | **str** | The file&#39;s owner, specified either as a name or numeric ID. Defaults to \&quot;root\&quot;. | [optional] 
**group** | **str** | The file&#39;s group, specified either as a name or numeric ID. Defaults to \&quot;root\&quot;. | [optional] 

## Example

```python
from flightctl.models.file_metadata import FileMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FileMetadata from a JSON string
file_metadata_instance = FileMetadata.from_json(json)
# print the JSON string representation of the object
print(FileMetadata.to_json())

# convert the object into a dict
file_metadata_dict = file_metadata_instance.to_dict()
# create an instance of FileMetadata from a dict
file_metadata_from_dict = FileMetadata.from_dict(file_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


