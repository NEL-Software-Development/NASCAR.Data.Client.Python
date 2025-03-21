# nascar_data_client.OpticalTrackingApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**optical_tracking_utm_offsets_get**](OpticalTrackingApi.md#optical_tracking_utm_offsets_get) | **GET** /optical-tracking/utm-offsets | 

# **optical_tracking_utm_offsets_get**
> list[OpticalTrackingUTMOffset] optical_tracking_utm_offsets_get()



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
    api_response = api_instance.optical_tracking_utm_offsets_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpticalTrackingApi->optical_tracking_utm_offsets_get: %s\n" % e)
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

