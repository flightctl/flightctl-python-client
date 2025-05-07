# flightctl.LabelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_labels**](LabelApi.md#list_labels) | **GET** /api/v1/labels | 


# **list_labels**
> List[str] list_labels(kind, label_selector=label_selector, field_selector=field_selector, limit=limit)



Retrieves a distinct list of labels for the specified resource type. 

### Example


```python
import flightctl
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
    api_instance = flightctl.LabelApi(api_client)
    kind = 'kind_example' # str | The type of resource to retrieve labels from.
    label_selector = 'label_selector_example' # str | A filter to retrieve labels only from resources that match the given label selector. (optional)
    field_selector = 'field_selector_example' # str | A filter to retrieve labels only from resources that match the given field selector. (optional)
    limit = 56 # int | The maximum number of distinct labels to return in the response. (optional)

    try:
        api_response = api_instance.list_labels(kind, label_selector=label_selector, field_selector=field_selector, limit=limit)
        print("The response of LabelApi->list_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelApi->list_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**| The type of resource to retrieve labels from. | 
 **label_selector** | **str**| A filter to retrieve labels only from resources that match the given label selector. | [optional] 
 **field_selector** | **str**| A filter to retrieve labels only from resources that match the given field selector. | [optional] 
 **limit** | **int**| The maximum number of distinct labels to return in the response. | [optional] 

### Return type

**List[str]**

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

