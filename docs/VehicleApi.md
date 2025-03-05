# nascar_data_client.VehicleApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vehicle_get**](VehicleApi.md#vehicle_get) | **GET** /vehicle | 
[**vehicle_season_finishes_get**](VehicleApi.md#vehicle_season_finishes_get) | **GET** /vehicle/season-finishes | 

# **vehicle_get**
> VehicleDetails vehicle_get(id=id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.VehicleApi(nascar_data_client.ApiClient(configuration))
id = 56 # int |  (optional)

try:
    api_response = api_instance.vehicle_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehicleApi->vehicle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 

### Return type

[**VehicleDetails**](VehicleDetails.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vehicle_season_finishes_get**
> list[RaceResultSummary] vehicle_season_finishes_get(season=season, series_id=series_id, vehicle=vehicle)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.VehicleApi(nascar_data_client.ApiClient(configuration))
season = 56 # int |  (optional)
series_id = 56 # int |  (optional)
vehicle = 'vehicle_example' # str |  (optional)

try:
    api_response = api_instance.vehicle_season_finishes_get(season=season, series_id=series_id, vehicle=vehicle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehicleApi->vehicle_season_finishes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**|  | [optional] 
 **series_id** | **int**|  | [optional] 
 **vehicle** | **str**|  | [optional] 

### Return type

[**list[RaceResultSummary]**](RaceResultSummary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

