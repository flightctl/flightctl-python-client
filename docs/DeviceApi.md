# flightctl.DeviceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device**](DeviceApi.md#create_device) | **POST** /api/v1/devices | 
[**decommission_device**](DeviceApi.md#decommission_device) | **PUT** /api/v1/devices/{name}/decommission | 
[**delete_device**](DeviceApi.md#delete_device) | **DELETE** /api/v1/devices/{name} | 
[**delete_devices**](DeviceApi.md#delete_devices) | **DELETE** /api/v1/devices | 
[**get_rendered_device**](DeviceApi.md#get_rendered_device) | **GET** /api/v1/devices/{name}/rendered | 
[**list_devices**](DeviceApi.md#list_devices) | **GET** /api/v1/devices | 
[**patch_device**](DeviceApi.md#patch_device) | **PATCH** /api/v1/devices/{name} | 
[**patch_device_status**](DeviceApi.md#patch_device_status) | **PATCH** /api/v1/devices/{name}/status | 
[**read_device**](DeviceApi.md#read_device) | **GET** /api/v1/devices/{name} | 
[**read_device_status**](DeviceApi.md#read_device_status) | **GET** /api/v1/devices/{name}/status | 
[**replace_device**](DeviceApi.md#replace_device) | **PUT** /api/v1/devices/{name} | 
[**replace_device_status**](DeviceApi.md#replace_device_status) | **PUT** /api/v1/devices/{name}/status | 


# **create_device**
> Device create_device(device)



Create a Device resource.

### Example


```python
import flightctl
from flightctl.models.device import Device
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
    api_instance = flightctl.DeviceApi(api_client)
    device = flightctl.Device() # Device | 

    try:
        api_response = api_instance.create_device(device)
        print("The response of DeviceApi->create_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->create_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**Device**](Device.md)|  | 

### Return type

[**Device**](Device.md)

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

# **decommission_device**
> Device decommission_device(name, device_decommission)



schedule the device to decommission

### Example


```python
import flightctl
from flightctl.models.device import Device
from flightctl.models.device_decommission import DeviceDecommission
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
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | The name of the Device resource to decommission.
    device_decommission = flightctl.DeviceDecommission() # DeviceDecommission | 

    try:
        api_response = api_instance.decommission_device(name, device_decommission)
        print("The response of DeviceApi->decommission_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->decommission_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Device resource to decommission. | 
 **device_decommission** | [**DeviceDecommission**](DeviceDecommission.md)|  | 

### Return type

[**Device**](Device.md)

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

# **delete_device**
> Device delete_device(name)



Delete a Device resource.

### Example


```python
import flightctl
from flightctl.models.device import Device
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
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | The name of the Device resource to delete.

    try:
        api_response = api_instance.delete_device(name)
        print("The response of DeviceApi->delete_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->delete_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Device resource to delete. | 

### Return type

[**Device**](Device.md)

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

# **delete_devices**
> Status delete_devices()



Delete Device resources.

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
    api_instance = flightctl.DeviceApi(api_client)

    try:
        api_response = api_instance.delete_devices()
        print("The response of DeviceApi->delete_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->delete_devices: %s\n" % e)
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

# **get_rendered_device**
> Device get_rendered_device(name, known_rendered_version=known_rendered_version)



Get the rendered device.

### Example


```python
import flightctl
from flightctl.models.device import Device
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
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | The name of the Device resource to get the rendered device specification for.
    known_rendered_version = 'known_rendered_version_example' # str | The last known renderedVersion. (optional)

    try:
        api_response = api_instance.get_rendered_device(name, known_rendered_version=known_rendered_version)
        print("The response of DeviceApi->get_rendered_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_rendered_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Device resource to get the rendered device specification for. | 
 **known_rendered_version** | **str**| The last known renderedVersion. | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**409** | StatusConflict |  -  |
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_devices**
> DeviceList list_devices(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit, summary_only=summary_only)



List Device resources.

### Example


```python
import flightctl
from flightctl.models.device_list import DeviceList
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
    api_instance = flightctl.DeviceApi(api_client)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the paramter must match the value of the 'continue' field in the previous list response. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supporting operators like '=', '==', and '!=' (e.g., \"key1=value1,key2!=value2\"). (optional)
    limit = 56 # int | The maximum number of results returned in the list response. The server will set the 'continue' field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. (optional)
    summary_only = True # bool | A boolean flag to include only a summary of the devices. When set to true, the response will contain only the summary information. Only the 'owner' and 'labelSelector' parameters are supported when 'summaryOnly' is true. (optional)

    try:
        api_response = api_instance.list_devices(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit, summary_only=summary_only)
        print("The response of DeviceApi->list_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->list_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_continue** | **str**| An optional parameter to query more results from the server. The value of the paramter must match the value of the &#39;continue&#39; field in the previous list response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields, supporting operators like &#39;&#x3D;&#39;, &#39;&#x3D;&#x3D;&#39;, and &#39;!&#x3D;&#39; (e.g., \&quot;key1&#x3D;value1,key2!&#x3D;value2\&quot;). | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. The server will set the &#39;continue&#39; field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. | [optional] 
 **summary_only** | **bool**| A boolean flag to include only a summary of the devices. When set to true, the response will contain only the summary information. Only the &#39;owner&#39; and &#39;labelSelector&#39; parameters are supported when &#39;summaryOnly&#39; is true. | [optional] 

### Return type

[**DeviceList**](DeviceList.md)

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
**403** | Not allowed |  -  |
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device**
> Device patch_device(name, patch_request_inner)



Patch a Device resource.

### Example


```python
import flightctl
from flightctl.models.device import Device
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
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | The name of the Device resource to patch.
    patch_request_inner = [flightctl.PatchRequestInner()] # List[PatchRequestInner] | 

    try:
        api_response = api_instance.patch_device(name, patch_request_inner)
        print("The response of DeviceApi->patch_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->patch_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Device resource to patch. | 
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  | 

### Return type

[**Device**](Device.md)

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
**409** | StatusConflict |  -  |
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_status**
> Device patch_device_status(name, patch_request_inner)



Patch the status of a Device resource.

### Example


```python
import flightctl
from flightctl.models.device import Device
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
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | The name of the Device resource to patch.
    patch_request_inner = [flightctl.PatchRequestInner()] # List[PatchRequestInner] | 

    try:
        api_response = api_instance.patch_device_status(name, patch_request_inner)
        print("The response of DeviceApi->patch_device_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->patch_device_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Device resource to patch. | 
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  | 

### Return type

[**Device**](Device.md)

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
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_device**
> Device read_device(name)



Get a Device resource.

### Example


```python
import flightctl
from flightctl.models.device import Device
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
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | The name of the Device resource to get.

    try:
        api_response = api_instance.read_device(name)
        print("The response of DeviceApi->read_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->read_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Device resource to get. | 

### Return type

[**Device**](Device.md)

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

# **read_device_status**
> Device read_device_status(name)



Get the status of a Device resource.

### Example


```python
import flightctl
from flightctl.models.device import Device
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
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | The name of the Device resource to get.

    try:
        api_response = api_instance.read_device_status(name)
        print("The response of DeviceApi->read_device_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->read_device_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Device resource to get. | 

### Return type

[**Device**](Device.md)

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

# **replace_device**
> Device replace_device(name, device)



Update a Device resource.

### Example


```python
import flightctl
from flightctl.models.device import Device
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
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | The name of the Device resource to update.
    device = flightctl.Device() # Device | 

    try:
        api_response = api_instance.replace_device(name, device)
        print("The response of DeviceApi->replace_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->replace_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Device resource to update. | 
 **device** | [**Device**](Device.md)|  | 

### Return type

[**Device**](Device.md)

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

# **replace_device_status**
> Device replace_device_status(name, device)



Update the status of a Device resource.

### Example


```python
import flightctl
from flightctl.models.device import Device
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
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | The name of the Device resource to update.
    device = flightctl.Device() # Device | 

    try:
        api_response = api_instance.replace_device_status(name, device)
        print("The response of DeviceApi->replace_device_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->replace_device_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Device resource to update. | 
 **device** | [**Device**](Device.md)|  | 

### Return type

[**Device**](Device.md)

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

