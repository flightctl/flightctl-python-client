# flightctl.imagebuilder.ImagepromotionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_image_promotion**](ImagepromotionApi.md#create_image_promotion) | **POST** /api/v1/imagepromotions | 
[**delete_image_promotion**](ImagepromotionApi.md#delete_image_promotion) | **DELETE** /api/v1/imagepromotions/{name} | 
[**get_image_promotion**](ImagepromotionApi.md#get_image_promotion) | **GET** /api/v1/imagepromotions/{name} | 
[**list_image_promotions**](ImagepromotionApi.md#list_image_promotions) | **GET** /api/v1/imagepromotions | 
[**patch_image_promotion**](ImagepromotionApi.md#patch_image_promotion) | **PATCH** /api/v1/imagepromotions/{name} | 
[**replace_image_promotion**](ImagepromotionApi.md#replace_image_promotion) | **PUT** /api/v1/imagepromotions/{name} | 


# **create_image_promotion**
> ImagePromotion create_image_promotion(image_promotion)

Create an ImagePromotion resource to publish a completed image build to the software catalog.

### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.models.image_promotion import ImagePromotion
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
    api_instance = flightctl.imagebuilder.ImagepromotionApi(api_client)
    image_promotion = flightctl.imagebuilder.ImagePromotion() # ImagePromotion | 

    try:
        api_response = api_instance.create_image_promotion(image_promotion)
        print("The response of ImagepromotionApi->create_image_promotion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagepromotionApi->create_image_promotion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_promotion** | [**ImagePromotion**](ImagePromotion.md)|  | 

### Return type

[**ImagePromotion**](ImagePromotion.md)

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
**409** | Conflict - an ImagePromotion with the given name already exists. |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image_promotion**
> Status delete_image_promotion(name)

Delete an ImagePromotion resource.

### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.models.status import Status
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
    api_instance = flightctl.imagebuilder.ImagepromotionApi(api_client)
    name = 'name_example' # str | The name of the ImagePromotion resource.

    try:
        api_response = api_instance.delete_image_promotion(name)
        print("The response of ImagepromotionApi->delete_image_promotion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagepromotionApi->delete_image_promotion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the ImagePromotion resource. | 

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
**400** | Bad Request. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_promotion**
> ImagePromotion get_image_promotion(name)

Get an ImagePromotion resource.

### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.models.image_promotion import ImagePromotion
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
    api_instance = flightctl.imagebuilder.ImagepromotionApi(api_client)
    name = 'name_example' # str | The name of the ImagePromotion resource.

    try:
        api_response = api_instance.get_image_promotion(name)
        print("The response of ImagepromotionApi->get_image_promotion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagepromotionApi->get_image_promotion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the ImagePromotion resource. | 

### Return type

[**ImagePromotion**](ImagePromotion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_image_promotions**
> ImagePromotionList list_image_promotions(label_selector=label_selector, field_selector=field_selector, limit=limit, var_continue=var_continue)

List ImagePromotion resources.

### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.models.image_promotion_list import ImagePromotionList
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
    api_instance = flightctl.imagebuilder.ImagepromotionApi(api_client)
    label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. (optional)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. (optional)
    limit = 56 # int | The maximum number of results returned in the list response. (optional)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. (optional)

    try:
        api_response = api_instance.list_image_promotions(label_selector=label_selector, field_selector=field_selector, limit=limit, var_continue=var_continue)
        print("The response of ImagepromotionApi->list_image_promotions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagepromotionApi->list_image_promotions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. | [optional] 
 **limit** | **int**| The maximum number of results returned in the list response. | [optional] 
 **var_continue** | **str**| An optional parameter to query more results from the server. | [optional] 

### Return type

[**ImagePromotionList**](ImagePromotionList.md)

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

# **patch_image_promotion**
> ImagePromotion patch_image_promotion(name, patch_request_inner)

Patch an ImagePromotion resource using RFC 6902 JSON Patch. Only operations targeting /spec/source/exportFormats (or its children) and /metadata/labels are accepted. Export formats may only be added (append-only). The promotion must not be in Failed or Publishing state.


### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.models.image_promotion import ImagePromotion
from flightctl.imagebuilder.models.patch_request_inner import PatchRequestInner
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
    api_instance = flightctl.imagebuilder.ImagepromotionApi(api_client)
    name = 'name_example' # str | The name of the ImagePromotion resource.
    patch_request_inner = [flightctl.imagebuilder.PatchRequestInner()] # List[PatchRequestInner] | 

    try:
        api_response = api_instance.patch_image_promotion(name, patch_request_inner)
        print("The response of ImagepromotionApi->patch_image_promotion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagepromotionApi->patch_image_promotion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the ImagePromotion resource. | 
 **patch_request_inner** | [**List[PatchRequestInner]**](PatchRequestInner.md)|  | 

### Return type

[**ImagePromotion**](ImagePromotion.md)

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

# **replace_image_promotion**
> ImagePromotion replace_image_promotion(name, image_promotion)

Replace an ImagePromotion resource. Only spec.source.exportFormats (append-only — the submitted list must be a superset of the current list) and metadata.labels may be changed. All other spec fields must be identical to the stored values or a 400 is returned. The promotion must not be in Failed or Publishing state.


### Example


```python
import flightctl.imagebuilder
from flightctl.imagebuilder.models.image_promotion import ImagePromotion
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
    api_instance = flightctl.imagebuilder.ImagepromotionApi(api_client)
    name = 'name_example' # str | The name of the ImagePromotion resource.
    image_promotion = flightctl.imagebuilder.ImagePromotion() # ImagePromotion | 

    try:
        api_response = api_instance.replace_image_promotion(name, image_promotion)
        print("The response of ImagepromotionApi->replace_image_promotion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagepromotionApi->replace_image_promotion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the ImagePromotion resource. | 
 **image_promotion** | [**ImagePromotion**](ImagePromotion.md)|  | 

### Return type

[**ImagePromotion**](ImagePromotion.md)

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
**409** | Conflict - concurrent update conflict. |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

