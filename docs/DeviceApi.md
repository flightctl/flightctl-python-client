# flightctl.DeviceApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device**](DeviceApi.md#create_device) | **POST** /devices | 
[**decommission_device**](DeviceApi.md#decommission_device) | **PUT** /devices/{name}/decommission | 
[**delete_device**](DeviceApi.md#delete_device) | **DELETE** /devices/{name} | 
[**get_device**](DeviceApi.md#get_device) | **GET** /devices/{name} | 
[**get_device_application_console**](DeviceApi.md#get_device_application_console) | **GET** /ws/v1/devices/{name}/applications/{appname}/console | 
[**get_device_console**](DeviceApi.md#get_device_console) | **GET** /ws/v1/devices/{name}/console | 
[**get_device_last_seen**](DeviceApi.md#get_device_last_seen) | **GET** /devices/{name}/lastseen | 
[**get_device_status**](DeviceApi.md#get_device_status) | **GET** /devices/{name}/status | 
[**get_rendered_device**](DeviceApi.md#get_rendered_device) | **GET** /devices/{name}/rendered | 
[**list_devices**](DeviceApi.md#list_devices) | **GET** /devices | 
[**patch_device**](DeviceApi.md#patch_device) | **PATCH** /devices/{name} | 
[**patch_device_status**](DeviceApi.md#patch_device_status) | **PATCH** /devices/{name}/status | 
[**replace_device**](DeviceApi.md#replace_device) | **PUT** /devices/{name} | 
[**replace_device_status**](DeviceApi.md#replace_device_status) | **PUT** /devices/{name}/status | 
[**restart_device_application**](DeviceApi.md#restart_device_application) | **POST** /devices/{name}/applications/{appname}/actions/restart | 
[**start_device_application**](DeviceApi.md#start_device_application) | **POST** /devices/{name}/applications/{appname}/actions/start | 
[**stop_device_application**](DeviceApi.md#stop_device_application) | **POST** /devices/{name}/applications/{appname}/actions/stop | 


# **create_device**
> Device create_device(device)

Create a Device resource.

### Example


```python
import flightctl
from flightctl.models.device import Device
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
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

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

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "/api/v1"
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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> Status delete_device(name)

Delete a Device resource.

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

# **get_device**
> Device get_device(name)

Get a Device resource.

### Example


```python
import flightctl
from flightctl.models.device import Device
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
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | The name of the Device resource to get.

    try:
        api_response = api_instance.get_device(name)
        print("The response of DeviceApi->get_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device: %s\n" % e)
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_application_console**
> get_device_application_console(name, appname, console_type, force=force)

Open a WebSocket console session to an application running on the Device.

### Example


```python
import flightctl
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
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | The name of the Device resource.
    appname = 'appname_example' # str | The name of the application to connect to.
    console_type = 'console_type_example' # str | The type of console session to open. \"serial\" opens a text terminal; \"vnc\" opens a VNC proxy tunnel.
    force = False # bool | If true, take over an already-active console session of the same type for this application instead of failing with a 409 Conflict. The replaced session is disconnected and told why. (optional) (default to False)

    try:
        api_instance.get_device_application_console(name, appname, console_type, force=force)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_application_console: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Device resource. | 
 **appname** | **str**| The name of the application to connect to. | 
 **console_type** | **str**| The type of console session to open. \&quot;serial\&quot; opens a text terminal; \&quot;vnc\&quot; opens a VNC proxy tunnel. | 
 **force** | **bool**| If true, take over an already-active console session of the same type for this application instead of failing with a 409 Conflict. The replaced session is disconnected and told why. | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**101** | Switching Protocols |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_console**
> get_device_console(name)

Open a WebSocket console session to the Device.

### Example


```python
import flightctl
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
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | The name of the Device resource.

    try:
        api_instance.get_device_console(name)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_console: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Device resource. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**101** | Switching Protocols |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_last_seen**
> DeviceLastSeen get_device_last_seen(name)

Get the last seen timestamp of the Device resource.

### Example


```python
import flightctl
from flightctl.models.device_last_seen import DeviceLastSeen
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
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | The name of the Device resource to get the last seen timestamp for.

    try:
        api_response = api_instance.get_device_last_seen(name)
        print("The response of DeviceApi->get_device_last_seen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_last_seen: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Device resource to get the last seen timestamp for. | 

### Return type

[**DeviceLastSeen**](DeviceLastSeen.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_status**
> Device get_device_status(name)

Get the status of a Device resource.

### Example


```python
import flightctl
from flightctl.models.device import Device
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
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | The name of the Device resource to get.

    try:
        api_response = api_instance.get_device_status(name)
        print("The response of DeviceApi->get_device_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_status: %s\n" % e)
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

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

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "/api/v1"
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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_devices**
> DeviceList list_devices(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit, summary_only=summary_only, cve_id=cve_id)

List Device resources.

### Example


```python
import flightctl
from flightctl.models.device_list import DeviceList
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
    api_instance = flightctl.DeviceApi(api_client)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the paramter must match the value of the 'continue' field in the previous list response. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supporting operators like '=', '==', and '!=' (e.g., \"key1=value1,key2!=value2\"). (optional)
    limit = 56 # int | The maximum number of results returned in the list response. The server will set the 'continue' field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. (optional)
    summary_only = True # bool | A boolean flag to include only a summary of the devices. When set to true, the response will contain only the summary information. Only the 'owner' and 'labelSelector' parameters are supported when 'summaryOnly' is true. (optional)
    cve_id = 'cve_id_example' # str | Filter devices by CVE ID. Only returns devices whose OS image digest has the specified vulnerability. Must be a MITRE-style identifier (CVE-YYYY-sequence, e.g. CVE-2024-12345). (optional)

    try:
        api_response = api_instance.list_devices(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit, summary_only=summary_only, cve_id=cve_id)
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
 **cve_id** | **str**| Filter devices by CVE ID. Only returns devices whose OS image digest has the specified vulnerability. Must be a MITRE-style identifier (CVE-YYYY-sequence, e.g. CVE-2024-12345). | [optional] 

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
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

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

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "/api/v1"
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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

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

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "/api/v1"
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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

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

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "/api/v1"
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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

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

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "/api/v1"
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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_device_application**
> Device restart_device_application(name, appname)

Restart an application on this device. Sets a device-level restartGeneration override (independent of the application's declarative spec, fleet template or standalone device); the control plane computes the next generation, and the agent restarts the application using the type-appropriate restart operation when it observes the change. The override is applied on top of the rendered application spec at render time and survives fleet template rollouts, since it is never stored as part of the device's spec. Only meaningful while the application's desired state is "running".


### Example


```python
import flightctl
from flightctl.models.device import Device
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
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | The name of the Device resource.
    appname = 'appname_example' # str | The name of the application, as defined in the device's rendered application spec.

    try:
        api_response = api_instance.restart_device_application(name, appname)
        print("The response of DeviceApi->restart_device_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->restart_device_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Device resource. | 
 **appname** | **str**| The name of the application, as defined in the device&#39;s rendered application spec. | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_device_application**
> Device start_device_application(name, appname)

Start an application on this device. Sets a device-level lifecycle override (independent of the application's declarative spec, fleet template or standalone device) that is applied on top of the rendered application spec at render time and survives fleet template rollouts, since it is never stored as part of the device's spec. If the application is also owned by a fleet with its own stop/start default for this application, whichever of the two actions was issued most recently takes effect.


### Example


```python
import flightctl
from flightctl.models.device import Device
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
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | The name of the Device resource.
    appname = 'appname_example' # str | The name of the application, as defined in the device's rendered application spec.

    try:
        api_response = api_instance.start_device_application(name, appname)
        print("The response of DeviceApi->start_device_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->start_device_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Device resource. | 
 **appname** | **str**| The name of the application, as defined in the device&#39;s rendered application spec. | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_device_application**
> Device stop_device_application(name, appname)

Stop an application on this device. Sets a device-level lifecycle override (independent of the application's declarative spec, fleet template or standalone device) that is applied on top of the rendered application spec at render time and survives fleet template rollouts, since it is never stored as part of the device's spec.


### Example


```python
import flightctl
from flightctl.models.device import Device
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
    api_instance = flightctl.DeviceApi(api_client)
    name = 'name_example' # str | The name of the Device resource.
    appname = 'appname_example' # str | The name of the application, as defined in the device's rendered application spec.

    try:
        api_response = api_instance.stop_device_application(name, appname)
        print("The response of DeviceApi->stop_device_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->stop_device_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Device resource. | 
 **appname** | **str**| The name of the application, as defined in the device&#39;s rendered application spec. | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

