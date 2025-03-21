# nascar_data_client.InspectionsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inspections_oss_get**](InspectionsApi.md#inspections_oss_get) | **GET** /inspections/oss | 
[**inspections_vehicle_weights_get**](InspectionsApi.md#inspections_vehicle_weights_get) | **GET** /inspections/vehicle-weights | 

# **inspections_oss_get**
> list[OSSScan] inspections_oss_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InspectionsApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.inspections_oss_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionsApi->inspections_oss_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**list[OSSScan]**](OSSScan.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspections_vehicle_weights_get**
> list[VehicleWeight] inspections_vehicle_weights_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InspectionsApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.inspections_vehicle_weights_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionsApi->inspections_vehicle_weights_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**list[VehicleWeight]**](VehicleWeight.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

