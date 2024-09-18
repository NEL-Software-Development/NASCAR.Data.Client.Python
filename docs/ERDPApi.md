# nascar_data_client.ERDPApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**erdp_datapoints_get**](ERDPApi.md#erdp_datapoints_get) | **GET** /erdp/datapoints | 
[**erdp_sources_get**](ERDPApi.md#erdp_sources_get) | **GET** /erdp/sources | 

# **erdp_datapoints_get**
> list[NextGenDatapoint] erdp_datapoints_get()



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.ERDPApi(nascar_data_client.ApiClient(configuration))

try:
    api_response = api_instance.erdp_datapoints_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ERDPApi->erdp_datapoints_get: %s\n" % e)
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

# **erdp_sources_get**
> list[NextGenSource] erdp_sources_get()



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.ERDPApi(nascar_data_client.ApiClient(configuration))

try:
    api_response = api_instance.erdp_sources_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ERDPApi->erdp_sources_get: %s\n" % e)
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

