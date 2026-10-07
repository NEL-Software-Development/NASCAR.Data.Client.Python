# nascar_data_client.HealthApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_jobs_get**](HealthApi.md#health_jobs_get) | **GET** /health/jobs | Returns time-series run metrics for every registered recurring ETL job: fixed  fields (current status, cron, staleness) appear once per job, with a TimeSeries  array of per-minute buckets within the requested window for plotting cadence,  latency, and drift trends over time.

# **health_jobs_get**
> list[JobHealthMetric] health_jobs_get(window_minutes=window_minutes)

Returns time-series run metrics for every registered recurring ETL job: fixed  fields (current status, cron, staleness) appear once per job, with a TimeSeries  array of per-minute buckets within the requested window for plotting cadence,  latency, and drift trends over time.

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.HealthApi(nascar_data_client.ApiClient(configuration))
window_minutes = 60 # int | How far back to return time-series buckets. Defaults to 60 minutes. (optional) (default to 60)

try:
    # Returns time-series run metrics for every registered recurring ETL job: fixed  fields (current status, cron, staleness) appear once per job, with a TimeSeries  array of per-minute buckets within the requested window for plotting cadence,  latency, and drift trends over time.
    api_response = api_instance.health_jobs_get(window_minutes=window_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->health_jobs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **window_minutes** | **int**| How far back to return time-series buckets. Defaults to 60 minutes. | [optional] [default to 60]

### Return type

[**list[JobHealthMetric]**](JobHealthMetric.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

