# nascar_data_client.OpticalTrackingApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**utm_offsets**](OpticalTrackingApi.md#utm_offsets) | **GET** /utm-offsets | 

# **utm_offsets**
> list[OpticalTrackingUTMOffset] utm_offsets()



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.OpticalTrackingApi(nascar_data_client.ApiClient(configuration))

try:
    api_response = api_instance.utm_offsets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpticalTrackingApi->utm_offsets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OpticalTrackingUTMOffset]**](OpticalTrackingUTMOffset.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

