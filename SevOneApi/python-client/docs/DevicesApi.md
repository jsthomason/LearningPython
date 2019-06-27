# swagger_client.DevicesApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_device_rules**](DevicesApi.md#apply_device_rules) | **POST** /api/v2/devices/{id}/rules/apply | Apply the rules for the specified device
[**create_device**](DevicesApi.md#create_device) | **POST** /api/v1/devices | Create device
[**create_device1**](DevicesApi.md#create_device1) | **POST** /api/v2/devices | Create device
[**create_device_data**](DevicesApi.md#create_device_data) | **POST** /api/v2/devices/data | Create device data
[**delete_device_by_id**](DevicesApi.md#delete_device_by_id) | **DELETE** /api/v1/devices/{id} | Delete device
[**delete_device_by_id1**](DevicesApi.md#delete_device_by_id1) | **DELETE** /api/v2/devices/{id} | Delete device
[**filter_device**](DevicesApi.md#filter_device) | **POST** /api/v1/devices/filter | Filter devices
[**filter_device1**](DevicesApi.md#filter_device1) | **POST** /api/v2/devices/filter | Filter devices
[**get_device_by_id**](DevicesApi.md#get_device_by_id) | **GET** /api/v1/devices/{id} | Get device by Id
[**get_device_by_id1**](DevicesApi.md#get_device_by_id1) | **GET** /api/v2/devices/{id} | Get device by Id
[**get_devices**](DevicesApi.md#get_devices) | **GET** /api/v1/devices | Get all devices
[**get_devices1**](DevicesApi.md#get_devices1) | **GET** /api/v2/devices | Get all devices
[**partially_update_device_by_id**](DevicesApi.md#partially_update_device_by_id) | **PATCH** /api/v1/devices/{id} | Partially update device
[**partially_update_device_by_id1**](DevicesApi.md#partially_update_device_by_id1) | **PATCH** /api/v2/devices/{id} | Partially update device
[**update_device_by_id**](DevicesApi.md#update_device_by_id) | **PUT** /api/v1/devices/{id} | Update device
[**update_device_by_id1**](DevicesApi.md#update_device_by_id1) | **PUT** /api/v2/devices/{id} | Update device


# **apply_device_rules**
> ResponseEntity apply_device_rules(id)

Apply the rules for the specified device

Applies device group and object group rules for the specified device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 789 # int | The id of the device

try:
    # Apply the rules for the specified device
    api_response = api_instance.apply_device_rules(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->apply_device_rules: %s\n" % e)
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

# **create_device**
> DeviceDto create_device(device)

Create device

Creates a new device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
device = swagger_client.CreateDeviceRequestDto() # CreateDeviceRequestDto | Device request object

try:
    # Create device
    api_response = api_instance.create_device(device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**CreateDeviceRequestDto**](CreateDeviceRequestDto.md)| Device request object | 

### Return type

[**DeviceDto**](DeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device1**
> DeviceDto create_device1(device)

Create device

Creates a new device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
device = swagger_client.CreateDeviceRequestDto() # CreateDeviceRequestDto | Device request object

try:
    # Create device
    api_response = api_instance.create_device1(device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_device1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**CreateDeviceRequestDto**](CreateDeviceRequestDto.md)| Device request object | 

### Return type

[**DeviceDto**](DeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_data**
> str create_device_data(device_data)

Create device data

Creates new device data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
device_data = swagger_client.DeviceDescription() # DeviceDescription | Device data request object

try:
    # Create device data
    api_response = api_instance.create_device_data(device_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_device_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_data** | [**DeviceDescription**](DeviceDescription.md)| Device data request object | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_by_id**
> ResponseEntity delete_device_by_id(id)

Delete device

Deletes an existing device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 789 # int | The id of the device to be deleted

try:
    # Delete device
    api_response = api_instance.delete_device_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_by_id1**
> ResponseEntity delete_device_by_id1(id)

Delete device

Deletes an existing device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 789 # int | The id of the device to be deleted

try:
    # Delete device
    api_response = api_instance.delete_device_by_id1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_device_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_device**
> PagerDeviceDto filter_device(filter, page=page, size=size, include_objects=include_objects, include_indicators=include_indicators, include_extended_info=include_extended_info, local_only=local_only)

Filter devices

Find all devices that match the criteria

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
filter = swagger_client.DeviceFilter() # DeviceFilter | Device object that will be used for filtering
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_objects = false # bool | Determines whether to include objects (optional) (default to false)
include_indicators = false # bool | Determines whether to include indicators (optional) (default to false)
include_extended_info = false # bool | Determines whether to include extendedInfo or not (optional) (default to false)
local_only = true # bool | Determines whether to execute distributed request or not (optional) (default to true)

try:
    # Filter devices
    api_response = api_instance.filter_device(filter, page=page, size=size, include_objects=include_objects, include_indicators=include_indicators, include_extended_info=include_extended_info, local_only=local_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->filter_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**DeviceFilter**](DeviceFilter.md)| Device object that will be used for filtering | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_objects** | **bool**| Determines whether to include objects | [optional] [default to false]
 **include_indicators** | **bool**| Determines whether to include indicators | [optional] [default to false]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to false]
 **local_only** | **bool**| Determines whether to execute distributed request or not | [optional] [default to true]

### Return type

[**PagerDeviceDto**](PagerDeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_device1**
> PagerDeviceDto filter_device1(filter, include_objects=include_objects, include_indicators=include_indicators, include_extended_info=include_extended_info, local_only=local_only, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Filter devices

Find all devices that match the criteria

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
filter = swagger_client.DeviceFilter() # DeviceFilter | Device object that will be used for filtering
include_objects = false # bool | Determines whether to include objects (optional) (default to false)
include_indicators = false # bool | Determines whether to include indicators (optional) (default to false)
include_extended_info = false # bool | Determines whether to include extendedInfo or not (optional) (default to false)
local_only = true # bool | Determines whether to execute distributed request or not (optional) (default to true)
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Filter devices
    api_response = api_instance.filter_device1(filter, include_objects=include_objects, include_indicators=include_indicators, include_extended_info=include_extended_info, local_only=local_only, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->filter_device1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**DeviceFilter**](DeviceFilter.md)| Device object that will be used for filtering | 
 **include_objects** | **bool**| Determines whether to include objects | [optional] [default to false]
 **include_indicators** | **bool**| Determines whether to include indicators | [optional] [default to false]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to false]
 **local_only** | **bool**| Determines whether to execute distributed request or not | [optional] [default to true]
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerDeviceDto**](PagerDeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_by_id**
> DeviceDto get_device_by_id(id, include_objects=include_objects, include_indicators=include_indicators, include_extended_info=include_extended_info)

Get device by Id

Gets a single device object by provided Id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 789 # int | The id of the requested device
include_objects = false # bool | Determines whether to include objects of the device (optional) (default to false)
include_indicators = false # bool | Determines whether to include indicators and objects (optional) (default to false)
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Get device by Id
    api_response = api_instance.get_device_by_id(id, include_objects=include_objects, include_indicators=include_indicators, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the requested device | 
 **include_objects** | **bool**| Determines whether to include objects of the device | [optional] [default to false]
 **include_indicators** | **bool**| Determines whether to include indicators and objects | [optional] [default to false]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**DeviceDto**](DeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_by_id1**
> DeviceDto get_device_by_id1(id, include_objects=include_objects, include_indicators=include_indicators, include_extended_info=include_extended_info)

Get device by Id

Gets a single device object by provided Id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 789 # int | The id of the requested device
include_objects = false # bool | Determines whether to include objects of the device (optional) (default to false)
include_indicators = false # bool | Determines whether to include indicators and objects (optional) (default to false)
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Get device by Id
    api_response = api_instance.get_device_by_id1(id, include_objects=include_objects, include_indicators=include_indicators, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the requested device | 
 **include_objects** | **bool**| Determines whether to include objects of the device | [optional] [default to false]
 **include_indicators** | **bool**| Determines whether to include indicators and objects | [optional] [default to false]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**DeviceDto**](DeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices**
> PagerDeviceDto get_devices(page=page, size=size)

Get all devices

Endpoint for retrieving all devices that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)

try:
    # Get all devices
    api_response = api_instance.get_devices(page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]

### Return type

[**PagerDeviceDto**](PagerDeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices1**
> PagerDeviceDto get_devices1(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all devices

Endpoint for retrieving all devices that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all devices
    api_response = api_instance.get_devices1(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerDeviceDto**](PagerDeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_device_by_id**
> DeviceDto partially_update_device_by_id(id, device)

Partially update device

Partial update an existing device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 789 # int | The id of the device to be updated
device = swagger_client.DeviceUpdateRequestDto() # DeviceUpdateRequestDto | Device to be updated

try:
    # Partially update device
    api_response = api_instance.partially_update_device_by_id(id, device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->partially_update_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device to be updated | 
 **device** | [**DeviceUpdateRequestDto**](DeviceUpdateRequestDto.md)| Device to be updated | 

### Return type

[**DeviceDto**](DeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_device_by_id1**
> DeviceDto partially_update_device_by_id1(id, device)

Partially update device

Partial update an existing device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 789 # int | The id of the device to be updated
device = swagger_client.DeviceUpdateRequestDto() # DeviceUpdateRequestDto | Device to be updated

try:
    # Partially update device
    api_response = api_instance.partially_update_device_by_id1(id, device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->partially_update_device_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device to be updated | 
 **device** | [**DeviceUpdateRequestDto**](DeviceUpdateRequestDto.md)| Device to be updated | 

### Return type

[**DeviceDto**](DeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_by_id**
> DeviceDto update_device_by_id(id, device)

Update device

Updates an existing device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 789 # int | The id of the device to be updated
device = swagger_client.DeviceUpdateRequestDto() # DeviceUpdateRequestDto | Device to be updated

try:
    # Update device
    api_response = api_instance.update_device_by_id(id, device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device to be updated | 
 **device** | [**DeviceUpdateRequestDto**](DeviceUpdateRequestDto.md)| Device to be updated | 

### Return type

[**DeviceDto**](DeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_by_id1**
> DeviceDto update_device_by_id1(id, device)

Update device

Updates an existing device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 789 # int | The id of the device to be updated
device = swagger_client.DeviceUpdateRequestDto() # DeviceUpdateRequestDto | Device to be updated

try:
    # Update device
    api_response = api_instance.update_device_by_id1(id, device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_device_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device to be updated | 
 **device** | [**DeviceUpdateRequestDto**](DeviceUpdateRequestDto.md)| Device to be updated | 

### Return type

[**DeviceDto**](DeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

