# nascar_data_client.TracksApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**track_details_get**](TracksApi.md#track_details_get) | **GET** /track-details | Retrieves detailed information about a specific track, including its history, notable events, and other relevant data, given the track&#x27;s unique identifier from /tracks.
[**tracks_get**](TracksApi.md#tracks_get) | **GET** /tracks | Retrieves a list of all tracks in the NASCAR database, including basic information such as track name, location, and type.

# **track_details_get**
> TrackDetails track_details_get(track_id=track_id)

Retrieves detailed information about a specific track, including its history, notable events, and other relevant data, given the track's unique identifier from /tracks.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.TracksApi(nascar_data_client.ApiClient(configuration))
track_id = 56 # int | The unique identifier of the track. (optional)

try:
    # Retrieves detailed information about a specific track, including its history, notable events, and other relevant data, given the track's unique identifier from /tracks.
    api_response = api_instance.track_details_get(track_id=track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TracksApi->track_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **track_id** | **int**| The unique identifier of the track. | [optional] 

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

Retrieves a list of all tracks in the NASCAR database, including basic information such as track name, location, and type.

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
    # Retrieves a list of all tracks in the NASCAR database, including basic information such as track name, location, and type.
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

