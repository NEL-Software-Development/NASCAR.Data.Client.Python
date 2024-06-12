# nascar_data_client.NextGenApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_points**](NextGenApi.md#data_points) | **GET** /nextgen-datapoints | 
[**sources**](NextGenApi.md#sources) | **GET** /nextgen-sources | 

# **data_points**
> list[NextGenDatapoint] data_points()



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.NextGenApi(nascar_data_client.ApiClient(configuration))

try:
    api_response = api_instance.data_points()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NextGenApi->data_points: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NextGenDatapoint]**](NextGenDatapoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources**
> list[NextGenSource] sources()



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.NextGenApi(nascar_data_client.ApiClient(configuration))

try:
    api_response = api_instance.sources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NextGenApi->sources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NextGenSource]**](NextGenSource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

