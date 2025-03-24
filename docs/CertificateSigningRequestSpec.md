# CertificateSigningRequestSpec

Wrapper around a user-created CSR, modeled on kubernetes io.k8s.api.certificates.v1.CertificateSigningRequestSpec.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration_seconds** | **int** | Requested duration of validity for the certificate. | [optional] 
**extra** | **Dict[str, List[str]]** | Extra attributes of the user that created the CSR, populated by the API server on creation and immutable. | [optional] 
**request** | **bytearray** | The base64-encoded PEM-encoded PKCS#10 CSR. Matches the spec.request field in a kubernetes CertificateSigningRequest resource. | 
**signer_name** | **str** | Indicates the requested signer, and is a qualified name. | 
**uid** | **str** | UID of the user that created the CSR, populated by the API server on creation and immutable. | [optional] 
**usages** | **List[str]** | Usages specifies a set of key usages requested in the issued certificate. | [optional] 
**username** | **str** | Name of the user that created the CSR, populated by the API server on creation and immutable. | [optional] 

## Example

```python
from flightctl.models.certificate_signing_request_spec import CertificateSigningRequestSpec

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateSigningRequestSpec from a JSON string
certificate_signing_request_spec_instance = CertificateSigningRequestSpec.from_json(json)
# print the JSON string representation of the object
print(CertificateSigningRequestSpec.to_json())

# convert the object into a dict
certificate_signing_request_spec_dict = certificate_signing_request_spec_instance.to_dict()
# create an instance of CertificateSigningRequestSpec from a dict
certificate_signing_request_spec_from_dict = CertificateSigningRequestSpec.from_dict(certificate_signing_request_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


