# nascar-data-client

- API version: 1.0
- Package version: 1.0.0

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

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

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**refresh_token**](docs/AccountApi.md#refresh_token) | **GET** /account/refresh-token | 
*CompanyApi* | [**find_company**](docs/CompanyApi.md#find_company) | **GET** /company/search | 
*DriverApi* | [**by_season**](docs/DriverApi.md#by_season) | **GET** /driver/season | 
*DriverApi* | [**driver**](docs/DriverApi.md#driver) | **GET** /driver | 
*DriverApi* | [**driver_season_finishes**](docs/DriverApi.md#driver_season_finishes) | **GET** /driver/season-finishes | 
*DriverSummaryApi* | [**driver_summary**](docs/DriverSummaryApi.md#driver_summary) | **GET** /driver-summary | 
*InspectionsApi* | [**o_ss**](docs/InspectionsApi.md#o_ss) | **GET** /inspections/oss | 
*InspectionsApi* | [**vehicle_weights**](docs/InspectionsApi.md#vehicle_weights) | **GET** /inspections/vehicle-weights | 
*NextGenApi* | [**data_points**](docs/NextGenApi.md#data_points) | **GET** /nextgen-datapoints | 
*NextGenApi* | [**sources**](docs/NextGenApi.md#sources) | **GET** /nextgen-sources | 
*OpticalTrackingApi* | [**utm_offsets**](docs/OpticalTrackingApi.md#utm_offsets) | **GET** /utm-offsets | 
*PointsApi* | [**driver_points**](docs/PointsApi.md#driver_points) | **GET** /points/driver-points | 
*PointsApi* | [**manufacturer_points**](docs/PointsApi.md#manufacturer_points) | **GET** /points/manufacturer-points | 
*PointsApi* | [**owner_points**](docs/PointsApi.md#owner_points) | **GET** /points/owner-points | 
*RaceApi* | [**cautions**](docs/RaceApi.md#cautions) | **GET** /race/cautions | 
*RaceApi* | [**discipline_updates**](docs/RaceApi.md#discipline_updates) | **GET** /race/discipline-updates | 
*RaceApi* | [**entries**](docs/RaceApi.md#entries) | **GET** /race/entries | 
*RaceApi* | [**infractions**](docs/RaceApi.md#infractions) | **GET** /race/infractions | 
*RaceApi* | [**lap_leaders**](docs/RaceApi.md#lap_leaders) | **GET** /race/lap-leaders | 
*RaceApi* | [**loop_stats**](docs/RaceApi.md#loop_stats) | **GET** /race/loop-stats | 
*RaceApi* | [**pit_stops**](docs/RaceApi.md#pit_stops) | **GET** /race/pitstops | 
*RaceApi* | [**practice_results**](docs/RaceApi.md#practice_results) | **GET** /race/practice-results | 
*RaceApi* | [**qualifying_results**](docs/RaceApi.md#qualifying_results) | **GET** /race/qualifying-results | 
*RaceApi* | [**race**](docs/RaceApi.md#race) | **GET** /race | 
*RaceApi* | [**race_results**](docs/RaceApi.md#race_results) | **GET** /race/race-results | 
*RaceApi* | [**race_season**](docs/RaceApi.md#race_season) | **GET** /race/season | 
*RaceApi* | [**rosters**](docs/RaceApi.md#rosters) | **GET** /race/rosters | 
*RaceApi* | [**stage_results**](docs/RaceApi.md#stage_results) | **GET** /race/stage-results | 
*RaceApi* | [**view_model**](docs/RaceApi.md#view_model) | **GET** /race/viewmodel | 
*RaceApi* | [**weekend_schedule**](docs/RaceApi.md#weekend_schedule) | **GET** /race/weekend-schedule | 
*RaceWeekApi* | [**details**](docs/RaceWeekApi.md#details) | **GET** /race-week/details | 
*RaceWeekApi* | [**live**](docs/RaceWeekApi.md#live) | **GET** /race-week/live | 
*RaceWeekApi* | [**season**](docs/RaceWeekApi.md#season) | **GET** /race-week/season | 
*SeriesApi* | [**series**](docs/SeriesApi.md#series) | **GET** /series | 
*VehicleApi* | [**vehicle**](docs/VehicleApi.md#vehicle) | **GET** /vehicle | 
*VehicleApi* | [**vehicle_season_finishes**](docs/VehicleApi.md#vehicle_season_finishes) | **GET** /vehicle/season-finishes | 

## Documentation For Models

 - [Caution](docs/Caution.md)
 - [Company](docs/Company.md)
 - [DisciplineUpdate](docs/DisciplineUpdate.md)
 - [Driver](docs/Driver.md)
 - [DriverPoint](docs/DriverPoint.md)
 - [DriverSummary](docs/DriverSummary.md)
 - [DriverSummaryByPrincipalRaceID](docs/DriverSummaryByPrincipalRaceID.md)
 - [DriverSummaryBySeason](docs/DriverSummaryBySeason.md)
 - [DriverSummaryByTrack](docs/DriverSummaryByTrack.md)
 - [DriverSummaryByTrackType](docs/DriverSummaryByTrackType.md)
 - [Flag](docs/Flag.md)
 - [LapLeader](docs/LapLeader.md)
 - [LoopStat](docs/LoopStat.md)
 - [ManufacturerPoint](docs/ManufacturerPoint.md)
 - [NextGenDatapoint](docs/NextGenDatapoint.md)
 - [NextGenSource](docs/NextGenSource.md)
 - [OSSScan](docs/OSSScan.md)
 - [OpticalTrackingUTMOffset](docs/OpticalTrackingUTMOffset.md)
 - [OwnerPoint](docs/OwnerPoint.md)
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
 - [TokenResponse](docs/TokenResponse.md)
 - [VehicleDetails](docs/VehicleDetails.md)
 - [VehicleWeight](docs/VehicleWeight.md)
 - [WeekendSchedule](docs/WeekendSchedule.md)

