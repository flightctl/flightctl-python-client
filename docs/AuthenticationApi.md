# flightctl.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_config**](AuthenticationApi.md#auth_config) | **GET** /api/v1/auth/config | 
[**auth_get_permissions**](AuthenticationApi.md#auth_get_permissions) | **GET** /api/v1/auth/permissions | 
[**auth_token**](AuthenticationApi.md#auth_token) | **POST** /api/v1/auth/{providername}/token | 
[**auth_user_info**](AuthenticationApi.md#auth_user_info) | **GET** /api/v1/auth/userinfo | 
[**auth_validate**](AuthenticationApi.md#auth_validate) | **GET** /api/v1/auth/validate | 


# **auth_config**
> AuthConfig auth_config()

Get authentication configuration.

### Example


```python
import flightctl
from flightctl.models.auth_config import AuthConfig
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
    api_instance = flightctl.AuthenticationApi(api_client)

    try:
        api_response = api_instance.auth_config()
        print("The response of AuthenticationApi->auth_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthConfig**](AuthConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**418** | Auth not configured |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_get_permissions**
> PermissionList auth_get_permissions()

Get the list of available permissions for the authenticated user.

### Example


```python
import flightctl
from flightctl.models.permission_list import PermissionList
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
    api_instance = flightctl.AuthenticationApi(api_client)

    try:
        api_response = api_instance.auth_get_permissions()
        print("The response of AuthenticationApi->auth_get_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_get_permissions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PermissionList**](PermissionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available permissions |  -  |
**401** | Unauthorized |  -  |
**418** | Auth not configured |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_token**
> TokenResponse auth_token(providername, token_request)

OAuth2 token exchange endpoint. Proxies token requests to the configured authentication provider (PAM issuer) for authorization code flow with PKCE support.

### Example


```python
import flightctl
from flightctl.models.token_request import TokenRequest
from flightctl.models.token_response import TokenResponse
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
    api_instance = flightctl.AuthenticationApi(api_client)
    providername = 'providername_example' # str | Name of the authentication provider to use.
    token_request = flightctl.TokenRequest() # TokenRequest | 

    try:
        api_response = api_instance.auth_token(providername, token_request)
        print("The response of AuthenticationApi->auth_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providername** | **str**| Name of the authentication provider to use. | 
 **token_request** | [**TokenRequest**](TokenRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token response |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_user_info**
> UserInfoResponse auth_user_info()

OIDC UserInfo endpoint. Proxies the request to the configured authentication provider to retrieve user information.

### Example


```python
import flightctl
from flightctl.models.user_info_response import UserInfoResponse
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
    api_instance = flightctl.AuthenticationApi(api_client)

    try:
        api_response = api_instance.auth_user_info()
        print("The response of AuthenticationApi->auth_user_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_user_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserInfoResponse**](UserInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User information |  -  |
**401** | Unauthorized |  -  |
**418** | Auth not configured |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_validate**
> Status auth_validate(authorization=authorization)

Validate an authentication token.

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
    api_instance = flightctl.AuthenticationApi(api_client)
    authorization = 'authorization_example' # str | The authentication token to validate. (optional)

    try:
        api_response = api_instance.auth_validate(authorization=authorization)
        print("The response of AuthenticationApi->auth_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| The authentication token to validate. | [optional] 

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
**200** | Token valid |  -  |
**400** | Bad Request |  -  |
**401** | Token invalid |  -  |
**418** | Auth not configured |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

