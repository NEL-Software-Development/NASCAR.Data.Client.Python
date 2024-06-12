# nascar_data_client.RaceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cautions**](RaceApi.md#cautions) | **GET** /race/cautions | 
[**discipline_updates**](RaceApi.md#discipline_updates) | **GET** /race/discipline-updates | 
[**entries**](RaceApi.md#entries) | **GET** /race/entries | 
[**infractions**](RaceApi.md#infractions) | **GET** /race/infractions | 
[**lap_leaders**](RaceApi.md#lap_leaders) | **GET** /race/lap-leaders | 
[**loop_stats**](RaceApi.md#loop_stats) | **GET** /race/loop-stats | 
[**pit_stops**](RaceApi.md#pit_stops) | **GET** /race/pitstops | 
[**practice_results**](RaceApi.md#practice_results) | **GET** /race/practice-results | 
[**qualifying_results**](RaceApi.md#qualifying_results) | **GET** /race/qualifying-results | 
[**race**](RaceApi.md#race) | **GET** /race | 
[**race_results**](RaceApi.md#race_results) | **GET** /race/race-results | 
[**race_season**](RaceApi.md#race_season) | **GET** /race/season | 
[**rosters**](RaceApi.md#rosters) | **GET** /race/rosters | 
[**stage_results**](RaceApi.md#stage_results) | **GET** /race/stage-results | 
[**view_model**](RaceApi.md#view_model) | **GET** /race/viewmodel | 
[**weekend_schedule**](RaceApi.md#weekend_schedule) | **GET** /race/weekend-schedule | 

# **cautions**
> list[Caution] cautions(race_id=race_id)



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
    api_response = api_instance.cautions(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->cautions: %s\n" % e)
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

# **discipline_updates**
> list[DisciplineUpdate] discipline_updates(race_id=race_id)



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
    api_response = api_instance.discipline_updates(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->discipline_updates: %s\n" % e)
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

# **entries**
> list[RunEntry] entries(race_id=race_id)



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
    api_response = api_instance.entries(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->entries: %s\n" % e)
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

# **infractions**
> list[RaceInfraction] infractions(race_id=race_id)



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
    api_response = api_instance.infractions(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->infractions: %s\n" % e)
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

# **lap_leaders**
> list[LapLeader] lap_leaders(race_id=race_id)



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
    api_response = api_instance.lap_leaders(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->lap_leaders: %s\n" % e)
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

# **loop_stats**
> list[LoopStat] loop_stats(race_id=race_id)



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
    api_response = api_instance.loop_stats(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->loop_stats: %s\n" % e)
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

# **pit_stops**
> list[Pitstop] pit_stops(race_id=race_id)



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
    api_response = api_instance.pit_stops(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->pit_stops: %s\n" % e)
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

# **practice_results**
> list[PracticeRunResults] practice_results(race_id=race_id)



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
    api_response = api_instance.practice_results(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->practice_results: %s\n" % e)
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

# **qualifying_results**
> list[QualifyingRunResults] qualifying_results(race_id=race_id)



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
    api_response = api_instance.qualifying_results(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->qualifying_results: %s\n" % e)
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

# **race**
> RaceDetails race(race_id=race_id)



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
    api_response = api_instance.race(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race: %s\n" % e)
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

# **race_results**
> list[RaceRunResults] race_results(race_id=race_id)



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
    api_response = api_instance.race_results(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_results: %s\n" % e)
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

# **race_season**
> list[list[Race]] race_season(season=season, series_id=series_id)



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
    api_response = api_instance.race_season(season=season, series_id=series_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->race_season: %s\n" % e)
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

# **rosters**
> list[TeamRoster] rosters(race_id=race_id)



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
    api_response = api_instance.rosters(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->rosters: %s\n" % e)
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

# **stage_results**
> list[StageRunResults] stage_results(race_id=race_id)



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
    api_response = api_instance.stage_results(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->stage_results: %s\n" % e)
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

# **view_model**
> RaceViewModel view_model(race_id=race_id)



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
    api_response = api_instance.view_model(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->view_model: %s\n" % e)
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

# **weekend_schedule**
> list[WeekendSchedule] weekend_schedule(race_id=race_id)



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
    api_response = api_instance.weekend_schedule(race_id=race_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RaceApi->weekend_schedule: %s\n" % e)
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

