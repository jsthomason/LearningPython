# swagger_client.DeviceTypesApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_member_by_id_to_type**](DeviceTypesApi.md#add_member_by_id_to_type) | **POST** /api/v1/devicetypes/{id}/members/{deviceId} | Associate an existing device with device type
[**add_member_by_id_to_type1**](DeviceTypesApi.md#add_member_by_id_to_type1) | **POST** /api/v2/devicetypes/{id}/members/{deviceId} | Associate an existing device with device type
[**create_device_type**](DeviceTypesApi.md#create_device_type) | **POST** /api/v1/devicetypes | Create device type
[**create_device_type1**](DeviceTypesApi.md#create_device_type1) | **POST** /api/v2/devicetypes | Create device type
[**delete_device_type_by_id**](DeviceTypesApi.md#delete_device_type_by_id) | **DELETE** /api/v1/devicetypes/{id} | Delete device type
[**delete_device_type_by_id1**](DeviceTypesApi.md#delete_device_type_by_id1) | **DELETE** /api/v2/devicetypes/{id} | Delete device type
[**delete_device_type_member_by_id**](DeviceTypesApi.md#delete_device_type_member_by_id) | **DELETE** /api/v1/devicetypes/{id}/members/{deviceId} | Remove device type member
[**delete_device_type_member_by_id1**](DeviceTypesApi.md#delete_device_type_member_by_id1) | **DELETE** /api/v2/devicetypes/{id}/members/{deviceId} | Remove device type member
[**filter_device_types**](DeviceTypesApi.md#filter_device_types) | **POST** /api/v2/devicetypes/filter | Filter devices
[**get_ancestors_for_device_type**](DeviceTypesApi.md#get_ancestors_for_device_type) | **GET** /api/v2/devicetypes/{id}/ancestors | Get ancestors of the device type
[**get_ancestors_for_device_types**](DeviceTypesApi.md#get_ancestors_for_device_types) | **GET** /api/v2/devicetypes/ancestors/{ids} | Get ancestors of the device types
[**get_device_type_by_id**](DeviceTypesApi.md#get_device_type_by_id) | **GET** /api/v1/devicetypes/{id} | Get device type
[**get_device_type_by_id1**](DeviceTypesApi.md#get_device_type_by_id1) | **GET** /api/v2/devicetypes/{id} | Get device type
[**get_device_type_for_device_by_id**](DeviceTypesApi.md#get_device_type_for_device_by_id) | **GET** /api/v1/devicetypes/members/{deviceId} | Get device types for device
[**get_device_type_for_device_by_id1**](DeviceTypesApi.md#get_device_type_for_device_by_id1) | **GET** /api/v2/devicetypes/members/{deviceId} | Get device types for device
[**get_device_types**](DeviceTypesApi.md#get_device_types) | **GET** /api/v1/devicetypes | Get all device types
[**get_device_types1**](DeviceTypesApi.md#get_device_types1) | **GET** /api/v2/devicetypes | Get all device types


# **add_member_by_id_to_type**
> add_member_by_id_to_type(id, device_id)

Associate an existing device with device type

Adds an existing device to a device type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceTypesApi()
id = 789 # int | The id of the device type
device_id = 789 # int | The id of the device

try:
    # Associate an existing device with device type
    api_instance.add_member_by_id_to_type(id, device_id)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->add_member_by_id_to_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device type | 
 **device_id** | **int**| The id of the device | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_member_by_id_to_type1**
> add_member_by_id_to_type1(id, device_id)

Associate an existing device with device type

Adds an existing device to a device type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceTypesApi()
id = 789 # int | The id of the device type
device_id = 789 # int | The id of the device

try:
    # Associate an existing device with device type
    api_instance.add_member_by_id_to_type1(id, device_id)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->add_member_by_id_to_type1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device type | 
 **device_id** | **int**| The id of the device | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_type**
> DeviceTypeResponseDtoV1 create_device_type(device_type_request_dto)

Create device type

Create new device type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceTypesApi()
device_type_request_dto = swagger_client.DeviceTypeRequestDto() # DeviceTypeRequestDto | Device request object

try:
    # Create device type
    api_response = api_instance.create_device_type(device_type_request_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->create_device_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_type_request_dto** | [**DeviceTypeRequestDto**](DeviceTypeRequestDto.md)| Device request object | 

### Return type

[**DeviceTypeResponseDtoV1**](DeviceTypeResponseDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_type1**
> DeviceTypeResponseDto create_device_type1(device_type_request_dto)

Create device type

Create new device type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceTypesApi()
device_type_request_dto = swagger_client.DeviceTypeRequestDto() # DeviceTypeRequestDto | Device request object

try:
    # Create device type
    api_response = api_instance.create_device_type1(device_type_request_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->create_device_type1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_type_request_dto** | [**DeviceTypeRequestDto**](DeviceTypeRequestDto.md)| Device request object | 

### Return type

[**DeviceTypeResponseDto**](DeviceTypeResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_type_by_id**
> ResponseEntity delete_device_type_by_id(id)

Delete device type

Deletes an existing device type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceTypesApi()
id = 789 # int | The id of the device type to be deleted

try:
    # Delete device type
    api_response = api_instance.delete_device_type_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->delete_device_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device type to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_type_by_id1**
> ResponseEntity delete_device_type_by_id1(id)

Delete device type

Deletes an existing device type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceTypesApi()
id = 789 # int | The id of the device type to be deleted

try:
    # Delete device type
    api_response = api_instance.delete_device_type_by_id1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->delete_device_type_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device type to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_type_member_by_id**
> ResponseEntity delete_device_type_member_by_id(id, device_id)

Remove device type member

Removes a single device from a device type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceTypesApi()
id = 789 # int | The id of the device type
device_id = 789 # int | The id of the device

try:
    # Remove device type member
    api_response = api_instance.delete_device_type_member_by_id(id, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->delete_device_type_member_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device type | 
 **device_id** | **int**| The id of the device | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_type_member_by_id1**
> ResponseEntity delete_device_type_member_by_id1(id, device_id)

Remove device type member

Removes a single device from a device type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceTypesApi()
id = 789 # int | The id of the device type
device_id = 789 # int | The id of the device

try:
    # Remove device type member
    api_response = api_instance.delete_device_type_member_by_id1(id, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->delete_device_type_member_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device type | 
 **device_id** | **int**| The id of the device | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_device_types**
> PagerDeviceTypeResponseDto filter_device_types(filter, include_devices=include_devices, include_object_types=include_object_types, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Filter devices

Find all device types that match the criteria

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceTypesApi()
filter = swagger_client.DeviceGroupFilter() # DeviceGroupFilter | Device group filter that will be used for filtering
include_devices = false # bool | Determines whether to include device members of device types (optional) (default to false)
include_object_types = false # bool | Determines whether to include object type members of device types (optional) (default to false)
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Filter devices
    api_response = api_instance.filter_device_types(filter, include_devices=include_devices, include_object_types=include_object_types, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->filter_device_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**DeviceGroupFilter**](DeviceGroupFilter.md)| Device group filter that will be used for filtering | 
 **include_devices** | **bool**| Determines whether to include device members of device types | [optional] [default to false]
 **include_object_types** | **bool**| Determines whether to include object type members of device types | [optional] [default to false]
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerDeviceTypeResponseDto**](PagerDeviceTypeResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ancestors_for_device_type**
> list[list[DeviceTypeDto]] get_ancestors_for_device_type(id)

Get ancestors of the device type

Gets a list of ancestors for each type id in the input list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceTypesApi()
id = 789 # int | The id of the device type

try:
    # Get ancestors of the device type
    api_response = api_instance.get_ancestors_for_device_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->get_ancestors_for_device_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device type | 

### Return type

**list[list[DeviceTypeDto]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ancestors_for_device_types**
> list[list[DeviceTypeDto]] get_ancestors_for_device_types(ids)

Get ancestors of the device types

Gets a list of ancestors for each type id in the input list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceTypesApi()
ids = 'ids_example' # str | The ids of the device types

try:
    # Get ancestors of the device types
    api_response = api_instance.get_ancestors_for_device_types(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->get_ancestors_for_device_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| The ids of the device types | 

### Return type

**list[list[DeviceTypeDto]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type_by_id**
> DeviceTypeResponseDtoV1 get_device_type_by_id(id)

Get device type

Get device type by device id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceTypesApi()
id = 789 # int | Device type id

try:
    # Get device type
    api_response = api_instance.get_device_type_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->get_device_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Device type id | 

### Return type

[**DeviceTypeResponseDtoV1**](DeviceTypeResponseDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type_by_id1**
> DeviceTypeResponseDto get_device_type_by_id1(id)

Get device type

Get device type by device id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceTypesApi()
id = 789 # int | Device type id

try:
    # Get device type
    api_response = api_instance.get_device_type_by_id1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->get_device_type_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Device type id | 

### Return type

[**DeviceTypeResponseDto**](DeviceTypeResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type_for_device_by_id**
> list[DeviceTypeDto] get_device_type_for_device_by_id(device_id)

Get device types for device

Get devices types for device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceTypesApi()
device_id = 789 # int | Device id

try:
    # Get device types for device
    api_response = api_instance.get_device_type_for_device_by_id(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->get_device_type_for_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Device id | 

### Return type

[**list[DeviceTypeDto]**](DeviceTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type_for_device_by_id1**
> list[DeviceTypeDto] get_device_type_for_device_by_id1(device_id, sort_by=sort_by)

Get device types for device

Get devices types for device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceTypesApi()
device_id = 789 # int | Device id
sort_by = 'sort_by_example' # str | String array of format \"property, -property\", where minus is for descending (optional)

try:
    # Get device types for device
    api_response = api_instance.get_device_type_for_device_by_id1(device_id, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->get_device_type_for_device_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Device id | 
 **sort_by** | **str**| String array of format \&quot;property, -property\&quot;, where minus is for descending | [optional] 

### Return type

[**list[DeviceTypeDto]**](DeviceTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_types**
> PagerDeviceTypeResponseDtoV1 get_device_types(page=page, size=size, include_members=include_members)

Get all device types

Endpoint for retrieving all device types that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceTypesApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_members = false # bool | Determines whether to include members of device types (optional) (default to false)

try:
    # Get all device types
    api_response = api_instance.get_device_types(page=page, size=size, include_members=include_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->get_device_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_members** | **bool**| Determines whether to include members of device types | [optional] [default to false]

### Return type

[**PagerDeviceTypeResponseDtoV1**](PagerDeviceTypeResponseDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_types1**
> PagerDeviceTypeResponseDto get_device_types1(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields, include_object_types=include_object_types)

Get all device types

Endpoint for retrieving all device types that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceTypesApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)
include_object_types = false # bool | Determines whether to include object type members of device types (optional) (default to false)

try:
    # Get all device types
    api_response = api_instance.get_device_types1(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields, include_object_types=include_object_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->get_device_types1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 
 **include_object_types** | **bool**| Determines whether to include object type members of device types | [optional] [default to false]

### Return type

[**PagerDeviceTypeResponseDto**](PagerDeviceTypeResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

