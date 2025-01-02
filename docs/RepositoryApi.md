# flightctl.RepositoryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_repository**](RepositoryApi.md#create_repository) | **POST** /api/v1/repositories | 
[**delete_repositories**](RepositoryApi.md#delete_repositories) | **DELETE** /api/v1/repositories | 
[**delete_repository**](RepositoryApi.md#delete_repository) | **DELETE** /api/v1/repositories/{name} | 
[**list_repositories**](RepositoryApi.md#list_repositories) | **GET** /api/v1/repositories | 
[**patch_repository**](RepositoryApi.md#patch_repository) | **PATCH** /api/v1/repositories/{name} | 
[**read_repository**](RepositoryApi.md#read_repository) | **GET** /api/v1/repositories/{name} | 
[**replace_repository**](RepositoryApi.md#replace_repository) | **PUT** /api/v1/repositories/{name} | 


# **create_repository**
> Repository create_repository(repository)



Create a Repository resource.

### Example


```python
import flightctl
from flightctl.models.repository import Repository
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
    api_instance = flightctl.RepositoryApi(api_client)
    repository = flightctl.Repository() # Repository | 

    try:
        api_response = api_instance.create_repository(repository)
        print("The response of RepositoryApi->create_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->create_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | [**Repository**](Repository.md)|  | 

### Return type

[**Repository**](Repository.md)

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

# **delete_repositories**
> Status delete_repositories()



Delete Repository resources.

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
    api_instance = flightctl.RepositoryApi(api_client)

    try:
        api_response = api_instance.delete_repositories()
        print("The response of RepositoryApi->delete_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->delete_repositories: %s\n" % e)
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

# **delete_repository**
> Repository delete_repository(name)



Delete a Repository resource.

### Example


```python
import flightctl
from flightctl.models.repository import Repository
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
    api_instance = flightctl.RepositoryApi(api_client)
    name = 'name_example' # str | The name of the Repository resource to delete.

    try:
        api_response = api_instance.delete_repository(name)
        print("The response of RepositoryApi->delete_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->delete_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Repository resource to delete. | 

### Return type

[**Repository**](Repository.md)

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

# **list_repositories**
> RepositoryList list_repositories(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)



List Repository resources.

### Example


```python
import flightctl
from flightctl.models.repository_list import RepositoryList
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
    api_instance = flightctl.RepositoryApi(api_client)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the paramter must match the value of the 'continue' field in the previous list response. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supporting operators like '=', '==', and '!=' (e.g., \"key1=value1,key2!=value2\"). (optional)
    limit = 56 # int | The maximum number of results returned in the list response. The server will set the 'continue' field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. (optional)

    try:
        api_response = api_instance.list_repositories(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)
        print("The response of RepositoryApi->list_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->list_repositories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_continue** | **str**| An optional parameter to query more results from the server. The value of the paramter must match the value of the &#39;continue&#39; field in the previous list response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields, supporting operators like &#39;&#x3D;&#39;, &#39;&#x3D;&#x3D;&#39;, and &#39;!&#x3D;&#39; (e.g., \&quot;key1&#x3D;value1,key2!&#x3D;value2\&quot;). | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. The server will set the &#39;continue&#39; field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. | [optional] 

### Return type

[**RepositoryList**](RepositoryList.md)

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

# **patch_repository**
> Repository patch_repository(name, patch_request_inner=patch_request_inner)



Patch a Repository resource.

### Example


```python
import flightctl
from flightctl.models.patch_request_inner import PatchRequestInner
from flightctl.models.repository import Repository
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
    api_instance = flightctl.RepositoryApi(api_client)
    name = 'name_example' # str | The name of the Repository resource to patch.
    patch_request_inner = [flightctl.PatchRequestInner()] # List[PatchRequestInner] |  (optional)

    try:
        api_response = api_instance.patch_repository(name, patch_request_inner=patch_request_inner)
        print("The response of RepositoryApi->patch_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->patch_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Repository resource to patch. | 
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  | [optional] 

### Return type

[**Repository**](Repository.md)

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

# **read_repository**
> Repository read_repository(name)



Get a Repository resource.

### Example


```python
import flightctl
from flightctl.models.repository import Repository
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
    api_instance = flightctl.RepositoryApi(api_client)
    name = 'name_example' # str | The name of the Repository resource to get.

    try:
        api_response = api_instance.read_repository(name)
        print("The response of RepositoryApi->read_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->read_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Repository resource to get. | 

### Return type

[**Repository**](Repository.md)

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

# **replace_repository**
> Repository replace_repository(name, repository)



Update a Repository resource.

### Example


```python
import flightctl
from flightctl.models.repository import Repository
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
    api_instance = flightctl.RepositoryApi(api_client)
    name = 'name_example' # str | The name of the Repository resource to update.
    repository = flightctl.Repository() # Repository | 

    try:
        api_response = api_instance.replace_repository(name, repository)
        print("The response of RepositoryApi->replace_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->replace_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Repository resource to update. | 
 **repository** | [**Repository**](Repository.md)|  | 

### Return type

[**Repository**](Repository.md)

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

