# CheckRepositoryOciImageRequest

Request to check if a specific OCI image is accessible in a registry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_name** | **str** | The image name/path within the registry (e.g. \&quot;centos-bootc/centos-bootc\&quot;). Combined with the registry host from the Repository resource, this forms the full image reference (e.g. \&quot;quay.io/centos-bootc/centos-bootc\&quot;). | 

## Example

```python
from flightctl.models.check_repository_oci_image_request import CheckRepositoryOciImageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckRepositoryOciImageRequest from a JSON string
check_repository_oci_image_request_instance = CheckRepositoryOciImageRequest.from_json(json)
# print the JSON string representation of the object
print(CheckRepositoryOciImageRequest.to_json())

# convert the object into a dict
check_repository_oci_image_request_dict = check_repository_oci_image_request_instance.to_dict()
# create an instance of CheckRepositoryOciImageRequest from a dict
check_repository_oci_image_request_from_dict = CheckRepositoryOciImageRequest.from_dict(check_repository_oci_image_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


