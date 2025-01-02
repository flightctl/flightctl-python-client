# CertificateSigningRequestStatus

Indicates approval/denial/failure status of the CSR, and contains the issued certifiate if any exists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **bytearray** | The issued signed certificate, immutable once populated. | [optional] 
**conditions** | [**List[Condition]**](Condition.md) | Conditions applied to the request. Known conditions are Approved, Denied, and Failed. | 

## Example

```python
from flightctl.models.certificate_signing_request_status import CertificateSigningRequestStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateSigningRequestStatus from a JSON string
certificate_signing_request_status_instance = CertificateSigningRequestStatus.from_json(json)
# print the JSON string representation of the object
print(CertificateSigningRequestStatus.to_json())

# convert the object into a dict
certificate_signing_request_status_dict = certificate_signing_request_status_instance.to_dict()
# create an instance of CertificateSigningRequestStatus from a dict
certificate_signing_request_status_from_dict = CertificateSigningRequestStatus.from_dict(certificate_signing_request_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


