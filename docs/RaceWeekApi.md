# nascar_data_client.RaceWeekApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**race_week_details_get**](RaceWeekApi.md#race_week_details_get) | **GET** /race-week/details | 
[**race_week_live_get**](RaceWeekApi.md#race_week_live_get) | **GET** /race-week/live | 
[**race_week_season_get**](RaceWeekApi.md#race_week_season_get) | **GET** /race-week/season | 

# **race_week_details_get**
> RaceWeekDetails race_week_details_get(id=id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceWeekApi(nascar_data_client.ApiClient(configuration))
id = 56 # int |  (optional)

try:
    api_response = api_instance.race_week_details_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceWeekApi->race_week_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 

### Return type

[**RaceWeekDetails**](RaceWeekDetails.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_week_live_get**
> list[RaceWeek] race_week_live_get()



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceWeekApi(nascar_data_client.ApiClient(configuration))

try:
    api_response = api_instance.race_week_live_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceWeekApi->race_week_live_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RaceWeek]**](RaceWeek.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_week_season_get**
> list[RaceWeek] race_week_season_get(season=season)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceWeekApi(nascar_data_client.ApiClient(configuration))
season = 56 # int |  (optional)

try:
    api_response = api_instance.race_week_season_get(season=season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceWeekApi->race_week_season_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**|  | [optional] 

### Return type

[**list[RaceWeek]**](RaceWeek.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

