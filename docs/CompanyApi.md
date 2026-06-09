# nascar_data_client.CompanyApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**company_get**](CompanyApi.md#company_get) | **GET** /company | Retrieves a single company by ID.
[**company_search_get**](CompanyApi.md#company_search_get) | **GET** /company/search | Searches for companies by name or keyword.

# **company_get**
> Company company_get(id=id)

Retrieves a single company by ID.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.CompanyApi(nascar_data_client.ApiClient(configuration))
id = 56 # int | Unique company identifier. (optional)

try:
    # Retrieves a single company by ID.
    api_response = api_instance.company_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Unique company identifier. | [optional] 

### Return type

[**Company**](Company.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_search_get**
> list[Company] company_search_get(search_term=search_term)

Searches for companies by name or keyword.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.CompanyApi(nascar_data_client.ApiClient(configuration))
search_term = 'search_term_example' # str | Partial or full company name to search for (e.g. \"Daytona\"). (optional)

try:
    # Searches for companies by name or keyword.
    api_response = api_instance.company_search_get(search_term=search_term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| Partial or full company name to search for (e.g. \&quot;Daytona\&quot;). | [optional] 

### Return type

[**list[Company]**](Company.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

