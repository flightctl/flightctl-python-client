# flightctl.AuthproviderApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auth_provider**](AuthproviderApi.md#create_auth_provider) | **POST** /api/v1/authproviders | 
[**delete_auth_provider**](AuthproviderApi.md#delete_auth_provider) | **DELETE** /api/v1/authproviders/{name} | 
[**get_auth_provider**](AuthproviderApi.md#get_auth_provider) | **GET** /api/v1/authproviders/{name} | 
[**list_auth_providers**](AuthproviderApi.md#list_auth_providers) | **GET** /api/v1/authproviders | 
[**patch_auth_provider**](AuthproviderApi.md#patch_auth_provider) | **PATCH** /api/v1/authproviders/{name} | 
[**replace_auth_provider**](AuthproviderApi.md#replace_auth_provider) | **PUT** /api/v1/authproviders/{name} | 


# **create_auth_provider**
> AuthProvider create_auth_provider(auth_provider)

Create an AuthProvider resource.

### Example


```python
import flightctl
from flightctl.models.auth_provider import AuthProvider
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
    api_instance = flightctl.AuthproviderApi(api_client)
    auth_provider = flightctl.AuthProvider() # AuthProvider | 

    try:
        api_response = api_instance.create_auth_provider(auth_provider)
        print("The response of AuthproviderApi->create_auth_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthproviderApi->create_auth_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_provider** | [**AuthProvider**](AuthProvider.md)|  | 

### Return type

[**AuthProvider**](AuthProvider.md)

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

# **delete_auth_provider**
> Status delete_auth_provider(name)

Delete an AuthProvider resource.

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
    api_instance = flightctl.AuthproviderApi(api_client)
    name = 'name_example' # str | The name of the AuthProvider resource to delete.

    try:
        api_response = api_instance.delete_auth_provider(name)
        print("The response of AuthproviderApi->delete_auth_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthproviderApi->delete_auth_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the AuthProvider resource to delete. | 

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_provider**
> AuthProvider get_auth_provider(name)

Get an AuthProvider resource.

### Example


```python
import flightctl
from flightctl.models.auth_provider import AuthProvider
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
    api_instance = flightctl.AuthproviderApi(api_client)
    name = 'name_example' # str | The name of the AuthProvider resource to get.

    try:
        api_response = api_instance.get_auth_provider(name)
        print("The response of AuthproviderApi->get_auth_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthproviderApi->get_auth_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the AuthProvider resource to get. | 

### Return type

[**AuthProvider**](AuthProvider.md)

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auth_providers**
> AuthProviderList list_auth_providers(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)

List AuthProvider resources.

### Example


```python
import flightctl
from flightctl.models.auth_provider_list import AuthProviderList
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
    api_instance = flightctl.AuthproviderApi(api_client)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the paramter must match the value of the 'continue' field in the previous list response. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supporting operators like '=', '==', and '!=' (e.g., \"key1=value1,key2!=value2\"). (optional)
    limit = 56 # int | The maximum number of results returned in the list response. The server will set the 'continue' field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. (optional)

    try:
        api_response = api_instance.list_auth_providers(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)
        print("The response of AuthproviderApi->list_auth_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthproviderApi->list_auth_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_continue** | **str**| An optional parameter to query more results from the server. The value of the paramter must match the value of the &#39;continue&#39; field in the previous list response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields, supporting operators like &#39;&#x3D;&#39;, &#39;&#x3D;&#x3D;&#39;, and &#39;!&#x3D;&#39; (e.g., \&quot;key1&#x3D;value1,key2!&#x3D;value2\&quot;). | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. The server will set the &#39;continue&#39; field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. | [optional] 

### Return type

[**AuthProviderList**](AuthProviderList.md)

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

# **patch_auth_provider**
> AuthProvider patch_auth_provider(name, patch_request_inner)

Patch an AuthProvider resource.

### Example


```python
import flightctl
from flightctl.models.auth_provider import AuthProvider
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
    api_instance = flightctl.AuthproviderApi(api_client)
    name = 'name_example' # str | The name of the AuthProvider resource to patch.
    patch_request_inner = [flightctl.PatchRequestInner()] # List[PatchRequestInner] | 

    try:
        api_response = api_instance.patch_auth_provider(name, patch_request_inner)
        print("The response of AuthproviderApi->patch_auth_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthproviderApi->patch_auth_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the AuthProvider resource to patch. | 
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  | 

### Return type

[**AuthProvider**](AuthProvider.md)

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

# **replace_auth_provider**
> AuthProvider replace_auth_provider(name, auth_provider)

Update an AuthProvider resource.

### Example


```python
import flightctl
from flightctl.models.auth_provider import AuthProvider
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
    api_instance = flightctl.AuthproviderApi(api_client)
    name = 'name_example' # str | The name of the AuthProvider resource to update.
    auth_provider = flightctl.AuthProvider() # AuthProvider | 

    try:
        api_response = api_instance.replace_auth_provider(name, auth_provider)
        print("The response of AuthproviderApi->replace_auth_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthproviderApi->replace_auth_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the AuthProvider resource to update. | 
 **auth_provider** | [**AuthProvider**](AuthProvider.md)|  | 

### Return type

[**AuthProvider**](AuthProvider.md)

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

