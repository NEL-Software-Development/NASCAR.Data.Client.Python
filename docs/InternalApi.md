# nascar_data_client.InternalApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**internal_erdp_companies_get**](InternalApi.md#internal_erdp_companies_get) | **GET** /internal/erdp/companies | return list of company ids for erdp companies
[**internal_erdp_datapoints_get**](InternalApi.md#internal_erdp_datapoints_get) | **GET** /internal/erdp/datapoints | Get ERDP Datapoints
[**internal_erdp_datapoints_post**](InternalApi.md#internal_erdp_datapoints_post) | **POST** /internal/erdp/datapoints | Create ERDP Datapoints
[**internal_erdp_ingestion_datapoints_get**](InternalApi.md#internal_erdp_ingestion_datapoints_get) | **GET** /internal/erdp/ingestion_datapoints | Called by the ingestion service for publishing
[**internal_erdp_ingestion_sources_get**](InternalApi.md#internal_erdp_ingestion_sources_get) | **GET** /internal/erdp/ingestion_sources | Called by the ingestion service for publishing
[**internal_erdp_sources_get**](InternalApi.md#internal_erdp_sources_get) | **GET** /internal/erdp/sources | Get ERDP Sources
[**internal_erdp_sources_post**](InternalApi.md#internal_erdp_sources_post) | **POST** /internal/erdp/sources | Create ERDP Sources
[**internal_erdp_subscriptions_auth_service_company_id_get**](InternalApi.md#internal_erdp_subscriptions_auth_service_company_id_get) | **GET** /internal/erdp/subscriptions/auth_service/{companyId} | nats auth service calls with company id, returns the topics that the company is allowed to sub on
[**internal_erdp_subscriptions_company_id_get**](InternalApi.md#internal_erdp_subscriptions_company_id_get) | **GET** /internal/erdp/subscriptions/{companyId} | Get Subscriptions by company id
[**internal_erdp_subscriptions_post**](InternalApi.md#internal_erdp_subscriptions_post) | **POST** /internal/erdp/subscriptions | Create erdp subscriptions
[**internal_erdp_topic_company_types_company_type_id_get**](InternalApi.md#internal_erdp_topic_company_types_company_type_id_get) | **GET** /internal/erdp/topic_company_types/{company_type_id} | Get Topic Company Types by company id
[**internal_erdp_topic_company_types_get**](InternalApi.md#internal_erdp_topic_company_types_get) | **GET** /internal/erdp/topic_company_types | Get Topic Company Types
[**internal_erdp_topic_company_types_post**](InternalApi.md#internal_erdp_topic_company_types_post) | **POST** /internal/erdp/topic_company_types | Create Topic Company Types
[**internal_erdp_topics_get**](InternalApi.md#internal_erdp_topics_get) | **GET** /internal/erdp/topics | Get Topics
[**internal_erdp_topics_post**](InternalApi.md#internal_erdp_topics_post) | **POST** /internal/erdp/topics | Create Topic
[**internal_erdp_vehicle_sources_get**](InternalApi.md#internal_erdp_vehicle_sources_get) | **GET** /internal/erdp/vehicle_sources | Get vehicle sources
[**internal_erdp_vehicle_sources_post**](InternalApi.md#internal_erdp_vehicle_sources_post) | **POST** /internal/erdp/vehicle_sources | Create vehicle sources
[**internal_tires_get**](InternalApi.md#internal_tires_get) | **GET** /internal/tires | tire service get tire data for enhanced tire data to nats

# **internal_erdp_companies_get**
> list[int] internal_erdp_companies_get()

return list of company ids for erdp companies

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))

try:
    # return list of company ids for erdp companies
    api_response = api_instance.internal_erdp_companies_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_erdp_companies_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[int]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_erdp_datapoints_get**
> list[ERDPDatapoint] internal_erdp_datapoints_get()

Get ERDP Datapoints

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))

try:
    # Get ERDP Datapoints
    api_response = api_instance.internal_erdp_datapoints_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_erdp_datapoints_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ERDPDatapoint]**](ERDPDatapoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_erdp_datapoints_post**
> ERDPDatapointListETLSaveResult internal_erdp_datapoints_post(body=body)

Create ERDP Datapoints

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))
body = [nascar_data_client.ERDPDatapoint()] # list[ERDPDatapoint] |  (optional)

try:
    # Create ERDP Datapoints
    api_response = api_instance.internal_erdp_datapoints_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_erdp_datapoints_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ERDPDatapoint]**](ERDPDatapoint.md)|  | [optional] 

### Return type

[**ERDPDatapointListETLSaveResult**](ERDPDatapointListETLSaveResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_erdp_ingestion_datapoints_get**
> list[ERDPDatapoint] internal_erdp_ingestion_datapoints_get(include_not_active=include_not_active)

Called by the ingestion service for publishing

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))
include_not_active = true # bool |  (optional)

try:
    # Called by the ingestion service for publishing
    api_response = api_instance.internal_erdp_ingestion_datapoints_get(include_not_active=include_not_active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_erdp_ingestion_datapoints_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_not_active** | **bool**|  | [optional] 

### Return type

[**list[ERDPDatapoint]**](ERDPDatapoint.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_erdp_ingestion_sources_get**
> list[ERDPSource] internal_erdp_ingestion_sources_get(include_not_active=include_not_active)

Called by the ingestion service for publishing

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))
include_not_active = true # bool |  (optional)

try:
    # Called by the ingestion service for publishing
    api_response = api_instance.internal_erdp_ingestion_sources_get(include_not_active=include_not_active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_erdp_ingestion_sources_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_not_active** | **bool**|  | [optional] 

### Return type

[**list[ERDPSource]**](ERDPSource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_erdp_sources_get**
> list[ERDPSource] internal_erdp_sources_get()

Get ERDP Sources

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))

try:
    # Get ERDP Sources
    api_response = api_instance.internal_erdp_sources_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_erdp_sources_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ERDPSource]**](ERDPSource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_erdp_sources_post**
> ERDPSourceListETLSaveResult internal_erdp_sources_post(body=body)

Create ERDP Sources

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))
body = [nascar_data_client.ERDPSource()] # list[ERDPSource] |  (optional)

try:
    # Create ERDP Sources
    api_response = api_instance.internal_erdp_sources_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_erdp_sources_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ERDPSource]**](ERDPSource.md)|  | [optional] 

### Return type

[**ERDPSourceListETLSaveResult**](ERDPSourceListETLSaveResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_erdp_subscriptions_auth_service_company_id_get**
> ERDPUserPermissions internal_erdp_subscriptions_auth_service_company_id_get(company_id)

nats auth service calls with company id, returns the topics that the company is allowed to sub on

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))
company_id = 56 # int | 

try:
    # nats auth service calls with company id, returns the topics that the company is allowed to sub on
    api_response = api_instance.internal_erdp_subscriptions_auth_service_company_id_get(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_erdp_subscriptions_auth_service_company_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**|  | 

### Return type

[**ERDPUserPermissions**](ERDPUserPermissions.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_erdp_subscriptions_company_id_get**
> ERDPSubscriptionPaginatedResult internal_erdp_subscriptions_company_id_get(company_id, offset=offset, count=count, filter=filter, allowed=allowed)

Get Subscriptions by company id

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))
company_id = 56 # int | 
offset = 56 # int |  (optional)
count = 56 # int |  (optional)
filter = 'filter_example' # str |  (optional)
allowed = true # bool |  (optional)

try:
    # Get Subscriptions by company id
    api_response = api_instance.internal_erdp_subscriptions_company_id_get(company_id, offset=offset, count=count, filter=filter, allowed=allowed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_erdp_subscriptions_company_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**|  | 
 **offset** | **int**|  | [optional] 
 **count** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **allowed** | **bool**|  | [optional] 

### Return type

[**ERDPSubscriptionPaginatedResult**](ERDPSubscriptionPaginatedResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_erdp_subscriptions_post**
> CreateSubscriptionListETLSaveResult internal_erdp_subscriptions_post(body=body)

Create erdp subscriptions

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))
body = [nascar_data_client.CreateSubscription()] # list[CreateSubscription] |  (optional)

try:
    # Create erdp subscriptions
    api_response = api_instance.internal_erdp_subscriptions_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_erdp_subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[CreateSubscription]**](CreateSubscription.md)|  | [optional] 

