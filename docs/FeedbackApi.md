# nascar_data_client.FeedbackApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**feedback_dev_notes_get**](FeedbackApi.md#feedback_dev_notes_get) | **GET** /feedback/dev-notes | 
[**feedback_submit_feedback_post**](FeedbackApi.md#feedback_submit_feedback_post) | **POST** /feedback/submit-feedback | 

# **feedback_dev_notes_get**
> list[DevNote] feedback_dev_notes_get()



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.FeedbackApi(nascar_data_client.ApiClient(configuration))

try:
    api_response = api_instance.feedback_dev_notes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeedbackApi->feedback_dev_notes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DevNote]**](DevNote.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **feedback_submit_feedback_post**
> feedback_submit_feedback_post(body=body)



### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.FeedbackApi(nascar_data_client.ApiClient(configuration))
body = nascar_data_client.Feedback() # Feedback |  (optional)

try:
    api_instance.feedback_submit_feedback_post(body=body)
except ApiException as e:
    print("Exception when calling FeedbackApi->feedback_submit_feedback_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Feedback**](Feedback.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

