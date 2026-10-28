# flightctl.EnrollmenthookpolicyApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_enrollment_hook_policy**](EnrollmenthookpolicyApi.md#create_enrollment_hook_policy) | **POST** /enrollmenthookpolicies |
[**delete_enrollment_hook_policy**](EnrollmenthookpolicyApi.md#delete_enrollment_hook_policy) | **DELETE** /enrollmenthookpolicies/{name} |
[**get_enrollment_hook_policy**](EnrollmenthookpolicyApi.md#get_enrollment_hook_policy) | **GET** /enrollmenthookpolicies/{name} |
[**list_enrollment_hook_policies**](EnrollmenthookpolicyApi.md#list_enrollment_hook_policies) | **GET** /enrollmenthookpolicies |
[**patch_enrollment_hook_policy**](EnrollmenthookpolicyApi.md#patch_enrollment_hook_policy) | **PATCH** /enrollmenthookpolicies/{name} |
[**replace_enrollment_hook_policy**](EnrollmenthookpolicyApi.md#replace_enrollment_hook_policy) | **PUT** /enrollmenthookpolicies/{name} |


# **create_enrollment_hook_policy**
> EnrollmentHookPolicy create_enrollment_hook_policy(enrollment_hook_policy)

Create an EnrollmentHookPolicy resource.

### Example


```python
import flightctl
from flightctl.models.enrollment_hook_policy import EnrollmentHookPolicy
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.EnrollmenthookpolicyApi(api_client)
    enrollment_hook_policy = flightctl.EnrollmentHookPolicy() # EnrollmentHookPolicy |

    try:
        api_response = api_instance.create_enrollment_hook_policy(enrollment_hook_policy)
        print("The response of EnrollmenthookpolicyApi->create_enrollment_hook_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmenthookpolicyApi->create_enrollment_hook_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_hook_policy** | [**EnrollmentHookPolicy**](EnrollmentHookPolicy.md)|  |

### Return type

[**EnrollmentHookPolicy**](EnrollmentHookPolicy.md)

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
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_enrollment_hook_policy**
> Status delete_enrollment_hook_policy(name)

Delete an EnrollmentHookPolicy resource.

### Example


```python
import flightctl
from flightctl.models.status import Status
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.EnrollmenthookpolicyApi(api_client)
    name = 'name_example' # str | The name of the EnrollmentHookPolicy resource to delete.

    try:
        api_response = api_instance.delete_enrollment_hook_policy(name)
        print("The response of EnrollmenthookpolicyApi->delete_enrollment_hook_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmenthookpolicyApi->delete_enrollment_hook_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the EnrollmentHookPolicy resource to delete. |

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enrollment_hook_policy**
> EnrollmentHookPolicy get_enrollment_hook_policy(name)

Get an EnrollmentHookPolicy resource.

### Example


```python
import flightctl
from flightctl.models.enrollment_hook_policy import EnrollmentHookPolicy
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.EnrollmenthookpolicyApi(api_client)
    name = 'name_example' # str | The name of the EnrollmentHookPolicy resource to get.

    try:
        api_response = api_instance.get_enrollment_hook_policy(name)
        print("The response of EnrollmenthookpolicyApi->get_enrollment_hook_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmenthookpolicyApi->get_enrollment_hook_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the EnrollmentHookPolicy resource to get. |

### Return type

[**EnrollmentHookPolicy**](EnrollmentHookPolicy.md)

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
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_enrollment_hook_policies**
> EnrollmentHookPolicyList list_enrollment_hook_policies(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)

List EnrollmentHookPolicy resources.

### Example


```python
import flightctl
from flightctl.models.enrollment_hook_policy_list import EnrollmentHookPolicyList
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.EnrollmenthookpolicyApi(api_client)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the paramter must match the value of the 'continue' field in the previous list response. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supporting operators like '=', '==', and '!=' (e.g., \"key1=value1,key2!=value2\"). (optional)
    limit = 56 # int | The maximum number of results returned in the list response. The server will set the 'continue' field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. (optional)

    try:
        api_response = api_instance.list_enrollment_hook_policies(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)
        print("The response of EnrollmenthookpolicyApi->list_enrollment_hook_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmenthookpolicyApi->list_enrollment_hook_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_continue** | **str**| An optional parameter to query more results from the server. The value of the paramter must match the value of the &#39;continue&#39; field in the previous list response. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional]
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields, supporting operators like &#39;&#x3D;&#39;, &#39;&#x3D;&#x3D;&#39;, and &#39;!&#x3D;&#39; (e.g., \&quot;key1&#x3D;value1,key2!&#x3D;value2\&quot;). | [optional]
 **limit** | **int**| The maximum number of results returned in the list response. The server will set the &#39;continue&#39; field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. | [optional]

### Return type

[**EnrollmentHookPolicyList**](EnrollmentHookPolicyList.md)

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
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_enrollment_hook_policy**
> EnrollmentHookPolicy patch_enrollment_hook_policy(name, patch_request_inner)

Patch an EnrollmentHookPolicy resource.

### Example


```python
import flightctl
from flightctl.models.enrollment_hook_policy import EnrollmentHookPolicy
from flightctl.models.patch_request_inner import PatchRequestInner
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.EnrollmenthookpolicyApi(api_client)
    name = 'name_example' # str | The name of the EnrollmentHookPolicy resource to patch.
    patch_request_inner = [flightctl.PatchRequestInner()] # List[PatchRequestInner] |

    try:
        api_response = api_instance.patch_enrollment_hook_policy(name, patch_request_inner)
        print("The response of EnrollmenthookpolicyApi->patch_enrollment_hook_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmenthookpolicyApi->patch_enrollment_hook_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the EnrollmentHookPolicy resource to patch. |
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  |

### Return type

[**EnrollmentHookPolicy**](EnrollmentHookPolicy.md)

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_enrollment_hook_policy**
> EnrollmentHookPolicy replace_enrollment_hook_policy(name, enrollment_hook_policy)

Update an EnrollmentHookPolicy resource.

### Example


```python
import flightctl
from flightctl.models.enrollment_hook_policy import EnrollmentHookPolicy
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.EnrollmenthookpolicyApi(api_client)
    name = 'name_example' # str | The name of the EnrollmentHookPolicy resource to update.
    enrollment_hook_policy = flightctl.EnrollmentHookPolicy() # EnrollmentHookPolicy |

    try:
        api_response = api_instance.replace_enrollment_hook_policy(name, enrollment_hook_policy)
        print("The response of EnrollmenthookpolicyApi->replace_enrollment_hook_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmenthookpolicyApi->replace_enrollment_hook_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the EnrollmentHookPolicy resource to update. |
 **enrollment_hook_policy** | [**EnrollmentHookPolicy**](EnrollmentHookPolicy.md)|  |

### Return type

[**EnrollmentHookPolicy**](EnrollmentHookPolicy.md)

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
