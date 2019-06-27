# swagger_client.AuthenticationApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_sessions**](AuthenticationApi.md#get_active_sessions) | **GET** /api/v1/authentication/active-sessions | View active sessions
[**get_active_sessions1**](AuthenticationApi.md#get_active_sessions1) | **GET** /api/v2/authentication/active-sessions | View active sessions
[**keep_alive**](AuthenticationApi.md#keep_alive) | **GET** /api/v1/authentication/keep-alive | Keep-alive endpoint
[**keep_alive1**](AuthenticationApi.md#keep_alive1) | **GET** /api/v2/authentication/keep-alive | Keep-alive endpoint
[**sign_in**](AuthenticationApi.md#sign_in) | **POST** /api/v1/authentication/signin | Sign in user
[**sign_in1**](AuthenticationApi.md#sign_in1) | **POST** /api/v2/authentication/signin | Sign in user
[**sign_out**](AuthenticationApi.md#sign_out) | **DELETE** /api/v1/authentication/signout | Sign out user
[**sign_out1**](AuthenticationApi.md#sign_out1) | **DELETE** /api/v2/authentication/signout | Sign out user
[**sign_out_others**](AuthenticationApi.md#sign_out_others) | **DELETE** /api/v1/authentication/signout-others | Sign out others
[**sign_out_others1**](AuthenticationApi.md#sign_out_others1) | **DELETE** /api/v2/authentication/signout-others | Sign out others
[**sign_out_user**](AuthenticationApi.md#sign_out_user) | **DELETE** /api/v1/authentication/signout/{userId} | Sign out user
[**sign_out_user1**](AuthenticationApi.md#sign_out_user1) | **DELETE** /api/v2/authentication/signout/{userId} | Sign out user


# **get_active_sessions**
> list[Token] get_active_sessions(token=token)

View active sessions

View all active sessions at the moment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
token = 'token_example' # str | token (optional)

try:
    # View active sessions
    api_response = api_instance.get_active_sessions(token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_active_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| token | [optional] 

### Return type

[**list[Token]**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_sessions1**
> list[Token] get_active_sessions1(token=token)

View active sessions

View all active sessions at the moment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
token = 'token_example' # str | token (optional)

try:
    # View active sessions
    api_response = api_instance.get_active_sessions1(token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_active_sessions1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| token | [optional] 

### Return type

[**list[Token]**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keep_alive**
> object keep_alive()

Keep-alive endpoint

Checks if the REST API responds and has connection to local database

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()

try:
    # Keep-alive endpoint
    api_response = api_instance.keep_alive()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->keep_alive: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keep_alive1**
> object keep_alive1()

Keep-alive endpoint

Checks if the REST API responds and has connection to local database

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()

try:
    # Keep-alive endpoint
    api_response = api_instance.keep_alive1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->keep_alive1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_in**
> SignInResponseDto sign_in(user, nms_login=nms_login)

Sign in user

Signs in user known to SevOne NMS and returns an API token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
user = swagger_client.UserRequestDto() # UserRequestDto | User and password known to the SevOne NMS
nms_login = false # bool | nmsLogin (optional) (default to false)

try:
    # Sign in user
    api_response = api_instance.sign_in(user, nms_login=nms_login)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->sign_in: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**UserRequestDto**](UserRequestDto.md)| User and password known to the SevOne NMS | 
 **nms_login** | **bool**| nmsLogin | [optional] [default to false]

### Return type

[**SignInResponseDto**](SignInResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_in1**
> SignInResponseDto sign_in1(user, nms_login=nms_login)

Sign in user

Signs in user known to SevOne NMS and returns an API token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
user = swagger_client.UserRequestDto() # UserRequestDto | User and password known to the SevOne NMS
nms_login = false # bool | nmsLogin (optional) (default to false)

try:
    # Sign in user
    api_response = api_instance.sign_in1(user, nms_login=nms_login)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->sign_in1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**UserRequestDto**](UserRequestDto.md)| User and password known to the SevOne NMS | 
 **nms_login** | **bool**| nmsLogin | [optional] [default to false]

### Return type

[**SignInResponseDto**](SignInResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_out**
> int sign_out()

Sign out user

Signs out the current session

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()

try:
    # Sign out user
    api_response = api_instance.sign_out()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->sign_out: %s\n" % e)
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

# **sign_out1**
> int sign_out1()

Sign out user

Signs out the current session

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()

try:
    # Sign out user
    api_response = api_instance.sign_out1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->sign_out1: %s\n" % e)
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

# **sign_out_others**
> int sign_out_others()

Sign out others

Signs out all other sessions but the current one

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()

try:
    # Sign out others
    api_response = api_instance.sign_out_others()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->sign_out_others: %s\n" % e)
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

# **sign_out_others1**
> int sign_out_others1()

Sign out others

Signs out all other sessions but the current one

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()

try:
    # Sign out others
    api_response = api_instance.sign_out_others1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->sign_out_others1: %s\n" % e)
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

# **sign_out_user**
> int sign_out_user(user_id)

Sign out user

Signs out the session of particular user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
user_id = 789 # int | The id of the user

try:
    # Sign out user
    api_response = api_instance.sign_out_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->sign_out_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_out_user1**
> int sign_out_user1(user_id)

Sign out user

Signs out the session of particular user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
user_id = 789 # int | The id of the user

try:
    # Sign out user
    api_response = api_instance.sign_out_user1(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->sign_out_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

