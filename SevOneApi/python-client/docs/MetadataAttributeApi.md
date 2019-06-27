# swagger_client.MetadataAttributeApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_attribute**](MetadataAttributeApi.md#create_attribute) | **POST** /api/v2/metadata/attribute | Create Metadata Attribute
[**delete_attribute_by_id**](MetadataAttributeApi.md#delete_attribute_by_id) | **DELETE** /api/v2/metadata/attribute/{id} | Delete Metadata Attribute
[**filter_attributes**](MetadataAttributeApi.md#filter_attributes) | **POST** /api/v2/metadata/attribute/filter | Filter Metadata Attributes
[**get_attribute**](MetadataAttributeApi.md#get_attribute) | **GET** /api/v2/metadata/attribute/{id} | Get Metadata Attribute
[**get_attributes**](MetadataAttributeApi.md#get_attributes) | **GET** /api/v2/metadata/attribute | Get all Metadata Attributes
[**update_attribute_by_id**](MetadataAttributeApi.md#update_attribute_by_id) | **PUT** /api/v2/metadata/attribute/{id} | Update Metadata Attribute


# **create_attribute**
> AttributeDto create_attribute(attribute)

Create Metadata Attribute

Creates a new Metadata Attribute

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataAttributeApi()
attribute = swagger_client.AttributeDto() # AttributeDto | Attribute object that will be added to the database

try:
    # Create Metadata Attribute
    api_response = api_instance.create_attribute(attribute)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataAttributeApi->create_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute** | [**AttributeDto**](AttributeDto.md)| Attribute object that will be added to the database | 

### Return type

[**AttributeDto**](AttributeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attribute_by_id**
> ResponseEntity delete_attribute_by_id(id)

Delete Metadata Attribute

Deletes an existing Metadata Attribute

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataAttributeApi()
id = 789 # int | The id of the deleteAttributeById to be deleted

try:
    # Delete Metadata Attribute
    api_response = api_instance.delete_attribute_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataAttributeApi->delete_attribute_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the deleteAttributeById to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_attributes**
> PagerAttributeDto filter_attributes(attribute_dto, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Filter Metadata Attributes

Endpoint for retrieving metadata attributes that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataAttributeApi()
attribute_dto = swagger_client.AttributeFilterDto() # AttributeFilterDto | attributeDto
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Filter Metadata Attributes
    api_response = api_instance.filter_attributes(attribute_dto, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataAttributeApi->filter_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_dto** | [**AttributeFilterDto**](AttributeFilterDto.md)| attributeDto | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerAttributeDto**](PagerAttributeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute**
> AttributeDto get_attribute(id)

Get Metadata Attribute

Endpoint for retrieving Metadata Attribute

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataAttributeApi()
id = 789 # int | Attribute Id

try:
    # Get Metadata Attribute
    api_response = api_instance.get_attribute(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataAttributeApi->get_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Attribute Id | 

### Return type

[**AttributeDto**](AttributeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes**
> PagerAttributeDto get_attributes(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all Metadata Attributes

Endpoint for retrieving all metadata attributes that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataAttributeApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all Metadata Attributes
    api_response = api_instance.get_attributes(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataAttributeApi->get_attributes: %s\n" % e)
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

[**PagerAttributeDto**](PagerAttributeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attribute_by_id**
> AttributeDto update_attribute_by_id(id, attribute)

Update Metadata Attribute

Updates an existing Metadata Attribute

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataAttributeApi()
id = 789 # int | The id of the Attribute to be updated
attribute = swagger_client.AttributeDto() # AttributeDto | Attribute to be updated

try:
    # Update Metadata Attribute
    api_response = api_instance.update_attribute_by_id(id, attribute)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataAttributeApi->update_attribute_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the Attribute to be updated | 
 **attribute** | [**AttributeDto**](AttributeDto.md)| Attribute to be updated | 

### Return type

[**AttributeDto**](AttributeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

