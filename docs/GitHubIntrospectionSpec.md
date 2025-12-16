# GitHubIntrospectionSpec

GitHubIntrospectionSpec defines token introspection using GitHub API (POST /applications/{client_id}/token). Uses the OAuth2ProviderSpec clientId and clientSecret for Basic Auth and URL path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The introspection type. | 
**url** | **str** | The GitHub API base URL. Defaults to https://api.github.com for GitHub.com, but can be customized for GitHub Enterprise Server. | [optional] [default to 'https://api.github.com']

## Example

```python
from flightctl.models.git_hub_introspection_spec import GitHubIntrospectionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubIntrospectionSpec from a JSON string
git_hub_introspection_spec_instance = GitHubIntrospectionSpec.from_json(json)
# print the JSON string representation of the object
print(GitHubIntrospectionSpec.to_json())

# convert the object into a dict
git_hub_introspection_spec_dict = git_hub_introspection_spec_instance.to_dict()
# create an instance of GitHubIntrospectionSpec from a dict
git_hub_introspection_spec_from_dict = GitHubIntrospectionSpec.from_dict(git_hub_introspection_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


