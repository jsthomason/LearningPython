# swagger_client.MetadataApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metadata_value**](MetadataApi.md#get_metadata_value) | **GET** /api/v2/{entityType}/{entityId}/metadata | Get Metadata values
[**get_object_metadata_value**](MetadataApi.md#get_object_metadata_value) | **GET** /api/v2/devices/{deviceId}/objects/{objectId}/metadata | Get Object Metadata value
[**partial_update_metadata**](MetadataApi.md#partial_update_metadata) | **PATCH** /api/v2/{entityType}/{entityId}/metadata | Partially update Metadata Attributes
[**partial_update_metadata1**](MetadataApi.md#partial_update_metadata1) | **PATCH** /api/v2/devices/{deviceId}/objects/{objectId}/metadata | Partially update Metadata Attributes
[**update_metadata**](MetadataApi.md#update_metadata) | **PUT** /api/v2/{entityType}/{entityId}/metadata | Update Metadata Attributes
[**update_metadata1**](MetadataApi.md#update_metadata1) | **PUT** /api/v2/devices/{deviceId}/objects/{objectId}/metadata | Update Metadata Attributes
[**update_metadata_by_attribute**](MetadataApi.md#update_metadata_by_attribute) | **PUT** /api/v2/{entityType}/{entityId}/metadata/{attributeKey} | Update Metadata Attributes
[**update_metadata_by_attribute1**](MetadataApi.md#update_metadata_by_attribute1) | **PUT** /api/v2/devices/{deviceId}/objects/{objectId}/metadata/{attributeKey} | Update Metadata Attributes


# **get_metadata_value**
> AttributeValues get_metadata_value(entity_type, entity_id)

Get Metadata values

This endpoint will get metadata value for entity type (device/object group/device group/object type/indicator type) and entity id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
entity_type = 'entity_type_example' # str | Entity Type
entity_id = 789 # int | Entity Id

try:
    # Get Metadata values
    api_response = api_instance.get_metadata_value(entity_type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_metadata_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| Entity Type | 
 **entity_id** | **int**| Entity Id | 

### Return type

[**AttributeValues**](AttributeValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_metadata_value**
> AttributeValues get_object_metadata_value(device_id, object_id)

Get Object Metadata value

This endpoint will get metadata value for entity type (object) and entity id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
device_id = 789 # int | Device Id
object_id = 789 # int | Object Id

try:
    # Get Object Metadata value
    api_response = api_instance.get_object_metadata_value(device_id, object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_object_metadata_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Device Id | 
 **object_id** | **int**| Object Id | 

### Return type

[**AttributeValues**](AttributeValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_metadata**
> AttributeValues partial_update_metadata(entity_type, entity_id, values=values)

Partially update Metadata Attributes

This endpoint will update the provided metadata values for this entity type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
entity_type = 'entity_type_example' # str | Entity Type
entity_id = 789 # int | Entity Id
values = NULL # object | Type of the param is `Map<String, AttributeValues>`, the string key consists of 'namespacename.attributename' (optional)

try:
    # Partially update Metadata Attributes
    api_response = api_instance.partial_update_metadata(entity_type, entity_id, values=values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->partial_update_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| Entity Type | 
 **entity_id** | **int**| Entity Id | 
 **values** | **object**| Type of the param is &#x60;Map&lt;String, AttributeValues&gt;&#x60;, the string key consists of &#39;namespacename.attributename&#39; | [optional] 

### Return type

[**AttributeValues**](AttributeValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_metadata1**
> AttributeValues partial_update_metadata1(device_id, object_id, values=values)

Partially update Metadata Attributes

This endpoint will update the provided metadata values for this object

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
device_id = 789 # int | Device Id
object_id = 789 # int | Object Id
values = NULL # object | Type of the param is `Map<String, AttributeValues>`, the string key consists of 'namespacename.attributename' (optional)

try:
    # Partially update Metadata Attributes
    api_response = api_instance.partial_update_metadata1(device_id, object_id, values=values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->partial_update_metadata1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Device Id | 
 **object_id** | **int**| Object Id | 
 **values** | **object**| Type of the param is &#x60;Map&lt;String, AttributeValues&gt;&#x60;, the string key consists of &#39;namespacename.attributename&#39; | [optional] 

### Return type

[**AttributeValues**](AttributeValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata**
> AttributeValues update_metadata(entity_type, entity_id, values=values)

Update Metadata Attributes

This endpoint will delete all metadata values for this entity type and will create the values provided

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
entity_type = 'entity_type_example' # str | Entity Type
entity_id = 789 # int | Entity Id
values = NULL # object | Type of the param is `Map<String, AttributeValues>`, the string key consists of 'namespacename.attributename' (optional)

try:
    # Update Metadata Attributes
    api_response = api_instance.update_metadata(entity_type, entity_id, values=values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->update_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| Entity Type | 
 **entity_id** | **int**| Entity Id | 
 **values** | **object**| Type of the param is &#x60;Map&lt;String, AttributeValues&gt;&#x60;, the string key consists of &#39;namespacename.attributename&#39; | [optional] 

### Return type

[**AttributeValues**](AttributeValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata1**
> AttributeValues update_metadata1(device_id, object_id, values=values)

Update Metadata Attributes

This endpoint will delete all metadata values for this object and will create the values provided

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
device_id = 789 # int | Device Id
object_id = 789 # int | Object Id
values = NULL # object | Type of the param is `Map<String, AttributeValues>`, the string key consists of 'namespacename.attributename' (optional)

try:
    # Update Metadata Attributes
    api_response = api_instance.update_metadata1(device_id, object_id, values=values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->update_metadata1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Device Id | 
 **object_id** | **int**| Object Id | 
 **values** | **object**| Type of the param is &#x60;Map&lt;String, AttributeValues&gt;&#x60;, the string key consists of &#39;namespacename.attributename&#39; | [optional] 

### Return type

[**AttributeValues**](AttributeValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_by_attribute**
> AttributeValues update_metadata_by_attribute(entity_type, entity_id, attribute_key, values)

Update Metadata Attributes

This endpoint will delete all metadata values for this entity type and attribute and will create the values provided

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
entity_type = 'entity_type_example' # str | Entity Type
entity_id = 789 # int | Entity Id
attribute_key = 'attribute_key_example' # str | AttributeKey
values = swagger_client.AttributeValues() # AttributeValues | values

try:
    # Update Metadata Attributes
    api_response = api_instance.update_metadata_by_attribute(entity_type, entity_id, attribute_key, values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->update_metadata_by_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| Entity Type | 
 **entity_id** | **int**| Entity Id | 
 **attribute_key** | **str**| AttributeKey | 
 **values** | [**AttributeValues**](AttributeValues.md)| values | 

### Return type

[**AttributeValues**](AttributeValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_by_attribute1**
> AttributeValues update_metadata_by_attribute1(device_id, object_id, attribute_key, values)

Update Metadata Attributes

This endpoint will delete all metadata values for this object and attribute and will create the values provided

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
device_id = 789 # int | Device Id
object_id = 789 # int | Object Id
attribute_key = 'attribute_key_example' # str | AttributeKey
values = swagger_client.AttributeValues() # AttributeValues | values

try:
    # Update Metadata Attributes
    api_response = api_instance.update_metadata_by_attribute1(device_id, object_id, attribute_key, values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->update_metadata_by_attribute1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**| Device Id | 
 **object_id** | **int**| Object Id | 
 **attribute_key** | **str**| AttributeKey | 
 **values** | [**AttributeValues**](AttributeValues.md)| values | 

### Return type

[**AttributeValues**](AttributeValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

