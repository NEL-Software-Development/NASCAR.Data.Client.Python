# nascar_data_client.ERDPApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**erdp_topics_get**](ERDPApi.md#erdp_topics_get) | **GET** /erdp/topics | Get a users erdp topics.

# **erdp_topics_get**
> list[ClientERDPTopic] erdp_topics_get()

Get a users erdp topics.

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
    # Get a users erdp topics.
    api_response = api_instance.erdp_topics_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ERDPApi->erdp_topics_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ClientERDPTopic]**](ClientERDPTopic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

