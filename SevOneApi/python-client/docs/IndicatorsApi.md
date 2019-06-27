# swagger_client.IndicatorsApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_indicator_data**](IndicatorsApi.md#create_device_indicator_data) | **POST** /api/v1/device-indicators/data | Create device indicator data
[**create_device_indicator_data1**](IndicatorsApi.md#create_device_indicator_data1) | **POST** /api/v2/device-indicators/data | Create device indicator data
[**get_indicator**](IndicatorsApi.md#get_indicator) | **GET** /api/v1/devices/{deviceId}/objects/{objectId}/indicators/{indicatorId} | Get indicator by deviceId, objectId and indicatorId
[**get_indicator1**](IndicatorsApi.md#get_indicator1) | **GET** /api/v2/devices/{deviceId}/objects/{objectId}/indicators/{indicatorId} | Get indicator by deviceId, objectId and indicatorId
[**get_indicator_data**](IndicatorsApi.md#get_indicator_data) | **GET** /api/v1/devices/{deviceId}/objects/{objectId}/indicators/{indicatorId}/data | Get indicator data by deviceId, objectId and indicatorId
[**get_indicator_data1**](IndicatorsApi.md#get_indicator_data1) | **GET** /api/v2/devices/{deviceId}/objects/{objectId}/indicators/{indicatorId}/data | Get indicator data by deviceId, objectId and indicatorId
[**get_indicators**](IndicatorsApi.md#get_indicators) | **GET** /api/v1/devices/{deviceId}/objects/{objectId}/indicators | Get indicators by deviceId and objectId
[**get_indicators1**](IndicatorsApi.md#get_indicators1) | **GET** /api/v2/devices/{deviceId}/objects/{objectId}/indicators | Get indicators by deviceId and objectId


# **create_device_indicator_data**
> ResponseEntity create_device_indicator_data(data)

Create device indicator data

Creates a new device indicator data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatorsApi()
data = [swagger_client.ObjectDataDto()] # list[ObjectDataDto] | Device indicator data to be created

try:
    # Create device indicator data
    api_response = api_instance.create_device_indicator_data(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorsApi->create_device_indicator_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**list[ObjectDataDto]**](ObjectDataDto.md)| Device indicator data to be created | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_indicator_data1**
> ResponseEntity create_device_indicator_data1(data)

Create device indicator data

Creates a new device indicator data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatorsApi()
data = [swagger_client.ObjectDataDto()] # list[ObjectDataDto] | Device indicator data to be created

try:
    # Create device indicator data
    api_response = api_instance.create_device_indicator_data1(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorsApi->create_device_indicator_data1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**list[ObjectDataDto]**](ObjectDataDto.md)| Device indicator data to be created | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicator**
> IndicatorDto get_indicator(device_id, object_id, indicator_id, include_extended_info=include_extended_info)

Get indicator by deviceId, objectId and indicatorId

Endpoint for retrieving a single indicator for given deviceId, objectId and indicatorId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatorsApi()
device_id = 789 # int | The Id of the device
object_id = 789 # int | The Id of the object
indicator_id = 789 # int | The Id of the indicator
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Get indicator by deviceId, objectId and indicatorId
    api_response = api_instance.get_indicator(device_id, object_id, indicator_id, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorsApi->get_indicator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The Id of the device | 
 **object_id** | **int**| The Id of the object | 
 **indicator_id** | **int**| The Id of the indicator | 
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**IndicatorDto**](IndicatorDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicator1**
> IndicatorDto get_indicator1(device_id, object_id, indicator_id, include_extended_info=include_extended_info)

Get indicator by deviceId, objectId and indicatorId

Endpoint for retrieving a single indicator for given deviceId, objectId and indicatorId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatorsApi()
device_id = 789 # int | The Id of the device
object_id = 789 # int | The Id of the object
indicator_id = 789 # int | The Id of the indicator
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Get indicator by deviceId, objectId and indicatorId
    api_response = api_instance.get_indicator1(device_id, object_id, indicator_id, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorsApi->get_indicator1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The Id of the device | 
 **object_id** | **int**| The Id of the object | 
 **indicator_id** | **int**| The Id of the indicator | 
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**IndicatorDto**](IndicatorDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicator_data**
> list[DataPointDto] get_indicator_data(device_id, object_id, indicator_id, start_time, end_time)

Get indicator data by deviceId, objectId and indicatorId

Endpoint for retrieving indicators data for a given indicatorId and period of time

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatorsApi()
device_id = 789 # int | The Id of the device
object_id = 789 # int | The Id of the object
indicator_id = 789 # int | The Id of the indicator
start_time = 789 # int | Start time for the data, unix timestamp with milliseconds proximity
end_time = 789 # int | End time for the data, unix timestamp with milliseconds proximity

try:
    # Get indicator data by deviceId, objectId and indicatorId
    api_response = api_instance.get_indicator_data(device_id, object_id, indicator_id, start_time, end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorsApi->get_indicator_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The Id of the device | 
 **object_id** | **int**| The Id of the object | 
 **indicator_id** | **int**| The Id of the indicator | 
 **start_time** | **int**| Start time for the data, unix timestamp with milliseconds proximity | 
 **end_time** | **int**| End time for the data, unix timestamp with milliseconds proximity | 

### Return type

[**list[DataPointDto]**](DataPointDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicator_data1**
> list[DataPointDto] get_indicator_data1(device_id, object_id, indicator_id, start_time, end_time, raw_data=raw_data)

Get indicator data by deviceId, objectId and indicatorId

Endpoint for retrieving indicators data for a given indicatorId and period of time

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatorsApi()
device_id = 789 # int | The Id of the device
object_id = 789 # int | The Id of the object
indicator_id = 789 # int | The Id of the indicator
start_time = 789 # int | Start time for the data, unix timestamp with milliseconds proximity
end_time = 789 # int | End time for the data, unix timestamp with milliseconds proximity
raw_data = false # bool | Determines whether to return raw data (optional) (default to false)

try:
    # Get indicator data by deviceId, objectId and indicatorId
    api_response = api_instance.get_indicator_data1(device_id, object_id, indicator_id, start_time, end_time, raw_data=raw_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorsApi->get_indicator_data1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The Id of the device | 
 **object_id** | **int**| The Id of the object | 
 **indicator_id** | **int**| The Id of the indicator | 
 **start_time** | **int**| Start time for the data, unix timestamp with milliseconds proximity | 
 **end_time** | **int**| End time for the data, unix timestamp with milliseconds proximity | 
 **raw_data** | **bool**| Determines whether to return raw data | [optional] [default to false]

### Return type

[**list[DataPointDto]**](DataPointDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicators**
> PagerIndicatorDto get_indicators(device_id, object_id, page=page, size=size, include_extended_info=include_extended_info)

Get indicators by deviceId and objectId

Endpoint for retrieving all indicators for a given deviceId and objectId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatorsApi()
device_id = 789 # int | The Id of the device
object_id = 789 # int | The Id of the object
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Get indicators by deviceId and objectId
    api_response = api_instance.get_indicators(device_id, object_id, page=page, size=size, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorsApi->get_indicators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The Id of the device | 
 **object_id** | **int**| The Id of the object | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**PagerIndicatorDto**](PagerIndicatorDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indicators1**
> PagerIndicatorDto get_indicators1(device_id, object_id, include_extended_info=include_extended_info, include_indicator_metadata=include_indicator_metadata, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get indicators by deviceId and objectId

Endpoint for retrieving all indicators for a given deviceId and objectId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IndicatorsApi()
device_id = 789 # int | The Id of the device
object_id = 789 # int | The Id of the object
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)
include_indicator_metadata = false # bool | Determines whether to include indicator metadata (optional) (default to false)
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get indicators by deviceId and objectId
    api_response = api_instance.get_indicators1(device_id, object_id, include_extended_info=include_extended_info, include_indicator_metadata=include_indicator_metadata, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndicatorsApi->get_indicators1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The Id of the device | 
 **object_id** | **int**| The Id of the object | 
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]
 **include_indicator_metadata** | **bool**| Determines whether to include indicator metadata | [optional] [default to false]
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerIndicatorDto**](PagerIndicatorDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

