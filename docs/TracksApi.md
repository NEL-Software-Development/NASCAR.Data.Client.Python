# nascar_data_client.TracksApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**track_details_get**](TracksApi.md#track_details_get) | **GET** /track-details | 
[**tracks_get**](TracksApi.md#tracks_get) | **GET** /tracks | 

# **track_details_get**
> TrackDetails track_details_get(track_id=track_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.TracksApi(nascar_data_client.ApiClient(configuration))
track_id = 56 # int |  (optional)

try:
    api_response = api_instance.track_details_get(track_id=track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracksApi->track_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **track_id** | **int**|  | [optional] 

### Return type

[**TrackDetails**](TrackDetails.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tracks_get**
> Track tracks_get()



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.TracksApi(nascar_data_client.ApiClient(configuration))

try:
    api_response = api_instance.tracks_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracksApi->tracks_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Track**](Track.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

