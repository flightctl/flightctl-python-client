# DockerAuth

Docker-style authentication for OCI registries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | [**OciAuthType**](OciAuthType.md) |  | 
**username** | **str** | The username for registry authentication. | 
**password** | **str** | The password or token for registry authentication. | 

## Example

```python
from flightctl.models.docker_auth import DockerAuth

# TODO update the JSON string below
json = "{}"
# create an instance of DockerAuth from a JSON string
docker_auth_instance = DockerAuth.from_json(json)
# print the JSON string representation of the object
print(DockerAuth.to_json())

# convert the object into a dict
docker_auth_dict = docker_auth_instance.to_dict()
# create an instance of DockerAuth from a dict
docker_auth_from_dict = DockerAuth.from_dict(docker_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


