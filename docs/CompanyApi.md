# nascar_data_client.CompanyApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**company_search_get**](CompanyApi.md#company_search_get) | **GET** /company/search | 

# **company_search_get**
> list[Company] company_search_get(search_term=search_term)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.CompanyApi(nascar_data_client.ApiClient(configuration))
search_term = 'search_term_example' # str |  (optional)

try:
    api_response = api_instance.company_search_get(search_term=search_term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**|  | [optional] 

### Return type

[**list[Company]**](Company.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

