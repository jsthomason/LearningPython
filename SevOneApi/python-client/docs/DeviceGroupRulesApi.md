# swagger_client.DeviceGroupRulesApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_device_group_rules**](DeviceGroupRulesApi.md#apply_device_group_rules) | **POST** /api/v2/devicegroups/rules/apply | Apply rules for all device groups
[**apply_device_group_rules_by_group_id**](DeviceGroupRulesApi.md#apply_device_group_rules_by_group_id) | **POST** /api/v2/devicegroups/{id}/rules/apply | Apply rules for the specified device group
[**create_device_group_rule**](DeviceGroupRulesApi.md#create_device_group_rule) | **POST** /api/v2/devicegroups/rules | Create device group rule
[**create_device_group_rule1**](DeviceGroupRulesApi.md#create_device_group_rule1) | **POST** /api/v1/devicegroups/rules | Create device group rule
[**delete_device_group_rule**](DeviceGroupRulesApi.md#delete_device_group_rule) | **DELETE** /api/v2/devicegroups/rules/{id} | Delete device group rule
[**delete_device_group_rule1**](DeviceGroupRulesApi.md#delete_device_group_rule1) | **DELETE** /api/v1/devicegroups/rules/{id} | Delete device group rule
[**get_device_group_rule**](DeviceGroupRulesApi.md#get_device_group_rule) | **GET** /api/v2/devicegroups/rules/{id} | Get device group rule by Id
[**get_device_group_rule1**](DeviceGroupRulesApi.md#get_device_group_rule1) | **GET** /api/v1/devicegroups/rules/{id} | Get device group rule by Id
[**get_device_group_rules**](DeviceGroupRulesApi.md#get_device_group_rules) | **GET** /api/v2/devicegroups/{id}/rules | Get device group rules
[**get_device_group_rules1**](DeviceGroupRulesApi.md#get_device_group_rules1) | **GET** /api/v1/devicegroups/{id}/rules | Get device group rules
[**get_device_groups_rules**](DeviceGroupRulesApi.md#get_device_groups_rules) | **GET** /api/v2/devicegroups/rules | Get all device group rules
[**get_device_groups_rules1**](DeviceGroupRulesApi.md#get_device_groups_rules1) | **GET** /api/v1/devicegroups/rules | Get all device group rules
[**update_device_group_rule**](DeviceGroupRulesApi.md#update_device_group_rule) | **PUT** /api/v2/devicegroups/rules/{id} | Update device group rule
[**update_device_group_rule1**](DeviceGroupRulesApi.md#update_device_group_rule1) | **PUT** /api/v1/devicegroups/rules/{id} | Update device group rule


# **apply_device_group_rules**
> ResponseEntity apply_device_group_rules()

Apply rules for all device groups

Apply rules for all device groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupRulesApi()

try:
    # Apply rules for all device groups
    api_response = api_instance.apply_device_group_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupRulesApi->apply_device_group_rules: %s\n" % e)
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

# **apply_device_group_rules_by_group_id**
> ResponseEntity apply_device_group_rules_by_group_id(id)

Apply rules for the specified device group

Applies rules for the specified device group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupRulesApi()
id = 789 # int | The id of the device group

try:
    # Apply rules for the specified device group
    api_response = api_instance.apply_device_group_rules_by_group_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupRulesApi->apply_device_group_rules_by_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_group_rule**
> DeviceGroupRuleDto create_device_group_rule(rule)

Create device group rule

Creates a new device group rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupRulesApi()
rule = swagger_client.DeviceGroupRuleDto() # DeviceGroupRuleDto | Device group rule request object

try:
    # Create device group rule
    api_response = api_instance.create_device_group_rule(rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupRulesApi->create_device_group_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | [**DeviceGroupRuleDto**](DeviceGroupRuleDto.md)| Device group rule request object | 

### Return type

[**DeviceGroupRuleDto**](DeviceGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_group_rule1**
> DeviceGroupRuleDto create_device_group_rule1(rule)

Create device group rule

Creates a new device group rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupRulesApi()
rule = swagger_client.DeviceGroupRuleDto() # DeviceGroupRuleDto | Device group rule request object

try:
    # Create device group rule
    api_response = api_instance.create_device_group_rule1(rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupRulesApi->create_device_group_rule1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | [**DeviceGroupRuleDto**](DeviceGroupRuleDto.md)| Device group rule request object | 

### Return type

[**DeviceGroupRuleDto**](DeviceGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_group_rule**
> ResponseEntity delete_device_group_rule(id)

Delete device group rule

Deletes an existing device group rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupRulesApi()
id = 789 # int | The id of the device group rule to be deleted

try:
    # Delete device group rule
    api_response = api_instance.delete_device_group_rule(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupRulesApi->delete_device_group_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group rule to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_group_rule1**
> ResponseEntity delete_device_group_rule1(id)

Delete device group rule

Deletes an existing device group rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupRulesApi()
id = 789 # int | The id of the device group rule to be deleted

try:
    # Delete device group rule
    api_response = api_instance.delete_device_group_rule1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupRulesApi->delete_device_group_rule1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group rule to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_rule**
> DeviceGroupRuleDto get_device_group_rule(id)

Get device group rule by Id

Gets a single device group rule by provided id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupRulesApi()
id = 789 # int | The id of the requested device group rule

try:
    # Get device group rule by Id
    api_response = api_instance.get_device_group_rule(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupRulesApi->get_device_group_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the requested device group rule | 

### Return type

[**DeviceGroupRuleDto**](DeviceGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_rule1**
> DeviceGroupRuleDto get_device_group_rule1(id)

Get device group rule by Id

Gets a single device group rule by provided id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupRulesApi()
id = 789 # int | The id of the requested device group rule

try:
    # Get device group rule by Id
    api_response = api_instance.get_device_group_rule1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupRulesApi->get_device_group_rule1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the requested device group rule | 

### Return type

[**DeviceGroupRuleDto**](DeviceGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_rules**
> PagerDeviceGroupRuleDto get_device_group_rules(id, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get device group rules

Gets all device group rules for a device group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupRulesApi()
id = 789 # int | The id of the device group
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get device group rules
    api_response = api_instance.get_device_group_rules(id, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupRulesApi->get_device_group_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerDeviceGroupRuleDto**](PagerDeviceGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_rules1**
> PagerDeviceGroupRuleDto get_device_group_rules1(id, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get device group rules

Gets all device group rules for a device group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupRulesApi()
id = 789 # int | The id of the device group
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get device group rules
    api_response = api_instance.get_device_group_rules1(id, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupRulesApi->get_device_group_rules1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerDeviceGroupRuleDto**](PagerDeviceGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_groups_rules**
> PagerDeviceGroupRuleDto get_device_groups_rules(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all device group rules

Gets all device group rules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupRulesApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all device group rules
    api_response = api_instance.get_device_groups_rules(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupRulesApi->get_device_groups_rules: %s\n" % e)
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

[**PagerDeviceGroupRuleDto**](PagerDeviceGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_groups_rules1**
> PagerDeviceGroupRuleDto get_device_groups_rules1(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all device group rules

Gets all device group rules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupRulesApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all device group rules
    api_response = api_instance.get_device_groups_rules1(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupRulesApi->get_device_groups_rules1: %s\n" % e)
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

[**PagerDeviceGroupRuleDto**](PagerDeviceGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_rule**
> DeviceGroupRuleDto update_device_group_rule(id, rule)

Update device group rule

Updates an existing device group rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupRulesApi()
id = 789 # int | The id of the device group rule to be updated
rule = swagger_client.DeviceGroupRuleDto() # DeviceGroupRuleDto | Device group rule to be updated

try:
    # Update device group rule
    api_response = api_instance.update_device_group_rule(id, rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupRulesApi->update_device_group_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group rule to be updated | 
 **rule** | [**DeviceGroupRuleDto**](DeviceGroupRuleDto.md)| Device group rule to be updated | 

### Return type

[**DeviceGroupRuleDto**](DeviceGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_rule1**
> DeviceGroupRuleDto update_device_group_rule1(id, rule)

Update device group rule

Updates an existing device group rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceGroupRulesApi()
id = 789 # int | The id of the device group rule to be updated
rule = swagger_client.DeviceGroupRuleDto() # DeviceGroupRuleDto | Device group rule to be updated

try:
    # Update device group rule
    api_response = api_instance.update_device_group_rule1(id, rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceGroupRulesApi->update_device_group_rule1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device group rule to be updated | 
 **rule** | [**DeviceGroupRuleDto**](DeviceGroupRuleDto.md)| Device group rule to be updated | 

### Return type

[**DeviceGroupRuleDto**](DeviceGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

