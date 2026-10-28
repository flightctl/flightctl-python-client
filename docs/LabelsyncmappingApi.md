# flightctl.LabelsyncmappingApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_label_sync_mapping**](LabelsyncmappingApi.md#create_label_sync_mapping) | **POST** /labelsyncmappings |
[**delete_label_sync_mapping**](LabelsyncmappingApi.md#delete_label_sync_mapping) | **DELETE** /labelsyncmappings/{name} |
[**get_label_sync_mapping**](LabelsyncmappingApi.md#get_label_sync_mapping) | **GET** /labelsyncmappings/{name} |
[**get_label_sync_provenance**](LabelsyncmappingApi.md#get_label_sync_provenance) | **GET** /labelsyncprovenance |
[**list_label_sync_mappings**](LabelsyncmappingApi.md#list_label_sync_mappings) | **GET** /labelsyncmappings |
[**patch_label_sync_mapping**](LabelsyncmappingApi.md#patch_label_sync_mapping) | **PATCH** /labelsyncmappings/{name} |
[**replace_label_sync_mapping**](LabelsyncmappingApi.md#replace_label_sync_mapping) | **PUT** /labelsyncmappings/{name} |


# **create_label_sync_mapping**
> LabelSyncMapping create_label_sync_mapping(label_sync_mapping)

Create a LabelSyncMapping resource.

### Example


```python
import flightctl
from flightctl.models.label_sync_mapping import LabelSyncMapping
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
    api_instance = flightctl.LabelsyncmappingApi(api_client)
    label_sync_mapping = flightctl.LabelSyncMapping() # LabelSyncMapping |

    try:
        api_response = api_instance.create_label_sync_mapping(label_sync_mapping)
        print("The response of LabelsyncmappingApi->create_label_sync_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsyncmappingApi->create_label_sync_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_sync_mapping** | [**LabelSyncMapping**](LabelSyncMapping.md)|  |

### Return type

[**LabelSyncMapping**](LabelSyncMapping.md)

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
**422** | Unprocessable Content |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_label_sync_mapping**
> Status delete_label_sync_mapping(name)

Delete a LabelSyncMapping resource.

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
    api_instance = flightctl.LabelsyncmappingApi(api_client)
    name = 'name_example' # str | The name of the LabelSyncMapping resource to delete.

    try:
        api_response = api_instance.delete_label_sync_mapping(name)
        print("The response of LabelsyncmappingApi->delete_label_sync_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsyncmappingApi->delete_label_sync_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the LabelSyncMapping resource to delete. |

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

# **get_label_sync_mapping**
> LabelSyncMapping get_label_sync_mapping(name)

Get a LabelSyncMapping resource.

### Example


```python
import flightctl
from flightctl.models.label_sync_mapping import LabelSyncMapping
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
    api_instance = flightctl.LabelsyncmappingApi(api_client)
    name = 'name_example' # str | The name of the LabelSyncMapping resource to get.

    try:
        api_response = api_instance.get_label_sync_mapping(name)
        print("The response of LabelsyncmappingApi->get_label_sync_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsyncmappingApi->get_label_sync_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the LabelSyncMapping resource to get. |

### Return type

[**LabelSyncMapping**](LabelSyncMapping.md)

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

# **get_label_sync_provenance**
> LabelSyncProvenanceList get_label_sync_provenance(label_keys)

Resolve exact label keys to their current owning LabelSyncMapping names in the request organization. Return one item per supplied key in request order, including repeated keys. Keys with no current mapping owner have an empty owners array. Label values are not returned.

### Example


```python
import flightctl
from flightctl.models.label_sync_provenance_list import LabelSyncProvenanceList
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
    api_instance = flightctl.LabelsyncmappingApi(api_client)
    label_keys = ['label_keys_example'] # List[str] | Exact label keys to resolve. Supply between 1 and 50 repeated labelKeys parameters. Repeated key values are preserved as repeated response items in request order.

    try:
        api_response = api_instance.get_label_sync_provenance(label_keys)
        print("The response of LabelsyncmappingApi->get_label_sync_provenance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsyncmappingApi->get_label_sync_provenance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_keys** | [**List[str]**](str.md)| Exact label keys to resolve. Supply between 1 and 50 repeated labelKeys parameters. Repeated key values are preserved as repeated response items in request order. |

### Return type

[**LabelSyncProvenanceList**](LabelSyncProvenanceList.md)

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

# **list_label_sync_mappings**
> LabelSyncMappingList list_label_sync_mappings(var_continue=var_continue, limit=limit)

List LabelSyncMapping resources.

### Example


```python
import flightctl
from flightctl.models.label_sync_mapping_list import LabelSyncMappingList
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
    api_instance = flightctl.LabelsyncmappingApi(api_client)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the parameter must match the value of the 'continue' field in the previous list response. (optional)
    limit = 56 # int | The maximum number of results returned in the list response. (optional)

    try:
        api_response = api_instance.list_label_sync_mappings(var_continue=var_continue, limit=limit)
        print("The response of LabelsyncmappingApi->list_label_sync_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsyncmappingApi->list_label_sync_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_continue** | **str**| An optional parameter to query more results from the server. The value of the parameter must match the value of the &#39;continue&#39; field in the previous list response. | [optional]
 **limit** | **int**| The maximum number of results returned in the list response. | [optional]

### Return type

[**LabelSyncMappingList**](LabelSyncMappingList.md)

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

# **patch_label_sync_mapping**
> LabelSyncMapping patch_label_sync_mapping(name, patch_request_inner)

Patch a LabelSyncMapping resource.

### Example


```python
import flightctl
from flightctl.models.label_sync_mapping import LabelSyncMapping
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
    api_instance = flightctl.LabelsyncmappingApi(api_client)
    name = 'name_example' # str | The name of the LabelSyncMapping resource to patch.
    patch_request_inner = [flightctl.PatchRequestInner()] # List[PatchRequestInner] |

    try:
        api_response = api_instance.patch_label_sync_mapping(name, patch_request_inner)
        print("The response of LabelsyncmappingApi->patch_label_sync_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsyncmappingApi->patch_label_sync_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the LabelSyncMapping resource to patch. |
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  |

### Return type

[**LabelSyncMapping**](LabelSyncMapping.md)

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
**422** | Unprocessable Content |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_label_sync_mapping**
> LabelSyncMapping replace_label_sync_mapping(name, label_sync_mapping)

Update a LabelSyncMapping resource.

### Example


```python
import flightctl
from flightctl.models.label_sync_mapping import LabelSyncMapping
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
    api_instance = flightctl.LabelsyncmappingApi(api_client)
    name = 'name_example' # str | The name of the LabelSyncMapping resource to update.
    label_sync_mapping = flightctl.LabelSyncMapping() # LabelSyncMapping |

    try:
        api_response = api_instance.replace_label_sync_mapping(name, label_sync_mapping)
        print("The response of LabelsyncmappingApi->replace_label_sync_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsyncmappingApi->replace_label_sync_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the LabelSyncMapping resource to update. |
 **label_sync_mapping** | [**LabelSyncMapping**](LabelSyncMapping.md)|  |

### Return type

[**LabelSyncMapping**](LabelSyncMapping.md)

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
**422** | Unprocessable Content |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
