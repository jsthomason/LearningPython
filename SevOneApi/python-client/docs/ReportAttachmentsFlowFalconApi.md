# swagger_client.ReportAttachmentsFlowFalconApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_flow_falcon_attachment**](ReportAttachmentsFlowFalconApi.md#create_flow_falcon_attachment) | **POST** /api/v2/reports/{id}/attachments/flow-falcon | Create flow falcon attachment
[**create_flow_falcon_attachment1**](ReportAttachmentsFlowFalconApi.md#create_flow_falcon_attachment1) | **POST** /api/v1/reports/{id}/attachments/flow-falcon | Create flow falcon attachment
[**get_flow_falcon_attachment**](ReportAttachmentsFlowFalconApi.md#get_flow_falcon_attachment) | **GET** /api/v2/reports/attachments/flow-falcon/{id} | Get a flow falcon attachment
[**get_flow_falcon_attachment_filter_schema**](ReportAttachmentsFlowFalconApi.md#get_flow_falcon_attachment_filter_schema) | **GET** /api/v2/reports/attachments/flow-falcon/filters/schema | Gets the filters schema
[**get_flow_falcon_attachment_filter_schema1**](ReportAttachmentsFlowFalconApi.md#get_flow_falcon_attachment_filter_schema1) | **GET** /api/v1/reports/attachments/flow-falcon/filters/schema | Gets the filters schema
[**get_flow_falcon_attachment_filters**](ReportAttachmentsFlowFalconApi.md#get_flow_falcon_attachment_filters) | **GET** /api/v2/reports/attachments/flow-falcon/{id}/filters | Get filters
[**get_flow_falcon_attachment_filters1**](ReportAttachmentsFlowFalconApi.md#get_flow_falcon_attachment_filters1) | **GET** /api/v1/reports/attachments/flow-falcon/{id}/filters | Get filters
[**get_flow_falcon_attachment_resources**](ReportAttachmentsFlowFalconApi.md#get_flow_falcon_attachment_resources) | **GET** /api/v2/reports/attachments/flow-falcon/{id}/resources | Get resources
[**get_flow_falcon_attachment_resources1**](ReportAttachmentsFlowFalconApi.md#get_flow_falcon_attachment_resources1) | **GET** /api/v1/reports/attachments/flow-falcon/{id}/resources | Get resources
[**get_flow_falcon_attachment_settings**](ReportAttachmentsFlowFalconApi.md#get_flow_falcon_attachment_settings) | **GET** /api/v2/reports/attachments/flow-falcon/{id}/settings | Get attachment settings
[**get_flow_falcon_attachment_settings1**](ReportAttachmentsFlowFalconApi.md#get_flow_falcon_attachment_settings1) | **GET** /api/v1/reports/attachments/flow-falcon/{id}/settings | Get attachment settings
[**get_flow_falcon_attachment_time_settings**](ReportAttachmentsFlowFalconApi.md#get_flow_falcon_attachment_time_settings) | **GET** /api/v2/reports/attachments/flow-falcon/{id}/time | GET time ranges
[**get_flow_falcon_attachment_time_settings1**](ReportAttachmentsFlowFalconApi.md#get_flow_falcon_attachment_time_settings1) | **GET** /api/v1/reports/attachments/flow-falcon/{id}/time | GET time ranges
[**get_flow_falcon_attachment_visualization_settings**](ReportAttachmentsFlowFalconApi.md#get_flow_falcon_attachment_visualization_settings) | **GET** /api/v2/reports/attachments/flow-falcon/{id}/visualizations | Get attachment visualization settings
[**get_flow_falcon_attachment_visualization_settings1**](ReportAttachmentsFlowFalconApi.md#get_flow_falcon_attachment_visualization_settings1) | **GET** /api/v1/reports/attachments/flow-falcon/{id}/visualizations | Get attachment visualization settings
[**partially_update_flow_falcon_attachment_settings**](ReportAttachmentsFlowFalconApi.md#partially_update_flow_falcon_attachment_settings) | **PATCH** /api/v2/reports/attachments/flow-falcon/{id}/settings | Partially update attachment settings
[**partially_update_flow_falcon_attachment_settings1**](ReportAttachmentsFlowFalconApi.md#partially_update_flow_falcon_attachment_settings1) | **PATCH** /api/v1/reports/attachments/flow-falcon/{id}/settings | Partially update attachment settings
[**partially_update_flow_falcon_attachment_visualization_settings**](ReportAttachmentsFlowFalconApi.md#partially_update_flow_falcon_attachment_visualization_settings) | **PATCH** /api/v2/reports/attachments/flow-falcon/{id}/visualizations | Partially update visualization settings
[**partially_update_flow_falcon_attachment_visualization_settings1**](ReportAttachmentsFlowFalconApi.md#partially_update_flow_falcon_attachment_visualization_settings1) | **PATCH** /api/v1/reports/attachments/flow-falcon/{id}/visualizations | Partially update visualization settings
[**update_flow_falcon_attachment_filters**](ReportAttachmentsFlowFalconApi.md#update_flow_falcon_attachment_filters) | **PUT** /api/v2/reports/attachments/flow-falcon/{id}/filters | Update filters
[**update_flow_falcon_attachment_filters1**](ReportAttachmentsFlowFalconApi.md#update_flow_falcon_attachment_filters1) | **PUT** /api/v1/reports/attachments/flow-falcon/{id}/filters | Update filters
[**update_flow_falcon_attachment_resources**](ReportAttachmentsFlowFalconApi.md#update_flow_falcon_attachment_resources) | **PUT** /api/v2/reports/attachments/flow-falcon/{id}/resources | Update resources
[**update_flow_falcon_attachment_resources1**](ReportAttachmentsFlowFalconApi.md#update_flow_falcon_attachment_resources1) | **PUT** /api/v1/reports/attachments/flow-falcon/{id}/resources | Update resources
[**update_flow_falcon_attachment_settings**](ReportAttachmentsFlowFalconApi.md#update_flow_falcon_attachment_settings) | **PUT** /api/v2/reports/attachments/flow-falcon/{id}/settings | Update attachment settings
[**update_flow_falcon_attachment_settings1**](ReportAttachmentsFlowFalconApi.md#update_flow_falcon_attachment_settings1) | **PUT** /api/v1/reports/attachments/flow-falcon/{id}/settings | Update attachment settings
[**update_flow_falcon_attachment_time_settings**](ReportAttachmentsFlowFalconApi.md#update_flow_falcon_attachment_time_settings) | **PUT** /api/v2/reports/attachments/flow-falcon/{id}/time | Update time ranges
[**update_flow_falcon_attachment_time_settings1**](ReportAttachmentsFlowFalconApi.md#update_flow_falcon_attachment_time_settings1) | **PUT** /api/v1/reports/attachments/flow-falcon/{id}/time | Update time ranges
[**update_flow_falcon_attachment_visualization_settings**](ReportAttachmentsFlowFalconApi.md#update_flow_falcon_attachment_visualization_settings) | **PUT** /api/v2/reports/attachments/flow-falcon/{id}/visualizations | Update visualization settings
[**update_flow_falcon_attachment_visualization_settings1**](ReportAttachmentsFlowFalconApi.md#update_flow_falcon_attachment_visualization_settings1) | **PUT** /api/v1/reports/attachments/flow-falcon/{id}/visualizations | Update visualization settings


# **create_flow_falcon_attachment**
> FlowFalconAttachmentDto create_flow_falcon_attachment(id, flow_falcon_request_dto)

Create flow falcon attachment

Create a new flow falcon attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report where the report attachment will be created
flow_falcon_request_dto = swagger_client.FlowFalconRequestDto() # FlowFalconRequestDto | FlowFalcon attachment object

try:
    # Create flow falcon attachment
    api_response = api_instance.create_flow_falcon_attachment(id, flow_falcon_request_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->create_flow_falcon_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report where the report attachment will be created | 
 **flow_falcon_request_dto** | [**FlowFalconRequestDto**](FlowFalconRequestDto.md)| FlowFalcon attachment object | 

### Return type

[**FlowFalconAttachmentDto**](FlowFalconAttachmentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_flow_falcon_attachment1**
> FlowFalconResponseDtoV1 create_flow_falcon_attachment1(id, flow_falcon_request_dto)

Create flow falcon attachment

Create a new flow falcon attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report where the report attachment will be created
flow_falcon_request_dto = swagger_client.FlowFalconRequestDto() # FlowFalconRequestDto | FlowFalcon attachment object

try:
    # Create flow falcon attachment
    api_response = api_instance.create_flow_falcon_attachment1(id, flow_falcon_request_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->create_flow_falcon_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report where the report attachment will be created | 
 **flow_falcon_request_dto** | [**FlowFalconRequestDto**](FlowFalconRequestDto.md)| FlowFalcon attachment object | 

### Return type

[**FlowFalconResponseDtoV1**](FlowFalconResponseDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_falcon_attachment**
> FlowFalconAttachmentDto get_flow_falcon_attachment(id)

Get a flow falcon attachment

Get a flow falcon attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment

try:
    # Get a flow falcon attachment
    api_response = api_instance.get_flow_falcon_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->get_flow_falcon_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**FlowFalconAttachmentDto**](FlowFalconAttachmentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_falcon_attachment_filter_schema**
> FlowFalconAttachmentFiltersSchema get_flow_falcon_attachment_filter_schema()

Gets the filters schema

Gets the filters schema containing available filter fields and values

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()

try:
    # Gets the filters schema
    api_response = api_instance.get_flow_falcon_attachment_filter_schema()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->get_flow_falcon_attachment_filter_schema: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FlowFalconAttachmentFiltersSchema**](FlowFalconAttachmentFiltersSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_falcon_attachment_filter_schema1**
> FlowFalconAttachmentFiltersSchema get_flow_falcon_attachment_filter_schema1()

Gets the filters schema

Gets the filters schema containing available filter fields and values

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()

try:
    # Gets the filters schema
    api_response = api_instance.get_flow_falcon_attachment_filter_schema1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->get_flow_falcon_attachment_filter_schema1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FlowFalconAttachmentFiltersSchema**](FlowFalconAttachmentFiltersSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_falcon_attachment_filters**
> AttachmentFilters get_flow_falcon_attachment_filters(id)

Get filters

Get the report attachment filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment

try:
    # Get filters
    api_response = api_instance.get_flow_falcon_attachment_filters(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->get_flow_falcon_attachment_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**AttachmentFilters**](AttachmentFilters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_falcon_attachment_filters1**
> AttachmentFilters get_flow_falcon_attachment_filters1(id)

Get filters

Get the report attachment filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment

try:
    # Get filters
    api_response = api_instance.get_flow_falcon_attachment_filters1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->get_flow_falcon_attachment_filters1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**AttachmentFilters**](AttachmentFilters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_falcon_attachment_resources**
> FlowFalconResource get_flow_falcon_attachment_resources(id)

Get resources

Get flow falcon resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources
    api_response = api_instance.get_flow_falcon_attachment_resources(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->get_flow_falcon_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**FlowFalconResource**](FlowFalconResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_falcon_attachment_resources1**
> FlowFalconResource get_flow_falcon_attachment_resources1(id)

Get resources

Get flow falcon resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources
    api_response = api_instance.get_flow_falcon_attachment_resources1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->get_flow_falcon_attachment_resources1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**FlowFalconResource**](FlowFalconResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_falcon_attachment_settings**
> FlowFalconSettings get_flow_falcon_attachment_settings(id)

Get attachment settings

Get flow falcon attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment settings
    api_response = api_instance.get_flow_falcon_attachment_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->get_flow_falcon_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**FlowFalconSettings**](FlowFalconSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_falcon_attachment_settings1**
> FlowFalconSettingsV1 get_flow_falcon_attachment_settings1(id)

Get attachment settings

Get flow falcon attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment settings
    api_response = api_instance.get_flow_falcon_attachment_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->get_flow_falcon_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**FlowFalconSettingsV1**](FlowFalconSettingsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_falcon_attachment_time_settings**
> TimeSetting get_flow_falcon_attachment_time_settings(id)

GET time ranges

Get flow falcon time ranges

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment

try:
    # GET time ranges
    api_response = api_instance.get_flow_falcon_attachment_time_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->get_flow_falcon_attachment_time_settings: %s\n" % e)
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

# **get_flow_falcon_attachment_time_settings1**
> TimeSettingV1 get_flow_falcon_attachment_time_settings1(id)

GET time ranges

Get flow falcon time ranges

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment

try:
    # GET time ranges
    api_response = api_instance.get_flow_falcon_attachment_time_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->get_flow_falcon_attachment_time_settings1: %s\n" % e)
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

# **get_flow_falcon_attachment_visualization_settings**
> FlowFalconVisualization get_flow_falcon_attachment_visualization_settings(id)

Get attachment visualization settings

Get flow falcon attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_flow_falcon_attachment_visualization_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->get_flow_falcon_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**FlowFalconVisualization**](FlowFalconVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_falcon_attachment_visualization_settings1**
> FlowFalconVisualizationV1 get_flow_falcon_attachment_visualization_settings1(id)

Get attachment visualization settings

Get flow falcon attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_flow_falcon_attachment_visualization_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->get_flow_falcon_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**FlowFalconVisualizationV1**](FlowFalconVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_flow_falcon_attachment_settings**
> FlowFalconSettings partially_update_flow_falcon_attachment_settings(id, settings)

Partially update attachment settings

Partially update flow falcon attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment
settings = swagger_client.FlowFalconSettings() # FlowFalconSettings | FlowFalcon attachment settings

try:
    # Partially update attachment settings
    api_response = api_instance.partially_update_flow_falcon_attachment_settings(id, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->partially_update_flow_falcon_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **settings** | [**FlowFalconSettings**](FlowFalconSettings.md)| FlowFalcon attachment settings | 

### Return type

[**FlowFalconSettings**](FlowFalconSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_flow_falcon_attachment_settings1**
> FlowFalconSettingsV1 partially_update_flow_falcon_attachment_settings1(id, settings)

Partially update attachment settings

Partially update flow falcon attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment
settings = swagger_client.FlowFalconSettingsV1() # FlowFalconSettingsV1 | FlowFalcon attachment settings

try:
    # Partially update attachment settings
    api_response = api_instance.partially_update_flow_falcon_attachment_settings1(id, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->partially_update_flow_falcon_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **settings** | [**FlowFalconSettingsV1**](FlowFalconSettingsV1.md)| FlowFalcon attachment settings | 

### Return type

[**FlowFalconSettingsV1**](FlowFalconSettingsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_flow_falcon_attachment_visualization_settings**
> FlowFalconVisualization partially_update_flow_falcon_attachment_visualization_settings(id, visualizations)

Partially update visualization settings

Partially update flow falcon visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment
visualizations = swagger_client.FlowFalconVisualization() # FlowFalconVisualization | FlowFalcon attachment visualization settings

try:
    # Partially update visualization settings
    api_response = api_instance.partially_update_flow_falcon_attachment_visualization_settings(id, visualizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->partially_update_flow_falcon_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **visualizations** | [**FlowFalconVisualization**](FlowFalconVisualization.md)| FlowFalcon attachment visualization settings | 

### Return type

[**FlowFalconVisualization**](FlowFalconVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_flow_falcon_attachment_visualization_settings1**
> FlowFalconVisualizationV1 partially_update_flow_falcon_attachment_visualization_settings1(id, visualizations)

Partially update visualization settings

Partially update flow falcon visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment
visualizations = swagger_client.FlowFalconVisualizationV1() # FlowFalconVisualizationV1 | FlowFalcon attachment visualization settings

try:
    # Partially update visualization settings
    api_response = api_instance.partially_update_flow_falcon_attachment_visualization_settings1(id, visualizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->partially_update_flow_falcon_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **visualizations** | [**FlowFalconVisualizationV1**](FlowFalconVisualizationV1.md)| FlowFalcon attachment visualization settings | 

### Return type

[**FlowFalconVisualizationV1**](FlowFalconVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_flow_falcon_attachment_filters**
> AttachmentFilters update_flow_falcon_attachment_filters(id, filters)

Update filters

Updates the report attachment filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment
filters = swagger_client.AttachmentFilters() # AttachmentFilters | Filters that will be updated

try:
    # Update filters
    api_response = api_instance.update_flow_falcon_attachment_filters(id, filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->update_flow_falcon_attachment_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **filters** | [**AttachmentFilters**](AttachmentFilters.md)| Filters that will be updated | 

### Return type

[**AttachmentFilters**](AttachmentFilters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_flow_falcon_attachment_filters1**
> AttachmentFilters update_flow_falcon_attachment_filters1(id, filters)

Update filters

Updates the report attachment filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment
filters = swagger_client.AttachmentFilters() # AttachmentFilters | Filters that will be updated

try:
    # Update filters
    api_response = api_instance.update_flow_falcon_attachment_filters1(id, filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->update_flow_falcon_attachment_filters1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **filters** | [**AttachmentFilters**](AttachmentFilters.md)| Filters that will be updated | 

### Return type

[**AttachmentFilters**](AttachmentFilters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_flow_falcon_attachment_resources**
> FlowFalconResource update_flow_falcon_attachment_resources(id, resources)

Update resources

Update flow falcon resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment
resources = swagger_client.FlowFalconResource() # FlowFalconResource | FlowFalcon attachment resources

try:
    # Update resources
    api_response = api_instance.update_flow_falcon_attachment_resources(id, resources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->update_flow_falcon_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **resources** | [**FlowFalconResource**](FlowFalconResource.md)| FlowFalcon attachment resources | 

### Return type

[**FlowFalconResource**](FlowFalconResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_flow_falcon_attachment_resources1**
> FlowFalconResource update_flow_falcon_attachment_resources1(id, resources)

Update resources

Update flow falcon resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment
resources = swagger_client.FlowFalconResource() # FlowFalconResource | FlowFalcon attachment resources

try:
    # Update resources
    api_response = api_instance.update_flow_falcon_attachment_resources1(id, resources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->update_flow_falcon_attachment_resources1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **resources** | [**FlowFalconResource**](FlowFalconResource.md)| FlowFalcon attachment resources | 

### Return type

[**FlowFalconResource**](FlowFalconResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_flow_falcon_attachment_settings**
> FlowFalconSettings update_flow_falcon_attachment_settings(id, settings)

Update attachment settings

Update flow falcon attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment
settings = swagger_client.FlowFalconSettings() # FlowFalconSettings | FlowFalcon attachment settings

try:
    # Update attachment settings
    api_response = api_instance.update_flow_falcon_attachment_settings(id, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->update_flow_falcon_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **settings** | [**FlowFalconSettings**](FlowFalconSettings.md)| FlowFalcon attachment settings | 

### Return type

[**FlowFalconSettings**](FlowFalconSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_flow_falcon_attachment_settings1**
> FlowFalconSettingsV1 update_flow_falcon_attachment_settings1(id, settings)

Update attachment settings

Update flow falcon attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment
settings = swagger_client.FlowFalconSettingsV1() # FlowFalconSettingsV1 | FlowFalcon attachment settings

try:
    # Update attachment settings
    api_response = api_instance.update_flow_falcon_attachment_settings1(id, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->update_flow_falcon_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **settings** | [**FlowFalconSettingsV1**](FlowFalconSettingsV1.md)| FlowFalcon attachment settings | 

### Return type

[**FlowFalconSettingsV1**](FlowFalconSettingsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_flow_falcon_attachment_time_settings**
> TimeSetting update_flow_falcon_attachment_time_settings(id, time)

Update time ranges

Update flow falcon time ranges

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment
time = swagger_client.TimeSetting() # TimeSetting | FlowFalcon attachment time settings

try:
    # Update time ranges
    api_response = api_instance.update_flow_falcon_attachment_time_settings(id, time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->update_flow_falcon_attachment_time_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **time** | [**TimeSetting**](TimeSetting.md)| FlowFalcon attachment time settings | 

### Return type

[**TimeSetting**](TimeSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_flow_falcon_attachment_time_settings1**
> TimeSettingV1 update_flow_falcon_attachment_time_settings1(id, time)

Update time ranges

Update flow falcon time ranges

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment
time = swagger_client.TimeSettingV1() # TimeSettingV1 | FlowFalcon attachment time settings

try:
    # Update time ranges
    api_response = api_instance.update_flow_falcon_attachment_time_settings1(id, time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->update_flow_falcon_attachment_time_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **time** | [**TimeSettingV1**](TimeSettingV1.md)| FlowFalcon attachment time settings | 

### Return type

[**TimeSettingV1**](TimeSettingV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_flow_falcon_attachment_visualization_settings**
> FlowFalconVisualization update_flow_falcon_attachment_visualization_settings(id, visualizations)

Update visualization settings

Update flow falcon visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment
visualizations = swagger_client.FlowFalconVisualization() # FlowFalconVisualization | FlowFalcon attachment visualization settings

try:
    # Update visualization settings
    api_response = api_instance.update_flow_falcon_attachment_visualization_settings(id, visualizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->update_flow_falcon_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **visualizations** | [**FlowFalconVisualization**](FlowFalconVisualization.md)| FlowFalcon attachment visualization settings | 

### Return type

[**FlowFalconVisualization**](FlowFalconVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_flow_falcon_attachment_visualization_settings1**
> FlowFalconVisualizationV1 update_flow_falcon_attachment_visualization_settings1(id, visualizations)

Update visualization settings

Update flow falcon visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsFlowFalconApi()
id = 789 # int | The id of the report attachment
visualizations = swagger_client.FlowFalconVisualizationV1() # FlowFalconVisualizationV1 | FlowFalcon attachment visualization settings

try:
    # Update visualization settings
    api_response = api_instance.update_flow_falcon_attachment_visualization_settings1(id, visualizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsFlowFalconApi->update_flow_falcon_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **visualizations** | [**FlowFalconVisualizationV1**](FlowFalconVisualizationV1.md)| FlowFalcon attachment visualization settings | 

### Return type

[**FlowFalconVisualizationV1**](FlowFalconVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