### Return type

[**CreateSubscriptionListETLSaveResult**](CreateSubscriptionListETLSaveResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_erdp_topic_company_types_company_type_id_get**
> list[ERDPTopic] internal_erdp_topic_company_types_company_type_id_get(company_type_id)

Get Topic Company Types by company id

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))
company_type_id = 56 # int | 

try:
    # Get Topic Company Types by company id
    api_response = api_instance.internal_erdp_topic_company_types_company_type_id_get(company_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_erdp_topic_company_types_company_type_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_type_id** | **int**|  | 

### Return type

[**list[ERDPTopic]**](ERDPTopic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_erdp_topic_company_types_get**
> ERDPTopicCompanyTypePaginatedResult internal_erdp_topic_company_types_get(count=count, offset=offset, filter=filter)

Get Topic Company Types

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))
count = 56 # int |  (optional)
offset = 56 # int |  (optional)
filter = 'filter_example' # str |  (optional)

try:
    # Get Topic Company Types
    api_response = api_instance.internal_erdp_topic_company_types_get(count=count, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_erdp_topic_company_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**ERDPTopicCompanyTypePaginatedResult**](ERDPTopicCompanyTypePaginatedResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_erdp_topic_company_types_post**
> ERDPTopicCompanyTypeListETLSaveResult internal_erdp_topic_company_types_post(body=body)

Create Topic Company Types

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))
body = [nascar_data_client.CreateTopicCompanyType()] # list[CreateTopicCompanyType] |  (optional)

