# nascar_data_client.SeriesApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**series_get**](SeriesApi.md#series_get) | **GET** /series | Retrieves a list of all racing series, including their unique identifiers and names.
[**series_season_get**](SeriesApi.md#series_season_get) | **GET** /series/season | 

# **series_get**
> list[Series] series_get()

Retrieves a list of all racing series, including their unique identifiers and names.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.SeriesApi(nascar_data_client.ApiClient(configuration))

try:
    # Retrieves a list of all racing series, including their unique identifiers and names.
    api_response = api_instance.series_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SeriesApi->series_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Series]**](Series.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **series_season_get**
> list[SeasonSeries] series_season_get()



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.SeriesApi(nascar_data_client.ApiClient(configuration))

try:
    api_response = api_instance.series_season_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SeriesApi->series_season_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SeasonSeries]**](SeasonSeries.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

