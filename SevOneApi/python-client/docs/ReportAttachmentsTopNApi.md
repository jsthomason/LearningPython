# swagger_client.ReportAttachmentsTopNApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_top_n_attachment**](ReportAttachmentsTopNApi.md#create_top_n_attachment) | **POST** /api/v2/reports/{id}/attachments/topn | Create topN report attachment
[**create_top_n_attachment1**](ReportAttachmentsTopNApi.md#create_top_n_attachment1) | **POST** /api/v1/reports/{id}/attachments/topn | Create topN report attachment
[**get_top_n_attachment**](ReportAttachmentsTopNApi.md#get_top_n_attachment) | **GET** /api/v2/reports/attachments/topn/{id} | Get topn attachment
[**get_top_n_attachment_resources**](ReportAttachmentsTopNApi.md#get_top_n_attachment_resources) | **GET** /api/v2/reports/attachments/topn/{id}/resources | Get resources
[**get_top_n_attachment_resources1**](ReportAttachmentsTopNApi.md#get_top_n_attachment_resources1) | **GET** /api/v1/reports/attachments/topn/{id}/resources | Get resources
[**get_top_n_attachment_settings**](ReportAttachmentsTopNApi.md#get_top_n_attachment_settings) | **GET** /api/v2/reports/attachments/topn/{id}/settings | Get attachment settings
[**get_top_n_attachment_settings1**](ReportAttachmentsTopNApi.md#get_top_n_attachment_settings1) | **GET** /api/v1/reports/attachments/topn/{id}/settings | Get attachment settings
[**get_top_n_attachment_time_settings**](ReportAttachmentsTopNApi.md#get_top_n_attachment_time_settings) | **GET** /api/v2/reports/attachments/topn/{id}/time | Get topN report attachment
[**get_top_n_attachment_time_settings1**](ReportAttachmentsTopNApi.md#get_top_n_attachment_time_settings1) | **GET** /api/v1/reports/attachments/topn/{id}/time | Get topN report attachment
[**get_top_n_attachment_visualization_settings**](ReportAttachmentsTopNApi.md#get_top_n_attachment_visualization_settings) | **GET** /api/v2/reports/attachments/topn/{id}/visualizations | Get attachment visualization settings
[**get_top_n_attachment_visualization_settings1**](ReportAttachmentsTopNApi.md#get_top_n_attachment_visualization_settings1) | **GET** /api/v1/reports/attachments/topn/{id}/visualizations | Get attachment visualization settings
[**partially_update_top_n_attachment_settings**](ReportAttachmentsTopNApi.md#partially_update_top_n_attachment_settings) | **PATCH** /api/v2/reports/attachments/topn/{id}/settings | Partially update attachment settings
[**partially_update_top_n_attachment_settings1**](ReportAttachmentsTopNApi.md#partially_update_top_n_attachment_settings1) | **PATCH** /api/v1/reports/attachments/topn/{id}/settings | Partially update attachment settings
[**partially_update_top_n_attachment_visualization_settings**](ReportAttachmentsTopNApi.md#partially_update_top_n_attachment_visualization_settings) | **PATCH** /api/v2/reports/attachments/topn/{id}/visualizations | Partially update visualization settings
[**partially_update_top_n_attachment_visualization_settings1**](ReportAttachmentsTopNApi.md#partially_update_top_n_attachment_visualization_settings1) | **PATCH** /api/v1/reports/attachments/topn/{id}/visualizations | Partially update visualization settings
[**update_top_n_attachment_resources**](ReportAttachmentsTopNApi.md#update_top_n_attachment_resources) | **PUT** /api/v2/reports/attachments/topn/{id}/resources | Update resources
[**update_top_n_attachment_resources1**](ReportAttachmentsTopNApi.md#update_top_n_attachment_resources1) | **PUT** /api/v1/reports/attachments/topn/{id}/resources | Update resources
[**update_top_n_attachment_settings**](ReportAttachmentsTopNApi.md#update_top_n_attachment_settings) | **PUT** /api/v2/reports/attachments/topn/{id}/settings | Update attachment settings
[**update_top_n_attachment_settings1**](ReportAttachmentsTopNApi.md#update_top_n_attachment_settings1) | **PUT** /api/v1/reports/attachments/topn/{id}/settings | Update attachment settings
[**update_top_n_attachment_time_settings**](ReportAttachmentsTopNApi.md#update_top_n_attachment_time_settings) | **PUT** /api/v2/reports/attachments/topn/{id}/time | Update topN report attachment
[**update_top_n_attachment_time_settings1**](ReportAttachmentsTopNApi.md#update_top_n_attachment_time_settings1) | **PUT** /api/v1/reports/attachments/topn/{id}/time | Update topN report attachment
[**update_top_n_attachment_visualization_settings**](ReportAttachmentsTopNApi.md#update_top_n_attachment_visualization_settings) | **PUT** /api/v2/reports/attachments/topn/{id}/visualizations | Update visualization settings
[**update_top_n_attachment_visualization_settings1**](ReportAttachmentsTopNApi.md#update_top_n_attachment_visualization_settings1) | **PUT** /api/v1/reports/attachments/topn/{id}/visualizations | Update visualization settings


# **create_top_n_attachment**
> TopNResponseDto create_top_n_attachment(id, top_n_request_dto)

Create topN report attachment

Creates a new topN report attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report where the report attachment will be created
top_n_request_dto = swagger_client.TopNRequestDto() # TopNRequestDto | TopN attachment object

try:
    # Create topN report attachment
    api_response = api_instance.create_top_n_attachment(id, top_n_request_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->create_top_n_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report where the report attachment will be created | 
 **top_n_request_dto** | [**TopNRequestDto**](TopNRequestDto.md)| TopN attachment object | 

### Return type

[**TopNResponseDto**](TopNResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_top_n_attachment1**
> TopNResponseDtoV1 create_top_n_attachment1(id, top_n_request_dto)

Create topN report attachment

Creates a new topN report attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report where the report attachment will be created
top_n_request_dto = swagger_client.TopNRequestDtoV1() # TopNRequestDtoV1 | TopN attachment object

try:
    # Create topN report attachment
    api_response = api_instance.create_top_n_attachment1(id, top_n_request_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->create_top_n_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report where the report attachment will be created | 
 **top_n_request_dto** | [**TopNRequestDtoV1**](TopNRequestDtoV1.md)| TopN attachment object | 

### Return type

[**TopNResponseDtoV1**](TopNResponseDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_n_attachment**
> TopNResponseDto get_top_n_attachment(id)

Get topn attachment

Get an existing topn attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | TopN attachment id

try:
    # Get topn attachment
    api_response = api_instance.get_top_n_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->get_top_n_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| TopN attachment id | 

### Return type

[**TopNResponseDto**](TopNResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_n_attachment_resources**
> TopNResource get_top_n_attachment_resources(id)

Get resources

Get topn resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources
    api_response = api_instance.get_top_n_attachment_resources(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->get_top_n_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TopNResource**](TopNResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_n_attachment_resources1**
> TopNResourceV1 get_top_n_attachment_resources1(id)

Get resources

Get topn resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources
    api_response = api_instance.get_top_n_attachment_resources1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->get_top_n_attachment_resources1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TopNResourceV1**](TopNResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_n_attachment_settings**
> TopNSettings get_top_n_attachment_settings(id)

Get attachment settings

Get topn attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment settings
    api_response = api_instance.get_top_n_attachment_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->get_top_n_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TopNSettings**](TopNSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_n_attachment_settings1**
> TopNSettingsV1 get_top_n_attachment_settings1(id)

Get attachment settings

Get topn attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment settings
    api_response = api_instance.get_top_n_attachment_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->get_top_n_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TopNSettingsV1**](TopNSettingsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_n_attachment_time_settings**
> TimeSettings get_top_n_attachment_time_settings(id)

Get topN report attachment

Get topN report attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment

try:
    # Get topN report attachment
    api_response = api_instance.get_top_n_attachment_time_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->get_top_n_attachment_time_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TimeSettings**](TimeSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_n_attachment_time_settings1**
> TimeSettingV1 get_top_n_attachment_time_settings1(id)

Get topN report attachment

Get topN report attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment

try:
    # Get topN report attachment
    api_response = api_instance.get_top_n_attachment_time_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->get_top_n_attachment_time_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TimeSettingV1**](TimeSettingV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_n_attachment_visualization_settings**
> TopNVisualization get_top_n_attachment_visualization_settings(id)

Get attachment visualization settings

Get topn attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_top_n_attachment_visualization_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->get_top_n_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TopNVisualization**](TopNVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_n_attachment_visualization_settings1**
> TopNVisualizationV1 get_top_n_attachment_visualization_settings1(id)

Get attachment visualization settings

Get topn attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_top_n_attachment_visualization_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->get_top_n_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TopNVisualizationV1**](TopNVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_top_n_attachment_settings**
> TopNSettings partially_update_top_n_attachment_settings(id, settings)

Partially update attachment settings

Partial update topn attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment
settings = swagger_client.TopNSettings() # TopNSettings | TopN attachment settings

try:
    # Partially update attachment settings
    api_response = api_instance.partially_update_top_n_attachment_settings(id, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->partially_update_top_n_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **settings** | [**TopNSettings**](TopNSettings.md)| TopN attachment settings | 

### Return type

[**TopNSettings**](TopNSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_top_n_attachment_settings1**
> TopNSettingsV1 partially_update_top_n_attachment_settings1(id, settings)

Partially update attachment settings

Partial update topn attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment
settings = swagger_client.TopNSettingsV1() # TopNSettingsV1 | TopN attachment settings

try:
    # Partially update attachment settings
    api_response = api_instance.partially_update_top_n_attachment_settings1(id, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->partially_update_top_n_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **settings** | [**TopNSettingsV1**](TopNSettingsV1.md)| TopN attachment settings | 

### Return type

[**TopNSettingsV1**](TopNSettingsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_top_n_attachment_visualization_settings**
> TopNVisualization partially_update_top_n_attachment_visualization_settings(id, visualizations)

Partially update visualization settings

Partial update topn visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment
visualizations = swagger_client.TopNVisualization() # TopNVisualization | TopN attachment visualization settings

try:
    # Partially update visualization settings
    api_response = api_instance.partially_update_top_n_attachment_visualization_settings(id, visualizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->partially_update_top_n_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **visualizations** | [**TopNVisualization**](TopNVisualization.md)| TopN attachment visualization settings | 

### Return type

[**TopNVisualization**](TopNVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_top_n_attachment_visualization_settings1**
> TopNVisualizationV1 partially_update_top_n_attachment_visualization_settings1(id, visualizations)

Partially update visualization settings

Partial update topn visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment
visualizations = swagger_client.TopNVisualizationV1() # TopNVisualizationV1 | TopN attachment visualization settings

try:
    # Partially update visualization settings
    api_response = api_instance.partially_update_top_n_attachment_visualization_settings1(id, visualizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->partially_update_top_n_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **visualizations** | [**TopNVisualizationV1**](TopNVisualizationV1.md)| TopN attachment visualization settings | 

### Return type

[**TopNVisualizationV1**](TopNVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_top_n_attachment_resources**
> TopNResource update_top_n_attachment_resources(id, resources)

Update resources

Update topn resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment
resources = swagger_client.TopNResource() # TopNResource | TopN attachment resources

try:
    # Update resources
    api_response = api_instance.update_top_n_attachment_resources(id, resources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->update_top_n_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **resources** | [**TopNResource**](TopNResource.md)| TopN attachment resources | 

### Return type

[**TopNResource**](TopNResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_top_n_attachment_resources1**
> TopNResourceV1 update_top_n_attachment_resources1(id, resources)

Update resources

Update topn resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment
resources = swagger_client.TopNResourceV1() # TopNResourceV1 | TopN attachment resources

try:
    # Update resources
    api_response = api_instance.update_top_n_attachment_resources1(id, resources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->update_top_n_attachment_resources1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **resources** | [**TopNResourceV1**](TopNResourceV1.md)| TopN attachment resources | 

### Return type

[**TopNResourceV1**](TopNResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_top_n_attachment_settings**
> TopNSettings update_top_n_attachment_settings(id, settings)

Update attachment settings

Update topN attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment
settings = swagger_client.TopNSettings() # TopNSettings | TopN attachment settings

try:
    # Update attachment settings
    api_response = api_instance.update_top_n_attachment_settings(id, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->update_top_n_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **settings** | [**TopNSettings**](TopNSettings.md)| TopN attachment settings | 

### Return type

[**TopNSettings**](TopNSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_top_n_attachment_settings1**
> TopNSettingsV1 update_top_n_attachment_settings1(id, settings)

Update attachment settings

Update topN attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment
settings = swagger_client.TopNSettingsV1() # TopNSettingsV1 | TopN attachment settings

try:
    # Update attachment settings
    api_response = api_instance.update_top_n_attachment_settings1(id, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->update_top_n_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **settings** | [**TopNSettingsV1**](TopNSettingsV1.md)| TopN attachment settings | 

### Return type

[**TopNSettingsV1**](TopNSettingsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_top_n_attachment_time_settings**
> TimeSettings update_top_n_attachment_time_settings(id, time)

Update topN report attachment

Update a new topN attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment
time = swagger_client.TimeSettings() # TimeSettings | TopN attachment time settings

try:
    # Update topN report attachment
    api_response = api_instance.update_top_n_attachment_time_settings(id, time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->update_top_n_attachment_time_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **time** | [**TimeSettings**](TimeSettings.md)| TopN attachment time settings | 

### Return type

[**TimeSettings**](TimeSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_top_n_attachment_time_settings1**
> TimeSettingV1 update_top_n_attachment_time_settings1(id, time)

Update topN report attachment

Update a new topN attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment
time = swagger_client.TimeSettingV1() # TimeSettingV1 | TopN attachment time settings

try:
    # Update topN report attachment
    api_response = api_instance.update_top_n_attachment_time_settings1(id, time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->update_top_n_attachment_time_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **time** | [**TimeSettingV1**](TimeSettingV1.md)| TopN attachment time settings | 

### Return type

[**TimeSettingV1**](TimeSettingV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_top_n_attachment_visualization_settings**
> TopNVisualization update_top_n_attachment_visualization_settings(id, visualizations)

Update visualization settings

Update topn visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment
visualizations = swagger_client.TopNVisualization() # TopNVisualization | TopN attachment visualization settings

try:
    # Update visualization settings
    api_response = api_instance.update_top_n_attachment_visualization_settings(id, visualizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->update_top_n_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **visualizations** | [**TopNVisualization**](TopNVisualization.md)| TopN attachment visualization settings | 

### Return type

[**TopNVisualization**](TopNVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_top_n_attachment_visualization_settings1**
> TopNVisualizationV1 update_top_n_attachment_visualization_settings1(id, visualizations)

Update visualization settings

Update topn visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopNApi()
id = 789 # int | The id of the report attachment
visualizations = swagger_client.TopNVisualizationV1() # TopNVisualizationV1 | TopN attachment visualization settings

try:
    # Update visualization settings
    api_response = api_instance.update_top_n_attachment_visualization_settings1(id, visualizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopNApi->update_top_n_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **visualizations** | [**TopNVisualizationV1**](TopNVisualizationV1.md)| TopN attachment visualization settings | 

### Return type

[**TopNVisualizationV1**](TopNVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

