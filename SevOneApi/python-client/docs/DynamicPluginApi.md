# swagger_client.DynamicPluginApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_dynamic_plugin**](DynamicPluginApi.md#register_dynamic_plugin) | **POST** /api/v1/pluginmanager/{id}/plugin/register | Register plugin in dynamic plugin manager
[**register_dynamic_plugin1**](DynamicPluginApi.md#register_dynamic_plugin1) | **POST** /api/v2/pluginmanager/{id}/plugin/register | Register plugin in dynamic plugin manager
[**register_dynamic_plugin_manager**](DynamicPluginApi.md#register_dynamic_plugin_manager) | **POST** /api/v1/pluginmanager/register | Register dynamic plugin manager
[**register_dynamic_plugin_manager1**](DynamicPluginApi.md#register_dynamic_plugin_manager1) | **POST** /api/v2/pluginmanager/register | Register dynamic plugin manager


# **register_dynamic_plugin**
> DynamicPluginResponseDto register_dynamic_plugin(id, dynamic_plugin_dto)

Register plugin in dynamic plugin manager

Register plugin in dynamic plugin manager

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DynamicPluginApi()
id = 789 # int | The id of the pluginmanager
dynamic_plugin_dto = swagger_client.DynamicPluginRequestDto() # DynamicPluginRequestDto | Plugin request object

try:
    # Register plugin in dynamic plugin manager
    api_response = api_instance.register_dynamic_plugin(id, dynamic_plugin_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicPluginApi->register_dynamic_plugin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the pluginmanager | 
 **dynamic_plugin_dto** | [**DynamicPluginRequestDto**](DynamicPluginRequestDto.md)| Plugin request object | 

### Return type

[**DynamicPluginResponseDto**](DynamicPluginResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_dynamic_plugin1**
> DynamicPluginResponseDto register_dynamic_plugin1(id, dynamic_plugin_dto)

Register plugin in dynamic plugin manager

Register plugin in dynamic plugin manager

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DynamicPluginApi()
id = 789 # int | The id of the pluginmanager
dynamic_plugin_dto = swagger_client.DynamicPluginRequestDto() # DynamicPluginRequestDto | Plugin request object

try:
    # Register plugin in dynamic plugin manager
    api_response = api_instance.register_dynamic_plugin1(id, dynamic_plugin_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicPluginApi->register_dynamic_plugin1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the pluginmanager | 
 **dynamic_plugin_dto** | [**DynamicPluginRequestDto**](DynamicPluginRequestDto.md)| Plugin request object | 

### Return type

[**DynamicPluginResponseDto**](DynamicPluginResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_dynamic_plugin_manager**
> DynamicPluginManagerResponseDto register_dynamic_plugin_manager(dynamic_plugin_manager_dto)

Register dynamic plugin manager

Registers new dynamic plugin manager

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DynamicPluginApi()
dynamic_plugin_manager_dto = swagger_client.DynamicPluginManagerRequestDto() # DynamicPluginManagerRequestDto | Dynamic Plugin Manager request object

try:
    # Register dynamic plugin manager
    api_response = api_instance.register_dynamic_plugin_manager(dynamic_plugin_manager_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicPluginApi->register_dynamic_plugin_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_plugin_manager_dto** | [**DynamicPluginManagerRequestDto**](DynamicPluginManagerRequestDto.md)| Dynamic Plugin Manager request object | 

### Return type

[**DynamicPluginManagerResponseDto**](DynamicPluginManagerResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_dynamic_plugin_manager1**
> DynamicPluginManagerResponseDto register_dynamic_plugin_manager1(dynamic_plugin_manager_dto)

Register dynamic plugin manager

Registers new dynamic plugin manager

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DynamicPluginApi()
dynamic_plugin_manager_dto = swagger_client.DynamicPluginManagerRequestDto() # DynamicPluginManagerRequestDto | Dynamic Plugin Manager request object

try:
    # Register dynamic plugin manager
    api_response = api_instance.register_dynamic_plugin_manager1(dynamic_plugin_manager_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicPluginApi->register_dynamic_plugin_manager1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_plugin_manager_dto** | [**DynamicPluginManagerRequestDto**](DynamicPluginManagerRequestDto.md)| Dynamic Plugin Manager request object | 

### Return type

[**DynamicPluginManagerResponseDto**](DynamicPluginManagerResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

