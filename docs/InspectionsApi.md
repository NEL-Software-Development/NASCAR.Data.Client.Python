# nascar_data_client.InspectionsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inspections_aim_id_get**](InspectionsApi.md#inspections_aim_id_get) | **GET** /inspections/aim/{id} | For use by the AIM system
[**inspections_device_numbers_get**](InspectionsApi.md#inspections_device_numbers_get) | **GET** /inspections/device-numbers | For use by the MLS system
[**inspections_idr_get**](InspectionsApi.md#inspections_idr_get) | **GET** /inspections/idr | For use by the AIM system
[**inspections_oss_get**](InspectionsApi.md#inspections_oss_get) | **GET** /inspections/oss | Retrieves a list of OSS scans for a specific race.
[**inspections_submissions_technique_get**](InspectionsApi.md#inspections_submissions_technique_get) | **GET** /inspections/submissions/technique | For use by Technique chassis builders to track submissions
[**inspections_vehicle_weights_get**](InspectionsApi.md#inspections_vehicle_weights_get) | **GET** /inspections/vehicle-weights | Retrieves a list of vehicle weights for a specific race.

# **inspections_aim_id_get**
> inspections_aim_id_get(id)

For use by the AIM system

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InspectionsApi(nascar_data_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # For use by the AIM system
    api_instance.inspections_aim_id_get(id)
except ApiException as e:
    print("Exception when calling InspectionsApi->inspections_aim_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspections_device_numbers_get**
> list[InspectionResult] inspections_device_numbers_get()

For use by the MLS system

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InspectionsApi(nascar_data_client.ApiClient(configuration))

try:
    # For use by the MLS system
    api_response = api_instance.inspections_device_numbers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionsApi->inspections_device_numbers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InspectionResult]**](InspectionResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspections_idr_get**
> list[InspectionResult] inspections_idr_get(idr_number=idr_number)

For use by the AIM system

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InspectionsApi(nascar_data_client.ApiClient(configuration))
idr_number = 56 # int | IDR number. (optional)

try:
    # For use by the AIM system
    api_response = api_instance.inspections_idr_get(idr_number=idr_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionsApi->inspections_idr_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idr_number** | **int**| IDR number. | [optional] 

### Return type

[**list[InspectionResult]**](InspectionResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspections_oss_get**
> list[OSSScan] inspections_oss_get(race_id=race_id)

Retrieves a list of OSS scans for a specific race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InspectionsApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | Unique race identifier. (optional)

try:
    # Retrieves a list of OSS scans for a specific race.
    api_response = api_instance.inspections_oss_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionsApi->inspections_oss_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| Unique race identifier. | [optional] 

### Return type

[**list[OSSScan]**](OSSScan.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspections_submissions_technique_get**
> list[RepairSubmission] inspections_submissions_technique_get()

For use by Technique chassis builders to track submissions

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InspectionsApi(nascar_data_client.ApiClient(configuration))

try:
    # For use by Technique chassis builders to track submissions
    api_response = api_instance.inspections_submissions_technique_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionsApi->inspections_submissions_technique_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RepairSubmission]**](RepairSubmission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspections_vehicle_weights_get**
> list[VehicleWeight] inspections_vehicle_weights_get(race_id=race_id)

Retrieves a list of vehicle weights for a specific race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InspectionsApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | Unique race identifier. (optional)

try:
    # Retrieves a list of vehicle weights for a specific race.
    api_response = api_instance.inspections_vehicle_weights_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InspectionsApi->inspections_vehicle_weights_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| Unique race identifier. | [optional] 

### Return type

[**list[VehicleWeight]**](VehicleWeight.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

