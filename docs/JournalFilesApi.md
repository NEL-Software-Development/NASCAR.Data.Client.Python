# nascar_data_client.JournalFilesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**journal_get**](JournalFilesApi.md#journal_get) | **GET** /journal | 

# **journal_get**
> str journal_get(historical_race_id=historical_race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.JournalFilesApi(nascar_data_client.ApiClient(configuration))
historical_race_id = 'historical_race_id_example' # str |  (optional)

try:
    api_response = api_instance.journal_get(historical_race_id=historical_race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalFilesApi->journal_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **historical_race_id** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

