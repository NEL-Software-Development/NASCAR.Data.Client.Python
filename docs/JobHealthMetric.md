# JobHealthMetric

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**cron_expression** | **str** |  | [optional] 
**expected_interval_seconds** | **int** |  | [optional] 
**last_run_utc** | **datetime** |  | [optional] 
**seconds_since_last_run** | **float** |  | [optional] 
**last_status** | **str** |  | [optional] 
**last_error** | **str** |  | [optional] 
**is_stale** | **bool** | True when the gap since the last run exceeds the expected interval by more than the configured threshold. | [optional] 
**time_series** | [**list[JobMetricPointDto]**](JobMetricPointDto.md) | One point per persisted minute-bucket within the requested window, ordered oldest to newest. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

