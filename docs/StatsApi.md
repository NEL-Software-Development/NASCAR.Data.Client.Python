# nascar_data_client.StatsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stats_loop_stats_get**](StatsApi.md#stats_loop_stats_get) | **GET** /stats/loop-stats | 
[**stats_report_get**](StatsApi.md#stats_report_get) | **GET** /stats/report | 
[**stats_reports_get**](StatsApi.md#stats_reports_get) | **GET** /stats/reports | 
[**stats_season_get**](StatsApi.md#stats_season_get) | **GET** /stats/season | 

# **stats_loop_stats_get**
> list[LoopStat] stats_loop_stats_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.StatsApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.stats_loop_stats_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats_loop_stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**list[LoopStat]**](LoopStat.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_report_get**
> str stats_report_get(key=key)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.StatsApi(nascar_data_client.ApiClient(configuration))
key = 'key_example' # str |  (optional)

try:
    api_response = api_instance.stats_report_get(key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats_report_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_reports_get**
> AvailableReports stats_reports_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.StatsApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.stats_reports_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats_reports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**AvailableReports**](AvailableReports.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_season_get**
> list[SeasonStat] stats_season_get(series_id=series_id, season=season)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.StatsApi(nascar_data_client.ApiClient(configuration))
series_id = 56 # int |  (optional)
season = 56 # int |  (optional)

try:
    api_response = api_instance.stats_season_get(series_id=series_id, season=season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats_season_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | [optional] 
 **season** | **int**|  | [optional] 

### Return type

[**list[SeasonStat]**](SeasonStat.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

