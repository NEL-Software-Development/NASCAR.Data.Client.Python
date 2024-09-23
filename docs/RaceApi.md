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
[**race_loop_stats_get**](RaceApi.md#race_loop_stats_get) | **GET** /race/loop-stats | 
[**race_pitstops_get**](RaceApi.md#race_pitstops_get) | **GET** /race/pitstops | 
[**race_practice_results_get**](RaceApi.md#race_practice_results_get) | **GET** /race/practice-results | 
[**race_qualifying_results_get**](RaceApi.md#race_qualifying_results_get) | **GET** /race/qualifying-results | 
[**race_race_results_get**](RaceApi.md#race_race_results_get) | **GET** /race/race-results | 
[**race_rosters_get**](RaceApi.md#race_rosters_get) | **GET** /race/rosters | 
[**race_season_get**](RaceApi.md#race_season_get) | **GET** /race/season | 
[**race_stage_results_get**](RaceApi.md#race_stage_results_get) | **GET** /race/stage-results | 
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

