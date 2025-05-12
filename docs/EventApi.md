# flightctl.EventApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_events**](EventApi.md#list_events) | **GET** /api/v1/events | 


# **list_events**
> EventList list_events(field_selector=field_selector, limit=limit, var_continue=var_continue)



Retrieves a list of events. 

### Example


```python
import flightctl
from flightctl.models.event_list import EventList
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
    api_instance = flightctl.EventApi(api_client)
    field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields, supporting operators like '=', '==', and '!=' (e.g., \"key1=value1,key2!=value2\"). (optional)
    limit = 56 # int | The maximum number of events to return in the response. (optional)
    var_continue = 'var_continue_example' # str | An optional parameter to query more results from the server. The value of the paramter must match the value of the 'continue' field in the previous list response. (optional)

    try:
        api_response = api_instance.list_events(field_selector=field_selector, limit=limit, var_continue=var_continue)
        print("The response of EventApi->list_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->list_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields, supporting operators like &#39;&#x3D;&#39;, &#39;&#x3D;&#x3D;&#39;, and &#39;!&#x3D;&#39; (e.g., \&quot;key1&#x3D;value1,key2!&#x3D;value2\&quot;). | [optional] 
 **limit** | **int**| The maximum number of events to return in the response. | [optional] 
 **var_continue** | **str**| An optional parameter to query more results from the server. The value of the paramter must match the value of the &#39;continue&#39; field in the previous list response. | [optional] 

### Return type

[**EventList**](EventList.md)

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

