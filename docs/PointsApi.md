# nascar_data_client.PointsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**points_driver_points_get**](PointsApi.md#points_driver_points_get) | **GET** /points/driver-points | 
[**points_manufacturer_points_get**](PointsApi.md#points_manufacturer_points_get) | **GET** /points/manufacturer-points | 
[**points_owner_points_get**](PointsApi.md#points_owner_points_get) | **GET** /points/owner-points | 

# **points_driver_points_get**
> list[DriverPoint] points_driver_points_get(season=season, series_id=series_id, race_id=race_id)



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
    api_response = api_instance.points_driver_points_get(season=season, series_id=series_id, race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointsApi->points_driver_points_get: %s\n" % e)
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

# **points_manufacturer_points_get**
> list[ManufacturerPoint] points_manufacturer_points_get(season=season, series_id=series_id, race_id=race_id)



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
    api_response = api_instance.points_manufacturer_points_get(season=season, series_id=series_id, race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointsApi->points_manufacturer_points_get: %s\n" % e)
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

# **points_owner_points_get**
> list[OwnerPoint] points_owner_points_get(season=season, series_id=series_id, race_id=race_id)



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
    api_response = api_instance.points_owner_points_get(season=season, series_id=series_id, race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointsApi->points_owner_points_get: %s\n" % e)
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

