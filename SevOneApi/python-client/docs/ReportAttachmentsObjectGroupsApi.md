# swagger_client.ReportAttachmentsObjectGroupsApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_object_group_attachment**](ReportAttachmentsObjectGroupsApi.md#create_object_group_attachment) | **POST** /api/v2/reports/{id}/attachments/object-groups | Create object group attachment
[**create_object_group_attachment1**](ReportAttachmentsObjectGroupsApi.md#create_object_group_attachment1) | **POST** /api/v1/reports/{id}/attachments/object-groups | Create object group attachment
[**get_object_group_attachment**](ReportAttachmentsObjectGroupsApi.md#get_object_group_attachment) | **GET** /api/v2/reports/attachments/object-groups/{id} | Get object group attachment
[**get_object_group_attachment_resources**](ReportAttachmentsObjectGroupsApi.md#get_object_group_attachment_resources) | **GET** /api/v2/reports/attachments/object-groups/{id}/resources | Get resources
[**get_object_group_attachment_resources1**](ReportAttachmentsObjectGroupsApi.md#get_object_group_attachment_resources1) | **GET** /api/v1/reports/attachments/object-groups/{id}/resources | Get resources
[**get_object_group_attachment_visualization_settings**](ReportAttachmentsObjectGroupsApi.md#get_object_group_attachment_visualization_settings) | **GET** /api/v2/reports/attachments/object-groups/{id}/visualizations | Get attachment visualization settings
[**get_object_group_attachment_visualization_settings1**](ReportAttachmentsObjectGroupsApi.md#get_object_group_attachment_visualization_settings1) | **GET** /api/v1/reports/attachments/object-groups/{id}/visualizations | Get attachment visualization settings
[**partially_update_object_group_attachment_visualization_settings**](ReportAttachmentsObjectGroupsApi.md#partially_update_object_group_attachment_visualization_settings) | **PATCH** /api/v2/reports/attachments/object-groups/{id}/visualizations | Partially update visualization settings
[**partially_update_object_group_attachment_visualization_settings1**](ReportAttachmentsObjectGroupsApi.md#partially_update_object_group_attachment_visualization_settings1) | **PATCH** /api/v1/reports/attachments/object-groups/{id}/visualizations | Partially update visualization settings
[**update_object_group_attachment_resources**](ReportAttachmentsObjectGroupsApi.md#update_object_group_attachment_resources) | **PUT** /api/v2/reports/attachments/object-groups/{id}/resources | Update resources
[**update_object_group_attachment_resources1**](ReportAttachmentsObjectGroupsApi.md#update_object_group_attachment_resources1) | **PUT** /api/v1/reports/attachments/object-groups/{id}/resources | Update resources
[**update_object_group_attachment_visualization_settings**](ReportAttachmentsObjectGroupsApi.md#update_object_group_attachment_visualization_settings) | **PUT** /api/v2/reports/attachments/object-groups/{id}/visualizations | Update visualization settings
[**update_object_group_attachment_visualization_settings1**](ReportAttachmentsObjectGroupsApi.md#update_object_group_attachment_visualization_settings1) | **PUT** /api/v1/reports/attachments/object-groups/{id}/visualizations | Update visualization settings


# **create_object_group_attachment**
> ObjectGroupAttachmentResponseDto create_object_group_attachment(id, object_group_attachment)

Create object group attachment

Create a new object group attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | The id of the report where the report attachment will be created
object_group_attachment = swagger_client.ObjectGroupAttachmentRequestDto() # ObjectGroupAttachmentRequestDto | Object group report attachment

try:
    # Create object group attachment
    api_response = api_instance.create_object_group_attachment(id, object_group_attachment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->create_object_group_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report where the report attachment will be created | 
 **object_group_attachment** | [**ObjectGroupAttachmentRequestDto**](ObjectGroupAttachmentRequestDto.md)| Object group report attachment | 

### Return type

[**ObjectGroupAttachmentResponseDto**](ObjectGroupAttachmentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_object_group_attachment1**
> ObjectGroupAttachmentResponseDtoV1 create_object_group_attachment1(id, object_group_attachment)

Create object group attachment

Create a new object group attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | The id of the report where the report attachment will be created
object_group_attachment = swagger_client.ObjectGroupAttachmentRequestDtoV1() # ObjectGroupAttachmentRequestDtoV1 | Object group report attachment

try:
    # Create object group attachment
    api_response = api_instance.create_object_group_attachment1(id, object_group_attachment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->create_object_group_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report where the report attachment will be created | 
 **object_group_attachment** | [**ObjectGroupAttachmentRequestDtoV1**](ObjectGroupAttachmentRequestDtoV1.md)| Object group report attachment | 

### Return type

[**ObjectGroupAttachmentResponseDtoV1**](ObjectGroupAttachmentResponseDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group_attachment**
> ObjectGroupAttachmentResponseDto get_object_group_attachment(id)

Get object group attachment

Get an existing object group attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | Object group attachment id

try:
    # Get object group attachment
    api_response = api_instance.get_object_group_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->get_object_group_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Object group attachment id | 

### Return type

[**ObjectGroupAttachmentResponseDto**](ObjectGroupAttachmentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group_attachment_resources**
> ObjectGroupAttachmentResource get_object_group_attachment_resources(id)

Get resources

Get object group resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources
    api_response = api_instance.get_object_group_attachment_resources(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->get_object_group_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectGroupAttachmentResource**](ObjectGroupAttachmentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group_attachment_resources1**
> ObjectGroupAttachmentResourceV1 get_object_group_attachment_resources1(id)

Get resources

Get object group resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources
    api_response = api_instance.get_object_group_attachment_resources1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->get_object_group_attachment_resources1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectGroupAttachmentResourceV1**](ObjectGroupAttachmentResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group_attachment_visualization_settings**
> ObjectGroupAttachmentVisualization get_object_group_attachment_visualization_settings(id)

Get attachment visualization settings

Get object group attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_object_group_attachment_visualization_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->get_object_group_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectGroupAttachmentVisualization**](ObjectGroupAttachmentVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_group_attachment_visualization_settings1**
> ObjectGroupAttachmentVisualizationV1 get_object_group_attachment_visualization_settings1(id)

Get attachment visualization settings

Get object group attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_object_group_attachment_visualization_settings1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->get_object_group_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**ObjectGroupAttachmentVisualizationV1**](ObjectGroupAttachmentVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_object_group_attachment_visualization_settings**
> ObjectGroupAttachmentVisualization partially_update_object_group_attachment_visualization_settings(id, visualizations)

Partially update visualization settings

Partially update object group visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | The id of the report attachment
visualizations = swagger_client.ObjectGroupAttachmentVisualization() # ObjectGroupAttachmentVisualization | Object group visualization settings

try:
    # Partially update visualization settings
    api_response = api_instance.partially_update_object_group_attachment_visualization_settings(id, visualizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->partially_update_object_group_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **visualizations** | [**ObjectGroupAttachmentVisualization**](ObjectGroupAttachmentVisualization.md)| Object group visualization settings | 

### Return type

[**ObjectGroupAttachmentVisualization**](ObjectGroupAttachmentVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_object_group_attachment_visualization_settings1**
> ObjectGroupAttachmentVisualizationV1 partially_update_object_group_attachment_visualization_settings1(id, visualizations)

Partially update visualization settings

Partially update object group visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | The id of the report attachment
visualizations = swagger_client.ObjectGroupAttachmentVisualizationV1() # ObjectGroupAttachmentVisualizationV1 | Object group visualization settings

try:
    # Partially update visualization settings
    api_response = api_instance.partially_update_object_group_attachment_visualization_settings1(id, visualizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->partially_update_object_group_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **visualizations** | [**ObjectGroupAttachmentVisualizationV1**](ObjectGroupAttachmentVisualizationV1.md)| Object group visualization settings | 

### Return type

[**ObjectGroupAttachmentVisualizationV1**](ObjectGroupAttachmentVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_group_attachment_resources**
> ObjectGroupAttachmentResource update_object_group_attachment_resources(id, resources)

Update resources

Update object group resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | The id of the report attachment
resources = swagger_client.ObjectGroupAttachmentResource() # ObjectGroupAttachmentResource | Object group attachment resources

try:
    # Update resources
    api_response = api_instance.update_object_group_attachment_resources(id, resources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->update_object_group_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **resources** | [**ObjectGroupAttachmentResource**](ObjectGroupAttachmentResource.md)| Object group attachment resources | 

### Return type

[**ObjectGroupAttachmentResource**](ObjectGroupAttachmentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_group_attachment_resources1**
> ObjectGroupAttachmentResourceV1 update_object_group_attachment_resources1(id, resources)

Update resources

Update object group resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | The id of the report attachment
resources = swagger_client.ObjectGroupAttachmentResourceV1() # ObjectGroupAttachmentResourceV1 | Object group attachment resources

try:
    # Update resources
    api_response = api_instance.update_object_group_attachment_resources1(id, resources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->update_object_group_attachment_resources1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **resources** | [**ObjectGroupAttachmentResourceV1**](ObjectGroupAttachmentResourceV1.md)| Object group attachment resources | 

### Return type

[**ObjectGroupAttachmentResourceV1**](ObjectGroupAttachmentResourceV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_group_attachment_visualization_settings**
> ObjectGroupAttachmentVisualization update_object_group_attachment_visualization_settings(id, visualizations)

Update visualization settings

Update object group visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | The id of the report attachment
visualizations = swagger_client.ObjectGroupAttachmentVisualization() # ObjectGroupAttachmentVisualization | Object group visualization settings

try:
    # Update visualization settings
    api_response = api_instance.update_object_group_attachment_visualization_settings(id, visualizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->update_object_group_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **visualizations** | [**ObjectGroupAttachmentVisualization**](ObjectGroupAttachmentVisualization.md)| Object group visualization settings | 

### Return type

[**ObjectGroupAttachmentVisualization**](ObjectGroupAttachmentVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_object_group_attachment_visualization_settings1**
> ObjectGroupAttachmentVisualizationV1 update_object_group_attachment_visualization_settings1(id, visualizations)

Update visualization settings

Update object group visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsObjectGroupsApi()
id = 789 # int | The id of the report attachment
visualizations = swagger_client.ObjectGroupAttachmentVisualizationV1() # ObjectGroupAttachmentVisualizationV1 | Object group visualization settings

try:
    # Update visualization settings
    api_response = api_instance.update_object_group_attachment_visualization_settings1(id, visualizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsObjectGroupsApi->update_object_group_attachment_visualization_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **visualizations** | [**ObjectGroupAttachmentVisualizationV1**](ObjectGroupAttachmentVisualizationV1.md)| Object group visualization settings | 

### Return type

[**ObjectGroupAttachmentVisualizationV1**](ObjectGroupAttachmentVisualizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