try:
    # Create Topic Company Types
    api_response = api_instance.internal_erdp_topic_company_types_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_erdp_topic_company_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[CreateTopicCompanyType]**](CreateTopicCompanyType.md)|  | [optional] 

### Return type

[**ERDPTopicCompanyTypeListETLSaveResult**](ERDPTopicCompanyTypeListETLSaveResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_erdp_topics_get**
> ERDPTopicPaginatedResult internal_erdp_topics_get(count=count, offset=offset, filter=filter)

Get Topics

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))
count = 56 # int |  (optional)
offset = 56 # int |  (optional)
filter = 'filter_example' # str |  (optional)

try:
    # Get Topics
    api_response = api_instance.internal_erdp_topics_get(count=count, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_erdp_topics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**ERDPTopicPaginatedResult**](ERDPTopicPaginatedResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_erdp_topics_post**
> CreateTopicListETLSaveResult internal_erdp_topics_post(body=body)

Create Topic

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))
body = [nascar_data_client.CreateTopic()] # list[CreateTopic] |  (optional)

try:
    # Create Topic
    api_response = api_instance.internal_erdp_topics_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_erdp_topics_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[CreateTopic]**](CreateTopic.md)|  | [optional] 

### Return type

[**CreateTopicListETLSaveResult**](CreateTopicListETLSaveResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_erdp_vehicle_sources_get**
> list[ERDPSourceVehicle] internal_erdp_vehicle_sources_get()

Get vehicle sources

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))

try:
    # Get vehicle sources
    api_response = api_instance.internal_erdp_vehicle_sources_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_erdp_vehicle_sources_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ERDPSourceVehicle]**](ERDPSourceVehicle.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_erdp_vehicle_sources_post**
> ERDPSourceVehicleListETLSaveResult internal_erdp_vehicle_sources_post(body=body)

Create vehicle sources

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))
body = [nascar_data_client.ERDPSourceVehicle()] # list[ERDPSourceVehicle] |  (optional)

try:
    # Create vehicle sources
    api_response = api_instance.internal_erdp_vehicle_sources_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_erdp_vehicle_sources_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ERDPSourceVehicle]**](ERDPSourceVehicle.md)|  | [optional] 

### Return type

[**ERDPSourceVehicleListETLSaveResult**](ERDPSourceVehicleListETLSaveResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_tires_get**
> list[Tire] internal_tires_get()

tire service get tire data for enhanced tire data to nats

### Example
```python
from __future__ import print_function
import time
import nascar_data_client
from nascar_data_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = nascar_data_client.InternalApi(nascar_data_client.ApiClient(configuration))

try:
    # tire service get tire data for enhanced tire data to nats
    api_response = api_instance.internal_tires_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalApi->internal_tires_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Tire]**](Tire.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

