# ActiveRun

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the run | [optional] 
**start_time** | **datetime** | Scheduled start time | [optional] 
**run_state** | [**RunState**](RunState.md) |  | [optional] 
**run_type** | [**RunType**](RunType.md) |  | [optional] 
**duration** | **int** | The scheduled duration of the run in seconds | [optional] 
**flag_state** | **str** | Current flag state (Green, Yellow, Red, Checkered, White, Stop, NoActiveFlag, Warm, Invalid) | [optional] 
**flags** | [**list[Flag]**](Flag.md) | Flags associated with this run | [optional] 
**entries** | [**list[RunEntry]**](RunEntry.md) | Run entries (vehicles and drivers participating in this run) | [optional] 
**results** | [**list[RunResult]**](RunResult.md) | Current results for this run | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

