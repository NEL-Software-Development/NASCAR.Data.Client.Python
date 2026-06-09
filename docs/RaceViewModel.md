# RaceViewModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series_id** | **int** | Series identifier | [optional] 
**name** | **str** | Race name | [optional] 
**promoter** | **str** | Promoter of the race | [optional] 
**laps** | **int** | Total number of laps | [optional] 
**distance** | **float** | Race distance | [optional] 
**race_type_id** | **int** | Race Type Identifier (1-Race, 2-Duel, 3-Heat, 4-Exhibition) | [optional] 
**total_race_time** | **str** | Total race time formatted as HH:MM:SS | [optional] 
**_date** | **datetime** | Race date | [optional] 
**comments** | **str** | Race comments | [optional] 
**cautions** | [**list[Caution]**](Caution.md) | Cautions during the race | [optional] 
**entries** | [**list[RunEntry]**](RunEntry.md) | Race entries | [optional] 
**infractions** | [**list[RaceInfraction]**](RaceInfraction.md) | Race infractions | [optional] 
**lap_leaders** | [**list[LapLeader]**](LapLeader.md) | Lap leaders | [optional] 
**loop_stats** | [**list[LoopStat]**](LoopStat.md) | Loop stats for the race | [optional] 
**pitstops** | [**list[Pitstop]**](Pitstop.md) | Pit stops during the race | [optional] 
**practice_results** | [**list[PracticeRunResults]**](PracticeRunResults.md) | Practice results | [optional] 
**qualifying_results** | [**list[QualifyingRunResults]**](QualifyingRunResults.md) | Qualifying results | [optional] 
**race_results** | [**list[RaceRunResults]**](RaceRunResults.md) | Race results | [optional] 
**runs** | [**list[RunDetails]**](RunDetails.md) | Runs associated with the race | [optional] 
**stage_results** | [**list[StageRunResults]**](StageRunResults.md) | Stage results | [optional] 
**schedule** | [**list[WeekendSchedule]**](WeekendSchedule.md) | Weekend schedule entries for the race | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

