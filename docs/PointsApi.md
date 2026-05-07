# nascar_data_client.PointsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**points_driver_points_get**](PointsApi.md#points_driver_points_get) | **GET** /points/driver-points | Retrieves driver points for a specific race.
[**points_manufacturer_points_get**](PointsApi.md#points_manufacturer_points_get) | **GET** /points/manufacturer-points | Retrieves manufacturer points for a specific season, series, and optionally a specific race.
[**points_owner_points_get**](PointsApi.md#points_owner_points_get) | **GET** /points/owner-points | Retrieves owner points for a specific season, series, and optionally a specific race.

# **points_driver_points_get**
> list[DriverPointsView] points_driver_points_get(race_id=race_id)

Retrieves driver points for a specific race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.PointsApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | Unique race identifier. If not provided, points for the most recent races will be returned. (optional)

try:
    # Retrieves driver points for a specific race.
    api_response = api_instance.points_driver_points_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointsApi->points_driver_points_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| Unique race identifier. If not provided, points for the most recent races will be returned. | [optional] 

### Return type

[**list[DriverPointsView]**](DriverPointsView.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **points_manufacturer_points_get**
> list[ManufacturerPoint] points_manufacturer_points_get(season=season, series_id=series_id, race_id=race_id)

Retrieves manufacturer points for a specific season, series, and optionally a specific race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.PointsApi(nascar_data_client.ApiClient(configuration))
season = 56 # int | Four-digit season year to query. (optional)
series_id = 56 # int | Series identifier. Common values are 1 for Cup, 2 for O'Reilly, and 3 for Truck. (optional)
race_id = 0 # int | Unique race identifier. If specified, the points will be limited to the given race. If not provided or set to 0, points for all races in the specified season and series will be returned. (optional) (default to 0)

try:
    # Retrieves manufacturer points for a specific season, series, and optionally a specific race.
    api_response = api_instance.points_manufacturer_points_get(season=season, series_id=series_id, race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointsApi->points_manufacturer_points_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Four-digit season year to query. | [optional] 
 **series_id** | **int**| Series identifier. Common values are 1 for Cup, 2 for O&#x27;Reilly, and 3 for Truck. | [optional] 
 **race_id** | **int**| Unique race identifier. If specified, the points will be limited to the given race. If not provided or set to 0, points for all races in the specified season and series will be returned. | [optional] [default to 0]

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

Retrieves owner points for a specific season, series, and optionally a specific race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.PointsApi(nascar_data_client.ApiClient(configuration))
season = 56 # int | Four-digit season year to query. (optional)
series_id = 56 # int | Series identifier. Common values are 1 for Cup, 2 for O'Reilly, and 3 for Truck. (optional)
race_id = 0 # int | Unique race identifier. If specified, the points will be limited to the given race. If not provided or set to 0, points for all races in the specified season and series will be returned. (optional) (default to 0)

try:
    # Retrieves owner points for a specific season, series, and optionally a specific race.
    api_response = api_instance.points_owner_points_get(season=season, series_id=series_id, race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PointsApi->points_owner_points_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Four-digit season year to query. | [optional] 
 **series_id** | **int**| Series identifier. Common values are 1 for Cup, 2 for O&#x27;Reilly, and 3 for Truck. | [optional] 
 **race_id** | **int**| Unique race identifier. If specified, the points will be limited to the given race. If not provided or set to 0, points for all races in the specified season and series will be returned. | [optional] [default to 0]

### Return type

[**list[OwnerPoint]**](OwnerPoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

