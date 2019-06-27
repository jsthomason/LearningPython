# swagger_client.DeviceGroupsApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_member_by_id_to_group**](DeviceGroupsApi.md#add_member_by_id_to_group) | **POST** /api/v1/devicegroups/{id}/members/{deviceId} | Add an existing device to device group
[**add_member_by_id_to_group1**](DeviceGroupsApi.md#add_member_by_id_to_group1) | **POST** /api/v2/devicegroups/{id}/members/{deviceId} | Add an existing device to device group
[**create_device_group**](DeviceGroupsApi.md#create_device_group) | **POST** /api/v1/devicegroups | Create device group
[**create_device_group1**](DeviceGroupsApi.md#create_device_group1) | **POST** /api/v2/devicegroups | Create device group
[**delete_device_group_by_id**](DeviceGroupsApi.md#delete_device_group_by_id) | **DELETE** /api/v1/devicegroups/{id} | Delete device group
[**delete_device_group_by_id1**](DeviceGroupsApi.md#delete_device_group_by_id1) | **DELETE** /api/v2/devicegroups/{id} | Delete device group
[**delete_device_group_member_by_id**](DeviceGroupsApi.md#delete_device_group_member_by_id) | **DELETE** /api/v1/devicegroups/{id}/members/{deviceId} | Remove device group member
[**delete_device_group_member_by_id1**](DeviceGroupsApi.md#delete_device_group_member_by_id1) | **DELETE** /api/v2/devicegroups/{id}/members/{deviceId} | Remove device group member
[**filter_device_group**](DeviceGroupsApi.md#filter_device_group) | **POST** /api/v2/devicegroups/filter | Filter device groups
[**get_ancestors_for_device_group**](DeviceGroupsApi.md#get_ancestors_for_device_group) | **GET** /api/v2/devicegroups/{id}/ancestors | Get ancestors of the device group
[**get_ancestors_for_device_groups**](DeviceGroupsApi.md#get_ancestors_for_device_groups) | **GET** /api/v2/devicegroups/ancestors/{ids} | Get ancestors of the device groups
[**get_device_group_by_id**](DeviceGroupsApi.md#get_device_group_by_id) | **GET** /api/v1/devicegroups/{id} | Get device group by Id
[**get_device_group_by_id1**](DeviceGroupsApi.md#get_device_group_by_id1) | **GET** /api/v2/devicegroups/{id} | Get device group by Id
[**get_device_groups**](DeviceGroupsApi.md#get_device_groups) | **GET** /api/v1/devicegroups | Get all device groups
[**get_device_groups1**](DeviceGroupsApi.md#get_device_groups1) | **GET** /api/v2/devicegroups | Get all device groups
[**get_device_tags_by_id**](DeviceGroupsApi.md#get_device_tags_by_id) | **GET** /api/v1/devicetags/{id} | Get device tags  by Id
[**get_device_tags_by_id1**](DeviceGroupsApi.md#get_device_tags_by_id1) | **GET** /api/v2/devicetags/{id} | Get device tags  by Id
[**partially_update_device_group_by_id**](DeviceGroupsApi.md#partially_update_device_group_by_id) | **PATCH** /api/v1/devicegroups/{id} | Partially update device group
[**partially_update_device_group_by_id1**](DeviceGroupsApi.md#partially_update_device_group_by_id1) | **PATCH** /api/v2/devicegroups/{id} | Partially update device group
[**update_device_group_by_id**](DeviceGroupsApi.md#update_device_group_by_id) | **PUT** /api/v1/devicegroups/{id} | Update device group
[**update_device_group_by_id1**](DeviceGroupsApi.md#update_device_group_by_id1) | **PUT** /api/v2/devicegroups/{id} | Update device group


# **add_member_by_id_to_group**
> add_member_by_id_to_group(id, device_id)

Add an existing device to device group

Adds an existing device to a device group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
id = 789 # int | The id of the device group
device_id = 789 # int | The id of the device

try:
    # Add an existing device to device group
    api_instance.add_member_by_id_to_group(id, device_id)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->add_member_by_id_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group | 
 **device_id** | **int**| The id of the device | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_member_by_id_to_group1**
> add_member_by_id_to_group1(id, device_id)

Add an existing device to device group

Adds an existing device to a device group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
id = 789 # int | The id of the device group
device_id = 789 # int | The id of the device

try:
    # Add an existing device to device group
    api_instance.add_member_by_id_to_group1(id, device_id)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->add_member_by_id_to_group1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group | 
 **device_id** | **int**| The id of the device | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_group**
> DeviceGroupDto create_device_group(device_group)

Create device group

Creates a new device group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
device_group = swagger_client.DeviceGroupRequestDto() # DeviceGroupRequestDto | DeviceGroup request object that contains required information for creating new device group

try:
    # Create device group
    api_response = api_instance.create_device_group(device_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->create_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group** | [**DeviceGroupRequestDto**](DeviceGroupRequestDto.md)| DeviceGroup request object that contains required information for creating new device group | 

### Return type

[**DeviceGroupDto**](DeviceGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_group1**
> DeviceGroupDto create_device_group1(device_group)

Create device group

Creates a new device group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
device_group = swagger_client.DeviceGroupRequestDto() # DeviceGroupRequestDto | DeviceGroup request object that contains required information for creating new device group

try:
    # Create device group
    api_response = api_instance.create_device_group1(device_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->create_device_group1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group** | [**DeviceGroupRequestDto**](DeviceGroupRequestDto.md)| DeviceGroup request object that contains required information for creating new device group | 

### Return type

[**DeviceGroupDto**](DeviceGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_group_by_id**
> ResponseEntity delete_device_group_by_id(id)

Delete device group

Deletes an existing device group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
id = 789 # int | The id of the device group to be deleted

try:
    # Delete device group
    api_response = api_instance.delete_device_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->delete_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_group_by_id1**
> ResponseEntity delete_device_group_by_id1(id)

Delete device group

Deletes an existing device group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
id = 789 # int | The id of the device group to be deleted

try:
    # Delete device group
    api_response = api_instance.delete_device_group_by_id1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->delete_device_group_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_group_member_by_id**
> ResponseEntity delete_device_group_member_by_id(id, device_id)

Remove device group member

Removes a single device from a device group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
id = 789 # int | The id of the device group
device_id = 789 # int | The id of the device

try:
    # Remove device group member
    api_response = api_instance.delete_device_group_member_by_id(id, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->delete_device_group_member_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group | 
 **device_id** | **int**| The id of the device | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_group_member_by_id1**
> ResponseEntity delete_device_group_member_by_id1(id, device_id)

Remove device group member

Removes a single device from a device group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
id = 789 # int | The id of the device group
device_id = 789 # int | The id of the device

try:
    # Remove device group member
    api_response = api_instance.delete_device_group_member_by_id1(id, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->delete_device_group_member_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group | 
 **device_id** | **int**| The id of the device | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_device_group**
> PagerDeviceGroupDto filter_device_group(filter, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Filter device groups

Find all device groups that match the criteria

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
filter = swagger_client.DeviceGroupFilter() # DeviceGroupFilter | Device group filter that will be used for filtering
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Filter device groups
    api_response = api_instance.filter_device_group(filter, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->filter_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**DeviceGroupFilter**](DeviceGroupFilter.md)| Device group filter that will be used for filtering | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerDeviceGroupDto**](PagerDeviceGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ancestors_for_device_group**
> list[list[DeviceGroupDto]] get_ancestors_for_device_group(id)

Get ancestors of the device group

Gets a list of ancestors for each group id in the input list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
id = 789 # int | The id of the device group

try:
    # Get ancestors of the device group
    api_response = api_instance.get_ancestors_for_device_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->get_ancestors_for_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group | 

### Return type

**list[list[DeviceGroupDto]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ancestors_for_device_groups**
> list[list[DeviceGroupDto]] get_ancestors_for_device_groups(ids)

Get ancestors of the device groups

Gets a list of ancestors for each group id in the input list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
ids = 'ids_example' # str | The ids of the device groups

try:
    # Get ancestors of the device groups
    api_response = api_instance.get_ancestors_for_device_groups(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->get_ancestors_for_device_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| The ids of the device groups | 

### Return type

**list[list[DeviceGroupDto]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_by_id**
> DeviceGroupDto get_device_group_by_id(id, include_members=include_members)

Get device group by Id

Gets a single device group object by provided Id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
id = 789 # int | The id of the requested device group
include_members = false # bool | Determines whether to include members of device groups (optional) (default to false)

try:
    # Get device group by Id
    api_response = api_instance.get_device_group_by_id(id, include_members=include_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->get_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the requested device group | 
 **include_members** | **bool**| Determines whether to include members of device groups | [optional] [default to false]

### Return type

[**DeviceGroupDto**](DeviceGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_by_id1**
> DeviceGroupDto get_device_group_by_id1(id, include_members=include_members)

Get device group by Id

Gets a single device group object by provided Id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
id = 789 # int | The id of the requested device group
include_members = false # bool | Determines whether to include members of device groups (optional) (default to false)

try:
    # Get device group by Id
    api_response = api_instance.get_device_group_by_id1(id, include_members=include_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->get_device_group_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the requested device group | 
 **include_members** | **bool**| Determines whether to include members of device groups | [optional] [default to false]

### Return type

[**DeviceGroupDto**](DeviceGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_groups**
> PagerDeviceGroupDto get_device_groups(page=page, size=size, include_members=include_members)

Get all device groups

Endpoint for retrieving all device groups that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_members = false # bool | Determines whether to include members of device groups (optional) (default to false)

try:
    # Get all device groups
    api_response = api_instance.get_device_groups(page=page, size=size, include_members=include_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->get_device_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_members** | **bool**| Determines whether to include members of device groups | [optional] [default to false]

### Return type

[**PagerDeviceGroupDto**](PagerDeviceGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_groups1**
> PagerDeviceGroupDto get_device_groups1(include_members=include_members, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all device groups

Endpoint for retrieving all device groups that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
include_members = false # bool | Determines whether to include members of device groups (optional) (default to false)
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all device groups
    api_response = api_instance.get_device_groups1(include_members=include_members, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->get_device_groups1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_members** | **bool**| Determines whether to include members of device groups | [optional] [default to false]
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerDeviceGroupDto**](PagerDeviceGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_tags_by_id**
> DeviceTagDto get_device_tags_by_id(id)

Get device tags  by Id

Gets a single entity of type device tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
id = 789 # int | The id of the requested device tag

try:
    # Get device tags  by Id
    api_response = api_instance.get_device_tags_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->get_device_tags_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the requested device tag | 

### Return type

[**DeviceTagDto**](DeviceTagDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_tags_by_id1**
> DeviceTagDto get_device_tags_by_id1(id)

Get device tags  by Id

Gets a single entity of type device tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
id = 789 # int | The id of the requested device tag

try:
    # Get device tags  by Id
    api_response = api_instance.get_device_tags_by_id1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->get_device_tags_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the requested device tag | 

### Return type

[**DeviceTagDto**](DeviceTagDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_device_group_by_id**
> DeviceGroupDto partially_update_device_group_by_id(id, device_group)

Partially update device group

Updates an existing device group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
id = 789 # int | The id of the device group to be updated
device_group = swagger_client.DeviceGroupRequestDto() # DeviceGroupRequestDto | DeviceGroup request object that contains required information for updating device group

try:
    # Partially update device group
    api_response = api_instance.partially_update_device_group_by_id(id, device_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->partially_update_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group to be updated | 
 **device_group** | [**DeviceGroupRequestDto**](DeviceGroupRequestDto.md)| DeviceGroup request object that contains required information for updating device group | 

### Return type

[**DeviceGroupDto**](DeviceGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_device_group_by_id1**
> DeviceGroupDto partially_update_device_group_by_id1(id, device_group)

Partially update device group

Updates an existing device group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
id = 789 # int | The id of the device group to be updated
device_group = swagger_client.DeviceGroupRequestDto() # DeviceGroupRequestDto | DeviceGroup request object that contains required information for updating device group

try:
    # Partially update device group
    api_response = api_instance.partially_update_device_group_by_id1(id, device_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->partially_update_device_group_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group to be updated | 
 **device_group** | [**DeviceGroupRequestDto**](DeviceGroupRequestDto.md)| DeviceGroup request object that contains required information for updating device group | 

### Return type

[**DeviceGroupDto**](DeviceGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_by_id**
> DeviceGroupDto update_device_group_by_id(id, device_group)

Update device group

Updates an existing device group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
id = 789 # int | The id of the device group to be updated
device_group = swagger_client.DeviceGroupRequestDto() # DeviceGroupRequestDto | DeviceGroup request object that contains required information for updating device group

try:
    # Update device group
    api_response = api_instance.update_device_group_by_id(id, device_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->update_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group to be updated | 
 **device_group** | [**DeviceGroupRequestDto**](DeviceGroupRequestDto.md)| DeviceGroup request object that contains required information for updating device group | 

### Return type

[**DeviceGroupDto**](DeviceGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_by_id1**
> DeviceGroupDto update_device_group_by_id1(id, device_group)

Update device group

Updates an existing device group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupsApi()
id = 789 # int | The id of the device group to be updated
device_group = swagger_client.DeviceGroupRequestDto() # DeviceGroupRequestDto | DeviceGroup request object that contains required information for updating device group

try:
    # Update device group
    api_response = api_instance.update_device_group_by_id1(id, device_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupsApi->update_device_group_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group to be updated | 
 **device_group** | [**DeviceGroupRequestDto**](DeviceGroupRequestDto.md)| DeviceGroup request object that contains required information for updating device group | 

### Return type

[**DeviceGroupDto**](DeviceGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

