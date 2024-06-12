# nascar_data_client.DriverApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**by_season**](DriverApi.md#by_season) | **GET** /driver/season | 
[**driver**](DriverApi.md#driver) | **GET** /driver | 
[**driver_season_finishes**](DriverApi.md#driver_season_finishes) | **GET** /driver/season-finishes | 

# **by_season**
> list[Driver] by_season(season=season, series_id=series_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.DriverApi(nascar_data_client.ApiClient(configuration))
season = 56 # int |  (optional)
series_id = 56 # int |  (optional)

try:
    api_response = api_instance.by_season(season=season, series_id=series_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriverApi->by_season: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**|  | [optional] 
 **series_id** | **int**|  | [optional] 

### Return type

[**list[Driver]**](Driver.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **driver**
> Driver driver(id=id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.DriverApi(nascar_data_client.ApiClient(configuration))
id = 56 # int |  (optional)

try:
    api_response = api_instance.driver(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriverApi->driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 

### Return type

[**Driver**](Driver.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **driver_season_finishes**
> list[RaceResultSummary] driver_season_finishes(id=id, season=season, series_id=series_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.DriverApi(nascar_data_client.ApiClient(configuration))
id = 56 # int |  (optional)
season = 56 # int |  (optional)
series_id = 56 # int |  (optional)

try:
    api_response = api_instance.driver_season_finishes(id=id, season=season, series_id=series_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriverApi->driver_season_finishes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 
 **season** | **int**|  | [optional] 
 **series_id** | **int**|  | [optional] 

### Return type

[**list[RaceResultSummary]**](RaceResultSummary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

