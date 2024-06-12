# nascar_data_client.AccountApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**refresh_token**](AccountApi.md#refresh_token) | **GET** /account/refresh-token | 

# **refresh_token**
> TokenResponse refresh_token(refresh_token=refresh_token)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.AccountApi(nascar_data_client.ApiClient(configuration))
refresh_token = 'refresh_token_example' # str |  (optional)

try:
    api_response = api_instance.refresh_token(refresh_token=refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token** | **str**|  | [optional] 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

