# ApplicationUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_as** | **str** | The username of the system user this application should be run under. This is not the same as the user within any containers of the application (if applicable). Defaults to the user that the agent runs as (generally root) if not specified. | [optional] 

## Example

```python
from flightctl.models.application_user import ApplicationUser

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationUser from a JSON string
application_user_instance = ApplicationUser.from_json(json)
# print the JSON string representation of the object
print(ApplicationUser.to_json())

# convert the object into a dict
application_user_dict = application_user_instance.to_dict()
# create an instance of ApplicationUser from a dict
application_user_from_dict = ApplicationUser.from_dict(application_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


