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
*RaceApi* | [**race_entries_get**](docs/RaceApi.md#race_entries_get) | **GET** /race/entries | 
*RaceApi* | [**race_get**](docs/RaceApi.md#race_get) | **GET** /race | 
*RaceApi* | [**race_infractions_get**](docs/RaceApi.md#race_infractions_get) | **GET** /race/infractions | 
*RaceApi* | [**race_lap_leaders_get**](docs/RaceApi.md#race_lap_leaders_get) | **GET** /race/lap-leaders | 
*RaceApi* | [**race_loop_stats_get**](docs/RaceApi.md#race_loop_stats_get) | **GET** /race/loop-stats | 
*RaceApi* | [**race_pitstops_get**](docs/RaceApi.md#race_pitstops_get) | **GET** /race/pitstops | 
*RaceApi* | [**race_practice_results_get**](docs/RaceApi.md#race_practice_results_get) | **GET** /race/practice-results | 
*RaceApi* | [**race_qualifying_results_get**](docs/RaceApi.md#race_qualifying_results_get) | **GET** /race/qualifying-results | 
*RaceApi* | [**race_race_results_get**](docs/RaceApi.md#race_race_results_get) | **GET** /race/race-results | 
*RaceApi* | [**race_rosters_get**](docs/RaceApi.md#race_rosters_get) | **GET** /race/rosters | 
*RaceApi* | [**race_season_get**](docs/RaceApi.md#race_season_get) | **GET** /race/season | 
*RaceApi* | [**race_stage_results_get**](docs/RaceApi.md#race_stage_results_get) | **GET** /race/stage-results | 
*RaceApi* | [**race_viewmodel_get**](docs/RaceApi.md#race_viewmodel_get) | **GET** /race/viewmodel | 
*RaceApi* | [**race_weekend_schedule_get**](docs/RaceApi.md#race_weekend_schedule_get) | **GET** /race/weekend-schedule | 
*RaceWeekApi* | [**race_week_details_get**](docs/RaceWeekApi.md#race_week_details_get) | **GET** /race-week/details | 
*RaceWeekApi* | [**race_week_live_get**](docs/RaceWeekApi.md#race_week_live_get) | **GET** /race-week/live | 
*RaceWeekApi* | [**race_week_season_get**](docs/RaceWeekApi.md#race_week_season_get) | **GET** /race-week/season | 
*SeriesApi* | [**series_get**](docs/SeriesApi.md#series_get) | **GET** /series | 
*TracksApi* | [**track_details_get**](docs/TracksApi.md#track_details_get) | **GET** /track-details | 
*TracksApi* | [**tracks_get**](docs/TracksApi.md#tracks_get) | **GET** /tracks | 
*VehicleApi* | [**vehicle_get**](docs/VehicleApi.md#vehicle_get) | **GET** /vehicle | 
*VehicleApi* | [**vehicle_season_finishes_get**](docs/VehicleApi.md#vehicle_season_finishes_get) | **GET** /vehicle/season-finishes | 
*VendorApi* | [**vendor_crl_testresult_post**](docs/VendorApi.md#vendor_crl_testresult_post) | **POST** /vendor/crl_testresult | 
*VendorApi* | [**vendor_tires_post**](docs/VendorApi.md#vendor_tires_post) | **POST** /vendor/tires | 
*VendorApi* | [**vendor_utm_offsets_post**](docs/VendorApi.md#vendor_utm_offsets_post) | **POST** /vendor/utm_offsets | 

## Documentation For Models

 - [Caution](docs/Caution.md)
 - [ClientERDPDatapoint](docs/ClientERDPDatapoint.md)
 - [ClientERDPSource](docs/ClientERDPSource.md)
 - [ClientERDPTopic](docs/ClientERDPTopic.md)
 - [Company](docs/Company.md)
 - [CrlFormFoxResult](docs/CrlFormFoxResult.md)
 - [DevNote](docs/DevNote.md)
 - [DisciplineUpdate](docs/DisciplineUpdate.md)
 - [Driver](docs/Driver.md)
 - [DriverPoint](docs/DriverPoint.md)
 - [DriverSummary](docs/DriverSummary.md)
 - [DriverSummaryByPrincipalRaceID](docs/DriverSummaryByPrincipalRaceID.md)
 - [DriverSummaryBySeason](docs/DriverSummaryBySeason.md)
 - [DriverSummaryByTrack](docs/DriverSummaryByTrack.md)
 - [DriverSummaryByTrackType](docs/DriverSummaryByTrackType.md)
 - [Feedback](docs/Feedback.md)
 - [Flag](docs/Flag.md)
 - [LapLeader](docs/LapLeader.md)
 - [LoopStat](docs/LoopStat.md)
 - [ManufacturerPoint](docs/ManufacturerPoint.md)
 - [OSSScan](docs/OSSScan.md)
 - [OpticalTrackingUTMOffset](docs/OpticalTrackingUTMOffset.md)
 - [OpticalTrackingUTMOffsetListETLSaveResult](docs/OpticalTrackingUTMOffsetListETLSaveResult.md)
 - [OwnerPoint](docs/OwnerPoint.md)
 - [PitPath](docs/PitPath.md)
 - [Pitstop](docs/Pitstop.md)
 - [PracticeRunResults](docs/PracticeRunResults.md)
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
 - [RosterMember](docs/RosterMember.md)
 - [RunDetails](docs/RunDetails.md)
 - [RunEntry](docs/RunEntry.md)
 - [RunResult](docs/RunResult.md)
 - [RunState](docs/RunState.md)
 - [RunType](docs/RunType.md)
 - [Series](docs/Series.md)
 - [StageResult](docs/StageResult.md)
 - [StageRunResults](docs/StageRunResults.md)
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

## Documentation For Authorization


## Bearer



## Author


