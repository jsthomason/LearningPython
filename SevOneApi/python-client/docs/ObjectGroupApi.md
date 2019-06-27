# swagger_client.ObjectGroupApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_object_group_member**](ObjectGroupApi.md#add_object_group_member) | **POST** /api/v2/objectgroups/{id}/members | Add a member to the object group
[**add_object_group_member1**](ObjectGroupApi.md#add_object_group_member1) | **POST** /api/v1/objectgroups/{id}/members | Add a member to the object group
[**create_object_group**](ObjectGroupApi.md#create_object_group) | **POST** /api/v2/objectgroups | Create object group
[**create_object_group1**](ObjectGroupApi.md#create_object_group1) | **POST** /api/v1/objectgroups | Create object group
[**delete_object_group_by_id**](ObjectGroupApi.md#delete_object_group_by_id) | **DELETE** /api/v2/objectgroups/{id} | Delete object group
[**delete_object_group_by_id1**](ObjectGroupApi.md#delete_object_group_by_id1) | **DELETE** /api/v1/objectgroups/{id} | Delete object group
[**filter_object_group_mappings**](ObjectGroupApi.md#filter_object_group_mappings) | **POST** /api/v2/objectgroups/members/filter | Filter object to object group mappings
[**find_object_group**](ObjectGroupApi.md#find_object_group) | **POST** /api/v2/objectgroups/filter | Find object groups
[**get_ancestors**](ObjectGroupApi.md#get_ancestors) | **GET** /api/v2/objectgroups/ancestors/{ids} | Get ancestors to the object groups
[**get_ancestors1**](ObjectGroupApi.md#get_ancestors1) | **GET** /api/v2/objectgroups/{id}/ancestors | Get ancestors to the object groups
[**get_object_group_by_id**](ObjectGroupApi.md#get_object_group_by_id) | **GET** /api/v2/objectgroups/{id} | Get object group by Id
[**get_object_group_by_id1**](ObjectGroupApi.md#get_object_group_by_id1) | **GET** /api/v1/objectgroups/{id} | Get object group by Id
[**get_object_group_mappings**](ObjectGroupApi.md#get_object_group_mappings) | **GET** /api/v2/objectgroups/{id}/members | Get object to object group mappings
[**get_object_groups**](ObjectGroupApi.md#get_object_groups) | **GET** /api/v2/objectgroups | Get all object groups
[**get_object_groups1**](ObjectGroupApi.md#get_object_groups1) | **GET** /api/v1/objectgroups | Get all object groups
[**partially_update_object_group_by_id**](ObjectGroupApi.md#partially_update_object_group_by_id) | **PATCH** /api/v2/objectgroups/{id} | Partially update object group
[**partially_update_object_group_by_id1**](ObjectGroupApi.md#partially_update_object_group_by_id1) | **PATCH** /api/v1/objectgroups/{id} | Partially update object group
[**remove_object_group_member**](ObjectGroupApi.md#remove_object_group_member) | **DELETE** /api/v2/objectgroups/{id}/members | Remove a member from the object group
[**remove_object_group_member1**](ObjectGroupApi.md#remove_object_group_member1) | **DELETE** /api/v1/objectgroups/{id}/members | Remove a member from the object group
[**update_object_group_by_id**](ObjectGroupApi.md#update_object_group_by_id) | **PUT** /api/v2/objectgroups/{id} | Update object group
[**update_object_group_by_id1**](ObjectGroupApi.md#update_object_group_by_id1) | **PUT** /api/v1/objectgroups/{id} | Update object group


# **add_object_group_member**
> bool add_object_group_member(id, request)

Add a member to the object group

Adds a single object to an object group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
id = 789 # int | The id of the object group
request = swagger_client.DeviceObjectId() # DeviceObjectId | request

try:
    # Add a member to the object group
    api_response = api_instance.add_object_group_member(id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->add_object_group_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group | 
 **request** | [**DeviceObjectId**](DeviceObjectId.md)| request | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_object_group_member1**
> bool add_object_group_member1(id, request)

Add a member to the object group

Adds a single object to an object group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
id = 789 # int | The id of the object group
request = swagger_client.DeviceObjectId() # DeviceObjectId | request

try:
    # Add a member to the object group
    api_response = api_instance.add_object_group_member1(id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->add_object_group_member1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group | 
 **request** | [**DeviceObjectId**](DeviceObjectId.md)| request | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_object_group**
> ObjectGroupDto create_object_group(object_group)

Create object group

Creates a new object group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
object_group = swagger_client.ObjectGroupRequestDto() # ObjectGroupRequestDto | ObjectGroup request object

try:
    # Create object group
    api_response = api_instance.create_object_group(object_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->create_object_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_group** | [**ObjectGroupRequestDto**](ObjectGroupRequestDto.md)| ObjectGroup request object | 

### Return type

[**ObjectGroupDto**](ObjectGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_object_group1**
> ObjectGroupDto create_object_group1(object_group)

Create object group

Creates a new object group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
object_group = swagger_client.ObjectGroupRequestDto() # ObjectGroupRequestDto | ObjectGroup request object

try:
    # Create object group
    api_response = api_instance.create_object_group1(object_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->create_object_group1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_group** | [**ObjectGroupRequestDto**](ObjectGroupRequestDto.md)| ObjectGroup request object | 

### Return type

[**ObjectGroupDto**](ObjectGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object_group_by_id**
> ResponseEntity delete_object_group_by_id(id)

Delete object group

Deletes an existing object group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
id = 789 # int | The id of the object group to be deleted

try:
    # Delete object group
    api_response = api_instance.delete_object_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->delete_object_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object_group_by_id1**
> ResponseEntity delete_object_group_by_id1(id)

Delete object group

Deletes an existing object group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
id = 789 # int | The id of the object group to be deleted

try:
    # Delete object group
    api_response = api_instance.delete_object_group_by_id1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->delete_object_group_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_object_group_mappings**
> PagerDeviceObjectGroupMapping filter_object_group_mappings(filter, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Filter object to object group mappings

Gets object to object group mappings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
filter = swagger_client.DeviceObjectGroupMapFilter() # DeviceObjectGroupMapFilter | The id of the object group
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Filter object to object group mappings
    api_response = api_instance.filter_object_group_mappings(filter, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->filter_object_group_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**DeviceObjectGroupMapFilter**](DeviceObjectGroupMapFilter.md)| The id of the object group | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerDeviceObjectGroupMapping**](PagerDeviceObjectGroupMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_object_group**
> PagerObjectGroupDto find_object_group(filter_dto, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Find object groups

Filter the entire object group collection with provided filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
filter_dto = swagger_client.ObjectGroupFilterDto() # ObjectGroupFilterDto | ObjectGroup request object
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Find object groups
    api_response = api_instance.find_object_group(filter_dto, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->find_object_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_dto** | [**ObjectGroupFilterDto**](ObjectGroupFilterDto.md)| ObjectGroup request object | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerObjectGroupDto**](PagerObjectGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ancestors**
> list[list[ObjectGroupDto]] get_ancestors(ids)

Get ancestors to the object groups

Gets a list of ancestors for each group id in the input list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
ids = 'ids_example' # str | The ids of the object groups

try:
    # Get ancestors to the object groups
    api_response = api_instance.get_ancestors(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->get_ancestors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| The ids of the object groups | 

### Return type

**list[list[ObjectGroupDto]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ancestors1**
> list[list[ObjectGroupDto]] get_ancestors1(id)

Get ancestors to the object groups

Gets a list of ancestors for each group id in the input list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
id = 789 # int | The id of the object group

try:
    # Get ancestors to the object groups
    api_response = api_instance.get_ancestors1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->get_ancestors1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group | 

### Return type

**list[list[ObjectGroupDto]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group_by_id**
> ObjectGroupDto get_object_group_by_id(id, include_members=include_members, local_only=local_only)

Get object group by Id

Gets a single object group by provided Id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
id = 789 # int | The id of the object group
include_members = false # bool | Determines whether to include members of object groups (optional) (default to false)
local_only = false # bool | Determines whether to execute distributed request or not (optional) (default to false)

try:
    # Get object group by Id
    api_response = api_instance.get_object_group_by_id(id, include_members=include_members, local_only=local_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->get_object_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group | 
 **include_members** | **bool**| Determines whether to include members of object groups | [optional] [default to false]
 **local_only** | **bool**| Determines whether to execute distributed request or not | [optional] [default to false]

### Return type

[**ObjectGroupDto**](ObjectGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group_by_id1**
> ObjectGroupDto get_object_group_by_id1(id, include_members=include_members)

Get object group by Id

Gets a single object group by provided Id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
id = 789 # int | The id of the object group
include_members = false # bool | Determines whether to include members of object groups (optional) (default to false)

try:
    # Get object group by Id
    api_response = api_instance.get_object_group_by_id1(id, include_members=include_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->get_object_group_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group | 
 **include_members** | **bool**| Determines whether to include members of object groups | [optional] [default to false]

### Return type

[**ObjectGroupDto**](ObjectGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group_mappings**
> PagerDeviceObjectGroupMapping get_object_group_mappings(id, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get object to object group mappings

Gets object to object group mappings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
id = 789 # int | The id of the object group
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get object to object group mappings
    api_response = api_instance.get_object_group_mappings(id, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->get_object_group_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerDeviceObjectGroupMapping**](PagerDeviceObjectGroupMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_groups**
> PagerObjectGroupDto get_object_groups(include_members=include_members, local_only=local_only, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all object groups

Endpoint for retrieving all object groups that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
include_members = false # bool | Determines whether to include members of object groups (optional) (default to false)
local_only = false # bool | Determines whether to execute distributed request or not (optional) (default to false)
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all object groups
    api_response = api_instance.get_object_groups(include_members=include_members, local_only=local_only, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->get_object_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_members** | **bool**| Determines whether to include members of object groups | [optional] [default to false]
 **local_only** | **bool**| Determines whether to execute distributed request or not | [optional] [default to false]
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerObjectGroupDto**](PagerObjectGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_groups1**
> PagerObjectGroupDto get_object_groups1(page=page, size=size, include_members=include_members)

Get all object groups

Endpoint for retrieving all object groups that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_members = false # bool | Determines whether to include members of object groups (optional) (default to false)

try:
    # Get all object groups
    api_response = api_instance.get_object_groups1(page=page, size=size, include_members=include_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->get_object_groups1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_members** | **bool**| Determines whether to include members of object groups | [optional] [default to false]

### Return type

[**PagerObjectGroupDto**](PagerObjectGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_object_group_by_id**
> ObjectGroupDto partially_update_object_group_by_id(id, object_group)

Partially update object group

Updates an existing object group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
id = 789 # int | The id of the object group
object_group = swagger_client.ObjectGroupRequestDto() # ObjectGroupRequestDto | ObjectGroup request object

try:
    # Partially update object group
    api_response = api_instance.partially_update_object_group_by_id(id, object_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->partially_update_object_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group | 
 **object_group** | [**ObjectGroupRequestDto**](ObjectGroupRequestDto.md)| ObjectGroup request object | 

### Return type

[**ObjectGroupDto**](ObjectGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_object_group_by_id1**
> ObjectGroupDto partially_update_object_group_by_id1(id, object_group)

Partially update object group

Updates an existing object group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
id = 789 # int | The id of the object group
object_group = swagger_client.ObjectGroupRequestDto() # ObjectGroupRequestDto | ObjectGroup request object

try:
    # Partially update object group
    api_response = api_instance.partially_update_object_group_by_id1(id, object_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->partially_update_object_group_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group | 
 **object_group** | [**ObjectGroupRequestDto**](ObjectGroupRequestDto.md)| ObjectGroup request object | 

### Return type

[**ObjectGroupDto**](ObjectGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_object_group_member**
> remove_object_group_member(id, request)

Remove a member from the object group

Removes a single object from an object group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
id = 789 # int | The id of the object group
request = swagger_client.DeviceObjectId() # DeviceObjectId | request

try:
    # Remove a member from the object group
    api_instance.remove_object_group_member(id, request)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->remove_object_group_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group | 
 **request** | [**DeviceObjectId**](DeviceObjectId.md)| request | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_object_group_member1**
> remove_object_group_member1(id, request)

Remove a member from the object group

Removes a single object from an object group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
id = 789 # int | The id of the object group
request = swagger_client.DeviceObjectId() # DeviceObjectId | request

try:
    # Remove a member from the object group
    api_instance.remove_object_group_member1(id, request)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->remove_object_group_member1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group | 
 **request** | [**DeviceObjectId**](DeviceObjectId.md)| request | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_group_by_id**
> ObjectGroupDto update_object_group_by_id(id, object_group)

Update object group

Updates an existing object group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
id = 789 # int | The id of the object group
object_group = swagger_client.ObjectGroupRequestDto() # ObjectGroupRequestDto | ObjectGroup request object

try:
    # Update object group
    api_response = api_instance.update_object_group_by_id(id, object_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->update_object_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group | 
 **object_group** | [**ObjectGroupRequestDto**](ObjectGroupRequestDto.md)| ObjectGroup request object | 

### Return type

[**ObjectGroupDto**](ObjectGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_group_by_id1**
> ObjectGroupDto update_object_group_by_id1(id, object_group)

Update object group

Updates an existing object group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupApi()
id = 789 # int | The id of the object group
object_group = swagger_client.ObjectGroupRequestDto() # ObjectGroupRequestDto | ObjectGroup request object

try:
    # Update object group
    api_response = api_instance.update_object_group_by_id1(id, object_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupApi->update_object_group_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group | 
 **object_group** | [**ObjectGroupRequestDto**](ObjectGroupRequestDto.md)| ObjectGroup request object | 

### Return type

[**ObjectGroupDto**](ObjectGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

