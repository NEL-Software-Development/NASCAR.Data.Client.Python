# nascar_data_client.VendorApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vendor_crl_testresult_post**](VendorApi.md#vendor_crl_testresult_post) | **POST** /vendor/crl_testresult | 
[**vendor_tires_post**](VendorApi.md#vendor_tires_post) | **POST** /vendor/tires | 
[**vendor_utm_offsets_post**](VendorApi.md#vendor_utm_offsets_post) | **POST** /vendor/utm_offsets | 

# **vendor_crl_testresult_post**
> vendor_crl_testresult_post(body=body)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.VendorApi(nascar_data_client.ApiClient(configuration))
body = nascar_data_client.CrlFormFoxResult() # CrlFormFoxResult |  (optional)

try:
    api_instance.vendor_crl_testresult_post(body=body)
except ApiException as e:
    print("Exception when calling VendorApi->vendor_crl_testresult_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CrlFormFoxResult**](CrlFormFoxResult.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_tires_post**
> TireListETLSaveResult vendor_tires_post(body=body)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.VendorApi(nascar_data_client.ApiClient(configuration))
body = [nascar_data_client.Tire()] # list[Tire] |  (optional)

try:
    api_response = api_instance.vendor_tires_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorApi->vendor_tires_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Tire]**](Tire.md)|  | [optional] 

### Return type

[**TireListETLSaveResult**](TireListETLSaveResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_utm_offsets_post**
> OpticalTrackingUTMOffsetListETLSaveResult vendor_utm_offsets_post(body=body)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.VendorApi(nascar_data_client.ApiClient(configuration))
body = [nascar_data_client.OpticalTrackingUTMOffset()] # list[OpticalTrackingUTMOffset] |  (optional)

try:
    api_response = api_instance.vendor_utm_offsets_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorApi->vendor_utm_offsets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[OpticalTrackingUTMOffset]**](OpticalTrackingUTMOffset.md)|  | [optional] 

### Return type

[**OpticalTrackingUTMOffsetListETLSaveResult**](OpticalTrackingUTMOffsetListETLSaveResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

