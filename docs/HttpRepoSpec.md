# HttpRepoSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The HTTP URL to call or clone from. | 
**type** | [**RepoSpecType**](RepoSpecType.md) |  | 
**http_config** | [**HttpConfig**](HttpConfig.md) |  | 
**validation_suffix** | **str** | URL suffix used only for validating access to the repository. Users might use the URL field as a root URL to be used by config sources adding suffixes. This will help with the validation of the http endpoint. | [optional] 

## Example

```python
from flightctl.models.http_repo_spec import HttpRepoSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HttpRepoSpec from a JSON string
http_repo_spec_instance = HttpRepoSpec.from_json(json)
# print the JSON string representation of the object
print(HttpRepoSpec.to_json())

# convert the object into a dict
http_repo_spec_dict = http_repo_spec_instance.to_dict()
# create an instance of HttpRepoSpec from a dict
http_repo_spec_from_dict = HttpRepoSpec.from_dict(http_repo_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


