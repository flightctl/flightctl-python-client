# Rfc7662IntrospectionSpec

Rfc7662IntrospectionSpec defines token introspection using RFC 7662 standard. Uses the OAuth2ProviderSpec clientId and clientSecret for authentication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The introspection type. | 
**url** | **str** | The RFC 7662 token introspection endpoint URL. | 

## Example

```python
from flightctl.models.rfc7662_introspection_spec import Rfc7662IntrospectionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of Rfc7662IntrospectionSpec from a JSON string
rfc7662_introspection_spec_instance = Rfc7662IntrospectionSpec.from_json(json)
# print the JSON string representation of the object
print(Rfc7662IntrospectionSpec.to_json())

# convert the object into a dict
rfc7662_introspection_spec_dict = rfc7662_introspection_spec_instance.to_dict()
# create an instance of Rfc7662IntrospectionSpec from a dict
rfc7662_introspection_spec_from_dict = Rfc7662IntrospectionSpec.from_dict(rfc7662_introspection_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


