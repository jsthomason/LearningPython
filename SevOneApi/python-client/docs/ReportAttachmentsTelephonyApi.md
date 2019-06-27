# swagger_client.ReportAttachmentsTelephonyApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_telephony_attachment**](ReportAttachmentsTelephonyApi.md#create_telephony_attachment) | **POST** /api/v2/reports/{id}/attachments/telephony | Create telephony report attachment
[**create_telephony_attachment1**](ReportAttachmentsTelephonyApi.md#create_telephony_attachment1) | **POST** /api/v1/reports/{id}/attachments/telephony | Create telephony report attachment
[**get_telephony_attachment**](ReportAttachmentsTelephonyApi.md#get_telephony_attachment) | **GET** /api/v2/reports/attachments/telephony/{id} | Get telephony attachment
[**get_telephony_attachment_aggregation**](ReportAttachmentsTelephonyApi.md#get_telephony_attachment_aggregation) | **GET** /api/v2/reports/attachments/telephony/{id}/aggregation | Get attachment aggregation
[**get_telephony_attachment_aggregation1**](ReportAttachmentsTelephonyApi.md#get_telephony_attachment_aggregation1) | **GET** /api/v1/reports/attachments/telephony/{id}/aggregation | Get attachment aggregation
[**get_telephony_attachment_settings**](ReportAttachmentsTelephonyApi.md#get_telephony_attachment_settings) | **GET** /api/v2/reports/attachments/telephony/{id}/settings | Get attachment settings
[**get_telephony_attachment_settings1**](ReportAttachmentsTelephonyApi.md#get_telephony_attachment_settings1) | **GET** /api/v1/reports/attachments/telephony/{id}/settings | Get attachment settings
[**get_telephony_attachment_time_settings**](ReportAttachmentsTelephonyApi.md#get_telephony_attachment_time_settings) | **GET** /api/v2/reports/attachments/telephony/{id}/time | Get telephony attachment time settings
[**get_telephony_attachment_time_settings1**](ReportAttachmentsTelephonyApi.md#get_telephony_attachment_time_settings1) | **GET** /api/v1/reports/attachments/telephony/{id}/time | Get telephony attachment time settings
[**get_telephony_attachment_visualization_settings**](ReportAttachmentsTelephonyApi.md#get_telephony_attachment_visualization_settings) | **GET** /api/v2/reports/attachments/telephony/{id}/visualizations | Get attachment visualization settings
[**get_telephony_attachment_visualization_settings1**](ReportAttachmentsTelephonyApi.md#get_telephony_attachment_visualization_settings1) | **GET** /api/v1/reports/attachments/telephony/{id}/visualizations | Get attachment visualization settings
[**update_telephony_attachment_aggregation**](ReportAttachmentsTelephonyApi.md#update_telephony_attachment_aggregation) | **PUT** /api/v2/reports/attachments/telephony/{id}/aggregation | Update attachment aggregation
[**update_telephony_attachment_aggregation1**](ReportAttachmentsTelephonyApi.md#update_telephony_attachment_aggregation1) | **PUT** /api/v1/reports/attachments/telephony/{id}/aggregation | Update attachment aggregation
[**update_telephony_attachment_settings**](ReportAttachmentsTelephonyApi.md#update_telephony_attachment_settings) | **PUT** /api/v2/reports/attachments/telephony/{id}/settings | Update attachment settings
[**update_telephony_attachment_settings1**](ReportAttachmentsTelephonyApi.md#update_telephony_attachment_settings1) | **PUT** /api/v1/reports/attachments/telephony/{id}/settings | Update attachment settings
[**update_telephony_attachment_time_settings**](ReportAttachmentsTelephonyApi.md#update_telephony_attachment_time_settings) | **PUT** /api/v2/reports/attachments/telephony/{id}/time | Update telephony attachment time settings
[**update_telephony_attachment_time_settings1**](ReportAttachmentsTelephonyApi.md#update_telephony_attachment_time_settings1) | **PUT** /api/v1/reports/attachments/telephony/{id}/time | Update telephony attachment time settings
[**update_telephony_attachment_visualization_settings**](ReportAttachmentsTelephonyApi.md#update_telephony_attachment_visualization_settings) | **PUT** /api/v2/reports/attachments/telephony/{id}/visualizations | Update visualization settings
[**update_telephony_attachment_visualization_settings1**](ReportAttachmentsTelephonyApi.md#update_telephony_attachment_visualization_settings1) | **PUT** /api/v1/reports/attachments/telephony/{id}/visualizations | Update visualization settings


# **create_telephony_attachment**
> TelephonyAttachmentResponseDto create_telephony_attachment(id, request_dto)

Create telephony report attachment

Creates a new telephony report attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report where the report attachment will be created
request_dto = swagger_client.TelephonyAttachmentRequestDto() # TelephonyAttachmentRequestDto | Telephony attachment object

try:
    # Create telephony report attachment
    api_response = api_instance.create_telephony_attachment(id, request_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->create_telephony_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report where the report attachment will be created | 
 **request_dto** | [**TelephonyAttachmentRequestDto**](TelephonyAttachmentRequestDto.md)| Telephony attachment object | 

### Return type

[**TelephonyAttachmentResponseDto**](TelephonyAttachmentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_telephony_attachment1**
> TelephonyAttachmentResponseDtoV1 create_telephony_attachment1(id, request_dto)

Create telephony report attachment

Creates a new telephony report attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report where the report attachment will be created
request_dto = swagger_client.TelephonyAttachmentRequestDtoV1() # TelephonyAttachmentRequestDtoV1 | Telephony attachment object

try:
    # Create telephony report attachment
    api_response = api_instance.create_telephony_attachment1(id, request_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->create_telephony_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report where the report attachment will be created | 
 **request_dto** | [**TelephonyAttachmentRequestDtoV1**](TelephonyAttachmentRequestDtoV1.md)| Telephony attachment object | 

### Return type

[**TelephonyAttachmentResponseDtoV1**](TelephonyAttachmentResponseDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_telephony_attachment**
> TelephonyAttachmentResponseDto get_telephony_attachment(id)

Get telephony attachment

Get an existing telephony attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | Telephony attachment id

try:
    # Get telephony attachment
    api_response = api_instance.get_telephony_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->get_telephony_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Telephony attachment id | 

### Return type

[**TelephonyAttachmentResponseDto**](TelephonyAttachmentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_telephony_attachment_aggregation**
> TelephonyAttachmentAggregation get_telephony_attachment_aggregation(id)

Get attachment aggregation

Get telephony attachment aggregation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment aggregation
    api_response = api_instance.get_telephony_attachment_aggregation(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->get_telephony_attachment_aggregation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TelephonyAttachmentAggregation**](TelephonyAttachmentAggregation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_telephony_attachment_aggregation1**
> TelephonyAttachmentAggregationV1 get_telephony_attachment_aggregation1(id)

Get attachment aggregation

Get telephony attachment aggregation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment aggregation
    api_response = api_instance.get_telephony_attachment_aggregation1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->get_telephony_attachment_aggregation1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TelephonyAttachmentAggregationV1**](TelephonyAttachmentAggregationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_telephony_attachment_settings**
> TelephonyAttachmentSettings get_telephony_attachment_settings(id)

Get attachment settings

Get telephony attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment settings
    api_response = api_instance.get_telephony_attachment_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->get_telephony_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TelephonyAttachmentSettings**](TelephonyAttachmentSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_telephony_attachment_settings1**
> TelephonyAttachmentSettingsV1 get_telephony_attachment_settings1(id)

Get attachment settings

Get telephony attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment settings
    api_response = api_instance.get_telephony_attachment_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->get_telephony_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TelephonyAttachmentSettingsV1**](TelephonyAttachmentSettingsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_telephony_attachment_time_settings**
> TimeSetting get_telephony_attachment_time_settings(id)

Get telephony attachment time settings

Get telephony attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report attachment

try:
    # Get telephony attachment time settings
    api_response = api_instance.get_telephony_attachment_time_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->get_telephony_attachment_time_settings: %s\n" % e)
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

# **get_telephony_attachment_time_settings1**
> TimeSettingV1 get_telephony_attachment_time_settings1(id)

Get telephony attachment time settings

Get telephony attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report attachment

try:
    # Get telephony attachment time settings
    api_response = api_instance.get_telephony_attachment_time_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->get_telephony_attachment_time_settings1: %s\n" % e)
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

# **get_telephony_attachment_visualization_settings**
> TelephonyAttachmentVisualization get_telephony_attachment_visualization_settings(id)

Get attachment visualization settings

Get telephony attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_telephony_attachment_visualization_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->get_telephony_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TelephonyAttachmentVisualization**](TelephonyAttachmentVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_telephony_attachment_visualization_settings1**
> TelephonyAttachmentVisualizationV1 get_telephony_attachment_visualization_settings1(id)

Get attachment visualization settings

Get telephony attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_telephony_attachment_visualization_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->get_telephony_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TelephonyAttachmentVisualizationV1**](TelephonyAttachmentVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_telephony_attachment_aggregation**
> TelephonyAttachmentAggregation update_telephony_attachment_aggregation(id, aggregation)

Update attachment aggregation

Update telephony attachment aggregation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report attachment
aggregation = swagger_client.TelephonyAttachmentAggregation() # TelephonyAttachmentAggregation | Telephony attachment aggregation that will be updated

try:
    # Update attachment aggregation
    api_response = api_instance.update_telephony_attachment_aggregation(id, aggregation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->update_telephony_attachment_aggregation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **aggregation** | [**TelephonyAttachmentAggregation**](TelephonyAttachmentAggregation.md)| Telephony attachment aggregation that will be updated | 

### Return type

[**TelephonyAttachmentAggregation**](TelephonyAttachmentAggregation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_telephony_attachment_aggregation1**
> TelephonyAttachmentAggregationV1 update_telephony_attachment_aggregation1(id, aggregation)

Update attachment aggregation

Update telephony attachment aggregation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report attachment
aggregation = swagger_client.TelephonyAttachmentAggregationV1() # TelephonyAttachmentAggregationV1 | Telephony attachment aggregation that will be updated

try:
    # Update attachment aggregation
    api_response = api_instance.update_telephony_attachment_aggregation1(id, aggregation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->update_telephony_attachment_aggregation1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **aggregation** | [**TelephonyAttachmentAggregationV1**](TelephonyAttachmentAggregationV1.md)| Telephony attachment aggregation that will be updated | 

### Return type

[**TelephonyAttachmentAggregationV1**](TelephonyAttachmentAggregationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_telephony_attachment_settings**
> TelephonyAttachmentSettings update_telephony_attachment_settings(id, settings)

Update attachment settings

Update telephony attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report attachment
settings = swagger_client.TelephonyAttachmentSettings() # TelephonyAttachmentSettings | Telephony attachment settings

try:
    # Update attachment settings
    api_response = api_instance.update_telephony_attachment_settings(id, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->update_telephony_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **settings** | [**TelephonyAttachmentSettings**](TelephonyAttachmentSettings.md)| Telephony attachment settings | 

### Return type

[**TelephonyAttachmentSettings**](TelephonyAttachmentSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_telephony_attachment_settings1**
> TelephonyAttachmentSettingsV1 update_telephony_attachment_settings1(id, settings)

Update attachment settings

Update telephony attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report attachment
settings = swagger_client.TelephonyAttachmentSettingsV1() # TelephonyAttachmentSettingsV1 | Telephony attachment settings

try:
    # Update attachment settings
    api_response = api_instance.update_telephony_attachment_settings1(id, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->update_telephony_attachment_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **settings** | [**TelephonyAttachmentSettingsV1**](TelephonyAttachmentSettingsV1.md)| Telephony attachment settings | 

### Return type

[**TelephonyAttachmentSettingsV1**](TelephonyAttachmentSettingsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_telephony_attachment_time_settings**
> TimeSetting update_telephony_attachment_time_settings(id, time_setting)

Update telephony attachment time settings

Update telephony attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report attachment
time_setting = swagger_client.TimeSetting() # TimeSetting | Telephony attachment time settings

try:
    # Update telephony attachment time settings
    api_response = api_instance.update_telephony_attachment_time_settings(id, time_setting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->update_telephony_attachment_time_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **time_setting** | [**TimeSetting**](TimeSetting.md)| Telephony attachment time settings | 

### Return type

[**TimeSetting**](TimeSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_telephony_attachment_time_settings1**
> TimeSettingV1 update_telephony_attachment_time_settings1(id, time_setting)

Update telephony attachment time settings

Update telephony attachment time settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report attachment
time_setting = swagger_client.TimeSettingV1() # TimeSettingV1 | Telephony attachment time settings

try:
    # Update telephony attachment time settings
    api_response = api_instance.update_telephony_attachment_time_settings1(id, time_setting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->update_telephony_attachment_time_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **time_setting** | [**TimeSettingV1**](TimeSettingV1.md)| Telephony attachment time settings | 

### Return type

[**TimeSettingV1**](TimeSettingV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_telephony_attachment_visualization_settings**
> TelephonyAttachmentVisualization update_telephony_attachment_visualization_settings(id, visualizations)

Update visualization settings

Update telephony attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report attachment
visualizations = swagger_client.TelephonyAttachmentVisualization() # TelephonyAttachmentVisualization | Telephony attachment visualization settings

try:
    # Update visualization settings
    api_response = api_instance.update_telephony_attachment_visualization_settings(id, visualizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->update_telephony_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **visualizations** | [**TelephonyAttachmentVisualization**](TelephonyAttachmentVisualization.md)| Telephony attachment visualization settings | 

### Return type

[**TelephonyAttachmentVisualization**](TelephonyAttachmentVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_telephony_attachment_visualization_settings1**
> TelephonyAttachmentVisualizationV1 update_telephony_attachment_visualization_settings1(id, visualizations)

Update visualization settings

Update telephony attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTelephonyApi()
id = 789 # int | The id of the report attachment
visualizations = swagger_client.TelephonyAttachmentVisualizationV1() # TelephonyAttachmentVisualizationV1 | Telephony attachment visualization settings

try:
    # Update visualization settings
    api_response = api_instance.update_telephony_attachment_visualization_settings1(id, visualizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTelephonyApi->update_telephony_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **visualizations** | [**TelephonyAttachmentVisualizationV1**](TelephonyAttachmentVisualizationV1.md)| Telephony attachment visualization settings | 

### Return type

[**TelephonyAttachmentVisualizationV1**](TelephonyAttachmentVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

