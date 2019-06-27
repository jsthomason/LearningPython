# swagger_client.ApplicationApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_metrics**](ApplicationApi.md#get_public_metrics) | **GET** /api/v1/application/metrics | Get public metrics
[**get_public_metrics1**](ApplicationApi.md#get_public_metrics1) | **GET** /api/v2/application/metrics | Get public metrics
[**get_version**](ApplicationApi.md#get_version) | **GET** /api/v1/application/version | Get build version
[**get_version1**](ApplicationApi.md#get_version1) | **GET** /api/v2/application/version | Get build version
[**post_logging_level**](ApplicationApi.md#post_logging_level) | **POST** /api/v1/application/logger | Change logging level per logger
[**post_logging_level1**](ApplicationApi.md#post_logging_level1) | **POST** /api/v2/application/logger | Change logging level per logger


# **get_public_metrics**
> dict(str, object) get_public_metrics(filter=filter)

Get public metrics

Get public metrics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
filter = 'filter_example' # str | Filter to retrieve only subset of public metrics (optional)

try:
    # Get public metrics
    api_response = api_instance.get_public_metrics(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_public_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to retrieve only subset of public metrics | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_metrics1**
> dict(str, object) get_public_metrics1(filter=filter)

Get public metrics

Get public metrics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
filter = 'filter_example' # str | Filter to retrieve only subset of public metrics (optional)

try:
    # Get public metrics
    api_response = api_instance.get_public_metrics1(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_public_metrics1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to retrieve only subset of public metrics | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> ApiInfo get_version(date_format=date_format)

Get build version

Get Git info for the build

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
date_format = 'yyyy-MM-dd'T'HH:mm:ssZ' # str | The date format for build time and commit time: (optional) (default to yyyy-MM-dd'T'HH:mm:ssZ)

try:
    # Get build version
    api_response = api_instance.get_version(date_format=date_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**| The date format for build time and commit time: | [optional] [default to yyyy-MM-dd&#39;T&#39;HH:mm:ssZ]

### Return type

[**ApiInfo**](ApiInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version1**
> ApiInfo get_version1(date_format=date_format)

Get build version

Get Git info for the build

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
date_format = 'yyyy-MM-dd'T'HH:mm:ssZ' # str | The date format for build time and commit time: (optional) (default to yyyy-MM-dd'T'HH:mm:ssZ)

try:
    # Get build version
    api_response = api_instance.get_version1(date_format=date_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_version1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**| The date format for build time and commit time: | [optional] [default to yyyy-MM-dd&#39;T&#39;HH:mm:ssZ]

### Return type

[**ApiInfo**](ApiInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_logging_level**
> ResponseEntity post_logging_level(logger)

Change logging level per logger

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
logger = swagger_client.LoggingLevel() # LoggingLevel | Requested logger with the requested level

try:
    # Change logging level per logger
    api_response = api_instance.post_logging_level(logger)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->post_logging_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logger** | [**LoggingLevel**](LoggingLevel.md)| Requested logger with the requested level | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_logging_level1**
> ResponseEntity post_logging_level1(logger)

Change logging level per logger

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
logger = swagger_client.LoggingLevel() # LoggingLevel | Requested logger with the requested level

try:
    # Change logging level per logger
    api_response = api_instance.post_logging_level1(logger)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->post_logging_level1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logger** | [**LoggingLevel**](LoggingLevel.md)| Requested logger with the requested level | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

