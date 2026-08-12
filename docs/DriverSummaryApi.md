# nascar_data_client.DriverSummaryApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**driver_summary_get**](DriverSummaryApi.md#driver_summary_get) | **GET** /driver-summary | Returns a summary of a driver&#x27;s performance for a given series and season, including statistics such as wins, top 5s, top 10s, poles, and more.

# **driver_summary_get**
> list[DriverSummary] driver_summary_get(series_id=series_id, season=season, driver_id=driver_id)

Returns a summary of a driver's performance for a given series and season, including statistics such as wins, top 5s, top 10s, poles, and more.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.DriverSummaryApi(nascar_data_client.ApiClient(configuration))
series_id = 56 # int | Series identifier. Common values are 1 for Cup, 2 for O'Reilly, and 3 for Truck. (optional)
season = 56 # int | Four-digit season year to query. (optional)
driver_id = 0 # int | Unique driver identifier. If specified, the summary will be limited to the given driver. If not provided or set to 0, summaries for all drivers in the specified series and season will be returned. (optional) (default to 0)

try:
    # Returns a summary of a driver's performance for a given series and season, including statistics such as wins, top 5s, top 10s, poles, and more.
    api_response = api_instance.driver_summary_get(series_id=series_id, season=season, driver_id=driver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriverSummaryApi->driver_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**| Series identifier. Common values are 1 for Cup, 2 for O&#x27;Reilly, and 3 for Truck. | [optional] 
 **season** | **int**| Four-digit season year to query. | [optional] 
 **driver_id** | **int**| Unique driver identifier. If specified, the summary will be limited to the given driver. If not provided or set to 0, summaries for all drivers in the specified series and season will be returned. | [optional] [default to 0]

### Return type

[**list[DriverSummary]**](DriverSummary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

