# swagger_client.TopNViewsApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_top_n_view**](TopNViewsApi.md#create_top_n_view) | **POST** /api/v2/topnviews | Create TopNView
[**delete_top_n_view_by_id**](TopNViewsApi.md#delete_top_n_view_by_id) | **DELETE** /api/v2/topnviews/{id} | Delete TopNVIew
[**get_top_n_view**](TopNViewsApi.md#get_top_n_view) | **GET** /api/v2/topnviews/{id} | Get TopNView
[**get_top_n_views**](TopNViewsApi.md#get_top_n_views) | **GET** /api/v2/topnviews | Get all TopNViews
[**update_top_n_view_by_id**](TopNViewsApi.md#update_top_n_view_by_id) | **PUT** /api/v2/topnviews/{id} | Update TopNView


# **create_top_n_view**
> TopNViewDto create_top_n_view(view)

Create TopNView

Creates a new TopNView

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopNViewsApi()
view = swagger_client.TopNViewDto() # TopNViewDto | TopNView object that will be added to the database

try:
    # Create TopNView
    api_response = api_instance.create_top_n_view(view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopNViewsApi->create_top_n_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | [**TopNViewDto**](TopNViewDto.md)| TopNView object that will be added to the database | 

### Return type

[**TopNViewDto**](TopNViewDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_top_n_view_by_id**
> ResponseEntity delete_top_n_view_by_id(id)

Delete TopNVIew

Deletes an existing TopNView

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopNViewsApi()
id = 789 # int | The id of the TopNView to be deleted

try:
    # Delete TopNVIew
    api_response = api_instance.delete_top_n_view_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopNViewsApi->delete_top_n_view_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the TopNView to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_n_view**
> TopNViewDto get_top_n_view(id)

Get TopNView

Endpoint for retrieving TopNView info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopNViewsApi()
id = 789 # int | TopNView Id

try:
    # Get TopNView
    api_response = api_instance.get_top_n_view(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopNViewsApi->get_top_n_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| TopNView Id | 

### Return type

[**TopNViewDto**](TopNViewDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_n_views**
> PagerTopNViewDto get_top_n_views(name=name, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all TopNViews

Endpoint for retrieving all views that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopNViewsApi()
name = 'name_example' # str | Filter by TopNView name (optional)
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all TopNViews
    api_response = api_instance.get_top_n_views(name=name, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopNViewsApi->get_top_n_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter by TopNView name | [optional] 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerTopNViewDto**](PagerTopNViewDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_top_n_view_by_id**
> TopNViewDto update_top_n_view_by_id(id, view)

Update TopNView

Updates an existing TopNVIew

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopNViewsApi()
id = 789 # int | The id of the TopNView to be updated
view = swagger_client.TopNViewDto() # TopNViewDto | TopNView to be updated

try:
    # Update TopNView
    api_response = api_instance.update_top_n_view_by_id(id, view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopNViewsApi->update_top_n_view_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the TopNView to be updated | 
 **view** | [**TopNViewDto**](TopNViewDto.md)| TopNView to be updated | 

### Return type

[**TopNViewDto**](TopNViewDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

