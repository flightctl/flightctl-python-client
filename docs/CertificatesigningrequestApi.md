# flightctl.CertificatesigningrequestApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_certificate_signing_request**](CertificatesigningrequestApi.md#create_certificate_signing_request) | **POST** /api/v1/certificatesigningrequests | 
[**delete_certificate_signing_request**](CertificatesigningrequestApi.md#delete_certificate_signing_request) | **DELETE** /api/v1/certificatesigningrequests/{name} | 
[**get_certificate_signing_request**](CertificatesigningrequestApi.md#get_certificate_signing_request) | **GET** /api/v1/certificatesigningrequests/{name} | 
[**list_certificate_signing_requests**](CertificatesigningrequestApi.md#list_certificate_signing_requests) | **GET** /api/v1/certificatesigningrequests | 
[**patch_certificate_signing_request**](CertificatesigningrequestApi.md#patch_certificate_signing_request) | **PATCH** /api/v1/certificatesigningrequests/{name} | 
[**replace_certificate_signing_request**](CertificatesigningrequestApi.md#replace_certificate_signing_request) | **PUT** /api/v1/certificatesigningrequests/{name} | 
[**update_certificate_signing_request_approval**](CertificatesigningrequestApi.md#update_certificate_signing_request_approval) | **PUT** /api/v1/certificatesigningrequests/{name}/approval | 


# **create_certificate_signing_request**
> CertificateSigningRequest create_certificate_signing_request(certificate_signing_request)



Create a CertificateSigningRequest resource.

### Example


```python
import flightctl
from flightctl.models.certificate_signing_request import CertificateSigningRequest
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.CertificatesigningrequestApi(api_client)
    certificate_signing_request = flightctl.CertificateSigningRequest() # CertificateSigningRequest | 

    try:
        api_response = api_instance.create_certificate_signing_request(certificate_signing_request)
        print("The response of CertificatesigningrequestApi->create_certificate_signing_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesigningrequestApi->create_certificate_signing_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_signing_request** | [**CertificateSigningRequest**](CertificateSigningRequest.md)|  | 

### Return type

[**CertificateSigningRequest**](CertificateSigningRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | StatusConflict |  -  |
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_certificate_signing_request**
> Status delete_certificate_signing_request(name)



delete a Certificate Signing Request

### Example


```python
import flightctl
from flightctl.models.status import Status
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.CertificatesigningrequestApi(api_client)
    name = 'name_example' # str | The name of the CertificateSigningRequest resource to delete.

    try:
        api_response = api_instance.delete_certificate_signing_request(name)
        print("The response of CertificatesigningrequestApi->delete_certificate_signing_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesigningrequestApi->delete_certificate_signing_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the CertificateSigningRequest resource to delete. | 

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_signing_request**
> CertificateSigningRequest get_certificate_signing_request(name)



read the specified certificateSigningRequest

### Example


```python
import flightctl
from flightctl.models.certificate_signing_request import CertificateSigningRequest
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.CertificatesigningrequestApi(api_client)
    name = 'name_example' # str | The name of the CertificateSigningRequest resource to get.

    try:
        api_response = api_instance.get_certificate_signing_request(name)
        print("The response of CertificatesigningrequestApi->get_certificate_signing_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesigningrequestApi->get_certificate_signing_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the CertificateSigningRequest resource to get. | 

### Return type

[**CertificateSigningRequest**](CertificateSigningRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_certificate_signing_requests**
> CertificateSigningRequestList list_certificate_signing_requests(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)



List CertificateSigningRequest resources.

### Example


```python
import flightctl
from flightctl.models.certificate_signing_request_list import CertificateSigningRequestList
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.CertificatesigningrequestApi(api_client)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the paramter must match the value of the 'continue' field in the previous list response. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supporting operators like '=', '==', and '!=' (e.g., \"key1=value1,key2!=value2\"). (optional)
    limit = 56 # int | The maximum number of results returned in the list response. The server will set the 'continue' field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. (optional)

    try:
        api_response = api_instance.list_certificate_signing_requests(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)
        print("The response of CertificatesigningrequestApi->list_certificate_signing_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesigningrequestApi->list_certificate_signing_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_continue** | **str**| An optional parameter to query more results from the server. The value of the paramter must match the value of the &#39;continue&#39; field in the previous list response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields, supporting operators like &#39;&#x3D;&#39;, &#39;&#x3D;&#x3D;&#39;, and &#39;!&#x3D;&#39; (e.g., \&quot;key1&#x3D;value1,key2!&#x3D;value2\&quot;). | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. The server will set the &#39;continue&#39; field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. | [optional] 

### Return type

[**CertificateSigningRequestList**](CertificateSigningRequestList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_certificate_signing_request**
> CertificateSigningRequest patch_certificate_signing_request(name, patch_request_inner)



Patch a CertificateSigningRequest resource.

### Example


```python
import flightctl
from flightctl.models.certificate_signing_request import CertificateSigningRequest
from flightctl.models.patch_request_inner import PatchRequestInner
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.CertificatesigningrequestApi(api_client)
    name = 'name_example' # str | The name of the CertificateSigningRequest resource to patch.
    patch_request_inner = [flightctl.PatchRequestInner()] # List[PatchRequestInner] | 

    try:
        api_response = api_instance.patch_certificate_signing_request(name, patch_request_inner)
        print("The response of CertificatesigningrequestApi->patch_certificate_signing_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesigningrequestApi->patch_certificate_signing_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the CertificateSigningRequest resource to patch. | 
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  | 

### Return type

[**CertificateSigningRequest**](CertificateSigningRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | NotFound |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_certificate_signing_request**
> CertificateSigningRequest replace_certificate_signing_request(name, certificate_signing_request)



replace the specified CertificateSigningRequest

### Example


```python
import flightctl
from flightctl.models.certificate_signing_request import CertificateSigningRequest
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.CertificatesigningrequestApi(api_client)
    name = 'name_example' # str | The name of the CertificateSigningRequest resource to update.
    certificate_signing_request = flightctl.CertificateSigningRequest() # CertificateSigningRequest | 

    try:
        api_response = api_instance.replace_certificate_signing_request(name, certificate_signing_request)
        print("The response of CertificatesigningrequestApi->replace_certificate_signing_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesigningrequestApi->replace_certificate_signing_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the CertificateSigningRequest resource to update. | 
 **certificate_signing_request** | [**CertificateSigningRequest**](CertificateSigningRequest.md)|  | 

### Return type

[**CertificateSigningRequest**](CertificateSigningRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**409** | Conflict |  -  |
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificate_signing_request_approval**
> CertificateSigningRequest update_certificate_signing_request_approval(name, certificate_signing_request)



Approve or deny a CertificateSigningRequest.

### Example


```python
import flightctl
from flightctl.models.certificate_signing_request import CertificateSigningRequest
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.CertificatesigningrequestApi(api_client)
    name = 'name_example' # str | The name of the CertificateSigningRequest to approve or deny.
    certificate_signing_request = flightctl.CertificateSigningRequest() # CertificateSigningRequest | 

    try:
        api_response = api_instance.update_certificate_signing_request_approval(name, certificate_signing_request)
        print("The response of CertificatesigningrequestApi->update_certificate_signing_request_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesigningrequestApi->update_certificate_signing_request_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the CertificateSigningRequest to approve or deny. | 
 **certificate_signing_request** | [**CertificateSigningRequest**](CertificateSigningRequest.md)|  | 

### Return type

[**CertificateSigningRequest**](CertificateSigningRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**409** | StatusConflict |  -  |
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

