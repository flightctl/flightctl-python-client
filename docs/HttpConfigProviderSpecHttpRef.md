# HttpConfigProviderSpecHttpRef

The reference to an HTTP configuration server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | The name of the repository resource to use as the sync source. | 
**suffix** | **str** | Part of the URL that comes after the base URL. It can include query parameters such as: \&quot;/path/to/endpoint?query&#x3D;param\&quot;. | [optional] 
**file_path** | **str** | Path in the device&#39;s file system to which the content returned by the HTTP sever should be written. | 

## Example

```python
from flightctl.models.http_config_provider_spec_http_ref import HttpConfigProviderSpecHttpRef

# TODO update the JSON string below
json = "{}"
# create an instance of HttpConfigProviderSpecHttpRef from a JSON string
http_config_provider_spec_http_ref_instance = HttpConfigProviderSpecHttpRef.from_json(json)
# print the JSON string representation of the object
print(HttpConfigProviderSpecHttpRef.to_json())

# convert the object into a dict
http_config_provider_spec_http_ref_dict = http_config_provider_spec_http_ref_instance.to_dict()
# create an instance of HttpConfigProviderSpecHttpRef from a dict
http_config_provider_spec_http_ref_from_dict = HttpConfigProviderSpecHttpRef.from_dict(http_config_provider_spec_http_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


