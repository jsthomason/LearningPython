# swagger_client.ApiKeysApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](ApiKeysApi.md#create_api_key) | **POST** /api/v1/users/api-keys | Create api key
[**create_api_key1**](ApiKeysApi.md#create_api_key1) | **POST** /api/v2/users/api-keys | Create api key
[**create_api_key_for_user**](ApiKeysApi.md#create_api_key_for_user) | **POST** /api/v1/users/{id}/api-keys | Create user api key 
[**create_api_key_for_user1**](ApiKeysApi.md#create_api_key_for_user1) | **POST** /api/v2/users/{id}/api-keys | Create user api key 
[**delete_api_key**](ApiKeysApi.md#delete_api_key) | **DELETE** /api/v1/users/api-keys/{apiKey} | Delete api keys
[**delete_api_key1**](ApiKeysApi.md#delete_api_key1) | **DELETE** /api/v2/users/api-keys/{apiKey} | Delete api keys
[**delete_api_key_for_user**](ApiKeysApi.md#delete_api_key_for_user) | **DELETE** /api/v1/users/{id}/api-keys/{apiKey} | Delete user api key
[**delete_api_key_for_user1**](ApiKeysApi.md#delete_api_key_for_user1) | **DELETE** /api/v2/users/{id}/api-keys/{apiKey} | Delete user api key
[**delete_api_keys**](ApiKeysApi.md#delete_api_keys) | **DELETE** /api/v1/users/api-keys | Delete api keys
[**delete_api_keys1**](ApiKeysApi.md#delete_api_keys1) | **DELETE** /api/v2/users/api-keys | Delete api keys
[**delete_api_keys_for_user**](ApiKeysApi.md#delete_api_keys_for_user) | **DELETE** /api/v1/users/{id}/api-keys | Delete user api keys
[**delete_api_keys_for_user1**](ApiKeysApi.md#delete_api_keys_for_user1) | **DELETE** /api/v2/users/{id}/api-keys | Delete user api keys
[**get_api_keys**](ApiKeysApi.md#get_api_keys) | **GET** /api/v1/users/api-keys | View your api keys
[**get_api_keys1**](ApiKeysApi.md#get_api_keys1) | **GET** /api/v2/users/api-keys | View your api keys
[**get_api_keys_for_user**](ApiKeysApi.md#get_api_keys_for_user) | **GET** /api/v1/users/{id}/api-keys | View user api keys
[**get_api_keys_for_user1**](ApiKeysApi.md#get_api_keys_for_user1) | **GET** /api/v2/users/{id}/api-keys | View user api keys
[**update_api_key**](ApiKeysApi.md#update_api_key) | **PUT** /api/v1/users/api-keys/{apiKey} | Update api key
[**update_api_key1**](ApiKeysApi.md#update_api_key1) | **PUT** /api/v2/users/api-keys/{apiKey} | Update api key
[**update_api_key_for_user**](ApiKeysApi.md#update_api_key_for_user) | **PUT** /api/v1/users/{id}/api-keys/{apiKey} | Update user api key
[**update_api_key_for_user1**](ApiKeysApi.md#update_api_key_for_user1) | **PUT** /api/v2/users/{id}/api-keys/{apiKey} | Update user api key


# **create_api_key**
> ApiKeyDto create_api_key(dto)

Create api key

Generate api key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()
dto = swagger_client.ApiKeyRequestDto() # ApiKeyRequestDto | Api key request object

try:
    # Create api key
    api_response = api_instance.create_api_key(dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->create_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dto** | [**ApiKeyRequestDto**](ApiKeyRequestDto.md)| Api key request object | 

### Return type

[**ApiKeyDto**](ApiKeyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_key1**
> ApiKeyDto create_api_key1(dto)

Create api key

Generate api key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()
dto = swagger_client.ApiKeyRequestDto() # ApiKeyRequestDto | Api key request object

try:
    # Create api key
    api_response = api_instance.create_api_key1(dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->create_api_key1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dto** | [**ApiKeyRequestDto**](ApiKeyRequestDto.md)| Api key request object | 

### Return type

[**ApiKeyDto**](ApiKeyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_key_for_user**
> ApiKeyDto create_api_key_for_user(id, dto)

Create user api key 

Generate api key for user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()
id = 789 # int | User for which api key will be created
dto = swagger_client.ApiKeyRequestDto() # ApiKeyRequestDto | Api key request object

try:
    # Create user api key 
    api_response = api_instance.create_api_key_for_user(id, dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->create_api_key_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User for which api key will be created | 
 **dto** | [**ApiKeyRequestDto**](ApiKeyRequestDto.md)| Api key request object | 

### Return type

[**ApiKeyDto**](ApiKeyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_key_for_user1**
> ApiKeyDto create_api_key_for_user1(id, dto)

Create user api key 

Generate api key for user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()
id = 789 # int | User for which api key will be created
dto = swagger_client.ApiKeyRequestDto() # ApiKeyRequestDto | Api key request object

try:
    # Create user api key 
    api_response = api_instance.create_api_key_for_user1(id, dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->create_api_key_for_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User for which api key will be created | 
 **dto** | [**ApiKeyRequestDto**](ApiKeyRequestDto.md)| Api key request object | 

### Return type

[**ApiKeyDto**](ApiKeyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> int delete_api_key(api_key)

Delete api keys

Delete your api key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()
api_key = 'api_key_example' # str | Api key as string

try:
    # Delete api keys
    api_response = api_instance.delete_api_key(api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->delete_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Api key as string | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key1**
> int delete_api_key1(api_key)

Delete api keys

Delete your api key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()
api_key = 'api_key_example' # str | Api key as string

try:
    # Delete api keys
    api_response = api_instance.delete_api_key1(api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->delete_api_key1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Api key as string | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key_for_user**
> int delete_api_key_for_user(api_key, id)

Delete user api key

Delete api key for user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()
api_key = 'api_key_example' # str | Api key as string
id = 789 # int | User for which api key will be deleted

try:
    # Delete user api key
    api_response = api_instance.delete_api_key_for_user(api_key, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->delete_api_key_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Api key as string | 
 **id** | **int**| User for which api key will be deleted | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key_for_user1**
> int delete_api_key_for_user1(api_key, id)

Delete user api key

Delete api key for user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()
api_key = 'api_key_example' # str | Api key as string
id = 789 # int | User for which api key will be deleted

try:
    # Delete user api key
    api_response = api_instance.delete_api_key_for_user1(api_key, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->delete_api_key_for_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Api key as string | 
 **id** | **int**| User for which api key will be deleted | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_keys**
> int delete_api_keys()

Delete api keys

Delete all your api keys

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()

try:
    # Delete api keys
    api_response = api_instance.delete_api_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->delete_api_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_keys1**
> int delete_api_keys1()

Delete api keys

Delete all your api keys

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()

try:
    # Delete api keys
    api_response = api_instance.delete_api_keys1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->delete_api_keys1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_keys_for_user**
> int delete_api_keys_for_user(id)

Delete user api keys

Delete api keys for user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()
id = 789 # int | User for which api keys will be deleted

try:
    # Delete user api keys
    api_response = api_instance.delete_api_keys_for_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->delete_api_keys_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User for which api keys will be deleted | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_keys_for_user1**
> int delete_api_keys_for_user1(id)

Delete user api keys

Delete api keys for user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()
id = 789 # int | User for which api keys will be deleted

try:
    # Delete user api keys
    api_response = api_instance.delete_api_keys_for_user1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->delete_api_keys_for_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User for which api keys will be deleted | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_keys**
> list[ApiKeyDto] get_api_keys()

View your api keys

View your api keys

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()

try:
    # View your api keys
    api_response = api_instance.get_api_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->get_api_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiKeyDto]**](ApiKeyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_keys1**
> list[ApiKeyDto] get_api_keys1()

View your api keys

View your api keys

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()

try:
    # View your api keys
    api_response = api_instance.get_api_keys1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->get_api_keys1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiKeyDto]**](ApiKeyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_keys_for_user**
> list[ApiKeyDto] get_api_keys_for_user(id)

View user api keys

View api keys for user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()
id = 789 # int | User for which api keys will be returned

try:
    # View user api keys
    api_response = api_instance.get_api_keys_for_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->get_api_keys_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User for which api keys will be returned | 

### Return type

[**list[ApiKeyDto]**](ApiKeyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_keys_for_user1**
> list[ApiKeyDto] get_api_keys_for_user1(id)

View user api keys

View api keys for user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()
id = 789 # int | User for which api keys will be returned

try:
    # View user api keys
    api_response = api_instance.get_api_keys_for_user1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->get_api_keys_for_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User for which api keys will be returned | 

### Return type

[**list[ApiKeyDto]**](ApiKeyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key**
> ApiKeyDto update_api_key(api_key, dto)

Update api key

Update your api key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()
api_key = 'api_key_example' # str | Api key as string
dto = swagger_client.ApiKeyRequestDto() # ApiKeyRequestDto | Api key request object

try:
    # Update api key
    api_response = api_instance.update_api_key(api_key, dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->update_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Api key as string | 
 **dto** | [**ApiKeyRequestDto**](ApiKeyRequestDto.md)| Api key request object | 

### Return type

[**ApiKeyDto**](ApiKeyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key1**
> ApiKeyDto update_api_key1(api_key, dto)

Update api key

Update your api key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()
api_key = 'api_key_example' # str | Api key as string
dto = swagger_client.ApiKeyRequestDto() # ApiKeyRequestDto | Api key request object

try:
    # Update api key
    api_response = api_instance.update_api_key1(api_key, dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->update_api_key1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Api key as string | 
 **dto** | [**ApiKeyRequestDto**](ApiKeyRequestDto.md)| Api key request object | 

### Return type

[**ApiKeyDto**](ApiKeyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key_for_user**
> ApiKeyDto update_api_key_for_user(id, api_key, dto)

Update user api key

Update api key for user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()
id = 789 # int | User for which api key will be updated
api_key = 'api_key_example' # str | Api key for which meta data will be updated
dto = swagger_client.ApiKeyRequestDto() # ApiKeyRequestDto | Api key request object

try:
    # Update user api key
    api_response = api_instance.update_api_key_for_user(id, api_key, dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->update_api_key_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User for which api key will be updated | 
 **api_key** | **str**| Api key for which meta data will be updated | 
 **dto** | [**ApiKeyRequestDto**](ApiKeyRequestDto.md)| Api key request object | 

### Return type

[**ApiKeyDto**](ApiKeyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key_for_user1**
> ApiKeyDto update_api_key_for_user1(id, api_key, dto)

Update user api key

Update api key for user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiKeysApi()
id = 789 # int | User for which api key will be updated
api_key = 'api_key_example' # str | Api key for which meta data will be updated
dto = swagger_client.ApiKeyRequestDto() # ApiKeyRequestDto | Api key request object

try:
    # Update user api key
    api_response = api_instance.update_api_key_for_user1(id, api_key, dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiKeysApi->update_api_key_for_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User for which api key will be updated | 
 **api_key** | **str**| Api key for which meta data will be updated | 
 **dto** | [**ApiKeyRequestDto**](ApiKeyRequestDto.md)| Api key request object | 

### Return type

[**ApiKeyDto**](ApiKeyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

