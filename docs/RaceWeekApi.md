# nascar_data_client.RaceWeekApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**details**](RaceWeekApi.md#details) | **GET** /race-week/details | 
[**live**](RaceWeekApi.md#live) | **GET** /race-week/live | 
[**season**](RaceWeekApi.md#season) | **GET** /race-week/season | 

# **details**
> RaceWeekDetails details(id=id)



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
    api_response = api_instance.details(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceWeekApi->details: %s\n" % e)
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

# **live**
> list[RaceWeek] live()



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
    api_response = api_instance.live()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceWeekApi->live: %s\n" % e)
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

# **season**
> list[RaceWeek] season(season=season)



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
    api_response = api_instance.season(season=season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceWeekApi->season: %s\n" % e)
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

