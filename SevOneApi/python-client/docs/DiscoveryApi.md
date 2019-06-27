# swagger_client.DiscoveryApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_devices_in_discovery**](DiscoveryApi.md#filter_devices_in_discovery) | **POST** /api/v1/discovery/filter | Filter devices currently in the discovery queue
[**filter_devices_in_discovery1**](DiscoveryApi.md#filter_devices_in_discovery1) | **POST** /api/v2/discovery/filter | Filter devices currently in the discovery queue
[**get_device_status_by_id**](DiscoveryApi.md#get_device_status_by_id) | **GET** /api/v1/discovery/{id} | Get device status from the discovery queue by Id
[**get_device_status_by_id1**](DiscoveryApi.md#get_device_status_by_id1) | **GET** /api/v2/discovery/{id} | Get device status from the discovery queue by Id
[**get_devices_in_discovery**](DiscoveryApi.md#get_devices_in_discovery) | **GET** /api/v1/discovery | Get all devices currently in the discovery queue
[**get_devices_in_discovery1**](DiscoveryApi.md#get_devices_in_discovery1) | **GET** /api/v2/discovery | Get all devices currently in the discovery queue
[**run_discover_device**](DiscoveryApi.md#run_discover_device) | **POST** /api/v2/discovery/{id}/run | Run discovery for a concrete device
[**run_discovery_all_devices**](DiscoveryApi.md#run_discovery_all_devices) | **POST** /api/v2/discovery/run | Run discovery for all devices in the discovery queue
[**update_device_priority**](DiscoveryApi.md#update_device_priority) | **PATCH** /api/v1/discovery/{id} | Update an existing task for this device in the discovery queue
[**update_device_priority1**](DiscoveryApi.md#update_device_priority1) | **PATCH** /api/v2/discovery/{id} | Update an existing task for this device in the discovery queue


# **filter_devices_in_discovery**
> PagerDeviceDiscoveryDto filter_devices_in_discovery(filter, page=page, size=size, include_members=include_members, include_objects=include_objects, include_indicators=include_indicators)

Filter devices currently in the discovery queue

Find all devices that match the criteria

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoveryApi()
filter = swagger_client.DeviceDiscoveryFilter() # DeviceDiscoveryFilter | Device discovery object that will be used for filtering
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_members = false # bool | Determines whether to include devices (optional) (default to false)
include_objects = false # bool | Determines whether to include objects (optional) (default to false)
include_indicators = false # bool | Determines whether to include indicators (optional) (default to false)

try:
    # Filter devices currently in the discovery queue
    api_response = api_instance.filter_devices_in_discovery(filter, page=page, size=size, include_members=include_members, include_objects=include_objects, include_indicators=include_indicators)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->filter_devices_in_discovery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**DeviceDiscoveryFilter**](DeviceDiscoveryFilter.md)| Device discovery object that will be used for filtering | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_members** | **bool**| Determines whether to include devices | [optional] [default to false]
 **include_objects** | **bool**| Determines whether to include objects | [optional] [default to false]
 **include_indicators** | **bool**| Determines whether to include indicators | [optional] [default to false]

### Return type

[**PagerDeviceDiscoveryDto**](PagerDeviceDiscoveryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_devices_in_discovery1**
> PagerDeviceDiscoveryDto filter_devices_in_discovery1(filter, include_members=include_members, include_objects=include_objects, include_indicators=include_indicators, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Filter devices currently in the discovery queue

Find all devices that match the criteria

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoveryApi()
filter = swagger_client.DeviceDiscoveryFilter() # DeviceDiscoveryFilter | Device discovery object that will be used for filtering
include_members = false # bool | Determines whether to include devices (optional) (default to false)
include_objects = false # bool | Determines whether to include objects (optional) (default to false)
include_indicators = false # bool | Determines whether to include indicators (optional) (default to false)
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Filter devices currently in the discovery queue
    api_response = api_instance.filter_devices_in_discovery1(filter, include_members=include_members, include_objects=include_objects, include_indicators=include_indicators, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->filter_devices_in_discovery1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**DeviceDiscoveryFilter**](DeviceDiscoveryFilter.md)| Device discovery object that will be used for filtering | 
 **include_members** | **bool**| Determines whether to include devices | [optional] [default to false]
 **include_objects** | **bool**| Determines whether to include objects | [optional] [default to false]
 **include_indicators** | **bool**| Determines whether to include indicators | [optional] [default to false]
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerDeviceDiscoveryDto**](PagerDeviceDiscoveryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_status_by_id**
> DeviceDiscoveryDto get_device_status_by_id(id, include_members=include_members)

Get device status from the discovery queue by Id

Gets a single device status object by provided Id from the discovery queue

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoveryApi()
id = 789 # int | The id of the device
include_members = false # bool | Determines whether to include devices in the response (optional) (default to false)

try:
    # Get device status from the discovery queue by Id
    api_response = api_instance.get_device_status_by_id(id, include_members=include_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_device_status_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device | 
 **include_members** | **bool**| Determines whether to include devices in the response | [optional] [default to false]

### Return type

[**DeviceDiscoveryDto**](DeviceDiscoveryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_status_by_id1**
> DeviceDiscoveryDto get_device_status_by_id1(id, include_members=include_members)

Get device status from the discovery queue by Id

Gets a single device status object by provided Id from the discovery queue

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoveryApi()
id = 789 # int | The id of the device
include_members = false # bool | Determines whether to include devices in the response (optional) (default to false)

try:
    # Get device status from the discovery queue by Id
    api_response = api_instance.get_device_status_by_id1(id, include_members=include_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_device_status_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device | 
 **include_members** | **bool**| Determines whether to include devices in the response | [optional] [default to false]

### Return type

[**DeviceDiscoveryDto**](DeviceDiscoveryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_in_discovery**
> PagerDeviceDiscoveryDto get_devices_in_discovery(page=page, size=size, include_members=include_members)

Get all devices currently in the discovery queue

Endpoint for retrieving all devices currently in the discovery queue that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoveryApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_members = false # bool | Determines whether to include devices in the response (optional) (default to false)

try:
    # Get all devices currently in the discovery queue
    api_response = api_instance.get_devices_in_discovery(page=page, size=size, include_members=include_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_devices_in_discovery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_members** | **bool**| Determines whether to include devices in the response | [optional] [default to false]

### Return type

[**PagerDeviceDiscoveryDto**](PagerDeviceDiscoveryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_in_discovery1**
> PagerDeviceDiscoveryDto get_devices_in_discovery1(include_members=include_members, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all devices currently in the discovery queue

Endpoint for retrieving all devices currently in the discovery queue that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoveryApi()
include_members = false # bool | Determines whether to include devices in the response (optional) (default to false)
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all devices currently in the discovery queue
    api_response = api_instance.get_devices_in_discovery1(include_members=include_members, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_devices_in_discovery1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_members** | **bool**| Determines whether to include devices in the response | [optional] [default to false]
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerDeviceDiscoveryDto**](PagerDeviceDiscoveryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_discover_device**
> ResponseEntity run_discover_device(id)

Run discovery for a concrete device

Needed Edit access to the concrete device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoveryApi()
id = 789 # int | The id of the device

try:
    # Run discovery for a concrete device
    api_response = api_instance.run_discover_device(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->run_discover_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_discovery_all_devices**
> ResponseEntity run_discovery_all_devices()

Run discovery for all devices in the discovery queue

Can be executed only from system administrators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoveryApi()

try:
    # Run discovery for all devices in the discovery queue
    api_response = api_instance.run_discovery_all_devices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->run_discovery_all_devices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_priority**
> DeviceDiscoveryDto update_device_priority(id, discovery)

Update an existing task for this device in the discovery queue

Updates an existing task for this device in the discovery queue

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoveryApi()
id = 789 # int | The id of the device
discovery = swagger_client.DiscoveryRequestDto() # DiscoveryRequestDto | Discovery request object to be updated

try:
    # Update an existing task for this device in the discovery queue
    api_response = api_instance.update_device_priority(id, discovery)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->update_device_priority: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device | 
 **discovery** | [**DiscoveryRequestDto**](DiscoveryRequestDto.md)| Discovery request object to be updated | 

### Return type

[**DeviceDiscoveryDto**](DeviceDiscoveryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_priority1**
> DeviceDiscoveryDto update_device_priority1(id, discovery)

Update an existing task for this device in the discovery queue

Updates an existing task for this device in the discovery queue

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoveryApi()
id = 789 # int | The id of the device
discovery = swagger_client.DiscoveryRequestDto() # DiscoveryRequestDto | Discovery request object to be updated

try:
    # Update an existing task for this device in the discovery queue
    api_response = api_instance.update_device_priority1(id, discovery)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->update_device_priority1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device | 
 **discovery** | [**DiscoveryRequestDto**](DiscoveryRequestDto.md)| Discovery request object to be updated | 

### Return type

[**DeviceDiscoveryDto**](DeviceDiscoveryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

