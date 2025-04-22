# flightctl.ResourcesyncApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_sync**](ResourcesyncApi.md#create_resource_sync) | **POST** /api/v1/resourcesyncs | 
[**delete_resource_sync**](ResourcesyncApi.md#delete_resource_sync) | **DELETE** /api/v1/resourcesyncs/{name} | 
[**delete_resource_syncs**](ResourcesyncApi.md#delete_resource_syncs) | **DELETE** /api/v1/resourcesyncs | 
[**get_resource_sync**](ResourcesyncApi.md#get_resource_sync) | **GET** /api/v1/resourcesyncs/{name} | 
[**list_resource_syncs**](ResourcesyncApi.md#list_resource_syncs) | **GET** /api/v1/resourcesyncs | 
[**patch_resource_sync**](ResourcesyncApi.md#patch_resource_sync) | **PATCH** /api/v1/resourcesyncs/{name} | 
[**replace_resource_sync**](ResourcesyncApi.md#replace_resource_sync) | **PUT** /api/v1/resourcesyncs/{name} | 


# **create_resource_sync**
> ResourceSync create_resource_sync(resource_sync)



Create a ResourceSync resource.

### Example


```python
import flightctl
from flightctl.models.resource_sync import ResourceSync
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
    api_instance = flightctl.ResourcesyncApi(api_client)
    resource_sync = flightctl.ResourceSync() # ResourceSync | 

    try:
        api_response = api_instance.create_resource_sync(resource_sync)
        print("The response of ResourcesyncApi->create_resource_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesyncApi->create_resource_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_sync** | [**ResourceSync**](ResourceSync.md)|  | 

### Return type

[**ResourceSync**](ResourceSync.md)

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

# **delete_resource_sync**
> Status delete_resource_sync(name)



Delete a ResourceSync resource.

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
    api_instance = flightctl.ResourcesyncApi(api_client)
    name = 'name_example' # str | The name of the ResourceSync resource to delete.

    try:
        api_response = api_instance.delete_resource_sync(name)
        print("The response of ResourcesyncApi->delete_resource_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesyncApi->delete_resource_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the ResourceSync resource to delete. | 

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

# **delete_resource_syncs**
> Status delete_resource_syncs()



Delete ResourceSync resources.

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
    api_instance = flightctl.ResourcesyncApi(api_client)

    try:
        api_response = api_instance.delete_resource_syncs()
        print("The response of ResourcesyncApi->delete_resource_syncs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesyncApi->delete_resource_syncs: %s\n" % e)
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

# **get_resource_sync**
> ResourceSync get_resource_sync(name)



Get a ResourceSync resource.

### Example


```python
import flightctl
from flightctl.models.resource_sync import ResourceSync
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
    api_instance = flightctl.ResourcesyncApi(api_client)
    name = 'name_example' # str | The name of the ResourceSync resource to get.

    try:
        api_response = api_instance.get_resource_sync(name)
        print("The response of ResourcesyncApi->get_resource_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesyncApi->get_resource_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the ResourceSync resource to get. | 

### Return type

[**ResourceSync**](ResourceSync.md)

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

# **list_resource_syncs**
> ResourceSyncList list_resource_syncs(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)



List ResourceSync resources.

### Example


```python
import flightctl
from flightctl.models.resource_sync_list import ResourceSyncList
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
    api_instance = flightctl.ResourcesyncApi(api_client)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the paramter must match the value of the 'continue' field in the previous list response. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supporting operators like '=', '==', and '!=' (e.g., \"key1=value1,key2!=value2\"). (optional)
    limit = 56 # int | The maximum number of results returned in the list response. The server will set the 'continue' field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. (optional)

    try:
        api_response = api_instance.list_resource_syncs(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)
        print("The response of ResourcesyncApi->list_resource_syncs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesyncApi->list_resource_syncs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_continue** | **str**| An optional parameter to query more results from the server. The value of the paramter must match the value of the &#39;continue&#39; field in the previous list response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields, supporting operators like &#39;&#x3D;&#39;, &#39;&#x3D;&#x3D;&#39;, and &#39;!&#x3D;&#39; (e.g., \&quot;key1&#x3D;value1,key2!&#x3D;value2\&quot;). | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. The server will set the &#39;continue&#39; field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. | [optional] 

### Return type

[**ResourceSyncList**](ResourceSyncList.md)

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

# **patch_resource_sync**
> ResourceSync patch_resource_sync(name, patch_request_inner)



Patch a ResourceSync resource.

### Example


```python
import flightctl
from flightctl.models.patch_request_inner import PatchRequestInner
from flightctl.models.resource_sync import ResourceSync
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
    api_instance = flightctl.ResourcesyncApi(api_client)
    name = 'name_example' # str | The name of the ResourceSync resource to patch.
    patch_request_inner = [flightctl.PatchRequestInner()] # List[PatchRequestInner] | 

    try:
        api_response = api_instance.patch_resource_sync(name, patch_request_inner)
        print("The response of ResourcesyncApi->patch_resource_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesyncApi->patch_resource_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the ResourceSync resource to patch. | 
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  | 

### Return type

[**ResourceSync**](ResourceSync.md)

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

# **replace_resource_sync**
> ResourceSync replace_resource_sync(name, resource_sync)



Update a ResourceSync resource.

### Example


```python
import flightctl
from flightctl.models.resource_sync import ResourceSync
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
    api_instance = flightctl.ResourcesyncApi(api_client)
    name = 'name_example' # str | The name of the ResourceSync resource to update.
    resource_sync = flightctl.ResourceSync() # ResourceSync | 

    try:
        api_response = api_instance.replace_resource_sync(name, resource_sync)
        print("The response of ResourcesyncApi->replace_resource_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesyncApi->replace_resource_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the ResourceSync resource to update. | 
 **resource_sync** | [**ResourceSync**](ResourceSync.md)|  | 

### Return type

[**ResourceSync**](ResourceSync.md)

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

