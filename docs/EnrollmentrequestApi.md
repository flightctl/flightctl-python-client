# flightctl.EnrollmentrequestApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_enrollment_request**](EnrollmentrequestApi.md#approve_enrollment_request) | **PUT** /api/v1/enrollmentrequests/{name}/approval | 
[**create_enrollment_request**](EnrollmentrequestApi.md#create_enrollment_request) | **POST** /api/v1/enrollmentrequests | 
[**delete_enrollment_request**](EnrollmentrequestApi.md#delete_enrollment_request) | **DELETE** /api/v1/enrollmentrequests/{name} | 
[**delete_enrollment_requests**](EnrollmentrequestApi.md#delete_enrollment_requests) | **DELETE** /api/v1/enrollmentrequests | 
[**get_enrollment_config**](EnrollmentrequestApi.md#get_enrollment_config) | **GET** /api/v1/enrollmentconfig | 
[**get_enrollment_request**](EnrollmentrequestApi.md#get_enrollment_request) | **GET** /api/v1/enrollmentrequests/{name} | 
[**get_enrollment_request_status**](EnrollmentrequestApi.md#get_enrollment_request_status) | **GET** /api/v1/enrollmentrequests/{name}/status | 
[**list_enrollment_requests**](EnrollmentrequestApi.md#list_enrollment_requests) | **GET** /api/v1/enrollmentrequests | 
[**patch_enrollment_request**](EnrollmentrequestApi.md#patch_enrollment_request) | **PATCH** /api/v1/enrollmentrequests/{name} | 
[**patch_enrollment_request_status**](EnrollmentrequestApi.md#patch_enrollment_request_status) | **PATCH** /api/v1/enrollmentrequests/{name}/status | 
[**replace_enrollment_request**](EnrollmentrequestApi.md#replace_enrollment_request) | **PUT** /api/v1/enrollmentrequests/{name} | 
[**replace_enrollment_request_status**](EnrollmentrequestApi.md#replace_enrollment_request_status) | **PUT** /api/v1/enrollmentrequests/{name}/status | 


# **approve_enrollment_request**
> EnrollmentRequestApprovalStatus approve_enrollment_request(name, enrollment_request_approval)



Approve or deny an EnrollmentRequest.

### Example


```python
import flightctl
from flightctl.models.enrollment_request_approval import EnrollmentRequestApproval
from flightctl.models.enrollment_request_approval_status import EnrollmentRequestApprovalStatus
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    name = 'name_example' # str | The name of the EnrollmentRequest to approve or deny.
    enrollment_request_approval = flightctl.EnrollmentRequestApproval() # EnrollmentRequestApproval | 

    try:
        api_response = api_instance.approve_enrollment_request(name, enrollment_request_approval)
        print("The response of EnrollmentrequestApi->approve_enrollment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->approve_enrollment_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the EnrollmentRequest to approve or deny. | 
 **enrollment_request_approval** | [**EnrollmentRequestApproval**](EnrollmentRequestApproval.md)|  | 

### Return type

[**EnrollmentRequestApprovalStatus**](EnrollmentRequestApprovalStatus.md)

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
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_enrollment_request**
> EnrollmentRequest create_enrollment_request(enrollment_request)



Create an EnrollmentRequest resource.

### Example


```python
import flightctl
from flightctl.models.enrollment_request import EnrollmentRequest
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    enrollment_request = flightctl.EnrollmentRequest() # EnrollmentRequest | 

    try:
        api_response = api_instance.create_enrollment_request(enrollment_request)
        print("The response of EnrollmentrequestApi->create_enrollment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->create_enrollment_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_request** | [**EnrollmentRequest**](EnrollmentRequest.md)|  | 

### Return type

[**EnrollmentRequest**](EnrollmentRequest.md)

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

# **delete_enrollment_request**
> Status delete_enrollment_request(name)



Delete an EnrollmentRequest resource.

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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    name = 'name_example' # str | The name of the EnrollmentRequest resource to delete.

    try:
        api_response = api_instance.delete_enrollment_request(name)
        print("The response of EnrollmentrequestApi->delete_enrollment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->delete_enrollment_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the EnrollmentRequest resource to delete. | 

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

# **delete_enrollment_requests**
> Status delete_enrollment_requests()



Delete EnrollmentRequest resources.

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
    api_instance = flightctl.EnrollmentrequestApi(api_client)

    try:
        api_response = api_instance.delete_enrollment_requests()
        print("The response of EnrollmentrequestApi->delete_enrollment_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->delete_enrollment_requests: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enrollment_config**
> EnrollmentConfig get_enrollment_config(csr=csr)



Get enrollment information.

### Example


```python
import flightctl
from flightctl.models.enrollment_config import EnrollmentConfig
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    csr = 'csr_example' # str | The name of a CertificateSigningRequest resource to query for an issued certificate. If provided, the service will check if the CertificateSigningRequest contains an issued certificate and in this case include it the returned EnrollmentConfig. In all other case, the enrollment certificate field will be empty. (optional)

    try:
        api_response = api_instance.get_enrollment_config(csr=csr)
        print("The response of EnrollmentrequestApi->get_enrollment_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->get_enrollment_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csr** | **str**| The name of a CertificateSigningRequest resource to query for an issued certificate. If provided, the service will check if the CertificateSigningRequest contains an issued certificate and in this case include it the returned EnrollmentConfig. In all other case, the enrollment certificate field will be empty. | [optional] 

### Return type

[**EnrollmentConfig**](EnrollmentConfig.md)

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
**404** | Not Found |  -  |
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enrollment_request**
> EnrollmentRequest get_enrollment_request(name)



Get an EnrollmentRequest resource.

### Example


```python
import flightctl
from flightctl.models.enrollment_request import EnrollmentRequest
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    name = 'name_example' # str | The name of the EnrollmentRequest resource to get.

    try:
        api_response = api_instance.get_enrollment_request(name)
        print("The response of EnrollmentrequestApi->get_enrollment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->get_enrollment_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the EnrollmentRequest resource to get. | 

### Return type

[**EnrollmentRequest**](EnrollmentRequest.md)

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

# **get_enrollment_request_status**
> EnrollmentRequest get_enrollment_request_status(name)



Get the status of an EnrollmentRequest resource.

### Example


```python
import flightctl
from flightctl.models.enrollment_request import EnrollmentRequest
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    name = 'name_example' # str | The name of the EnrollmentRequest resource to get.

    try:
        api_response = api_instance.get_enrollment_request_status(name)
        print("The response of EnrollmentrequestApi->get_enrollment_request_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->get_enrollment_request_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the EnrollmentRequest resource to get. | 

### Return type

[**EnrollmentRequest**](EnrollmentRequest.md)

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

# **list_enrollment_requests**
> EnrollmentRequestList list_enrollment_requests(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)



List EnrollmentRequest resources.

### Example


```python
import flightctl
from flightctl.models.enrollment_request_list import EnrollmentRequestList
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the paramter must match the value of the 'continue' field in the previous list response. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supporting operators like '=', '==', and '!=' (e.g., \"key1=value1,key2!=value2\"). (optional)
    limit = 56 # int | The maximum number of results returned in the list response. The server will set the 'continue' field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. (optional)

    try:
        api_response = api_instance.list_enrollment_requests(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)
        print("The response of EnrollmentrequestApi->list_enrollment_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->list_enrollment_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_continue** | **str**| An optional parameter to query more results from the server. The value of the paramter must match the value of the &#39;continue&#39; field in the previous list response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields, supporting operators like &#39;&#x3D;&#39;, &#39;&#x3D;&#x3D;&#39;, and &#39;!&#x3D;&#39; (e.g., \&quot;key1&#x3D;value1,key2!&#x3D;value2\&quot;). | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. The server will set the &#39;continue&#39; field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. | [optional] 

### Return type

[**EnrollmentRequestList**](EnrollmentRequestList.md)

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

# **patch_enrollment_request**
> EnrollmentRequest patch_enrollment_request(name, patch_request_inner)



Patch an EnrollmentRequest resource.

### Example


```python
import flightctl
from flightctl.models.enrollment_request import EnrollmentRequest
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    name = 'name_example' # str | The name of the EnrollmentRequest resource to patch.
    patch_request_inner = [flightctl.PatchRequestInner()] # List[PatchRequestInner] | 

    try:
        api_response = api_instance.patch_enrollment_request(name, patch_request_inner)
        print("The response of EnrollmentrequestApi->patch_enrollment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->patch_enrollment_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the EnrollmentRequest resource to patch. | 
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  | 

### Return type

[**EnrollmentRequest**](EnrollmentRequest.md)

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
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**409** | Conflict |  -  |
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_enrollment_request_status**
> EnrollmentRequest patch_enrollment_request_status(name, patch_request_inner)



Patch the status of an EnrollmentRequest resource.

### Example


```python
import flightctl
from flightctl.models.enrollment_request import EnrollmentRequest
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    name = 'name_example' # str | The name of the EnrollmentRequest resource to patch.
    patch_request_inner = [flightctl.PatchRequestInner()] # List[PatchRequestInner] | 

    try:
        api_response = api_instance.patch_enrollment_request_status(name, patch_request_inner)
        print("The response of EnrollmentrequestApi->patch_enrollment_request_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->patch_enrollment_request_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the EnrollmentRequest resource to patch. | 
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  | 

### Return type

[**EnrollmentRequest**](EnrollmentRequest.md)

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
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**409** | Conflict |  -  |
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_enrollment_request**
> EnrollmentRequest replace_enrollment_request(name, enrollment_request)



Update an EnrollmentRequest resource.

### Example


```python
import flightctl
from flightctl.models.enrollment_request import EnrollmentRequest
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    name = 'name_example' # str | The name of the EnrollmentRequest resource to update.
    enrollment_request = flightctl.EnrollmentRequest() # EnrollmentRequest | 

    try:
        api_response = api_instance.replace_enrollment_request(name, enrollment_request)
        print("The response of EnrollmentrequestApi->replace_enrollment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->replace_enrollment_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the EnrollmentRequest resource to update. | 
 **enrollment_request** | [**EnrollmentRequest**](EnrollmentRequest.md)|  | 

### Return type

[**EnrollmentRequest**](EnrollmentRequest.md)

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
**409** | StatusConflict |  -  |
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_enrollment_request_status**
> EnrollmentRequest replace_enrollment_request_status(name, enrollment_request)



Update the status of an EnrollmentRequest resource.

### Example


```python
import flightctl
from flightctl.models.enrollment_request import EnrollmentRequest
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
    api_instance = flightctl.EnrollmentrequestApi(api_client)
    name = 'name_example' # str | The name of the EnrollmentRequest resource to update.
    enrollment_request = flightctl.EnrollmentRequest() # EnrollmentRequest | 

    try:
        api_response = api_instance.replace_enrollment_request_status(name, enrollment_request)
        print("The response of EnrollmentrequestApi->replace_enrollment_request_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentrequestApi->replace_enrollment_request_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the EnrollmentRequest resource to update. | 
 **enrollment_request** | [**EnrollmentRequest**](EnrollmentRequest.md)|  | 

### Return type

[**EnrollmentRequest**](EnrollmentRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

