# CheckRepositoryOciTagRequest

Request to check if a specific image tag exists in an OCI registry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_name** | **str** | The image name/path within the registry (e.g. \&quot;centos-bootc/centos-bootc\&quot;). Combined with the registry host from the Repository resource, this forms the full repository reference (e.g. \&quot;quay.io/centos-bootc/centos-bootc\&quot;). | 
**tag** | **str** | The image tag to check for existence (e.g. \&quot;9.5\&quot;). | 

## Example

```python
from flightctl.models.check_repository_oci_tag_request import CheckRepositoryOciTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckRepositoryOciTagRequest from a JSON string
check_repository_oci_tag_request_instance = CheckRepositoryOciTagRequest.from_json(json)
# print the JSON string representation of the object
print(CheckRepositoryOciTagRequest.to_json())

# convert the object into a dict
check_repository_oci_tag_request_dict = check_repository_oci_tag_request_instance.to_dict()
# create an instance of CheckRepositoryOciTagRequest from a dict
check_repository_oci_tag_request_from_dict = CheckRepositoryOciTagRequest.from_dict(check_repository_oci_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


