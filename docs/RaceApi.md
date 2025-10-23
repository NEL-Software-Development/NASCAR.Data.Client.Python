# nascar_data_client.RaceApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**race_cautions_get**](RaceApi.md#race_cautions_get) | **GET** /race/cautions | 
[**race_discipline_updates_get**](RaceApi.md#race_discipline_updates_get) | **GET** /race/discipline-updates | 
[**race_entries_get**](RaceApi.md#race_entries_get) | **GET** /race/entries | 
[**race_get**](RaceApi.md#race_get) | **GET** /race | 
[**race_infractions_get**](RaceApi.md#race_infractions_get) | **GET** /race/infractions | 
[**race_lap_leaders_get**](RaceApi.md#race_lap_leaders_get) | **GET** /race/lap-leaders | 
[**race_live_session_get**](RaceApi.md#race_live_session_get) | **GET** /race/live-session | 
[**race_lookup_get**](RaceApi.md#race_lookup_get) | **GET** /race/lookup | 
[**race_loop_stats_get**](RaceApi.md#race_loop_stats_get) | **GET** /race/loop-stats | 
[**race_pitstops_get**](RaceApi.md#race_pitstops_get) | **GET** /race/pitstops | 
[**race_practice_results_get**](RaceApi.md#race_practice_results_get) | **GET** /race/practice-results | 
[**race_qualifying_results_get**](RaceApi.md#race_qualifying_results_get) | **GET** /race/qualifying-results | 
[**race_race_results_get**](RaceApi.md#race_race_results_get) | **GET** /race/race-results | 
[**race_report_get**](RaceApi.md#race_report_get) | **GET** /race/report | 
[**race_results_get**](RaceApi.md#race_results_get) | **GET** /race/results | 
[**race_rosters_get**](RaceApi.md#race_rosters_get) | **GET** /race/rosters | 
[**race_season_get**](RaceApi.md#race_season_get) | **GET** /race/season | 
[**race_stage_results_get**](RaceApi.md#race_stage_results_get) | **GET** /race/stage-results | 
[**race_stages_get**](RaceApi.md#race_stages_get) | **GET** /race/stages | 
[**race_stat_reports_get**](RaceApi.md#race_stat_reports_get) | **GET** /race/stat-reports | 
[**race_viewmodel_get**](RaceApi.md#race_viewmodel_get) | **GET** /race/viewmodel | 
[**race_weekend_schedule_get**](RaceApi.md#race_weekend_schedule_get) | **GET** /race/weekend-schedule | 

# **race_cautions_get**
> list[Caution] race_cautions_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_cautions_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_cautions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**list[Caution]**](Caution.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_discipline_updates_get**
> list[DisciplineUpdate] race_discipline_updates_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_discipline_updates_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_discipline_updates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**list[DisciplineUpdate]**](DisciplineUpdate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_entries_get**
> list[RunEntry] race_entries_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_entries_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_entries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**list[RunEntry]**](RunEntry.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_get**
> RaceDetails race_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**RaceDetails**](RaceDetails.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_infractions_get**
> list[RaceInfraction] race_infractions_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_infractions_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_infractions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**list[RaceInfraction]**](RaceInfraction.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_lap_leaders_get**
> list[LapLeader] race_lap_leaders_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_lap_leaders_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_lap_leaders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**list[LapLeader]**](LapLeader.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_live_session_get**
> ActiveRun race_live_session_get()



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))

try:
    api_response = api_instance.race_live_session_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_live_session_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ActiveRun**](ActiveRun.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_lookup_get**
> list[RaceDetails] race_lookup_get(history_race_id=history_race_id, date_start=date_start, date_end=date_end)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
history_race_id = 56 # int |  (optional)
date_start = '2013-10-20' # date | enter date_start in yyyy-mm-dd format (optional)
date_end = '2013-10-20' # date | enter date_end in yyyy-mm-dd format (optional)

try:
    api_response = api_instance.race_lookup_get(history_race_id=history_race_id, date_start=date_start, date_end=date_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_lookup_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history_race_id** | **int**|  | [optional] 
 **date_start** | **date**| enter date_start in yyyy-mm-dd format | [optional] 
 **date_end** | **date**| enter date_end in yyyy-mm-dd format | [optional] 

### Return type

[**list[RaceDetails]**](RaceDetails.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_loop_stats_get**
> list[LoopStat] race_loop_stats_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_loop_stats_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_loop_stats_get: %s\n" % e)
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

# **race_pitstops_get**
> list[Pitstop] race_pitstops_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_pitstops_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_pitstops_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**list[Pitstop]**](Pitstop.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_practice_results_get**
> list[PracticeRunResults] race_practice_results_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_practice_results_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_practice_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**list[PracticeRunResults]**](PracticeRunResults.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_qualifying_results_get**
> list[QualifyingRunResults] race_qualifying_results_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_qualifying_results_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_qualifying_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**list[QualifyingRunResults]**](QualifyingRunResults.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_race_results_get**
> list[RaceRunResults] race_race_results_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_race_results_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_race_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**list[RaceRunResults]**](RaceRunResults.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_report_get**
> AvailableReports race_report_get(key=key)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
key = 'key_example' # str |  (optional)

try:
    api_response = api_instance.race_report_get(key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_report_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | [optional] 

### Return type

[**AvailableReports**](AvailableReports.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_results_get**
> RunResults race_results_get(race_id=race_id, timing_run_id=timing_run_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)
timing_run_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_results_get(race_id=race_id, timing_run_id=timing_run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 
 **timing_run_id** | **int**|  | [optional] 

### Return type

[**RunResults**](RunResults.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_rosters_get**
> list[TeamRoster] race_rosters_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_rosters_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_rosters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**list[TeamRoster]**](TeamRoster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_season_get**
> list[list[Race]] race_season_get(season=season, series_id=series_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
season = 56 # int |  (optional)
series_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_season_get(season=season, series_id=series_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_season_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**|  | [optional] 
 **series_id** | **int**|  | [optional] 

### Return type

**list[list[Race]]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_stage_results_get**
> list[StageRunResults] race_stage_results_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_stage_results_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_stage_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**list[StageRunResults]**](StageRunResults.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_stages_get**
> list[Stage] race_stages_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_stages_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_stages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**list[Stage]**](Stage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_stat_reports_get**
> AvailableReports race_stat_reports_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_stat_reports_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_stat_reports_get: %s\n" % e)
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

# **race_viewmodel_get**
> RaceViewModel race_viewmodel_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_viewmodel_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_viewmodel_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**RaceViewModel**](RaceViewModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_weekend_schedule_get**
> list[WeekendSchedule] race_weekend_schedule_get(race_id=race_id)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int |  (optional)

try:
    api_response = api_instance.race_weekend_schedule_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_weekend_schedule_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**|  | [optional] 

### Return type

[**list[WeekendSchedule]**](WeekendSchedule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

