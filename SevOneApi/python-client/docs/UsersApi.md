# swagger_client.UsersApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_specific_user_roles**](UsersApi.md#add_specific_user_roles) | **PATCH** /api/v2/users/{id}/roles | Add roles to user
[**change_password**](UsersApi.md#change_password) | **PUT** /api/v2/users/mypreferences/password | Change user password
[**create_user_using_post**](UsersApi.md#create_user_using_post) | **POST** /api/v2/users | Create user
[**delete_user_using_delete**](UsersApi.md#delete_user_using_delete) | **DELETE** /api/v2/users/{id} | Delete user
[**filter_users**](UsersApi.md#filter_users) | **POST** /api/v2/users/filter | Filter users
[**get_all_users**](UsersApi.md#get_all_users) | **GET** /api/v2/users | Get all users
[**get_current_user**](UsersApi.md#get_current_user) | **GET** /api/v1/users/mypreferences | Get user
[**get_current_user1**](UsersApi.md#get_current_user1) | **GET** /api/v2/users/mypreferences | Get user
[**get_specific_user_roles**](UsersApi.md#get_specific_user_roles) | **GET** /api/v2/users/{id}/roles | Get all roles for a specific user
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /api/v2/users/{id} | Get one user
[**get_user_roles**](UsersApi.md#get_user_roles) | **GET** /api/v2/users/myroles | Get user roles
[**partially_update_user_using_patch**](UsersApi.md#partially_update_user_using_patch) | **PATCH** /api/v2/users/{id} | Update user
[**remove_specific_user_roles**](UsersApi.md#remove_specific_user_roles) | **DELETE** /api/v2/users/{id}/roles | Remove roles for user
[**update_user_preferences_using_patch**](UsersApi.md#update_user_preferences_using_patch) | **PATCH** /api/v2/users/mypreferences | Update user preferences


# **add_specific_user_roles**
> ResponseEntity add_specific_user_roles(id, role_ids)

Add roles to user

Adds roles to a specific user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 789 # int | userId
role_ids = [swagger_client.list[int]()] # list[int] | roleIds

try:
    # Add roles to user
    api_response = api_instance.add_specific_user_roles(id, role_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->add_specific_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| userId | 
 **role_ids** | **list[int]**| roleIds | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password**
> ResponseEntity change_password(password)

Change user password

Change password for the logged user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
password = swagger_client.PasswordDto() # PasswordDto | password

try:
    # Change user password
    api_response = api_instance.change_password(password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | [**PasswordDto**](PasswordDto.md)| password | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_using_post**
> UserDto create_user_using_post(user)

Create user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user = swagger_client.UserDto() # UserDto | user

try:
    # Create user
    api_response = api_instance.create_user_using_post(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**UserDto**](UserDto.md)| user | 

### Return type

[**UserDto**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_using_delete**
> ResponseEntity delete_user_using_delete(id)

Delete user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 789 # int | id

try:
    # Delete user
    api_response = api_instance.delete_user_using_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_users**
> PagerUserDto filter_users(user_filter_dto, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Filter users

The method will return all users that match the filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_filter_dto = swagger_client.UserFilterDto() # UserFilterDto | userFilterDto
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Filter users
    api_response = api_instance.filter_users(user_filter_dto, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->filter_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_filter_dto** | [**UserFilterDto**](UserFilterDto.md)| userFilterDto | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerUserDto**](PagerUserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users**
> PagerUserDto get_all_users(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all users

The method will return all visible users for the logged user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all users
    api_response = api_instance.get_all_users(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_all_users: %s\n" % e)
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

[**PagerUserDto**](PagerUserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> UserDto get_current_user()

Get user

Get user and user preferences

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()

try:
    # Get user
    api_response = api_instance.get_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserDto**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user1**
> UserDto get_current_user1()

Get user

Get user and user preferences

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()

try:
    # Get user
    api_response = api_instance.get_current_user1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_current_user1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserDto**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_specific_user_roles**
> list[UserRoleDto] get_specific_user_roles(id)

Get all roles for a specific user

Get all roles for a specific user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 789 # int | userId

try:
    # Get all roles for a specific user
    api_response = api_instance.get_specific_user_roles(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_specific_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| userId | 

### Return type

[**list[UserRoleDto]**](UserRoleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> UserDto get_user_by_id(id)

Get one user

Get a single user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 789 # int | id

try:
    # Get one user
    api_response = api_instance.get_user_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**UserDto**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_roles**
> list[UserRoleDto] get_user_roles()

Get user roles

Get user and user roles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()

try:
    # Get user roles
    api_response = api_instance.get_user_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserRoleDto]**](UserRoleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_user_using_patch**
> UserDto partially_update_user_using_patch(id, user)

Update user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 789 # int | id
user = swagger_client.UserDto() # UserDto | user

try:
    # Update user
    api_response = api_instance.partially_update_user_using_patch(id, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->partially_update_user_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **user** | [**UserDto**](UserDto.md)| user | 

### Return type

[**UserDto**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_specific_user_roles**
> ResponseEntity remove_specific_user_roles(id, role_ids)

Remove roles for user

Removes roles from a specific user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 789 # int | userId
role_ids = [swagger_client.list[int]()] # list[int] | roleIds

try:
    # Remove roles for user
    api_response = api_instance.remove_specific_user_roles(id, role_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->remove_specific_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| userId | 
 **role_ids** | **list[int]**| roleIds | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_preferences_using_patch**
> UserPreferencesDto update_user_preferences_using_patch(user)

Update user preferences

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user = swagger_client.UserPreferencesDto() # UserPreferencesDto | user

try:
    # Update user preferences
    api_response = api_instance.update_user_preferences_using_patch(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_preferences_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**UserPreferencesDto**](UserPreferencesDto.md)| user | 

### Return type

[**UserPreferencesDto**](UserPreferencesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

