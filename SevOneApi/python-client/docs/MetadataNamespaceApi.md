# swagger_client.MetadataNamespaceApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespace**](MetadataNamespaceApi.md#create_namespace) | **POST** /api/v2/metadata/namespace | Create Metadata Namespace
[**delete_namespace_by_id**](MetadataNamespaceApi.md#delete_namespace_by_id) | **DELETE** /api/v2/metadata/namespace/{id} | Delete Metadata Namespace
[**get_namespace**](MetadataNamespaceApi.md#get_namespace) | **GET** /api/v2/metadata/namespace/{id} | Get Metadata Namespace
[**get_namespaces**](MetadataNamespaceApi.md#get_namespaces) | **GET** /api/v2/metadata/namespace | Get all Metadata Namespaces
[**update_namespace_by_id**](MetadataNamespaceApi.md#update_namespace_by_id) | **PUT** /api/v2/metadata/namespace/{id} | Update Metadata Namespace


# **create_namespace**
> NamespaceDto create_namespace(namespace)

Create Metadata Namespace

Creates a new Metadata Namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataNamespaceApi()
namespace = swagger_client.NamespaceDto() # NamespaceDto | Namespace object that will be added to the database

try:
    # Create Metadata Namespace
    api_response = api_instance.create_namespace(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataNamespaceApi->create_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | [**NamespaceDto**](NamespaceDto.md)| Namespace object that will be added to the database | 

### Return type

[**NamespaceDto**](NamespaceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespace_by_id**
> ResponseEntity delete_namespace_by_id(id)

Delete Metadata Namespace

Deletes an existing Metadata Namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataNamespaceApi()
id = 789 # int | The id of the Namespace to be deleted

try:
    # Delete Metadata Namespace
    api_response = api_instance.delete_namespace_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataNamespaceApi->delete_namespace_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the Namespace to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespace**
> NamespaceDto get_namespace(id)

Get Metadata Namespace

Endpoint for retrieving Metadata Namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataNamespaceApi()
id = 789 # int | Namespace Id

try:
    # Get Metadata Namespace
    api_response = api_instance.get_namespace(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataNamespaceApi->get_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Namespace Id | 

### Return type

[**NamespaceDto**](NamespaceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaces**
> PagerNamespaceDto get_namespaces(name=name, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all Metadata Namespaces

Endpoint for retrieving all metadata namespaces that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataNamespaceApi()
name = 'name_example' # str | Filter by Namespace name (optional)
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all Metadata Namespaces
    api_response = api_instance.get_namespaces(name=name, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataNamespaceApi->get_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter by Namespace name | [optional] 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerNamespaceDto**](PagerNamespaceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_namespace_by_id**
> NamespaceDto update_namespace_by_id(id, namespace)

Update Metadata Namespace

Updates an existing Metadata Namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataNamespaceApi()
id = 789 # int | The id of the Namespace to be updated
namespace = swagger_client.NamespaceDto() # NamespaceDto | Namespace to be updated

try:
    # Update Metadata Namespace
    api_response = api_instance.update_namespace_by_id(id, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataNamespaceApi->update_namespace_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the Namespace to be updated | 
 **namespace** | [**NamespaceDto**](NamespaceDto.md)| Namespace to be updated | 

### Return type

[**NamespaceDto**](NamespaceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

