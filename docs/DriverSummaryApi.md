# nascar_data_client.DriverSummaryApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**driver_summary_get**](DriverSummaryApi.md#driver_summary_get) | **GET** /driver-summary | 

# **driver_summary_get**
> list[DriverSummary] driver_summary_get(series_id=series_id, season=season, driver_id=driver_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.DriverSummaryApi(nascar_data_client.ApiClient(configuration))
series_id = 56 # int |  (optional)
season = 56 # int |  (optional)
driver_id = 0 # int |  (optional) (default to 0)

try:
    api_response = api_instance.driver_summary_get(series_id=series_id, season=season, driver_id=driver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriverSummaryApi->driver_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | [optional] 
 **season** | **int**|  | [optional] 
 **driver_id** | **int**|  | [optional] [default to 0]

### Return type

[**list[DriverSummary]**](DriverSummary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

