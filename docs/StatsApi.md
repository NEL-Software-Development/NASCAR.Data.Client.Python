# nascar_data_client.StatsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stats_loop_stats_get**](StatsApi.md#stats_loop_stats_get) | **GET** /stats/loop-stats | Retrieves a list of driver loop statistics for a given race.
[**stats_report_get**](StatsApi.md#stats_report_get) | **GET** /stats/report | Retrieves a specific statistical report file for a given key, which typically corresponds to a report path or identifier returned by /reports.
[**stats_reports_get**](StatsApi.md#stats_reports_get) | **GET** /stats/reports | Retrieves a list of available statistical report paths for a given race.
[**stats_season_get**](StatsApi.md#stats_season_get) | **GET** /stats/season | Retrieves a list of driver season statistics for a given series and season.

# **stats_loop_stats_get**
> list[LoopStat] stats_loop_stats_get(race_id=race_id)

Retrieves a list of driver loop statistics for a given race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.StatsApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves a list of driver loop statistics for a given race.
    api_response = api_instance.stats_loop_stats_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats_loop_stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

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

Retrieves a specific statistical report file for a given key, which typically corresponds to a report path or identifier returned by /reports.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.StatsApi(nascar_data_client.ApiClient(configuration))
key = 'key_example' # str | The key or identifier of the statistical report. (optional)

try:
    # Retrieves a specific statistical report file for a given key, which typically corresponds to a report path or identifier returned by /reports.
    api_response = api_instance.stats_report_get(key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats_report_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key or identifier of the statistical report. | [optional] 

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

Retrieves a list of available statistical report paths for a given race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.StatsApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves a list of available statistical report paths for a given race.
    api_response = api_instance.stats_reports_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats_reports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

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

Retrieves a list of driver season statistics for a given series and season.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.StatsApi(nascar_data_client.ApiClient(configuration))
series_id = 56 # int | The unique identifier of the series. (optional)
season = 56 # int | The season for which to retrieve statistics. (optional)

try:
    # Retrieves a list of driver season statistics for a given series and season.
    api_response = api_instance.stats_season_get(series_id=series_id, season=season)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats_season_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**| The unique identifier of the series. | [optional] 
 **season** | **int**| The season for which to retrieve statistics. | [optional] 

### Return type

[**list[SeasonStat]**](SeasonStat.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

