# flightctl.imagebuilder.ImagebuildApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_image_build**](ImagebuildApi.md#cancel_image_build) | **POST** /api/v1/imagebuilds/{name}/cancel | 
[**create_image_build**](ImagebuildApi.md#create_image_build) | **POST** /api/v1/imagebuilds | 
[**delete_image_build**](ImagebuildApi.md#delete_image_build) | **DELETE** /api/v1/imagebuilds/{name} | 
[**get_image_build**](ImagebuildApi.md#get_image_build) | **GET** /api/v1/imagebuilds/{name} | 
[**get_image_build_log**](ImagebuildApi.md#get_image_build_log) | **GET** /api/v1/imagebuilds/{name}/log | 
[**list_image_builds**](ImagebuildApi.md#list_image_builds) | **GET** /api/v1/imagebuilds | 


# **cancel_image_build**
> ImageBuild cancel_image_build(name)

Cancel a running ImageBuild. Only builds in Pending, Building, or Pushing state can be canceled.

### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.models.image_build import ImageBuild
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
    api_instance = flightctl.imagebuilder.ImagebuildApi(api_client)
    name = 'name_example' # str | The name of the ImageBuild resource to cancel.

    try:
        api_response = api_instance.cancel_image_build(name)
        print("The response of ImagebuildApi->cancel_image_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagebuildApi->cancel_image_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the ImageBuild resource to cancel. | 

### Return type

[**ImageBuild**](ImageBuild.md)

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
**409** | Conflict - Build not in cancelable state |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_build**
> ImageBuild create_image_build(image_build)

Create an ImageBuild resource.

### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.models.image_build import ImageBuild
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
    api_instance = flightctl.imagebuilder.ImagebuildApi(api_client)
    image_build = flightctl.imagebuilder.ImageBuild() # ImageBuild | 

    try:
        api_response = api_instance.create_image_build(image_build)
        print("The response of ImagebuildApi->create_image_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagebuildApi->create_image_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_build** | [**ImageBuild**](ImageBuild.md)|  | 

### Return type

[**ImageBuild**](ImageBuild.md)

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

# **delete_image_build**
> ImageBuild delete_image_build(name)

Delete an ImageBuild resource.

### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.models.image_build import ImageBuild
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
    api_instance = flightctl.imagebuilder.ImagebuildApi(api_client)
    name = 'name_example' # str | The name of the ImageBuild resource.

    try:
        api_response = api_instance.delete_image_build(name)
        print("The response of ImagebuildApi->delete_image_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagebuildApi->delete_image_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the ImageBuild resource. | 

### Return type

[**ImageBuild**](ImageBuild.md)

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

# **get_image_build**
> ImageBuild get_image_build(name, with_exports=with_exports)

Get an ImageBuild resource.

### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.models.image_build import ImageBuild
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
    api_instance = flightctl.imagebuilder.ImagebuildApi(api_client)
    name = 'name_example' # str | The name of the ImageBuild resource.
    with_exports = False # bool | If true, includes related ImageExport resources in the response. (optional) (default to False)

    try:
        api_response = api_instance.get_image_build(name, with_exports=with_exports)
        print("The response of ImagebuildApi->get_image_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagebuildApi->get_image_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the ImageBuild resource. | 
 **with_exports** | **bool**| If true, includes related ImageExport resources in the response. | [optional] [default to False]

### Return type

[**ImageBuild**](ImageBuild.md)

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

# **get_image_build_log**
> str get_image_build_log(name, follow=follow)

Get logs for an ImageBuild resource. For active builds, streams logs live. For completed builds, returns last 500 lines.

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
    api_instance = flightctl.imagebuilder.ImagebuildApi(api_client)
    name = 'name_example' # str | The name of the ImageBuild resource.
    follow = False # bool | If true, stream logs continuously (like kubectl logs -f). For active builds, keeps connection open. For completed builds, returns all logs and closes. (optional) (default to False)

    try:
        api_response = api_instance.get_image_build_log(name, follow=follow)
        print("The response of ImagebuildApi->get_image_build_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagebuildApi->get_image_build_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the ImageBuild resource. | 
 **follow** | **bool**| If true, stream logs continuously (like kubectl logs -f). For active builds, keeps connection open. For completed builds, returns all logs and closes. | [optional] [default to False]

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

# **list_image_builds**
> ImageBuildList list_image_builds(label_selector=label_selector, field_selector=field_selector, limit=limit, var_continue=var_continue, with_exports=with_exports)

List ImageBuild resources.

### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.models.image_build_list import ImageBuildList
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
    api_instance = flightctl.imagebuilder.ImagebuildApi(api_client)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. (optional)
    limit = 56 # int | The maximum number of results returned in the list response. (optional)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. (optional)
    with_exports = False # bool | If true, includes related ImageExport resources in each ImageBuild in the response. (optional) (default to False)

    try:
        api_response = api_instance.list_image_builds(label_selector=label_selector, field_selector=field_selector, limit=limit, var_continue=var_continue, with_exports=with_exports)
        print("The response of ImagebuildApi->list_image_builds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagebuildApi->list_image_builds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. | [optional] 
 **var_continue** | **str**| An optional parameter to query more results from the server. | [optional] 
 **with_exports** | **bool**| If true, includes related ImageExport resources in each ImageBuild in the response. | [optional] [default to False]

### Return type

[**ImageBuildList**](ImageBuildList.md)

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

