# swagger_client.BackgroundTasksApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_background_task**](BackgroundTasksApi.md#create_background_task) | **POST** /api/v2/background/ | Create new background task
[**get_background_task**](BackgroundTasksApi.md#get_background_task) | **GET** /api/v2/background/{taskId} | Get background task status / response
[**get_background_tasks**](BackgroundTasksApi.md#get_background_tasks) | **GET** /api/v2/background/ | List background tasks


# **create_background_task**
> BackgroundTask create_background_task(endpoint, method, body=body)

Create new background task

Endpoint for creating background tasks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BackgroundTasksApi()
endpoint = 'endpoint_example' # str | Endpoint
method = 'GET' # str | Endpoint (default to GET)
body = 'body_example' # str | Body (optional)

try:
    # Create new background task
    api_response = api_instance.create_background_task(endpoint, method, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackgroundTasksApi->create_background_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **str**| Endpoint | 
 **method** | **str**| Endpoint | [default to GET]
 **body** | **str**| Body | [optional] 

### Return type

[**BackgroundTask**](BackgroundTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_background_task**
> BackgroundTask get_background_task(task_id)

Get background task status / response

Get background task status / response

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BackgroundTasksApi()
task_id = 'task_id_example' # str | The id of the background task

try:
    # Get background task status / response
    api_response = api_instance.get_background_task(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackgroundTasksApi->get_background_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The id of the background task | 

### Return type

[**BackgroundTask**](BackgroundTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_background_tasks**
> list[object] get_background_tasks()

List background tasks

List background tasks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BackgroundTasksApi()

try:
    # List background tasks
    api_response = api_instance.get_background_tasks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackgroundTasksApi->get_background_tasks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

