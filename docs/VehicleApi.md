# nascar_data_client.VehicleApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vehicle_get**](VehicleApi.md#vehicle_get) | **GET** /vehicle | Retrieves detailed information about a specific vehicle, including its finishes, given the vehicle&#x27;s unique identifier.
[**vehicle_season_finishes_get**](VehicleApi.md#vehicle_season_finishes_get) | **GET** /vehicle/season-finishes | Retrieves a list of all finishes for a specific vehicle across an entire season, given the season, series, and vehicle number.

# **vehicle_get**
> VehicleDetails vehicle_get(id=id)

Retrieves detailed information about a specific vehicle, including its finishes, given the vehicle's unique identifier.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.VehicleApi(nascar_data_client.ApiClient(configuration))
id = 56 # int | The unique identifier of the vehicle. (optional)

try:
    # Retrieves detailed information about a specific vehicle, including its finishes, given the vehicle's unique identifier.
    api_response = api_instance.vehicle_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehicleApi->vehicle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier of the vehicle. | [optional] 

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

Retrieves a list of all finishes for a specific vehicle across an entire season, given the season, series, and vehicle number.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.VehicleApi(nascar_data_client.ApiClient(configuration))
season = 56 # int | Four-digit season year to query (optional)
series_id = 56 # int | Series identifier. Common values are 1 for Cup, 2 for O'Reilly, and 3 for Truck. (optional)
vehicle = 'vehicle_example' # str | Vehicle number to query (optional)

try:
    # Retrieves a list of all finishes for a specific vehicle across an entire season, given the season, series, and vehicle number.
    api_response = api_instance.vehicle_season_finishes_get(season=season, series_id=series_id, vehicle=vehicle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehicleApi->vehicle_season_finishes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Four-digit season year to query | [optional] 
 **series_id** | **int**| Series identifier. Common values are 1 for Cup, 2 for O&#x27;Reilly, and 3 for Truck. | [optional] 
 **vehicle** | **str**| Vehicle number to query | [optional] 

### Return type

[**list[RaceResultSummary]**](RaceResultSummary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

