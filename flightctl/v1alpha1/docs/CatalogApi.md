# flightctl.v1alpha1.CatalogApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_catalog**](CatalogApi.md#create_catalog) | **POST** /catalogs | 
[**create_catalog_item**](CatalogApi.md#create_catalog_item) | **POST** /catalogs/{catalog}/items | 
[**delete_catalog**](CatalogApi.md#delete_catalog) | **DELETE** /catalogs/{name} | 
[**delete_catalog_item**](CatalogApi.md#delete_catalog_item) | **DELETE** /catalogs/{catalog}/items/{name} | 
[**get_catalog**](CatalogApi.md#get_catalog) | **GET** /catalogs/{name} | 
[**get_catalog_item**](CatalogApi.md#get_catalog_item) | **GET** /catalogs/{catalog}/items/{name} | 
[**get_catalog_status**](CatalogApi.md#get_catalog_status) | **GET** /catalogs/{name}/status | 
[**list_all_catalog_items**](CatalogApi.md#list_all_catalog_items) | **GET** /catalogitems | 
[**list_catalog_items**](CatalogApi.md#list_catalog_items) | **GET** /catalogs/{catalog}/items | 
[**list_catalogs**](CatalogApi.md#list_catalogs) | **GET** /catalogs | 
[**patch_catalog**](CatalogApi.md#patch_catalog) | **PATCH** /catalogs/{name} | 
[**patch_catalog_item**](CatalogApi.md#patch_catalog_item) | **PATCH** /catalogs/{catalog}/items/{name} | 
[**patch_catalog_status**](CatalogApi.md#patch_catalog_status) | **PATCH** /catalogs/{name}/status | 
[**replace_catalog**](CatalogApi.md#replace_catalog) | **PUT** /catalogs/{name} | 
[**replace_catalog_item**](CatalogApi.md#replace_catalog_item) | **PUT** /catalogs/{catalog}/items/{name} | 
[**replace_catalog_status**](CatalogApi.md#replace_catalog_status) | **PUT** /catalogs/{name}/status | 


# **create_catalog**
> Catalog create_catalog(catalog)

Create a Catalog resource.

### Example


```python
import flightctl.v1alpha1
from flightctl.v1alpha1.models.catalog import Catalog
from flightctl.v1alpha1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.v1alpha1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.v1alpha1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.v1alpha1.CatalogApi(api_client)
    catalog = flightctl.v1alpha1.Catalog() # Catalog | 

    try:
        api_response = api_instance.create_catalog(catalog)
        print("The response of CatalogApi->create_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->create_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | [**Catalog**](Catalog.md)|  | 

### Return type

[**Catalog**](Catalog.md)

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

# **create_catalog_item**
> CatalogItem create_catalog_item(catalog, catalog_item)

Create a CatalogItem in a Catalog.

### Example


```python
import flightctl.v1alpha1
from flightctl.v1alpha1.models.catalog_item import CatalogItem
from flightctl.v1alpha1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.v1alpha1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.v1alpha1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.v1alpha1.CatalogApi(api_client)
    catalog = 'catalog_example' # str | The name of the Catalog resource.
    catalog_item = flightctl.v1alpha1.CatalogItem() # CatalogItem | The CatalogItem resource to create.

    try:
        api_response = api_instance.create_catalog_item(catalog, catalog_item)
        print("The response of CatalogApi->create_catalog_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->create_catalog_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| The name of the Catalog resource. | 
 **catalog_item** | [**CatalogItem**](CatalogItem.md)| The CatalogItem resource to create. | 

### Return type

[**CatalogItem**](CatalogItem.md)

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_catalog**
> Status delete_catalog(name)

Delete a Catalog resource.

### Example


```python
import flightctl.v1alpha1
from flightctl.v1alpha1.models.status import Status
from flightctl.v1alpha1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.v1alpha1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.v1alpha1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.v1alpha1.CatalogApi(api_client)
    name = 'name_example' # str | The name of the Catalog resource to delete.

    try:
        api_response = api_instance.delete_catalog(name)
        print("The response of CatalogApi->delete_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->delete_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Catalog resource to delete. | 

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

# **delete_catalog_item**
> Status delete_catalog_item(catalog, name)

Delete a CatalogItem from a Catalog.

### Example


```python
import flightctl.v1alpha1
from flightctl.v1alpha1.models.status import Status
from flightctl.v1alpha1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.v1alpha1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.v1alpha1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.v1alpha1.CatalogApi(api_client)
    catalog = 'catalog_example' # str | The name of the Catalog resource.
    name = 'name_example' # str | The name of the CatalogItem resource.

    try:
        api_response = api_instance.delete_catalog_item(catalog, name)
        print("The response of CatalogApi->delete_catalog_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->delete_catalog_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| The name of the Catalog resource. | 
 **name** | **str**| The name of the CatalogItem resource. | 

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
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog**
> Catalog get_catalog(name)

Get a Catalog resource.

### Example


```python
import flightctl.v1alpha1
from flightctl.v1alpha1.models.catalog import Catalog
from flightctl.v1alpha1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.v1alpha1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.v1alpha1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.v1alpha1.CatalogApi(api_client)
    name = 'name_example' # str | The name of the Catalog resource to get.

    try:
        api_response = api_instance.get_catalog(name)
        print("The response of CatalogApi->get_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->get_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Catalog resource to get. | 

### Return type

[**Catalog**](Catalog.md)

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

# **get_catalog_item**
> CatalogItem get_catalog_item(catalog, name)

Get a CatalogItem from a Catalog.

### Example


```python
import flightctl.v1alpha1
from flightctl.v1alpha1.models.catalog_item import CatalogItem
from flightctl.v1alpha1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.v1alpha1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.v1alpha1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.v1alpha1.CatalogApi(api_client)
    catalog = 'catalog_example' # str | The name of the Catalog resource.
    name = 'name_example' # str | The name of the CatalogItem resource.

    try:
        api_response = api_instance.get_catalog_item(catalog, name)
        print("The response of CatalogApi->get_catalog_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->get_catalog_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| The name of the Catalog resource. | 
 **name** | **str**| The name of the CatalogItem resource. | 

### Return type

[**CatalogItem**](CatalogItem.md)

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
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_status**
> Catalog get_catalog_status(name)

Get status of a Catalog resource.

### Example


```python
import flightctl.v1alpha1
from flightctl.v1alpha1.models.catalog import Catalog
from flightctl.v1alpha1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.v1alpha1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.v1alpha1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.v1alpha1.CatalogApi(api_client)
    name = 'name_example' # str | The name of the Catalog resource.

    try:
        api_response = api_instance.get_catalog_status(name)
        print("The response of CatalogApi->get_catalog_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->get_catalog_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Catalog resource. | 

### Return type

[**Catalog**](Catalog.md)

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

# **list_all_catalog_items**
> CatalogItemList list_all_catalog_items(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)

List CatalogItems across all Catalogs.

### Example


```python
import flightctl.v1alpha1
from flightctl.v1alpha1.models.catalog_item_list import CatalogItemList
from flightctl.v1alpha1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.v1alpha1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.v1alpha1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.v1alpha1.CatalogApi(api_client)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the parameter must match the value of the 'continue' field in the previous list response. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supporting operators like '=', '==', and '!=' (e.g., \"key1=value1,key2!=value2\"). (optional)
    limit = 56 # int | The maximum number of results returned in the list response. The server will set the 'continue' field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. (optional)

    try:
        api_response = api_instance.list_all_catalog_items(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)
        print("The response of CatalogApi->list_all_catalog_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->list_all_catalog_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_continue** | **str**| An optional parameter to query more results from the server. The value of the parameter must match the value of the &#39;continue&#39; field in the previous list response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields, supporting operators like &#39;&#x3D;&#39;, &#39;&#x3D;&#x3D;&#39;, and &#39;!&#x3D;&#39; (e.g., \&quot;key1&#x3D;value1,key2!&#x3D;value2\&quot;). | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. The server will set the &#39;continue&#39; field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. | [optional] 

### Return type

[**CatalogItemList**](CatalogItemList.md)

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

# **list_catalog_items**
> CatalogItemList list_catalog_items(catalog, var_continue=var_continue, label_selector=label_selector, limit=limit)

List CatalogItems from a Catalog.

### Example


```python
import flightctl.v1alpha1
from flightctl.v1alpha1.models.catalog_item_list import CatalogItemList
from flightctl.v1alpha1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.v1alpha1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.v1alpha1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.v1alpha1.CatalogApi(api_client)
    catalog = 'catalog_example' # str | The name of the Catalog resource.
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. (optional)
    limit = 56 # int | The maximum number of results returned in the list response. (optional)

    try:
        api_response = api_instance.list_catalog_items(catalog, var_continue=var_continue, label_selector=label_selector, limit=limit)
        print("The response of CatalogApi->list_catalog_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->list_catalog_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| The name of the Catalog resource. | 
 **var_continue** | **str**| An optional parameter to query more results from the server. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. | [optional] 

### Return type

[**CatalogItemList**](CatalogItemList.md)

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

# **list_catalogs**
> CatalogList list_catalogs(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)

List Catalog resources.

### Example


```python
import flightctl.v1alpha1
from flightctl.v1alpha1.models.catalog_list import CatalogList
from flightctl.v1alpha1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.v1alpha1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.v1alpha1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.v1alpha1.CatalogApi(api_client)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the paramter must match the value of the 'continue' field in the previous list response. (optional)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supporting operators like '=', '==', and '!=' (e.g., \"key1=value1,key2!=value2\"). (optional)
    limit = 56 # int | The maximum number of results returned in the list response. The server will set the 'continue' field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. (optional)

    try:
        api_response = api_instance.list_catalogs(var_continue=var_continue, label_selector=label_selector, field_selector=field_selector, limit=limit)
        print("The response of CatalogApi->list_catalogs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->list_catalogs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_continue** | **str**| An optional parameter to query more results from the server. The value of the paramter must match the value of the &#39;continue&#39; field in the previous list response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields, supporting operators like &#39;&#x3D;&#39;, &#39;&#x3D;&#x3D;&#39;, and &#39;!&#x3D;&#39; (e.g., \&quot;key1&#x3D;value1,key2!&#x3D;value2\&quot;). | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. The server will set the &#39;continue&#39; field in the list response if more results exist. The continue value may then be specified as parameter in a subsequent query. | [optional] 

### Return type

[**CatalogList**](CatalogList.md)

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

# **patch_catalog**
> Catalog patch_catalog(name, patch_request_inner)

Patch a Catalog resource.

### Example


```python
import flightctl.v1alpha1
from flightctl.v1alpha1.models.catalog import Catalog
from flightctl.v1alpha1.models.patch_request_inner import PatchRequestInner
from flightctl.v1alpha1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.v1alpha1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.v1alpha1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.v1alpha1.CatalogApi(api_client)
    name = 'name_example' # str | The name of the Catalog resource to patch.
    patch_request_inner = [flightctl.v1alpha1.PatchRequestInner()] # List[PatchRequestInner] | 

    try:
        api_response = api_instance.patch_catalog(name, patch_request_inner)
        print("The response of CatalogApi->patch_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->patch_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Catalog resource to patch. | 
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  | 

### Return type

[**Catalog**](Catalog.md)

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

# **patch_catalog_item**
> CatalogItem patch_catalog_item(catalog, name, patch_request_inner)

Patch a CatalogItem in a Catalog.

### Example


```python
import flightctl.v1alpha1
from flightctl.v1alpha1.models.catalog_item import CatalogItem
from flightctl.v1alpha1.models.patch_request_inner import PatchRequestInner
from flightctl.v1alpha1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.v1alpha1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.v1alpha1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.v1alpha1.CatalogApi(api_client)
    catalog = 'catalog_example' # str | The name of the Catalog resource.
    name = 'name_example' # str | The name of the CatalogItem resource to patch.
    patch_request_inner = [flightctl.v1alpha1.PatchRequestInner()] # List[PatchRequestInner] | 

    try:
        api_response = api_instance.patch_catalog_item(catalog, name, patch_request_inner)
        print("The response of CatalogApi->patch_catalog_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->patch_catalog_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| The name of the Catalog resource. | 
 **name** | **str**| The name of the CatalogItem resource to patch. | 
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  | 

### Return type

[**CatalogItem**](CatalogItem.md)

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
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_catalog_status**
> Catalog patch_catalog_status(name, patch_request_inner)

Patch status of a Catalog resource.

### Example


```python
import flightctl.v1alpha1
from flightctl.v1alpha1.models.catalog import Catalog
from flightctl.v1alpha1.models.patch_request_inner import PatchRequestInner
from flightctl.v1alpha1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.v1alpha1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.v1alpha1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.v1alpha1.CatalogApi(api_client)
    name = 'name_example' # str | The name of the Catalog resource.
    patch_request_inner = [flightctl.v1alpha1.PatchRequestInner()] # List[PatchRequestInner] | 

    try:
        api_response = api_instance.patch_catalog_status(name, patch_request_inner)
        print("The response of CatalogApi->patch_catalog_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->patch_catalog_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Catalog resource. | 
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  | 

### Return type

[**Catalog**](Catalog.md)

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

# **replace_catalog**
> Catalog replace_catalog(name, catalog)

Update a Catalog resource.

### Example


```python
import flightctl.v1alpha1
from flightctl.v1alpha1.models.catalog import Catalog
from flightctl.v1alpha1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.v1alpha1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.v1alpha1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.v1alpha1.CatalogApi(api_client)
    name = 'name_example' # str | The name of the Catalog resource to update.
    catalog = flightctl.v1alpha1.Catalog() # Catalog | 

    try:
        api_response = api_instance.replace_catalog(name, catalog)
        print("The response of CatalogApi->replace_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->replace_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Catalog resource to update. | 
 **catalog** | [**Catalog**](Catalog.md)|  | 

### Return type

[**Catalog**](Catalog.md)

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

# **replace_catalog_item**
> CatalogItem replace_catalog_item(catalog, name, catalog_item)

Replace a CatalogItem in a Catalog.

### Example


```python
import flightctl.v1alpha1
from flightctl.v1alpha1.models.catalog_item import CatalogItem
from flightctl.v1alpha1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.v1alpha1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.v1alpha1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.v1alpha1.CatalogApi(api_client)
    catalog = 'catalog_example' # str | The name of the Catalog resource.
    name = 'name_example' # str | The name of the CatalogItem resource.
    catalog_item = flightctl.v1alpha1.CatalogItem() # CatalogItem | The CatalogItem resource to replace.

    try:
        api_response = api_instance.replace_catalog_item(catalog, name, catalog_item)
        print("The response of CatalogApi->replace_catalog_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->replace_catalog_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| The name of the Catalog resource. | 
 **name** | **str**| The name of the CatalogItem resource. | 
 **catalog_item** | [**CatalogItem**](CatalogItem.md)| The CatalogItem resource to replace. | 

### Return type

[**CatalogItem**](CatalogItem.md)

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
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_catalog_status**
> Catalog replace_catalog_status(name, catalog)

Update status of a Catalog resource.

### Example


```python
import flightctl.v1alpha1
from flightctl.v1alpha1.models.catalog import Catalog
from flightctl.v1alpha1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.v1alpha1.Configuration(
    host = "/api/v1"
)


# Enter a context with an instance of the API client
with flightctl.v1alpha1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.v1alpha1.CatalogApi(api_client)
    name = 'name_example' # str | The name of the Catalog resource.
    catalog = flightctl.v1alpha1.Catalog() # Catalog | 

    try:
        api_response = api_instance.replace_catalog_status(name, catalog)
        print("The response of CatalogApi->replace_catalog_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->replace_catalog_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Catalog resource. | 
 **catalog** | [**Catalog**](Catalog.md)|  | 

### Return type

[**Catalog**](Catalog.md)

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

