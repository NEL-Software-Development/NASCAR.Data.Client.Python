# JobMetricPointDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_start_utc** | **datetime** |  | [optional] 
**run_count** | **int** |  | [optional] 
**failure_count** | **int** |  | [optional] 
**average_latency_ms** | **float** |  | [optional] 
**min_latency_ms** | **float** |  | [optional] 
**max_latency_ms** | **float** |  | [optional] 
**average_interval_seconds** | **float** | Actual average time between runs during this bucket, in seconds. | [optional] 
**expected_interval_seconds** | **int** | Expected interval in seconds, derived from the job&#x27;s registered cron expression as of this bucket. | [optional] 
**interval_drift_percent** | **float** | Percent drift of AverageIntervalSeconds from ExpectedIntervalSeconds for this  bucket. Positive means the job ran less often than scheduled (falling behind);  negative means more often. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

