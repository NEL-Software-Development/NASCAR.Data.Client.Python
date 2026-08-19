# nascar_data_client.RaceApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**race_cautions_get**](RaceApi.md#race_cautions_get) | **GET** /race/cautions | Retrieves a list of cautions for a given race.
[**race_discipline_updates_get**](RaceApi.md#race_discipline_updates_get) | **GET** /race/discipline-updates | Retrieves a list of discipline updates for a given race.
[**race_entries_get**](RaceApi.md#race_entries_get) | **GET** /race/entries | Retrieves a list of entries for a given race.
[**race_entry_get**](RaceApi.md#race_entry_get) | **GET** /race/entry | Retrieves the details of a race entry.
[**race_fastest_laps_get**](RaceApi.md#race_fastest_laps_get) | **GET** /race/fastest-laps | Retrieves the fastest lap information for a specified race.
[**race_get**](RaceApi.md#race_get) | **GET** /race | Retrieves detailed information for a given race.
[**race_infractions_get**](RaceApi.md#race_infractions_get) | **GET** /race/infractions | Retrieves a list of infractions for a given race.
[**race_lap_chart_get**](RaceApi.md#race_lap_chart_get) | **GET** /race/lap-chart | Retrieves lap by lap driver information for a specified race.
[**race_lap_leaders_get**](RaceApi.md#race_lap_leaders_get) | **GET** /race/lap-leaders | Retrieves a list of lap leaders for a given race.
[**race_live_session_get**](RaceApi.md#race_live_session_get) | **GET** /race/live-session | Retrieves the active run session information.
[**race_lookup_get**](RaceApi.md#race_lookup_get) | **GET** /race/lookup | Retrieves a list of race details based on historic race ID or a date range.
[**race_loop_stats_get**](RaceApi.md#race_loop_stats_get) | **GET** /race/loop-stats | 
[**race_pitstops_get**](RaceApi.md#race_pitstops_get) | **GET** /race/pitstops | Retrieves a list of pit stops for a given race.
[**race_practice_results_get**](RaceApi.md#race_practice_results_get) | **GET** /race/practice-results | Retrieves practice run results for a given race.
[**race_qualifying_results_get**](RaceApi.md#race_qualifying_results_get) | **GET** /race/qualifying-results | Retrieves qualifying run results for a given race.
[**race_race_results_get**](RaceApi.md#race_race_results_get) | **GET** /race/race-results | Retrieves the race results for a specified race
[**race_report_get**](RaceApi.md#race_report_get) | **GET** /race/report | 
[**race_results_get**](RaceApi.md#race_results_get) | **GET** /race/results | Retrieves the run results for a specified race and timing run ID. Timing run ID corresponds to the different  timing runs within a race.
[**race_rosters_get**](RaceApi.md#race_rosters_get) | **GET** /race/rosters | Retrieves the team rosters for a specified race.
[**race_season_get**](RaceApi.md#race_season_get) | **GET** /race/season | Retrieves races for a specified season and series.
[**race_stage_results_get**](RaceApi.md#race_stage_results_get) | **GET** /race/stage-results | Retrieves a list of stage results for a specified race.
[**race_stages_get**](RaceApi.md#race_stages_get) | **GET** /race/stages | Retrieves the stage information for a specified race.
[**race_stat_reports_get**](RaceApi.md#race_stat_reports_get) | **GET** /race/stat-reports | 
[**race_viewmodel_get**](RaceApi.md#race_viewmodel_get) | **GET** /race/viewmodel | Retrieves a comprehensive view model for a specified race.
[**race_weekend_schedule_get**](RaceApi.md#race_weekend_schedule_get) | **GET** /race/weekend-schedule | Retrieves the weekend schedule for a specified race.

# **race_cautions_get**
> list[Caution] race_cautions_get(race_id=race_id)

Retrieves a list of cautions for a given race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves a list of cautions for a given race.
    api_response = api_instance.race_cautions_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_cautions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

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

Retrieves a list of discipline updates for a given race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves a list of discipline updates for a given race.
    api_response = api_instance.race_discipline_updates_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_discipline_updates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

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

Retrieves a list of entries for a given race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves a list of entries for a given race.
    api_response = api_instance.race_entries_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_entries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

### Return type

[**list[RunEntry]**](RunEntry.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_entry_get**
> RunEntry race_entry_get(entry_id=entry_id)

Retrieves the details of a race entry.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
entry_id = 56 # int | The unique identifier of the race entry. (optional)

try:
    # Retrieves the details of a race entry.
    api_response = api_instance.race_entry_get(entry_id=entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_entry_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **int**| The unique identifier of the race entry. | [optional] 

### Return type

[**RunEntry**](RunEntry.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_fastest_laps_get**
> FastestLapResult race_fastest_laps_get(race_id=race_id)

Retrieves the fastest lap information for a specified race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves the fastest lap information for a specified race.
    api_response = api_instance.race_fastest_laps_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_fastest_laps_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

### Return type

[**FastestLapResult**](FastestLapResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_get**
> RaceDetails race_get(race_id=race_id)

Retrieves detailed information for a given race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves detailed information for a given race.
    api_response = api_instance.race_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

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

Retrieves a list of infractions for a given race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves a list of infractions for a given race.
    api_response = api_instance.race_infractions_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_infractions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

### Return type

[**list[RaceInfraction]**](RaceInfraction.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_lap_chart_get**
> LapChartResult race_lap_chart_get(race_id=race_id)

Retrieves lap by lap driver information for a specified race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves lap by lap driver information for a specified race.
    api_response = api_instance.race_lap_chart_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_lap_chart_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

### Return type

[**LapChartResult**](LapChartResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **race_lap_leaders_get**
> list[LapLeader] race_lap_leaders_get(race_id=race_id)

Retrieves a list of lap leaders for a given race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves a list of lap leaders for a given race.
    api_response = api_instance.race_lap_leaders_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_lap_leaders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

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

Retrieves the active run session information.

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
    # Retrieves the active run session information.
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

Retrieves a list of race details based on historic race ID or a date range.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
history_race_id = 56 # int | The unique identifier of the historic race. (e.g. 5596) (optional)
date_start = '2013-10-20' # date | The start date of the date range in yyyy-mm-dd format. (optional)
date_end = '2013-10-20' # date | The end date of the date range in yyyy-mm-dd format. (optional)

try:
    # Retrieves a list of race details based on historic race ID or a date range.
    api_response = api_instance.race_lookup_get(history_race_id=history_race_id, date_start=date_start, date_end=date_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_lookup_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history_race_id** | **int**| The unique identifier of the historic race. (e.g. 5596) | [optional] 
 **date_start** | **date**| The start date of the date range in yyyy-mm-dd format. | [optional] 
 **date_end** | **date**| The end date of the date range in yyyy-mm-dd format. | [optional] 

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

Retrieves a list of pit stops for a given race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves a list of pit stops for a given race.
    api_response = api_instance.race_pitstops_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_pitstops_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

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

Retrieves practice run results for a given race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves practice run results for a given race.
    api_response = api_instance.race_practice_results_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_practice_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

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

Retrieves qualifying run results for a given race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves qualifying run results for a given race.
    api_response = api_instance.race_qualifying_results_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_qualifying_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

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

Retrieves the race results for a specified race

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
    # Retrieves the race results for a specified race
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

Retrieves the run results for a specified race and timing run ID. Timing run ID corresponds to the different  timing runs within a race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)
timing_run_id = 56 # int | The unique identifier of the timing run within the race. (optional)

try:
    # Retrieves the run results for a specified race and timing run ID. Timing run ID corresponds to the different  timing runs within a race.
    api_response = api_instance.race_results_get(race_id=race_id, timing_run_id=timing_run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 
 **timing_run_id** | **int**| The unique identifier of the timing run within the race. | [optional] 

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

Retrieves the team rosters for a specified race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves the team rosters for a specified race.
    api_response = api_instance.race_rosters_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_rosters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

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

Retrieves races for a specified season and series.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
season = 56 # int | The season for which to retrieve races. (optional)
series_id = 56 # int | Series identifier. Common values are 1 for Cup, 2 for O'Reilly, and 3 for Truck. (optional)

try:
    # Retrieves races for a specified season and series.
    api_response = api_instance.race_season_get(season=season, series_id=series_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_season_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| The season for which to retrieve races. | [optional] 
 **series_id** | **int**| Series identifier. Common values are 1 for Cup, 2 for O&#x27;Reilly, and 3 for Truck. | [optional] 

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

Retrieves a list of stage results for a specified race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves a list of stage results for a specified race.
    api_response = api_instance.race_stage_results_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_stage_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

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

Retrieves the stage information for a specified race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves the stage information for a specified race.
    api_response = api_instance.race_stages_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_stages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

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

Retrieves a comprehensive view model for a specified race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves a comprehensive view model for a specified race.
    api_response = api_instance.race_viewmodel_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_viewmodel_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

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

Retrieves the weekend schedule for a specified race.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.RaceApi(nascar_data_client.ApiClient(configuration))
race_id = 56 # int | The unique identifier of the race. (optional)

try:
    # Retrieves the weekend schedule for a specified race.
    api_response = api_instance.race_weekend_schedule_get(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_weekend_schedule_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_id** | **int**| The unique identifier of the race. | [optional] 

### Return type

[**list[WeekendSchedule]**](WeekendSchedule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

