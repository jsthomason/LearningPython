# swagger_client.ObjectGroupRulesApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_object_group_rules**](ObjectGroupRulesApi.md#apply_object_group_rules) | **POST** /api/v2/objectgroups/{id}/rules/apply | Apply the rules for the specified object group
[**apply_object_group_rules1**](ObjectGroupRulesApi.md#apply_object_group_rules1) | **POST** /api/v1/objectgroups/{id}/rules/apply | Apply the rules for the specified object group
[**create_object_group_rule**](ObjectGroupRulesApi.md#create_object_group_rule) | **POST** /api/v2/objectgroups/rules | Create object group rule
[**create_object_group_rule1**](ObjectGroupRulesApi.md#create_object_group_rule1) | **POST** /api/v1/objectgroups/rules | Create object group rule
[**delete_object_group_rule**](ObjectGroupRulesApi.md#delete_object_group_rule) | **DELETE** /api/v2/objectgroups/rules/{id} | Delete object group rule
[**delete_object_group_rule1**](ObjectGroupRulesApi.md#delete_object_group_rule1) | **DELETE** /api/v1/objectgroups/rules/{id} | Delete object group rule
[**get_object_group_rule**](ObjectGroupRulesApi.md#get_object_group_rule) | **GET** /api/v2/objectgroups/rules/{id} | Get object group rule by Id
[**get_object_group_rule1**](ObjectGroupRulesApi.md#get_object_group_rule1) | **GET** /api/v1/objectgroups/rules/{id} | Get object group rule by Id
[**get_object_group_rules**](ObjectGroupRulesApi.md#get_object_group_rules) | **GET** /api/v2/objectgroups/{id}/rules | Get object group rules
[**get_object_group_rules1**](ObjectGroupRulesApi.md#get_object_group_rules1) | **GET** /api/v1/objectgroups/{id}/rules | Get object group rules
[**get_object_groups_rules**](ObjectGroupRulesApi.md#get_object_groups_rules) | **GET** /api/v2/objectgroups/rules | Get all object group rules
[**get_object_groups_rules1**](ObjectGroupRulesApi.md#get_object_groups_rules1) | **GET** /api/v1/objectgroups/rules | Get all object group rules
[**update_object_group_rule**](ObjectGroupRulesApi.md#update_object_group_rule) | **PUT** /api/v2/objectgroups/rules/{id} | Update object group rule
[**update_object_group_rule1**](ObjectGroupRulesApi.md#update_object_group_rule1) | **PUT** /api/v1/objectgroups/rules/{id} | Update object group rule


# **apply_object_group_rules**
> ResponseEntity apply_object_group_rules(id)

Apply the rules for the specified object group

Applies the rules for the specified object group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupRulesApi()
id = 789 # int | The id of the object group

try:
    # Apply the rules for the specified object group
    api_response = api_instance.apply_object_group_rules(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupRulesApi->apply_object_group_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_object_group_rules1**
> ResponseEntity apply_object_group_rules1(id)

Apply the rules for the specified object group

Applies the rules for the specified object group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupRulesApi()
id = 789 # int | The id of the object group

try:
    # Apply the rules for the specified object group
    api_response = api_instance.apply_object_group_rules1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupRulesApi->apply_object_group_rules1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_object_group_rule**
> ObjectGroupRuleDto create_object_group_rule(rule)

Create object group rule

Creates a new object group rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupRulesApi()
rule = swagger_client.ObjectGroupRuleDto() # ObjectGroupRuleDto | Object group rule

try:
    # Create object group rule
    api_response = api_instance.create_object_group_rule(rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupRulesApi->create_object_group_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | [**ObjectGroupRuleDto**](ObjectGroupRuleDto.md)| Object group rule | 

### Return type

[**ObjectGroupRuleDto**](ObjectGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_object_group_rule1**
> ObjectGroupRuleDto create_object_group_rule1(rule)

Create object group rule

Creates a new object group rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupRulesApi()
rule = swagger_client.ObjectGroupRuleDto() # ObjectGroupRuleDto | Object group rule

try:
    # Create object group rule
    api_response = api_instance.create_object_group_rule1(rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupRulesApi->create_object_group_rule1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | [**ObjectGroupRuleDto**](ObjectGroupRuleDto.md)| Object group rule | 

### Return type

[**ObjectGroupRuleDto**](ObjectGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object_group_rule**
> ResponseEntity delete_object_group_rule(id)

Delete object group rule

Deletes an existing object group rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupRulesApi()
id = 789 # int | The id of the object group rule to be deleted

try:
    # Delete object group rule
    api_response = api_instance.delete_object_group_rule(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupRulesApi->delete_object_group_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group rule to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object_group_rule1**
> ResponseEntity delete_object_group_rule1(id)

Delete object group rule

Deletes an existing object group rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupRulesApi()
id = 789 # int | The id of the object group rule to be deleted

try:
    # Delete object group rule
    api_response = api_instance.delete_object_group_rule1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupRulesApi->delete_object_group_rule1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group rule to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group_rule**
> ObjectGroupRuleDto get_object_group_rule(id)

Get object group rule by Id

Gets a single object group rule by provided id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupRulesApi()
id = 789 # int | The id of the object group rule

try:
    # Get object group rule by Id
    api_response = api_instance.get_object_group_rule(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupRulesApi->get_object_group_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group rule | 

### Return type

[**ObjectGroupRuleDto**](ObjectGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group_rule1**
> ObjectGroupRuleDto get_object_group_rule1(id)

Get object group rule by Id

Gets a single object group rule by provided id if it exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupRulesApi()
id = 789 # int | The id of the object group rule

try:
    # Get object group rule by Id
    api_response = api_instance.get_object_group_rule1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupRulesApi->get_object_group_rule1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group rule | 

### Return type

[**ObjectGroupRuleDto**](ObjectGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group_rules**
> PagerObjectGroupRuleDto get_object_group_rules(id, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get object group rules

Gets all object group rules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupRulesApi()
id = 789 # int | The id of the object group
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get object group rules
    api_response = api_instance.get_object_group_rules(id, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupRulesApi->get_object_group_rules: %s\n" % e)
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

[**PagerObjectGroupRuleDto**](PagerObjectGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group_rules1**
> PagerObjectGroupRuleDto get_object_group_rules1(id, page=page, size=size)

Get object group rules

Gets all object group rules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupRulesApi()
id = 789 # int | The id of the object group
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)

try:
    # Get object group rules
    api_response = api_instance.get_object_group_rules1(id, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupRulesApi->get_object_group_rules1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]

### Return type

[**PagerObjectGroupRuleDto**](PagerObjectGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_groups_rules**
> PagerObjectGroupRuleDto get_object_groups_rules(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all object group rules

Gets all object group rules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupRulesApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all object group rules
    api_response = api_instance.get_object_groups_rules(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupRulesApi->get_object_groups_rules: %s\n" % e)
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

[**PagerObjectGroupRuleDto**](PagerObjectGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_groups_rules1**
> PagerObjectGroupRuleDto get_object_groups_rules1(page=page, size=size)

Get all object group rules

Gets all object group rules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupRulesApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)

try:
    # Get all object group rules
    api_response = api_instance.get_object_groups_rules1(page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupRulesApi->get_object_groups_rules1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]

### Return type

[**PagerObjectGroupRuleDto**](PagerObjectGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_group_rule**
> ObjectGroupRuleDto update_object_group_rule(id, rule)

Update object group rule

Updates an existing object group rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupRulesApi()
id = 789 # int | The id of the object group rule to be updated
rule = swagger_client.ObjectGroupRuleDto() # ObjectGroupRuleDto | Object group rule to be updated

try:
    # Update object group rule
    api_response = api_instance.update_object_group_rule(id, rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupRulesApi->update_object_group_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group rule to be updated | 
 **rule** | [**ObjectGroupRuleDto**](ObjectGroupRuleDto.md)| Object group rule to be updated | 

### Return type

[**ObjectGroupRuleDto**](ObjectGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_group_rule1**
> ObjectGroupRuleDto update_object_group_rule1(id, rule)

Update object group rule

Updates an existing object group rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ObjectGroupRulesApi()
id = 789 # int | The id of the object group rule to be updated
rule = swagger_client.ObjectGroupRuleDto() # ObjectGroupRuleDto | Object group rule to be updated

try:
    # Update object group rule
    api_response = api_instance.update_object_group_rule1(id, rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectGroupRulesApi->update_object_group_rule1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the object group rule to be updated | 
 **rule** | [**ObjectGroupRuleDto**](ObjectGroupRuleDto.md)| Object group rule to be updated | 

### Return type

[**ObjectGroupRuleDto**](ObjectGroupRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

