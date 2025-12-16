# flightctl.DeviceactionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resume_devices**](DeviceactionsApi.md#resume_devices) | **POST** /api/v1/deviceactions/resume | 


# **resume_devices**
> DeviceResumeResponse resume_devices(device_resume_request)

Resume devices based on label selector and/or field selector.

### Example


```python
import flightctl
from flightctl.models.device_resume_request import DeviceResumeRequest
from flightctl.models.device_resume_response import DeviceResumeResponse
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
    api_instance = flightctl.DeviceactionsApi(api_client)
    device_resume_request = flightctl.DeviceResumeRequest() # DeviceResumeRequest | 

    try:
        api_response = api_instance.resume_devices(device_resume_request)
        print("The response of DeviceactionsApi->resume_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceactionsApi->resume_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_resume_request** | [**DeviceResumeRequest**](DeviceResumeRequest.md)|  | 

### Return type

[**DeviceResumeResponse**](DeviceResumeResponse.md)

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
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

