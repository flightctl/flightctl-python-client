# CertificateSigningRequestList

CertificateSigningRequestList is a list of CertificateSigningRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. | 
**metadata** | [**ListMeta**](ListMeta.md) |  | 
**items** | [**List[CertificateSigningRequest]**](CertificateSigningRequest.md) | List of CertificateSigningRequest. | 

## Example

```python
from flightctl.models.certificate_signing_request_list import CertificateSigningRequestList

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateSigningRequestList from a JSON string
certificate_signing_request_list_instance = CertificateSigningRequestList.from_json(json)
# print the JSON string representation of the object
print(CertificateSigningRequestList.to_json())

# convert the object into a dict
certificate_signing_request_list_dict = certificate_signing_request_list_instance.to_dict()
# create an instance of CertificateSigningRequestList from a dict
certificate_signing_request_list_from_dict = CertificateSigningRequestList.from_dict(certificate_signing_request_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


