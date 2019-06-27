# swagger_client.ReportAttachmentsApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_report_attachment**](ReportAttachmentsApi.md#delete_report_attachment) | **DELETE** /api/v1/reports/attachments/{id} | Delete report attachment
[**delete_report_attachment1**](ReportAttachmentsApi.md#delete_report_attachment1) | **DELETE** /api/v2/reports/attachments/{id} | Delete report attachment
[**get_all_report_attachment_endpoints**](ReportAttachmentsApi.md#get_all_report_attachment_endpoints) | **GET** /api/v1/reports/attachments/{type}/endpoints | Get all report attachments endpoints
[**get_all_report_attachment_endpoints1**](ReportAttachmentsApi.md#get_all_report_attachment_endpoints1) | **GET** /api/v2/reports/attachments/{type}/endpoints | Get all report attachments endpoints
[**get_all_report_attachments**](ReportAttachmentsApi.md#get_all_report_attachments) | **GET** /api/v1/reports/{id}/attachments | Get all report attachments for a report
[**get_all_report_attachments1**](ReportAttachmentsApi.md#get_all_report_attachments1) | **GET** /api/v2/reports/{id}/attachments | Get all report attachments for a report
[**get_report_attachment**](ReportAttachmentsApi.md#get_report_attachment) | **GET** /api/v1/reports/attachments/{id} | Get report attachment
[**get_report_attachment1**](ReportAttachmentsApi.md#get_report_attachment1) | **GET** /api/v2/reports/attachments/{id} | Get report attachment
[**update_report_attachment_by_id**](ReportAttachmentsApi.md#update_report_attachment_by_id) | **PUT** /api/v1/reports/attachments/{id} | Update report attachment
[**update_report_attachment_by_id1**](ReportAttachmentsApi.md#update_report_attachment_by_id1) | **PUT** /api/v2/reports/attachments/{id} | Update report attachment


# **delete_report_attachment**
> ResponseEntity delete_report_attachment(id)

Delete report attachment

Deletes an existing report attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsApi()
id = 789 # int | The id of the reportAttachment to be deleted

try:
    # Delete report attachment
    api_response = api_instance.delete_report_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsApi->delete_report_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the reportAttachment to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report_attachment1**
> ResponseEntity delete_report_attachment1(id)

Delete report attachment

Deletes an existing report attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsApi()
id = 789 # int | The id of the reportAttachment to be deleted

try:
    # Delete report attachment
    api_response = api_instance.delete_report_attachment1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsApi->delete_report_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the reportAttachment to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_report_attachment_endpoints**
> dict(str, EndpointDto) get_all_report_attachment_endpoints(type)

Get all report attachments endpoints

Endpoint for retrieving all report attachment endpoints

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsApi()
type = 'type_example' # str | Attachment type

try:
    # Get all report attachments endpoints
    api_response = api_instance.get_all_report_attachment_endpoints(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsApi->get_all_report_attachment_endpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Attachment type | 

### Return type

[**dict(str, EndpointDto)**](EndpointDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_report_attachment_endpoints1**
> dict(str, EndpointDto) get_all_report_attachment_endpoints1(type)

Get all report attachments endpoints

Endpoint for retrieving all report attachment endpoints

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsApi()
type = 'type_example' # str | Attachment type

try:
    # Get all report attachments endpoints
    api_response = api_instance.get_all_report_attachment_endpoints1(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsApi->get_all_report_attachment_endpoints1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Attachment type | 

### Return type

[**dict(str, EndpointDto)**](EndpointDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_report_attachments**
> PagerAttachmentDto get_all_report_attachments(id, page=page, size=size)

Get all report attachments for a report

Endpoint for retrieving all report attachments for a  specific report, supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsApi()
id = 789 # int | Report Id
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)

try:
    # Get all report attachments for a report
    api_response = api_instance.get_all_report_attachments(id, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsApi->get_all_report_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Report Id | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]

### Return type

[**PagerAttachmentDto**](PagerAttachmentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_report_attachments1**
> PagerAttachmentDto get_all_report_attachments1(id, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all report attachments for a report

Endpoint for retrieving all report attachments for a  specific report, supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsApi()
id = 789 # int | Report Id
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all report attachments for a report
    api_response = api_instance.get_all_report_attachments1(id, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsApi->get_all_report_attachments1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Report Id | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerAttachmentDto**](PagerAttachmentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_attachment**
> AttachmentDto get_report_attachment(id)

Get report attachment

Endpoint for retrieving all report attachment info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsApi()
id = 789 # int | Attachment Id

try:
    # Get report attachment
    api_response = api_instance.get_report_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsApi->get_report_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Attachment Id | 

### Return type

[**AttachmentDto**](AttachmentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_attachment1**
> AttachmentDto get_report_attachment1(id)

Get report attachment

Endpoint for retrieving all report attachment info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsApi()
id = 789 # int | Attachment Id

try:
    # Get report attachment
    api_response = api_instance.get_report_attachment1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsApi->get_report_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Attachment Id | 

### Return type

[**AttachmentDto**](AttachmentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_attachment_by_id**
> AttachmentDto update_report_attachment_by_id(id, dto)

Update report attachment

Updates an existing report attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsApi()
id = 789 # int | The id of the reportAttachment to be updated
dto = swagger_client.AttachmentDto() # AttachmentDto | Report attachment to be updated

try:
    # Update report attachment
    api_response = api_instance.update_report_attachment_by_id(id, dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsApi->update_report_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the reportAttachment to be updated | 
 **dto** | [**AttachmentDto**](AttachmentDto.md)| Report attachment to be updated | 

### Return type

[**AttachmentDto**](AttachmentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_attachment_by_id1**
> AttachmentDto update_report_attachment_by_id1(id, dto)

Update report attachment

Updates an existing report attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsApi()
id = 789 # int | The id of the reportAttachment to be updated
dto = swagger_client.AttachmentDto() # AttachmentDto | Report attachment to be updated

try:
    # Update report attachment
    api_response = api_instance.update_report_attachment_by_id1(id, dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsApi->update_report_attachment_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the reportAttachment to be updated | 
 **dto** | [**AttachmentDto**](AttachmentDto.md)| Report attachment to be updated | 

### Return type

[**AttachmentDto**](AttachmentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

