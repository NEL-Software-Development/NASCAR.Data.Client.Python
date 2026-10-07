# nascar_data_client.AccountApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_refresh_token_get**](AccountApi.md#account_refresh_token_get) | **GET** /account/refresh-token | Refreshes an expired authentication token using a refresh token.

# **account_refresh_token_get**
> TokenResponse account_refresh_token_get(refresh_token=refresh_token)

Refreshes an expired authentication token using a refresh token.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.AccountApi(nascar_data_client.ApiClient(configuration))
refresh_token = 'refresh_token_example' # str | The refresh token obtained from a previous authentication.  Used to obtain a new access token without requiring user credentials. (optional)

try:
    # Refreshes an expired authentication token using a refresh token.
    api_response = api_instance.account_refresh_token_get(refresh_token=refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_refresh_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token** | **str**| The refresh token obtained from a previous authentication.  Used to obtain a new access token without requiring user credentials. | [optional] 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

