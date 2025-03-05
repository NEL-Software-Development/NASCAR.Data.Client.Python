# RaceDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the race | [optional] 
**history_race_id** | **int** | The race id from the history database | [optional] [default to -1]
**series_id** | **int** | The series id of the race | [optional] 
**name** | **str** | The race name | [optional] 
**promoter** | **str** | The promoter of the race | [optional] 
**laps** | **int** | Laps | [optional] 
**distance** | **float** | Race distance | [optional] 
**practice_results** | **str** | URL to Practice results | [optional] 
**qualifying_results** | **str** | URL to Qualifying results | [optional] 
**race_results** | **str** | URL to race results | [optional] 
**cautions** | **str** | URL to race cautions | [optional] 
**infractions** | **str** | URL to race infractions | [optional] 
**lap_leaders** | **str** | URL to race lap leaders | [optional] 
**pitstops** | **str** | URL to race pitstops | [optional] 
**_date** | **datetime** | Race date | [optional] 
**comments** | **str** | Race Comments | [optional] 
**track_name** | **str** | Track Name | [optional] 
**track_id** | **int** | Track Id | [optional] 
**inspection_complete** | **bool** | Has inspection been completed | [optional] 
**entries** | [**list[RunEntry]**](RunEntry.md) | Race entries | [optional] 
**runs** | [**list[RunDetails]**](RunDetails.md) | Runs | [optional] 
**schedule** | [**list[WeekendSchedule]**](WeekendSchedule.md) | Weekend Schedule | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

