# flightctl.imagebuilder.ImageexportApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_image_export**](ImageexportApi.md#cancel_image_export) | **POST** /api/v1/imageexports/{name}/cancel | 
[**create_image_export**](ImageexportApi.md#create_image_export) | **POST** /api/v1/imageexports | 
[**delete_image_export**](ImageexportApi.md#delete_image_export) | **DELETE** /api/v1/imageexports/{name} | 
[**download_image_export**](ImageexportApi.md#download_image_export) | **GET** /api/v1/imageexports/{name}/download | 
[**get_image_export**](ImageexportApi.md#get_image_export) | **GET** /api/v1/imageexports/{name} | 
[**get_image_export_log**](ImageexportApi.md#get_image_export_log) | **GET** /api/v1/imageexports/{name}/log | 
[**list_image_exports**](ImageexportApi.md#list_image_exports) | **GET** /api/v1/imageexports | 


# **cancel_image_export**
> ImageExport cancel_image_export(name)

Cancel a running ImageExport. Only exports in Pending, Converting, or Pushing state can be canceled.

### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.models.image_export import ImageExport
from flightctl.imagebuilder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.imagebuilder.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.imagebuilder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.imagebuilder.ImageexportApi(api_client)
    name = 'name_example' # str | The name of the ImageExport resource to cancel.

    try:
        api_response = api_instance.cancel_image_export(name)
        print("The response of ImageexportApi->cancel_image_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageexportApi->cancel_image_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the ImageExport resource to cancel. | 

### Return type

[**ImageExport**](ImageExport.md)

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
**409** | Conflict - Export not in cancelable state |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_export**
> ImageExport create_image_export(image_export)

Create an ImageExport resource.

### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.models.image_export import ImageExport
from flightctl.imagebuilder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.imagebuilder.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.imagebuilder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.imagebuilder.ImageexportApi(api_client)
    image_export = flightctl.imagebuilder.ImageExport() # ImageExport | 

    try:
        api_response = api_instance.create_image_export(image_export)
        print("The response of ImageexportApi->create_image_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageexportApi->create_image_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_export** | [**ImageExport**](ImageExport.md)|  | 

### Return type

[**ImageExport**](ImageExport.md)

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

# **delete_image_export**
> ImageExport delete_image_export(name)

Delete an ImageExport resource.

### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.models.image_export import ImageExport
from flightctl.imagebuilder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.imagebuilder.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.imagebuilder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.imagebuilder.ImageexportApi(api_client)
    name = 'name_example' # str | The name of the ImageExport resource.

    try:
        api_response = api_instance.delete_image_export(name)
        print("The response of ImageexportApi->delete_image_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageexportApi->delete_image_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the ImageExport resource. | 

### Return type

[**ImageExport**](ImageExport.md)

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

# **download_image_export**
> bytearray download_image_export(name)

Download an ImageExport artifact from the registry.

### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.imagebuilder.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.imagebuilder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.imagebuilder.ImageexportApi(api_client)
    name = 'name_example' # str | The name of the ImageExport resource.

    try:
        api_response = api_instance.download_image_export(name)
        print("The response of ImageexportApi->download_image_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageexportApi->download_image_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the ImageExport resource. | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Artifact blob content |  -  |
**302** | Found - Redirect to registry blob URL |  * Location -  <br>  |
**307** | Temporary Redirect - Redirect to registry blob URL |  * Location -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_export**
> ImageExport get_image_export(name)

Get an ImageExport resource.

### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.models.image_export import ImageExport
from flightctl.imagebuilder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.imagebuilder.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.imagebuilder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.imagebuilder.ImageexportApi(api_client)
    name = 'name_example' # str | The name of the ImageExport resource.

    try:
        api_response = api_instance.get_image_export(name)
        print("The response of ImageexportApi->get_image_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageexportApi->get_image_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the ImageExport resource. | 

### Return type

[**ImageExport**](ImageExport.md)

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

# **get_image_export_log**
> str get_image_export_log(name, follow=follow)

Get logs for an ImageExport resource. For active exports, streams logs live. For completed exports, returns last 500 lines.

### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.imagebuilder.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.imagebuilder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.imagebuilder.ImageexportApi(api_client)
    name = 'name_example' # str | The name of the ImageExport resource.
    follow = False # bool | If true, stream logs continuously (like kubectl logs -f). For active exports, keeps connection open. For completed exports, returns all logs and closes. (optional) (default to False)

    try:
        api_response = api_instance.get_image_export_log(name, follow=follow)
        print("The response of ImageexportApi->get_image_export_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageexportApi->get_image_export_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the ImageExport resource. | 
 **follow** | **bool**| If true, stream logs continuously (like kubectl logs -f). For active exports, keeps connection open. For completed exports, returns all logs and closes. | [optional] [default to False]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, text/event-stream, application/json

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

# **list_image_exports**
> ImageExportList list_image_exports(label_selector=label_selector, field_selector=field_selector, limit=limit, var_continue=var_continue)

List ImageExport resources.

### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.models.image_export_list import ImageExportList
from flightctl.imagebuilder.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.imagebuilder.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with flightctl.imagebuilder.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.imagebuilder.ImageexportApi(api_client)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. (optional)
    limit = 56 # int | The maximum number of results returned in the list response. (optional)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. (optional)

    try:
        api_response = api_instance.list_image_exports(label_selector=label_selector, field_selector=field_selector, limit=limit, var_continue=var_continue)
        print("The response of ImageexportApi->list_image_exports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImageexportApi->list_image_exports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. | [optional] 
 **var_continue** | **str**| An optional parameter to query more results from the server. | [optional] 

### Return type

[**ImageExportList**](ImageExportList.md)

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

