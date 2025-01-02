# ApplicationEnvVars


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env_vars** | **Dict[str, str]** | Environment variable key-value pairs, injected during runtime. | [optional] 

## Example

```python
from flightctl.models.application_env_vars import ApplicationEnvVars

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationEnvVars from a JSON string
application_env_vars_instance = ApplicationEnvVars.from_json(json)
# print the JSON string representation of the object
print(ApplicationEnvVars.to_json())

# convert the object into a dict
application_env_vars_dict = application_env_vars_instance.to_dict()
# create an instance of ApplicationEnvVars from a dict
application_env_vars_from_dict = ApplicationEnvVars.from_dict(application_env_vars_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


