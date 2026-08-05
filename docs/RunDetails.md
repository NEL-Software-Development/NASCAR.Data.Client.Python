# RunDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **int** | Unique identifier given and used by the NASCAR Data API | [optional] 
**name** | **str** | The name of the run | [optional] 
**start_time** | **datetime** | Scheduled start time | [optional] 
**run_state** | [**RunState**](RunState.md) |  | [optional] 
**run_type** | [**RunType**](RunType.md) |  | [optional] 
**duration** | **int** | The scheduled duration of the run in seconds | [optional] 
**timing_run_id** | **int** | Timing system run identifier | [optional] 
**flag_state** | **str** | Current flag state derived from the last flag in the run:  (NONE, WARMUP, GREEN, YELLOW, RED, WHITE, FINISH, EXTRA) | [optional] 
**flags** | [**list[Flag]**](Flag.md) | Flags associated with this run | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

