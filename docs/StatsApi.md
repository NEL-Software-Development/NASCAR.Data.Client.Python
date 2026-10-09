# nascar_data_client.StatsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stats_laps_get**](StatsApi.md#stats_laps_get) | **GET** /stats/laps | Retrieves a bounded page of per-passing lap statistics using optional filters.
[**stats_loop_stats_get**](StatsApi.md#stats_loop_stats_get) | **GET** /stats/loop-stats | Retrieves a list of driver loop statistics for a given race.
[**stats_race_get**](StatsApi.md#stats_race_get) | **GET** /stats/race | Retrieves a bounded page of driver race statistics using optional filters.
[**stats_report_get**](StatsApi.md#stats_report_get) | **GET** /stats/report | Retrieves a specific statistical report file for a given key, which typically corresponds to a report path or identifier returned by /reports.
[**stats_reports_get**](StatsApi.md#stats_reports_get) | **GET** /stats/reports | Retrieves a list of available statistical report paths for a given race.
[**stats_season_get**](StatsApi.md#stats_season_get) | **GET** /stats/season | Retrieves a list of driver season statistics for a given series and season.

# **stats_laps_get**
> LapStatStatsPage stats_laps_get(race_event_key=race_event_key, run_id=run_id, competitor_id=competitor_id, lap_from=lap_from, lap_to=lap_to, leader_lap_from=leader_lap_from, leader_lap_to=leader_lap_to, flag_state=flag_state, race_rank_from=race_rank_from, race_rank_to=race_rank_to, track_position_from=track_position_from, track_position_to=track_position_to, laptime_ms_from=laptime_ms_from, laptime_ms_to=laptime_ms_to, date_from=date_from, date_to=date_to, page=page, page_size=page_size, race_id=race_id, history_race_id=history_race_id, series_id=series_id, season=season, season_from=season_from, season_to=season_to, driver_id=driver_id, vehicle_number=vehicle_number, first_name=first_name, last_name=last_name, driver_name=driver_name, track_id=track_id, track=track)

Retrieves a bounded page of per-passing lap statistics using optional filters.

All filters are optional and combined with AND; no scope is required. Common filters behave as on /stats/race,  except that dates filter start_time (the race's scheduled start, denormalized onto every lap row; inclusive  UTC values) and finishing-position filters do not apply here (no reliable per-lap source; see /stats/race).  Additional filters cover race_event_key (source timing event), run_id, competitor_id, lap_count, leader_lap,  flag_state, race_rank, track_position and laptime_ms. Null source measurements do not match numeric bounds.  Rows are ordered by race_id, race_event_key, run_id, passing_id, not lap number, to preserve stable unique passing identities.  page defaults to 1; page_size defaults to 1000 (maximum 5000). Response: items, page, page_size, has_more.  No total count is computed. Pages can shift if an import completes between requests.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.StatsApi(nascar_data_client.ApiClient(configuration))
race_event_key = 56 # int | Source timing race-event key, independent of the NASCAR One/API race_id. (optional)
run_id = 56 # int | Source timing run identifier. (optional)
competitor_id = 56 # int | Source competitor identifier, not the API driver identifier. (optional)
lap_from = 56 # int | Inclusive minimum competitor lap_count (zero is allowed). (optional)
lap_to = 56 # int | Inclusive maximum competitor lap_count (zero is allowed). (optional)
leader_lap_from = 56 # int | Inclusive minimum leader_lap (zero is allowed). (optional)
leader_lap_to = 56 # int | Inclusive maximum leader_lap (zero is allowed). (optional)
flag_state = 56 # int | Exact source flag-state code (zero or greater). (optional)
race_rank_from = 56 # int | Inclusive minimum race rank (1 or greater). (optional)
race_rank_to = 56 # int | Inclusive maximum race rank (1 or greater). (optional)
track_position_from = 56 # int | Inclusive minimum track position (1 or greater). (optional)
track_position_to = 56 # int | Inclusive maximum track position (1 or greater). (optional)
laptime_ms_from = 56 # int | Inclusive minimum lap time in milliseconds (zero or greater). (optional)
laptime_ms_to = 56 # int | Inclusive maximum lap time in milliseconds (zero or greater). (optional)
date_from = '2013-10-20T19:20:30+01:00' # datetime | Inclusive lower UTC bound for start_time (the race's scheduled start, denormalized onto every lap row), year 1900-9999. Supply no source-local offset; this is UTC, unlike RaceStatsQuery.date_from. (optional)
date_to = '2013-10-20T19:20:30+01:00' # datetime | Inclusive upper UTC bound for start_time (the race's scheduled start, denormalized onto every lap row), year 1900-9999. A date without a time means midnight, not end of day. This is UTC, unlike RaceStatsQuery.date_to. (optional)
page = 56 # int | One-based page number. The resulting offset must fit a signed 32-bit integer. (optional)
page_size = 56 # int | Rows per page: 1-5000; defaults to 1000. Pagination cannot be disabled. (optional)
race_id = 56 # int | NASCAR One/API race identifier (not the History race identifier). (optional)
history_race_id = 56 # int | History race identifier, independent of race_id. (optional)
series_id = 56 # int | API series identifier. (optional)
season = 56 # int | Exact season year (1900-9999). (optional)
season_from = 56 # int | Inclusive first season year (1900-9999). (optional)
season_to = 56 # int | Inclusive last season year (1900-9999). (optional)
driver_id = 56 # int | API driver identifier. Records without a driver mapping cannot match this filter. (optional)
vehicle_number = 'vehicle_number_example' # str | Exact vehicle number as text; leading zeroes are significant. (optional)
first_name = 'first_name_example' # str | Substring of the driver's first name, using database collation. (optional)
last_name = 'last_name_example' # str | Substring of the driver's last name, using database collation. (optional)
driver_name = 'driver_name_example' # str | Substring of first name + space + last name, using database collation. (optional)
track_id = 56 # int | NASCAR One/API track identifier. (optional)
track = 'track_example' # str | Substring of the track name, using database collation. (optional)

try:
    # Retrieves a bounded page of per-passing lap statistics using optional filters.
    api_response = api_instance.stats_laps_get(race_event_key=race_event_key, run_id=run_id, competitor_id=competitor_id, lap_from=lap_from, lap_to=lap_to, leader_lap_from=leader_lap_from, leader_lap_to=leader_lap_to, flag_state=flag_state, race_rank_from=race_rank_from, race_rank_to=race_rank_to, track_position_from=track_position_from, track_position_to=track_position_to, laptime_ms_from=laptime_ms_from, laptime_ms_to=laptime_ms_to, date_from=date_from, date_to=date_to, page=page, page_size=page_size, race_id=race_id, history_race_id=history_race_id, series_id=series_id, season=season, season_from=season_from, season_to=season_to, driver_id=driver_id, vehicle_number=vehicle_number, first_name=first_name, last_name=last_name, driver_name=driver_name, track_id=track_id, track=track)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats_laps_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **race_event_key** | **int**| Source timing race-event key, independent of the NASCAR One/API race_id. | [optional] 
 **run_id** | **int**| Source timing run identifier. | [optional] 
 **competitor_id** | **int**| Source competitor identifier, not the API driver identifier. | [optional] 
 **lap_from** | **int**| Inclusive minimum competitor lap_count (zero is allowed). | [optional] 
 **lap_to** | **int**| Inclusive maximum competitor lap_count (zero is allowed). | [optional] 
 **leader_lap_from** | **int**| Inclusive minimum leader_lap (zero is allowed). | [optional] 
 **leader_lap_to** | **int**| Inclusive maximum leader_lap (zero is allowed). | [optional] 
 **flag_state** | **int**| Exact source flag-state code (zero or greater). | [optional] 
 **race_rank_from** | **int**| Inclusive minimum race rank (1 or greater). | [optional] 
 **race_rank_to** | **int**| Inclusive maximum race rank (1 or greater). | [optional] 
 **track_position_from** | **int**| Inclusive minimum track position (1 or greater). | [optional] 
 **track_position_to** | **int**| Inclusive maximum track position (1 or greater). | [optional] 
 **laptime_ms_from** | **int**| Inclusive minimum lap time in milliseconds (zero or greater). | [optional] 
 **laptime_ms_to** | **int**| Inclusive maximum lap time in milliseconds (zero or greater). | [optional] 
 **date_from** | **datetime**| Inclusive lower UTC bound for start_time (the race&#x27;s scheduled start, denormalized onto every lap row), year 1900-9999. Supply no source-local offset; this is UTC, unlike RaceStatsQuery.date_from. | [optional] 
 **date_to** | **datetime**| Inclusive upper UTC bound for start_time (the race&#x27;s scheduled start, denormalized onto every lap row), year 1900-9999. A date without a time means midnight, not end of day. This is UTC, unlike RaceStatsQuery.date_to. | [optional] 
 **page** | **int**| One-based page number. The resulting offset must fit a signed 32-bit integer. | [optional] 
 **page_size** | **int**| Rows per page: 1-5000; defaults to 1000. Pagination cannot be disabled. | [optional] 
 **race_id** | **int**| NASCAR One/API race identifier (not the History race identifier). | [optional] 
 **history_race_id** | **int**| History race identifier, independent of race_id. | [optional] 
 **series_id** | **int**| API series identifier. | [optional] 
 **season** | **int**| Exact season year (1900-9999). | [optional] 
 **season_from** | **int**| Inclusive first season year (1900-9999). | [optional] 
 **season_to** | **int**| Inclusive last season year (1900-9999). | [optional] 
 **driver_id** | **int**| API driver identifier. Records without a driver mapping cannot match this filter. | [optional] 
 **vehicle_number** | **str**| Exact vehicle number as text; leading zeroes are significant. | [optional] 
 **first_name** | **str**| Substring of the driver&#x27;s first name, using database collation. | [optional] 
 **last_name** | **str**| Substring of the driver&#x27;s last name, using database collation. | [optional] 
 **driver_name** | **str**| Substring of first name + space + last name, using database collation. | [optional] 
 **track_id** | **int**| NASCAR One/API track identifier. | [optional] 
 **track** | **str**| Substring of the track name, using database collation. | [optional] 

### Return type

[**LapStatStatsPage**](LapStatStatsPage.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **stats_race_get**
> RaceStatStatsPage stats_race_get(history_driver_id=history_driver_id, finish_position_from=finish_position_from, finish_position_to=finish_position_to, page=page, page_size=page_size, race_id=race_id, history_race_id=history_race_id, series_id=series_id, season=season, season_from=season_from, season_to=season_to, driver_id=driver_id, vehicle_number=vehicle_number, first_name=first_name, last_name=last_name, driver_name=driver_name, track_id=track_id, track=track, date_from=date_from, date_to=date_to)

Retrieves a bounded page of driver race statistics using optional filters.

All filters are optional and combined with AND. No race, season, series or driver scope is required.  IDs distinguish NASCAR One/API identities from History identities; unmapped driver_id values remain null.  Vehicle numbers retain leading zeroes. Name/track filters use substring matching and database collation.  Dates are inclusive source-local clock values without a UTC offset, using actual_date then scheduled_date.  Rows are ordered by race_id, history_driver_id. page defaults to 1; page_size defaults to 1000 (maximum 5000).  The response contains items, page, page_size and has_more; no total count is computed.  Pages reflect the current snapshot and can shift if an import completes between requests.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.StatsApi(nascar_data_client.ApiClient(configuration))
history_driver_id = 56 # int | History driver identifier, independent of the nullable API driver_id. (optional)
finish_position_from = 56 # int | Inclusive minimum finishing position (1 or greater). (optional)
finish_position_to = 56 # int | Inclusive maximum finishing position (1 or greater). (optional)
page = 56 # int | One-based page number. The resulting offset must fit a signed 32-bit integer. (optional)
page_size = 56 # int | Rows per page: 1-5000; defaults to 1000. Pagination cannot be disabled. (optional)
race_id = 56 # int | NASCAR One/API race identifier (not the History race identifier). (optional)
history_race_id = 56 # int | History race identifier, independent of race_id. (optional)
series_id = 56 # int | API series identifier. (optional)
season = 56 # int | Exact season year (1900-9999). (optional)
season_from = 56 # int | Inclusive first season year (1900-9999). (optional)
season_to = 56 # int | Inclusive last season year (1900-9999). (optional)
driver_id = 56 # int | API driver identifier. Records without a driver mapping cannot match this filter. (optional)
vehicle_number = 'vehicle_number_example' # str | Exact vehicle number as text; leading zeroes are significant. (optional)
first_name = 'first_name_example' # str | Substring of the driver's first name, using database collation. (optional)
last_name = 'last_name_example' # str | Substring of the driver's last name, using database collation. (optional)
driver_name = 'driver_name_example' # str | Substring of first name + space + last name, using database collation. (optional)
track_id = 56 # int | NASCAR One/API track identifier. (optional)
track = 'track_example' # str | Substring of the track name, using database collation. (optional)
date_from = '2013-10-20T19:20:30+01:00' # datetime | Inclusive lower source-local date/time bound, year 1900-9999, filtering actual_date (falling back to scheduled_date). Supply no UTC offset. See LapStatsQuery.date_from for the lap endpoint's UTC-based semantics. (optional)
date_to = '2013-10-20T19:20:30+01:00' # datetime | Inclusive upper source-local date/time bound, year 1900-9999, filtering actual_date (falling back to scheduled_date). A date without a time means midnight, not end of day. Supply no UTC offset. See LapStatsQuery.date_to for the lap endpoint's UTC-based semantics. (optional)

try:
    # Retrieves a bounded page of driver race statistics using optional filters.
    api_response = api_instance.stats_race_get(history_driver_id=history_driver_id, finish_position_from=finish_position_from, finish_position_to=finish_position_to, page=page, page_size=page_size, race_id=race_id, history_race_id=history_race_id, series_id=series_id, season=season, season_from=season_from, season_to=season_to, driver_id=driver_id, vehicle_number=vehicle_number, first_name=first_name, last_name=last_name, driver_name=driver_name, track_id=track_id, track=track, date_from=date_from, date_to=date_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->stats_race_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history_driver_id** | **int**| History driver identifier, independent of the nullable API driver_id. | [optional] 
 **finish_position_from** | **int**| Inclusive minimum finishing position (1 or greater). | [optional] 
 **finish_position_to** | **int**| Inclusive maximum finishing position (1 or greater). | [optional] 
 **page** | **int**| One-based page number. The resulting offset must fit a signed 32-bit integer. | [optional] 
 **page_size** | **int**| Rows per page: 1-5000; defaults to 1000. Pagination cannot be disabled. | [optional] 
 **race_id** | **int**| NASCAR One/API race identifier (not the History race identifier). | [optional] 
 **history_race_id** | **int**| History race identifier, independent of race_id. | [optional] 
 **series_id** | **int**| API series identifier. | [optional] 
 **season** | **int**| Exact season year (1900-9999). | [optional] 
 **season_from** | **int**| Inclusive first season year (1900-9999). | [optional] 
 **season_to** | **int**| Inclusive last season year (1900-9999). | [optional] 
 **driver_id** | **int**| API driver identifier. Records without a driver mapping cannot match this filter. | [optional] 
 **vehicle_number** | **str**| Exact vehicle number as text; leading zeroes are significant. | [optional] 
 **first_name** | **str**| Substring of the driver&#x27;s first name, using database collation. | [optional] 
 **last_name** | **str**| Substring of the driver&#x27;s last name, using database collation. | [optional] 
 **driver_name** | **str**| Substring of first name + space + last name, using database collation. | [optional] 
 **track_id** | **int**| NASCAR One/API track identifier. | [optional] 
 **track** | **str**| Substring of the track name, using database collation. | [optional] 
 **date_from** | **datetime**| Inclusive lower source-local date/time bound, year 1900-9999, filtering actual_date (falling back to scheduled_date). Supply no UTC offset. See LapStatsQuery.date_from for the lap endpoint&#x27;s UTC-based semantics. | [optional] 
 **date_to** | **datetime**| Inclusive upper source-local date/time bound, year 1900-9999, filtering actual_date (falling back to scheduled_date). A date without a time means midnight, not end of day. Supply no UTC offset. See LapStatsQuery.date_to for the lap endpoint&#x27;s UTC-based semantics. | [optional] 

### Return type

[**RaceStatStatsPage**](RaceStatStatsPage.md)

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

