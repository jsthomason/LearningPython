# swagger_client.ObjectsApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_object**](ObjectsApi.md#create_object) | **POST** /api/v1/devices/{deviceId}/objects | Create object
[**create_object1**](ObjectsApi.md#create_object1) | **POST** /api/v2/devices/{deviceId}/objects | Create object
[**delete_object_by_id**](ObjectsApi.md#delete_object_by_id) | **DELETE** /api/v1/devices/{deviceId}/objects/{id} | Delete object
[**delete_object_by_id1**](ObjectsApi.md#delete_object_by_id1) | **DELETE** /api/v2/devices/{deviceId}/objects/{id} | Delete object
[**filter_objects**](ObjectsApi.md#filter_objects) | **POST** /api/v1/devices/objects/filter | Find objects
[**filter_objects1**](ObjectsApi.md#filter_objects1) | **POST** /api/v2/devices/objects/filter | Find objects
[**get_object_by_id**](ObjectsApi.md#get_object_by_id) | **GET** /api/v1/devices/{deviceId}/objects/{id} | Get object by Id
[**get_object_by_id1**](ObjectsApi.md#get_object_by_id1) | **GET** /api/v2/devices/{deviceId}/objects/{id} | Get object by Id
[**get_objects**](ObjectsApi.md#get_objects) | **GET** /api/v1/devices/{deviceId}/objects | Get all objects for a device
[**get_objects1**](ObjectsApi.md#get_objects1) | **GET** /api/v2/devices/{deviceId}/objects | Get all objects for a device
[**partially_update_object_by_id**](ObjectsApi.md#partially_update_object_by_id) | **PATCH** /api/v1/devices/{deviceId}/objects/{id} | Partially update object
[**partially_update_object_by_id1**](ObjectsApi.md#partially_update_object_by_id1) | **PATCH** /api/v2/devices/{deviceId}/objects/{id} | Partially update object
[**update_object_by_id**](ObjectsApi.md#update_object_by_id) | **PUT** /api/v1/devices/{deviceId}/objects/{id} | Update object
[**update_object_by_id1**](ObjectsApi.md#update_object_by_id1) | **PUT** /api/v2/devices/{deviceId}/objects/{id} | Update object


# **create_object**
> DeviceObjectDto create_object(device_id, object)

Create object

Creates a new object for a specific device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectsApi()
device_id = 789 # int | The id of the device
object = swagger_client.DeviceObjectRequestDto() # DeviceObjectRequestDto | Object that will be created

try:
    # Create object
    api_response = api_instance.create_object(device_id, object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->create_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The id of the device | 
 **object** | [**DeviceObjectRequestDto**](DeviceObjectRequestDto.md)| Object that will be created | 

### Return type

[**DeviceObjectDto**](DeviceObjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_object1**
> DeviceObjectDto create_object1(device_id, object)

Create object

Creates a new object for a specific device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectsApi()
device_id = 789 # int | The id of the device
object = swagger_client.DeviceObjectRequestDto() # DeviceObjectRequestDto | Object that will be created

try:
    # Create object
    api_response = api_instance.create_object1(device_id, object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->create_object1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The id of the device | 
 **object** | [**DeviceObjectRequestDto**](DeviceObjectRequestDto.md)| Object that will be created | 

### Return type

[**DeviceObjectDto**](DeviceObjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object_by_id**
> ResponseEntity delete_object_by_id(device_id, id)

Delete object

Deletes an existing object

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectsApi()
device_id = 789 # int | The id of the device this object belongs to
id = 789 # int | The id of the object to be deleted

try:
    # Delete object
    api_response = api_instance.delete_object_by_id(device_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->delete_object_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The id of the device this object belongs to | 
 **id** | **int**| The id of the object to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object_by_id1**
> ResponseEntity delete_object_by_id1(device_id, id)

Delete object

Deletes an existing object

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectsApi()
device_id = 789 # int | The id of the device this object belongs to
id = 789 # int | The id of the object to be deleted

try:
    # Delete object
    api_response = api_instance.delete_object_by_id1(device_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->delete_object_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The id of the device this object belongs to | 
 **id** | **int**| The id of the object to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_objects**
> list[DeviceObjectDto] filter_objects(object_filter, include_indicators=include_indicators, include_extended_info=include_extended_info, local_only=local_only)

Find objects

Filter the entire object collection with provided filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectsApi()
object_filter = swagger_client.ObjectFilter() # ObjectFilter | ObjectFilter will be used for applying filtering to the set of objects.
include_indicators = false # bool | Determines whether to include indicators or not (optional) (default to false)
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)
local_only = false # bool | Determines whether to execute distributed request or not (optional) (default to false)

try:
    # Find objects
    api_response = api_instance.filter_objects(object_filter, include_indicators=include_indicators, include_extended_info=include_extended_info, local_only=local_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->filter_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_filter** | [**ObjectFilter**](ObjectFilter.md)| ObjectFilter will be used for applying filtering to the set of objects. | 
 **include_indicators** | **bool**| Determines whether to include indicators or not | [optional] [default to false]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]
 **local_only** | **bool**| Determines whether to execute distributed request or not | [optional] [default to false]

### Return type

[**list[DeviceObjectDto]**](DeviceObjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_objects1**
> PagerDeviceObjectDto filter_objects1(object_filter, include_indicators=include_indicators, include_extended_info=include_extended_info, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Find objects

Filter the entire object collection with provided filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectsApi()
object_filter = swagger_client.ObjectFilter() # ObjectFilter | ObjectFilter will be used for applying filtering to the set of objects.
include_indicators = false # bool | Determines whether to include indicators or not (optional) (default to false)
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Find objects
    api_response = api_instance.filter_objects1(object_filter, include_indicators=include_indicators, include_extended_info=include_extended_info, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->filter_objects1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_filter** | [**ObjectFilter**](ObjectFilter.md)| ObjectFilter will be used for applying filtering to the set of objects. | 
 **include_indicators** | **bool**| Determines whether to include indicators or not | [optional] [default to false]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerDeviceObjectDto**](PagerDeviceObjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_by_id**
> DeviceObjectDto get_object_by_id(device_id, id, include_indicators=include_indicators, include_extended_info=include_extended_info)

Get object by Id

Gets a single object object by provided Id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectsApi()
device_id = 789 # int | The id of the device this object belongs to
id = 789 # int | The id of the object
include_indicators = false # bool | Determines whether to include indicators (optional) (default to false)
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Get object by Id
    api_response = api_instance.get_object_by_id(device_id, id, include_indicators=include_indicators, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->get_object_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The id of the device this object belongs to | 
 **id** | **int**| The id of the object | 
 **include_indicators** | **bool**| Determines whether to include indicators | [optional] [default to false]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**DeviceObjectDto**](DeviceObjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_by_id1**
> DeviceObjectDto get_object_by_id1(device_id, id, include_indicators=include_indicators, include_indicator_metadata=include_indicator_metadata, include_extended_info=include_extended_info)

Get object by Id

Gets a single object object by provided Id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectsApi()
device_id = 789 # int | The id of the device this object belongs to
id = 789 # int | The id of the object
include_indicators = false # bool | Determines whether to include indicators (optional) (default to false)
include_indicator_metadata = false # bool | Determines whether to include indicator metadata (optional) (default to false)
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Get object by Id
    api_response = api_instance.get_object_by_id1(device_id, id, include_indicators=include_indicators, include_indicator_metadata=include_indicator_metadata, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->get_object_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The id of the device this object belongs to | 
 **id** | **int**| The id of the object | 
 **include_indicators** | **bool**| Determines whether to include indicators | [optional] [default to false]
 **include_indicator_metadata** | **bool**| Determines whether to include indicator metadata | [optional] [default to false]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**DeviceObjectDto**](DeviceObjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_objects**
> PagerDeviceObjectDto get_objects(device_id, page=page, size=size, include_indicators=include_indicators, include_extended_info=include_extended_info)

Get all objects for a device

Endpoint for retrieving all objects for a specific device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectsApi()
device_id = 789 # int | The id of the device
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_indicators = false # bool | Determines whether to include indicators (optional) (default to false)
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)

try:
    # Get all objects for a device
    api_response = api_instance.get_objects(device_id, page=page, size=size, include_indicators=include_indicators, include_extended_info=include_extended_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->get_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The id of the device | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_indicators** | **bool**| Determines whether to include indicators | [optional] [default to false]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]

### Return type

[**PagerDeviceObjectDto**](PagerDeviceObjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_objects1**
> PagerDeviceObjectDto get_objects1(device_id, include_indicators=include_indicators, include_indicator_metadata=include_indicator_metadata, include_extended_info=include_extended_info, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all objects for a device

Endpoint for retrieving all objects for a specific device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectsApi()
device_id = 789 # int | The id of the device
include_indicators = false # bool | Determines whether to include indicators (optional) (default to false)
include_indicator_metadata = false # bool | Determines whether to include indicator metadata (optional) (default to false)
include_extended_info = true # bool | Determines whether to include extendedInfo or not (optional) (default to true)
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all objects for a device
    api_response = api_instance.get_objects1(device_id, include_indicators=include_indicators, include_indicator_metadata=include_indicator_metadata, include_extended_info=include_extended_info, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->get_objects1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The id of the device | 
 **include_indicators** | **bool**| Determines whether to include indicators | [optional] [default to false]
 **include_indicator_metadata** | **bool**| Determines whether to include indicator metadata | [optional] [default to false]
 **include_extended_info** | **bool**| Determines whether to include extendedInfo or not | [optional] [default to true]
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerDeviceObjectDto**](PagerDeviceObjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_object_by_id**
> DeviceObjectDto partially_update_object_by_id(device_id, id, object)

Partially update object

Partially updates an existing object

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectsApi()
device_id = 789 # int | The id of the device this object belongs to
id = 789 # int | The id of the object to be updated
object = swagger_client.DeviceObjectUpdateRequestDto() # DeviceObjectUpdateRequestDto | Object to be updated

try:
    # Partially update object
    api_response = api_instance.partially_update_object_by_id(device_id, id, object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->partially_update_object_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The id of the device this object belongs to | 
 **id** | **int**| The id of the object to be updated | 
 **object** | [**DeviceObjectUpdateRequestDto**](DeviceObjectUpdateRequestDto.md)| Object to be updated | 

### Return type

[**DeviceObjectDto**](DeviceObjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_object_by_id1**
> DeviceObjectDto partially_update_object_by_id1(device_id, id, object)

Partially update object

Partially updates an existing object

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectsApi()
device_id = 789 # int | The id of the device this object belongs to
id = 789 # int | The id of the object to be updated
object = swagger_client.DeviceObjectUpdateRequestDto() # DeviceObjectUpdateRequestDto | Object to be updated

try:
    # Partially update object
    api_response = api_instance.partially_update_object_by_id1(device_id, id, object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->partially_update_object_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The id of the device this object belongs to | 
 **id** | **int**| The id of the object to be updated | 
 **object** | [**DeviceObjectUpdateRequestDto**](DeviceObjectUpdateRequestDto.md)| Object to be updated | 

### Return type

[**DeviceObjectDto**](DeviceObjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_by_id**
> DeviceObjectDto update_object_by_id(device_id, id, object)

Update object

Updates an existing object

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectsApi()
device_id = 789 # int | The id of the device this object belongs to
id = 789 # int | The id of the object to be updated
object = swagger_client.DeviceObjectUpdateRequestDto() # DeviceObjectUpdateRequestDto | DeviceObjectDto to be updated

try:
    # Update object
    api_response = api_instance.update_object_by_id(device_id, id, object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->update_object_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The id of the device this object belongs to | 
 **id** | **int**| The id of the object to be updated | 
 **object** | [**DeviceObjectUpdateRequestDto**](DeviceObjectUpdateRequestDto.md)| DeviceObjectDto to be updated | 

### Return type

[**DeviceObjectDto**](DeviceObjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_by_id1**
> DeviceObjectDto update_object_by_id1(device_id, id, object)

Update object

Updates an existing object

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectsApi()
device_id = 789 # int | The id of the device this object belongs to
id = 789 # int | The id of the object to be updated
object = swagger_client.DeviceObjectUpdateRequestDto() # DeviceObjectUpdateRequestDto | DeviceObjectDto to be updated

try:
    # Update object
    api_response = api_instance.update_object_by_id1(device_id, id, object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->update_object_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| The id of the device this object belongs to | 
 **id** | **int**| The id of the object to be updated | 
 **object** | [**DeviceObjectUpdateRequestDto**](DeviceObjectUpdateRequestDto.md)| DeviceObjectDto to be updated | 

### Return type

[**DeviceObjectDto**](DeviceObjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

