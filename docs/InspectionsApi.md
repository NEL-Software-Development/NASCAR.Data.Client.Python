# nascar_data_client.InspectionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_ss**](InspectionsApi.md#o_ss) | **GET** /inspections/oss | 
[**vehicle_weights**](InspectionsApi.md#vehicle_weights) | **GET** /inspections/vehicle-weights | 

# **o_ss**
> list[OSSScan] o_ss(race_id=race_id)



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
    api_response = api_instance.o_ss(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionsApi->o_ss: %s\n" % e)
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

# **vehicle_weights**
> list[VehicleWeight] vehicle_weights(race_id=race_id)



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
    api_response = api_instance.vehicle_weights(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionsApi->vehicle_weights: %s\n" % e)
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

