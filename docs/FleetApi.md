# flightctl.FleetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fleet**](FleetApi.md#create_fleet) | **POST** /api/v1/fleets | 
[**delete_fleet**](FleetApi.md#delete_fleet) | **DELETE** /api/v1/fleets/{name} | 
[**delete_fleets**](FleetApi.md#delete_fleets) | **DELETE** /api/v1/fleets | 
[**delete_template_version**](FleetApi.md#delete_template_version) | **DELETE** /api/v1/fleets/{fleet}/templateversions/{name} | 
[**delete_template_versions**](FleetApi.md#delete_template_versions) | **DELETE** /api/v1/fleets/{fleet}/templateversions | 
[**list_fleets**](FleetApi.md#list_fleets) | **GET** /api/v1/fleets | 
[**list_template_versions**](FleetApi.md#list_template_versions) | **GET** /api/v1/fleets/{fleet}/templateversions | 
[**patch_fleet**](FleetApi.md#patch_fleet) | **PATCH** /api/v1/fleets/{name} | 
[**patch_fleet_status**](FleetApi.md#patch_fleet_status) | **PATCH** /api/v1/fleets/{name}/status | 
[**read_fleet**](FleetApi.md#read_fleet) | **GET** /api/v1/fleets/{name} | 
[**read_fleet_status**](FleetApi.md#read_fleet_status) | **GET** /api/v1/fleets/{name}/status | 
[**read_template_version**](FleetApi.md#read_template_version) | **GET** /api/v1/fleets/{fleet}/templateversions/{name} | 
[**replace_fleet**](FleetApi.md#replace_fleet) | **PUT** /api/v1/fleets/{name} | 
[**replace_fleet_status**](FleetApi.md#replace_fleet_status) | **PUT** /api/v1/fleets/{name}/status | 


# **create_fleet**
> Fleet create_fleet(fleet)



Create a Fleet resource.

### Example


```python
import flightctl
from flightctl.models.fleet import Fleet
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
    api_instance = flightctl.FleetApi(api_client)
    fleet = flightctl.Fleet() # Fleet | 

    try:
        api_response = api_instance.create_fleet(fleet)
        print("The response of FleetApi->create_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->create_fleet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet** | [**Fleet**](Fleet.md)|  | 

### Return type

[**Fleet**](Fleet.md)

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

# **delete_fleet**
> Fleet delete_fleet(name)



Delete a Fleet resource.

### Example


```python
import flightctl
from flightctl.models.fleet import Fleet
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
    api_instance = flightctl.FleetApi(api_client)
    name = 'name_example' # str | The name of the Fleet resource to delete.

    try:
        api_response = api_instance.delete_fleet(name)
        print("The response of FleetApi->delete_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->delete_fleet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Fleet resource to delete. | 

### Return type

[**Fleet**](Fleet.md)

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

# **delete_fleets**
> Status delete_fleets()



Delete Fleet resources.

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
    api_instance = flightctl.FleetApi(api_client)

    try:
        api_response = api_instance.delete_fleets()
        print("The response of FleetApi->delete_fleets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->delete_fleets: %s\n" % e)
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

# **delete_template_version**
> TemplateVersion delete_template_version(fleet, name)



delete a template version

### Example


```python
import flightctl
from flightctl.models.template_version import TemplateVersion
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
    api_instance = flightctl.FleetApi(api_client)
    fleet = 'fleet_example' # str | The owner of the template version.
    name = 'name_example' # str | The name of the template version.

    try:
        api_response = api_instance.delete_template_version(fleet, name)
        print("The response of FleetApi->delete_template_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->delete_template_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet** | **str**| The owner of the template version. | 
 **name** | **str**| The name of the template version. | 

### Return type

[**TemplateVersion**](TemplateVersion.md)

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

# **delete_template_versions**
> Status delete_template_versions(fleet)



delete a collection of template versions

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
    api_instance = flightctl.FleetApi(api_client)
    fleet = 'fleet_example' # str | The owner of the template versions.

    try:
        api_response = api_instance.delete_template_versions(fleet)
        print("The response of FleetApi->delete_template_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->delete_template_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet** | **str**| The owner of the template versions. | 

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

# **list_fleets**
> FleetList list_fleets(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit, add_devices_summary=add_devices_summary)



List Fleet resources.

### Example


```python
import flightctl
from flightctl.models.fleet_list import FleetList
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
    api_instance = flightctl.FleetApi(api_client)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the paramter must match the value of the 'continue' field in the previous list response. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supporting operators like '=', '==', and '!=' (e.g., \"key1=value1,key2!=value2\"). (optional)
    limit = 56 # int | The maximum number of results returned in the list response. The server will set the 'continue' field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. (optional)
    add_devices_summary = True # bool | Include a summary of the devices in the fleet. (optional)

    try:
        api_response = api_instance.list_fleets(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit, add_devices_summary=add_devices_summary)
        print("The response of FleetApi->list_fleets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->list_fleets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_continue** | **str**| An optional parameter to query more results from the server. The value of the paramter must match the value of the &#39;continue&#39; field in the previous list response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields, supporting operators like &#39;&#x3D;&#39;, &#39;&#x3D;&#x3D;&#39;, and &#39;!&#x3D;&#39; (e.g., \&quot;key1&#x3D;value1,key2!&#x3D;value2\&quot;). | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. The server will set the &#39;continue&#39; field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. | [optional] 
 **add_devices_summary** | **bool**| Include a summary of the devices in the fleet. | [optional] 

### Return type

[**FleetList**](FleetList.md)

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

# **list_template_versions**
> TemplateVersionList list_template_versions(fleet, var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)



list template versions

### Example


```python
import flightctl
from flightctl.models.template_version_list import TemplateVersionList
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
    api_instance = flightctl.FleetApi(api_client)
    fleet = 'fleet_example' # str | The owner of the template versions.
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the paramter must match the value of the 'continue' field in the previous list response. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supporting operators like '=', '==', and '!=' (e.g., \"key1=value1,key2!=value2\"). (optional)
    limit = 56 # int | The maximum number of results returned in the list response. The server will set the 'continue' field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. (optional)

    try:
        api_response = api_instance.list_template_versions(fleet, var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)
        print("The response of FleetApi->list_template_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->list_template_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet** | **str**| The owner of the template versions. | 
 **var_continue** | **str**| An optional parameter to query more results from the server. The value of the paramter must match the value of the &#39;continue&#39; field in the previous list response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields, supporting operators like &#39;&#x3D;&#39;, &#39;&#x3D;&#x3D;&#39;, and &#39;!&#x3D;&#39; (e.g., \&quot;key1&#x3D;value1,key2!&#x3D;value2\&quot;). | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. The server will set the &#39;continue&#39; field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. | [optional] 

### Return type

[**TemplateVersionList**](TemplateVersionList.md)

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

# **patch_fleet**
> Fleet patch_fleet(name, patch_request_inner)



Patch a Fleet resource.

### Example


```python
import flightctl
from flightctl.models.fleet import Fleet
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
    api_instance = flightctl.FleetApi(api_client)
    name = 'name_example' # str | The name of the Fleet resource to patch.
    patch_request_inner = [flightctl.PatchRequestInner()] # List[PatchRequestInner] | 

    try:
        api_response = api_instance.patch_fleet(name, patch_request_inner)
        print("The response of FleetApi->patch_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->patch_fleet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Fleet resource to patch. | 
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  | 

### Return type

[**Fleet**](Fleet.md)

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

# **patch_fleet_status**
> Fleet patch_fleet_status(name, patch_request_inner)



Patch the status of a Fleet resource.

### Example


```python
import flightctl
from flightctl.models.fleet import Fleet
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
    api_instance = flightctl.FleetApi(api_client)
    name = 'name_example' # str | The name of the Fleet resource to patch.
    patch_request_inner = [flightctl.PatchRequestInner()] # List[PatchRequestInner] | 

    try:
        api_response = api_instance.patch_fleet_status(name, patch_request_inner)
        print("The response of FleetApi->patch_fleet_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->patch_fleet_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Fleet resource to patch. | 
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  | 

### Return type

[**Fleet**](Fleet.md)

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

# **read_fleet**
> Fleet read_fleet(name, add_devices_summary=add_devices_summary)



Get a Fleet resource.

### Example


```python
import flightctl
from flightctl.models.fleet import Fleet
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
    api_instance = flightctl.FleetApi(api_client)
    name = 'name_example' # str | The name of the Fleet resource to get.
    add_devices_summary = True # bool | Include a summary of the devices in the fleet. (optional)

    try:
        api_response = api_instance.read_fleet(name, add_devices_summary=add_devices_summary)
        print("The response of FleetApi->read_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->read_fleet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Fleet resource to get. | 
 **add_devices_summary** | **bool**| Include a summary of the devices in the fleet. | [optional] 

### Return type

[**Fleet**](Fleet.md)

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

# **read_fleet_status**
> Fleet read_fleet_status(name)



read status of the specified Fleet

### Example


```python
import flightctl
from flightctl.models.fleet import Fleet
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
    api_instance = flightctl.FleetApi(api_client)
    name = 'name_example' # str | The name of the Fleet resource to get.

    try:
        api_response = api_instance.read_fleet_status(name)
        print("The response of FleetApi->read_fleet_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->read_fleet_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Fleet resource to get. | 

### Return type

[**Fleet**](Fleet.md)

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

# **read_template_version**
> TemplateVersion read_template_version(fleet, name)



read the specified template version

### Example


```python
import flightctl
from flightctl.models.template_version import TemplateVersion
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
    api_instance = flightctl.FleetApi(api_client)
    fleet = 'fleet_example' # str | The owner of the template version.
    name = 'name_example' # str | The name of the template version.

    try:
        api_response = api_instance.read_template_version(fleet, name)
        print("The response of FleetApi->read_template_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->read_template_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fleet** | **str**| The owner of the template version. | 
 **name** | **str**| The name of the template version. | 

### Return type

[**TemplateVersion**](TemplateVersion.md)

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

# **replace_fleet**
> Fleet replace_fleet(name, fleet)



Update a Fleet resource.

### Example


```python
import flightctl
from flightctl.models.fleet import Fleet
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
    api_instance = flightctl.FleetApi(api_client)
    name = 'name_example' # str | The name of the Fleet resource to update.
    fleet = flightctl.Fleet() # Fleet | 

    try:
        api_response = api_instance.replace_fleet(name, fleet)
        print("The response of FleetApi->replace_fleet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->replace_fleet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Fleet resource to update. | 
 **fleet** | [**Fleet**](Fleet.md)|  | 

### Return type

[**Fleet**](Fleet.md)

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
**404** | NotFound |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**503** | ServiceUnavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_fleet_status**
> Fleet replace_fleet_status(name, fleet)



replace status of the specified Fleet

### Example


```python
import flightctl
from flightctl.models.fleet import Fleet
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
    api_instance = flightctl.FleetApi(api_client)
    name = 'name_example' # str | The name of the Fleet resource to update.
    fleet = flightctl.Fleet() # Fleet | 

    try:
        api_response = api_instance.replace_fleet_status(name, fleet)
        print("The response of FleetApi->replace_fleet_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FleetApi->replace_fleet_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Fleet resource to update. | 
 **fleet** | [**Fleet**](Fleet.md)|  | 

### Return type

[**Fleet**](Fleet.md)

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

