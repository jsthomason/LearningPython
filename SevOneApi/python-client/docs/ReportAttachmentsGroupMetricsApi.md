# swagger_client.ReportAttachmentsGroupMetricsApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group_metrics_attachment**](ReportAttachmentsGroupMetricsApi.md#create_group_metrics_attachment) | **POST** /api/v1/reports/{id}/attachments/group-metrics | Create group metrics report attachment
[**create_group_metrics_attachment1**](ReportAttachmentsGroupMetricsApi.md#create_group_metrics_attachment1) | **POST** /api/v2/reports/{id}/attachments/group-metrics | Create group metrics report attachment
[**get_group_metrics_attachment**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment) | **GET** /api/v1/reports/attachments/group-metrics/{id}/resources | Get group metrics report attachment
[**get_group_metrics_attachment1**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment1) | **GET** /api/v2/reports/attachments/group-metrics/{id} | Get group metrics attachment
[**get_group_metrics_attachment2**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment2) | **GET** /api/v2/reports/attachments/group-metrics/{id}/resources | Get group metrics report attachment
[**get_group_metrics_attachment_settings**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment_settings) | **GET** /api/v1/reports/attachments/group-metrics/{id}/settings | Get group metrics report attachment
[**get_group_metrics_attachment_settings1**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment_settings1) | **GET** /api/v2/reports/attachments/group-metrics/{id}/settings | Get group metrics report attachment
[**get_group_metrics_attachment_time_settings**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment_time_settings) | **GET** /api/v1/reports/attachments/group-metrics/{id}/time | Get group metrics report attachment
[**get_group_metrics_attachment_time_settings1**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment_time_settings1) | **GET** /api/v2/reports/attachments/group-metrics/{id}/time | Get group metrics report attachment
[**get_group_metrics_attachment_visualization**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment_visualization) | **GET** /api/v1/reports/attachments/group-metrics/{id}/visualization | Get group metrics report attachment
[**get_group_metrics_attachment_visualization1**](ReportAttachmentsGroupMetricsApi.md#get_group_metrics_attachment_visualization1) | **GET** /api/v2/reports/attachments/group-metrics/{id}/visualization | Get group metrics report attachment
[**update_group_metrics_attachment**](ReportAttachmentsGroupMetricsApi.md#update_group_metrics_attachment) | **PUT** /api/v1/reports/attachments/group-metrics/{id}/resources | Update group metrics report attachment
[**update_group_metrics_attachment1**](ReportAttachmentsGroupMetricsApi.md#update_group_metrics_attachment1) | **PUT** /api/v2/reports/attachments/group-metrics/{id}/resources | Update group metrics report attachment
[**update_group_metrics_attachment_settings**](ReportAttachmentsGroupMetricsApi.md#update_group_metrics_attachment_settings) | **PUT** /api/v1/reports/attachments/group-metrics/{id}/settings | Update group metrics report attachment
[**update_group_metrics_attachment_settings1**](ReportAttachmentsGroupMetricsApi.md#update_group_metrics_attachment_settings1) | **PUT** /api/v2/reports/attachments/group-metrics/{id}/settings | Update group metrics report attachment
[**update_group_metrics_attachment_time_settings**](ReportAttachmentsGroupMetricsApi.md#update_group_metrics_attachment_time_settings) | **PUT** /api/v1/reports/attachments/group-metrics/{id}/time | Update group metrics report attachment
[**update_group_metrics_attachment_time_settings1**](ReportAttachmentsGroupMetricsApi.md#update_group_metrics_attachment_time_settings1) | **PUT** /api/v2/reports/attachments/group-metrics/{id}/time | Update group metrics report attachment
[**update_group_metrics_attachment_visualization**](ReportAttachmentsGroupMetricsApi.md#update_group_metrics_attachment_visualization) | **PUT** /api/v1/reports/attachments/group-metrics/{id}/visualization | Update group metrics report attachment
[**update_group_metrics_attachment_visualization1**](ReportAttachmentsGroupMetricsApi.md#update_group_metrics_attachment_visualization1) | **PUT** /api/v2/reports/attachments/group-metrics/{id}/visualization | Update group metrics report attachment


# **create_group_metrics_attachment**
> GroupMetricsResponseDtoV1 create_group_metrics_attachment(id, group_setting_type)

Create group metrics report attachment

Creates a new group metrics attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report where the report attachment will be created
group_setting_type = swagger_client.GroupMetricsRequestDtoV1() # GroupMetricsRequestDtoV1 | GroupMetrics attachment

try:
    # Create group metrics report attachment
    api_response = api_instance.create_group_metrics_attachment(id, group_setting_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->create_group_metrics_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report where the report attachment will be created | 
 **group_setting_type** | [**GroupMetricsRequestDtoV1**](GroupMetricsRequestDtoV1.md)| GroupMetrics attachment | 

### Return type

[**GroupMetricsResponseDtoV1**](GroupMetricsResponseDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_metrics_attachment1**
> GroupMetricsResponseDto create_group_metrics_attachment1(id, group_setting_type)

Create group metrics report attachment

Creates a new group metrics attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report where the report attachment will be created
group_setting_type = swagger_client.GroupMetricsRequestDto() # GroupMetricsRequestDto | GroupMetrics attachment

try:
    # Create group metrics report attachment
    api_response = api_instance.create_group_metrics_attachment1(id, group_setting_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->create_group_metrics_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report where the report attachment will be created | 
 **group_setting_type** | [**GroupMetricsRequestDto**](GroupMetricsRequestDto.md)| GroupMetrics attachment | 

### Return type

[**GroupMetricsResponseDto**](GroupMetricsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metrics_attachment**
> GroupMetricsResourceV1 get_group_metrics_attachment(id)

Get group metrics report attachment

Get group metrics attachment resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get group metrics report attachment
    api_response = api_instance.get_group_metrics_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsResourceV1**](GroupMetricsResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metrics_attachment1**
> GroupMetricsResponseDto get_group_metrics_attachment1(id)

Get group metrics attachment

Get an existing group metrics attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | Group metrics attachment id

try:
    # Get group metrics attachment
    api_response = api_instance.get_group_metrics_attachment1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group metrics attachment id | 

### Return type

[**GroupMetricsResponseDto**](GroupMetricsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metrics_attachment2**
> GroupMetricsResource get_group_metrics_attachment2(id)

Get group metrics report attachment

Get group metrics attachment resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get group metrics report attachment
    api_response = api_instance.get_group_metrics_attachment2(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsResource**](GroupMetricsResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metrics_attachment_settings**
> GroupMetricsSettingsDtoV1 get_group_metrics_attachment_settings(id)

Get group metrics report attachment

Get group metrics attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get group metrics report attachment
    api_response = api_instance.get_group_metrics_attachment_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsSettingsDtoV1**](GroupMetricsSettingsDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metrics_attachment_settings1**
> GroupMetricsSettingsDto get_group_metrics_attachment_settings1(id)

Get group metrics report attachment

Get group metrics attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get group metrics report attachment
    api_response = api_instance.get_group_metrics_attachment_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsSettingsDto**](GroupMetricsSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metrics_attachment_time_settings**
> TimeSettingV1 get_group_metrics_attachment_time_settings(id)

Get group metrics report attachment

Get group metrics attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get group metrics report attachment
    api_response = api_instance.get_group_metrics_attachment_time_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment_time_settings: %s\n" % e)
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

# **get_group_metrics_attachment_time_settings1**
> TimeSetting get_group_metrics_attachment_time_settings1(id)

Get group metrics report attachment

Get group metrics attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get group metrics report attachment
    api_response = api_instance.get_group_metrics_attachment_time_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment_time_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TimeSetting**](TimeSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metrics_attachment_visualization**
> GroupMetricsVisualizationV1 get_group_metrics_attachment_visualization(id)

Get group metrics report attachment

Get group metrics attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get group metrics report attachment
    api_response = api_instance.get_group_metrics_attachment_visualization(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment_visualization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsVisualizationV1**](GroupMetricsVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_metrics_attachment_visualization1**
> GroupMetricsVisualization get_group_metrics_attachment_visualization1(id)

Get group metrics report attachment

Get group metrics attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment

try:
    # Get group metrics report attachment
    api_response = api_instance.get_group_metrics_attachment_visualization1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->get_group_metrics_attachment_visualization1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**GroupMetricsVisualization**](GroupMetricsVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_metrics_attachment**
> GroupMetricsResourceV1 update_group_metrics_attachment(id, resource)

Update group metrics report attachment

Update group metrics attachment resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment
resource = swagger_client.GroupMetricsResourceV1() # GroupMetricsResourceV1 | GroupMetrics attachment resources

try:
    # Update group metrics report attachment
    api_response = api_instance.update_group_metrics_attachment(id, resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->update_group_metrics_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **resource** | [**GroupMetricsResourceV1**](GroupMetricsResourceV1.md)| GroupMetrics attachment resources | 

### Return type

[**GroupMetricsResourceV1**](GroupMetricsResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_metrics_attachment1**
> GroupMetricsResource update_group_metrics_attachment1(id, resource)

Update group metrics report attachment

Update group metrics attachment resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment
resource = swagger_client.GroupMetricsResource() # GroupMetricsResource | GroupMetrics attachment resources

try:
    # Update group metrics report attachment
    api_response = api_instance.update_group_metrics_attachment1(id, resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->update_group_metrics_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **resource** | [**GroupMetricsResource**](GroupMetricsResource.md)| GroupMetrics attachment resources | 

### Return type

[**GroupMetricsResource**](GroupMetricsResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_metrics_attachment_settings**
> GroupMetricsSettingsDtoV1 update_group_metrics_attachment_settings(id, settings)

Update group metrics report attachment

Update group metrics attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment
settings = swagger_client.GroupMetricsSettingsDtoV1() # GroupMetricsSettingsDtoV1 | GroupMetrics attachment settings

try:
    # Update group metrics report attachment
    api_response = api_instance.update_group_metrics_attachment_settings(id, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->update_group_metrics_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **settings** | [**GroupMetricsSettingsDtoV1**](GroupMetricsSettingsDtoV1.md)| GroupMetrics attachment settings | 

### Return type

[**GroupMetricsSettingsDtoV1**](GroupMetricsSettingsDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_metrics_attachment_settings1**
> GroupMetricsSettingsDto update_group_metrics_attachment_settings1(id, settings)

Update group metrics report attachment

Update group metrics attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment
settings = swagger_client.GroupMetricsSettingsDto() # GroupMetricsSettingsDto | GroupMetrics attachment settings

try:
    # Update group metrics report attachment
    api_response = api_instance.update_group_metrics_attachment_settings1(id, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->update_group_metrics_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **settings** | [**GroupMetricsSettingsDto**](GroupMetricsSettingsDto.md)| GroupMetrics attachment settings | 

### Return type

[**GroupMetricsSettingsDto**](GroupMetricsSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_metrics_attachment_time_settings**
> TimeSettingV1 update_group_metrics_attachment_time_settings(id, time)

Update group metrics report attachment

Update group metrics attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment
time = swagger_client.TimeSettingV1() # TimeSettingV1 | GroupMetrics attachment time settings

try:
    # Update group metrics report attachment
    api_response = api_instance.update_group_metrics_attachment_time_settings(id, time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->update_group_metrics_attachment_time_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **time** | [**TimeSettingV1**](TimeSettingV1.md)| GroupMetrics attachment time settings | 

### Return type

[**TimeSettingV1**](TimeSettingV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_metrics_attachment_time_settings1**
> TimeSetting update_group_metrics_attachment_time_settings1(id, time)

Update group metrics report attachment

Update group metrics attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment
time = swagger_client.TimeSetting() # TimeSetting | GroupMetrics attachment time settings

try:
    # Update group metrics report attachment
    api_response = api_instance.update_group_metrics_attachment_time_settings1(id, time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->update_group_metrics_attachment_time_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **time** | [**TimeSetting**](TimeSetting.md)| GroupMetrics attachment time settings | 

### Return type

[**TimeSetting**](TimeSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_metrics_attachment_visualization**
> GroupMetricsVisualizationV1 update_group_metrics_attachment_visualization(id, visualization)

Update group metrics report attachment

Update group metrics attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment
visualization = swagger_client.GroupMetricsVisualizationV1() # GroupMetricsVisualizationV1 | Group metrics attachment visualizations

try:
    # Update group metrics report attachment
    api_response = api_instance.update_group_metrics_attachment_visualization(id, visualization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->update_group_metrics_attachment_visualization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **visualization** | [**GroupMetricsVisualizationV1**](GroupMetricsVisualizationV1.md)| Group metrics attachment visualizations | 

### Return type

[**GroupMetricsVisualizationV1**](GroupMetricsVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_metrics_attachment_visualization1**
> GroupMetricsVisualization update_group_metrics_attachment_visualization1(id, visualization)

Update group metrics report attachment

Update group metrics attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsGroupMetricsApi()
id = 789 # int | The id of the report attachment
visualization = swagger_client.GroupMetricsVisualization() # GroupMetricsVisualization | Group metrics attachment visualizations

try:
    # Update group metrics report attachment
    api_response = api_instance.update_group_metrics_attachment_visualization1(id, visualization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsGroupMetricsApi->update_group_metrics_attachment_visualization1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **visualization** | [**GroupMetricsVisualization**](GroupMetricsVisualization.md)| Group metrics attachment visualizations | 

### Return type

[**GroupMetricsVisualization**](GroupMetricsVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

