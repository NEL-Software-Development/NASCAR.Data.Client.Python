# nascar-data-client

- API version: 1.0
- Package version: 1.0.0

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

Installing directly from Github

```sh
pip install git+https://github.com/NEL-Software-Development/NASCAR.Data.Client.Python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/NEL-Software-Development/NASCAR.Data.Client.Python.git`)

Then import the package:
```python
import nascar_data_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import nascar_data_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.AccountApi(nascar_data_client.ApiClient(configuration))
refresh_token = 'refresh_token_example' # str |  (optional)

try:
    api_response = api_instance.refresh_token(refresh_token=refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->refresh_token: %s\n" % e)
```


## Documentation for API Endpoints

All URIs are relative to */api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**account_refresh_token_get**](docs/AccountApi.md#account_refresh_token_get) | **GET** /account/refresh-token | Refreshes an expired authentication token using a refresh token.
*CompanyApi* | [**company_get**](docs/CompanyApi.md#company_get) | **GET** /company | Retrieves a single company by ID.
*CompanyApi* | [**company_search_get**](docs/CompanyApi.md#company_search_get) | **GET** /company/search | Searches for companies by name or keyword.
*DriverApi* | [**driver_get**](docs/DriverApi.md#driver_get) | **GET** /driver | Retrieves a single driver by driver ID.
*DriverApi* | [**driver_season_finishes_get**](docs/DriverApi.md#driver_season_finishes_get) | **GET** /driver/season-finishes | Lists season finish results for a specific driver within a series and season.
*DriverApi* | [**driver_season_get**](docs/DriverApi.md#driver_season_get) | **GET** /driver/season | Lists all drivers for a given series and race season.
*DriverSummaryApi* | [**driver_summary_get**](docs/DriverSummaryApi.md#driver_summary_get) | **GET** /driver-summary | Returns a summary of a driver&#x27;s performance for a given series and season, including statistics such as wins, top 5s, top 10s, poles, and more.
*ERDPApi* | [**erdp_topics_get**](docs/ERDPApi.md#erdp_topics_get) | **GET** /erdp/topics | Get a users erdp topics.
*InspectionsApi* | [**inspections_aim_id_get**](docs/InspectionsApi.md#inspections_aim_id_get) | **GET** /inspections/aim/{id} | For use by the AIM system
*InspectionsApi* | [**inspections_device_numbers_get**](docs/InspectionsApi.md#inspections_device_numbers_get) | **GET** /inspections/device-numbers | For use by the MLS system
*InspectionsApi* | [**inspections_idr_get**](docs/InspectionsApi.md#inspections_idr_get) | **GET** /inspections/idr | For use by the AIM system
*InspectionsApi* | [**inspections_oss_get**](docs/InspectionsApi.md#inspections_oss_get) | **GET** /inspections/oss | Retrieves a list of OSS scans for a specific race.
*InspectionsApi* | [**inspections_submissions_technique_get**](docs/InspectionsApi.md#inspections_submissions_technique_get) | **GET** /inspections/submissions/technique | For use by Technique chassis builders to track submissions
*InspectionsApi* | [**inspections_vehicle_weights_get**](docs/InspectionsApi.md#inspections_vehicle_weights_get) | **GET** /inspections/vehicle-weights | Retrieves a list of vehicle weights for a specific race.
*JournalFilesApi* | [**journal_get**](docs/JournalFilesApi.md#journal_get) | **GET** /journal | 
*OpticalTrackingApi* | [**optical_tracking_utm_offsets_get**](docs/OpticalTrackingApi.md#optical_tracking_utm_offsets_get) | **GET** /optical-tracking/utm-offsets | 
*PointsApi* | [**points_driver_points_get**](docs/PointsApi.md#points_driver_points_get) | **GET** /points/driver-points | Retrieves driver points for a specific race.
*PointsApi* | [**points_manufacturer_points_get**](docs/PointsApi.md#points_manufacturer_points_get) | **GET** /points/manufacturer-points | Retrieves manufacturer points for a specific season, series, and optionally a specific race.
*PointsApi* | [**points_owner_points_get**](docs/PointsApi.md#points_owner_points_get) | **GET** /points/owner-points | Retrieves owner points for a specific season, series, and optionally a specific race.
*RaceApi* | [**race_cautions_get**](docs/RaceApi.md#race_cautions_get) | **GET** /race/cautions | Retrieves a list of cautions for a given race.
*RaceApi* | [**race_discipline_updates_get**](docs/RaceApi.md#race_discipline_updates_get) | **GET** /race/discipline-updates | Retrieves a list of discipline updates for a given race.
*RaceApi* | [**race_entries_get**](docs/RaceApi.md#race_entries_get) | **GET** /race/entries | Retrieves a list of entries for a given race.
*RaceApi* | [**race_entry_get**](docs/RaceApi.md#race_entry_get) | **GET** /race/entry | Retrieves the details of a race entry.
*RaceApi* | [**race_fastest_laps_get**](docs/RaceApi.md#race_fastest_laps_get) | **GET** /race/fastest-laps | Retrieves the fastest lap information for a specified race.
*RaceApi* | [**race_get**](docs/RaceApi.md#race_get) | **GET** /race | Retrieves detailed information for a given race.
*RaceApi* | [**race_infractions_get**](docs/RaceApi.md#race_infractions_get) | **GET** /race/infractions | Retrieves a list of infractions for a given race.
*RaceApi* | [**race_lap_chart_get**](docs/RaceApi.md#race_lap_chart_get) | **GET** /race/lap-chart | Retrieves lap by lap driver information for a specified race.
*RaceApi* | [**race_lap_leaders_get**](docs/RaceApi.md#race_lap_leaders_get) | **GET** /race/lap-leaders | Retrieves a list of lap leaders for a given race.
*RaceApi* | [**race_live_session_get**](docs/RaceApi.md#race_live_session_get) | **GET** /race/live-session | Retrieves the active run session information.
*RaceApi* | [**race_lookup_get**](docs/RaceApi.md#race_lookup_get) | **GET** /race/lookup | Retrieves a list of race details based on historic race ID or a date range.
*RaceApi* | [**race_loop_stats_get**](docs/RaceApi.md#race_loop_stats_get) | **GET** /race/loop-stats | 
*RaceApi* | [**race_pitstops_get**](docs/RaceApi.md#race_pitstops_get) | **GET** /race/pitstops | Retrieves a list of pit stops for a given race.
*RaceApi* | [**race_practice_results_get**](docs/RaceApi.md#race_practice_results_get) | **GET** /race/practice-results | Retrieves practice run results for a given race.
*RaceApi* | [**race_qualifying_results_get**](docs/RaceApi.md#race_qualifying_results_get) | **GET** /race/qualifying-results | Retrieves qualifying run results for a given race.
*RaceApi* | [**race_race_results_get**](docs/RaceApi.md#race_race_results_get) | **GET** /race/race-results | Retrieves the race results for a specified race
*RaceApi* | [**race_report_get**](docs/RaceApi.md#race_report_get) | **GET** /race/report | 
*RaceApi* | [**race_results_get**](docs/RaceApi.md#race_results_get) | **GET** /race/results | Retrieves the run results for a specified race and timing run ID. Timing run ID corresponds to the different  timing runs within a race.
*RaceApi* | [**race_rosters_get**](docs/RaceApi.md#race_rosters_get) | **GET** /race/rosters | Retrieves the team rosters for a specified race.
*RaceApi* | [**race_season_get**](docs/RaceApi.md#race_season_get) | **GET** /race/season | Retrieves races for a specified season and series.
*RaceApi* | [**race_stage_results_get**](docs/RaceApi.md#race_stage_results_get) | **GET** /race/stage-results | Retrieves a list of stage results for a specified race.
*RaceApi* | [**race_stages_get**](docs/RaceApi.md#race_stages_get) | **GET** /race/stages | Retrieves the stage information for a specified race.
*RaceApi* | [**race_stat_reports_get**](docs/RaceApi.md#race_stat_reports_get) | **GET** /race/stat-reports | 
*RaceApi* | [**race_viewmodel_get**](docs/RaceApi.md#race_viewmodel_get) | **GET** /race/viewmodel | Retrieves a comprehensive view model for a specified race.
*RaceApi* | [**race_weekend_schedule_get**](docs/RaceApi.md#race_weekend_schedule_get) | **GET** /race/weekend-schedule | Retrieves the weekend schedule for a specified race.
*RaceWeekApi* | [**race_week_details_get**](docs/RaceWeekApi.md#race_week_details_get) | **GET** /race-week/details | Retrieves details for a specific race week event given its unique identifier.
*RaceWeekApi* | [**race_week_live_get**](docs/RaceWeekApi.md#race_week_live_get) | **GET** /race-week/live | Retrieves a list of live race events
*RaceWeekApi* | [**race_week_season_get**](docs/RaceWeekApi.md#race_week_season_get) | **GET** /race-week/season | Retrieves all race week events for a given season, ordered by start date. This includes both past and upcoming events within the specified season.
*SeriesApi* | [**series_get**](docs/SeriesApi.md#series_get) | **GET** /series | Retrieves a list of all racing series, including their unique identifiers and names.
*SeriesApi* | [**series_season_get**](docs/SeriesApi.md#series_season_get) | **GET** /series/season | 
*StatsApi* | [**stats_loop_stats_get**](docs/StatsApi.md#stats_loop_stats_get) | **GET** /stats/loop-stats | Retrieves a list of driver loop statistics for a given race.
*StatsApi* | [**stats_report_get**](docs/StatsApi.md#stats_report_get) | **GET** /stats/report | Retrieves a specific statistical report file for a given key, which typically corresponds to a report path or identifier returned by /reports.
*StatsApi* | [**stats_reports_get**](docs/StatsApi.md#stats_reports_get) | **GET** /stats/reports | Retrieves a list of available statistical report paths for a given race.
*StatsApi* | [**stats_season_get**](docs/StatsApi.md#stats_season_get) | **GET** /stats/season | Retrieves a list of driver season statistics for a given series and season.
*TracksApi* | [**track_details_get**](docs/TracksApi.md#track_details_get) | **GET** /track-details | Retrieves detailed information about a specific track, including its history, notable events, and other relevant data, given the track&#x27;s unique identifier from /tracks.
*TracksApi* | [**tracks_get**](docs/TracksApi.md#tracks_get) | **GET** /tracks | Retrieves a list of all tracks in the NASCAR database, including basic information such as track name, location, and type.
*VehicleApi* | [**vehicle_get**](docs/VehicleApi.md#vehicle_get) | **GET** /vehicle | Retrieves detailed information about a specific vehicle, including its finishes, given the vehicle&#x27;s unique identifier.
*VehicleApi* | [**vehicle_season_finishes_get**](docs/VehicleApi.md#vehicle_season_finishes_get) | **GET** /vehicle/season-finishes | Retrieves a list of all finishes for a specific vehicle across an entire season, given the season, series, and vehicle number.
*VendorApi* | [**vendor_cone_coordinates_post**](docs/VendorApi.md#vendor_cone_coordinates_post) | **POST** /vendor/cone-coordinates | 
*VendorApi* | [**vendor_crl_testresult_post**](docs/VendorApi.md#vendor_crl_testresult_post) | **POST** /vendor/crl_testresult | 
*VendorApi* | [**vendor_tires_post**](docs/VendorApi.md#vendor_tires_post) | **POST** /vendor/tires | 
*VendorApi* | [**vendor_utm_offsets_post**](docs/VendorApi.md#vendor_utm_offsets_post) | **POST** /vendor/utm_offsets | 
*VendorApi* | [**vendor_wicket_request_post**](docs/VendorApi.md#vendor_wicket_request_post) | **POST** /vendor/wicket_request | 

## Documentation For Models

 - [ActiveRun](docs/ActiveRun.md)
 - [AvailableReport](docs/AvailableReport.md)
 - [AvailableReports](docs/AvailableReports.md)
 - [Caution](docs/Caution.md)
 - [ClientERDPDatapoint](docs/ClientERDPDatapoint.md)
 - [ClientERDPSource](docs/ClientERDPSource.md)
 - [ClientERDPTopic](docs/ClientERDPTopic.md)
 - [Company](docs/Company.md)
 - [ConeCoordinates](docs/ConeCoordinates.md)
 - [ConeCoordinatesIngest](docs/ConeCoordinatesIngest.md)
 - [ConeCoordinatesListETLSaveResult](docs/ConeCoordinatesListETLSaveResult.md)
 - [Coordinate](docs/Coordinate.md)
 - [CrlFormFoxResult](docs/CrlFormFoxResult.md)
 - [DisciplineUpdate](docs/DisciplineUpdate.md)
 - [Driver](docs/Driver.md)
 - [DriverPointsSlim](docs/DriverPointsSlim.md)
 - [DriverPointsView](docs/DriverPointsView.md)
 - [DriverSummary](docs/DriverSummary.md)
 - [DriverSummaryByPrincipalRaceID](docs/DriverSummaryByPrincipalRaceID.md)
 - [DriverSummaryBySeason](docs/DriverSummaryBySeason.md)
 - [DriverSummaryByTrack](docs/DriverSummaryByTrack.md)
 - [DriverSummaryByTrackType](docs/DriverSummaryByTrackType.md)
 - [FastestLapAwards](docs/FastestLapAwards.md)
 - [FastestLapResult](docs/FastestLapResult.md)
 - [Flag](docs/Flag.md)
 - [InspectionResult](docs/InspectionResult.md)
 - [LapChart](docs/LapChart.md)
 - [LapChartResult](docs/LapChartResult.md)
 - [LapLeader](docs/LapLeader.md)
 - [LoopStat](docs/LoopStat.md)
 - [ManufacturerPoint](docs/ManufacturerPoint.md)
 - [OSSScan](docs/OSSScan.md)
 - [OpticalTrackingUTMOffset](docs/OpticalTrackingUTMOffset.md)
 - [OpticalTrackingUTMOffsetListETLSaveResult](docs/OpticalTrackingUTMOffsetListETLSaveResult.md)
 - [OwnerPoints](docs/OwnerPoints.md)
 - [OwnerPointsView](docs/OwnerPointsView.md)
 - [PitPath](docs/PitPath.md)
 - [Pitstop](docs/Pitstop.md)
 - [PracticeRunResults](docs/PracticeRunResults.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [QualifyingRunResults](docs/QualifyingRunResults.md)
 - [Race](docs/Race.md)
 - [RaceDetails](docs/RaceDetails.md)
 - [RaceInfraction](docs/RaceInfraction.md)
 - [RaceResult](docs/RaceResult.md)
 - [RaceResultSummary](docs/RaceResultSummary.md)
 - [RaceRunResults](docs/RaceRunResults.md)
 - [RaceViewModel](docs/RaceViewModel.md)
 - [RaceWeek](docs/RaceWeek.md)
 - [RaceWeekDetails](docs/RaceWeekDetails.md)
 - [RepairSubmission](docs/RepairSubmission.md)
 - [Result](docs/Result.md)
 - [RosterMember](docs/RosterMember.md)
 - [RunDetails](docs/RunDetails.md)
 - [RunEntry](docs/RunEntry.md)
 - [RunResult](docs/RunResult.md)
 - [RunResults](docs/RunResults.md)
 - [RunState](docs/RunState.md)
 - [RunType](docs/RunType.md)
 - [SeasonSeries](docs/SeasonSeries.md)
 - [SeasonStat](docs/SeasonStat.md)
 - [Series](docs/Series.md)
 - [Stage](docs/Stage.md)
 - [StageResult](docs/StageResult.md)
 - [StageRunResults](docs/StageRunResults.md)
 - [Status](docs/Status.md)
 - [TeamRoster](docs/TeamRoster.md)
 - [Tire](docs/Tire.md)
 - [TireListETLSaveResult](docs/TireListETLSaveResult.md)
 - [TokenResponse](docs/TokenResponse.md)
 - [Track](docs/Track.md)
 - [TrackConfiguration](docs/TrackConfiguration.md)
 - [TrackDetails](docs/TrackDetails.md)
 - [TrackPath](docs/TrackPath.md)
 - [VehicleDetails](docs/VehicleDetails.md)
 - [VehicleWeight](docs/VehicleWeight.md)
 - [WeekendSchedule](docs/WeekendSchedule.md)
 - [WicketAccountIds](docs/WicketAccountIds.md)
 - [WicketRequest](docs/WicketRequest.md)
 - [WicketResponse](docs/WicketResponse.md)

## Documentation For Authorization


## Bearer



## Author
