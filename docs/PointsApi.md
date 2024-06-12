# nascar_data_client.PointsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**driver_points**](PointsApi.md#driver_points) | **GET** /points/driver-points | 
[**manufacturer_points**](PointsApi.md#manufacturer_points) | **GET** /points/manufacturer-points | 
[**owner_points**](PointsApi.md#owner_points) | **GET** /points/owner-points | 

# **driver_points**
> list[DriverPoint] driver_points(season=season, series_id=series_id, race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.PointsApi(nascar_data_client.ApiClient(configuration))
season = 56 # int |  (optional)
series_id = 56 # int |  (optional)
race_id = 0 # int |  (optional) (default to 0)

try:
    api_response = api_instance.driver_points(season=season, series_id=series_id, race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointsApi->driver_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**|  | [optional] 
 **series_id** | **int**|  | [optional] 
 **race_id** | **int**|  | [optional] [default to 0]

### Return type

[**list[DriverPoint]**](DriverPoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manufacturer_points**
> list[ManufacturerPoint] manufacturer_points(season=season, series_id=series_id, race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.PointsApi(nascar_data_client.ApiClient(configuration))
season = 56 # int |  (optional)
series_id = 56 # int |  (optional)
race_id = 0 # int |  (optional) (default to 0)

try:
    api_response = api_instance.manufacturer_points(season=season, series_id=series_id, race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointsApi->manufacturer_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**|  | [optional] 
 **series_id** | **int**|  | [optional] 
 **race_id** | **int**|  | [optional] [default to 0]

### Return type

[**list[ManufacturerPoint]**](ManufacturerPoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **owner_points**
> list[OwnerPoint] owner_points(season=season, series_id=series_id, race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.PointsApi(nascar_data_client.ApiClient(configuration))
season = 56 # int |  (optional)
series_id = 56 # int |  (optional)
race_id = 0 # int |  (optional) (default to 0)

try:
    api_response = api_instance.owner_points(season=season, series_id=series_id, race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointsApi->owner_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**|  | [optional] 
 **series_id** | **int**|  | [optional] 
 **race_id** | **int**|  | [optional] [default to 0]

### Return type

[**list[OwnerPoint]**](OwnerPoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

