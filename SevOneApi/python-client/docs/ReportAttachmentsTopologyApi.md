# swagger_client.ReportAttachmentsTopologyApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_topology_attachment**](ReportAttachmentsTopologyApi.md#create_topology_attachment) | **POST** /api/v2/reports/{id}/attachments/topology | Create topology attachment
[**get_topology_attachment**](ReportAttachmentsTopologyApi.md#get_topology_attachment) | **GET** /api/v2/reports/attachments/topology/{id} | Get topology attachment
[**get_topology_attachment_filters**](ReportAttachmentsTopologyApi.md#get_topology_attachment_filters) | **GET** /api/v2/reports/attachments/topology/{id}/filters | Get attachment topology filters
[**get_topology_attachment_resources**](ReportAttachmentsTopologyApi.md#get_topology_attachment_resources) | **GET** /api/v2/reports/attachments/topology/{id}/resources | Get resources
[**get_topology_attachment_settings**](ReportAttachmentsTopologyApi.md#get_topology_attachment_settings) | **GET** /api/v2/reports/attachments/topology/{id}/settings | Get attachment settings
[**get_topology_attachment_visualization_settings**](ReportAttachmentsTopologyApi.md#get_topology_attachment_visualization_settings) | **GET** /api/v2/reports/attachments/topology/{id}/visualizations | Get attachment visualization settings
[**partial_update_topology_attachment_settings**](ReportAttachmentsTopologyApi.md#partial_update_topology_attachment_settings) | **PATCH** /api/v2/reports/attachments/topology/{id}/settings | Partial update attachment settings
[**update_topology_attachment_filters**](ReportAttachmentsTopologyApi.md#update_topology_attachment_filters) | **PUT** /api/v2/reports/attachments/topology/{id}/filters | Update topology filters
[**update_topology_attachment_resources**](ReportAttachmentsTopologyApi.md#update_topology_attachment_resources) | **PUT** /api/v2/reports/attachments/topology/{id}/resources | Update resources
[**update_topology_attachment_settings**](ReportAttachmentsTopologyApi.md#update_topology_attachment_settings) | **PUT** /api/v2/reports/attachments/topology/{id}/settings | Update attachment settings
[**update_topology_attachment_visualization_settings**](ReportAttachmentsTopologyApi.md#update_topology_attachment_visualization_settings) | **PUT** /api/v2/reports/attachments/topology/{id}/visualizations | Update visualization settings


# **create_topology_attachment**
> TopologyAttachmentDto create_topology_attachment(id, topology_attachment)

Create topology attachment

Create a new topology attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopologyApi()
id = 789 # int | The id of the report where the report attachment will be created
topology_attachment = swagger_client.TopologyAttachmentRequestDto() # TopologyAttachmentRequestDto | Topology report attachment

try:
    # Create topology attachment
    api_response = api_instance.create_topology_attachment(id, topology_attachment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopologyApi->create_topology_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report where the report attachment will be created | 
 **topology_attachment** | [**TopologyAttachmentRequestDto**](TopologyAttachmentRequestDto.md)| Topology report attachment | 

### Return type

[**TopologyAttachmentDto**](TopologyAttachmentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology_attachment**
> TopologyAttachmentDto get_topology_attachment(id)

Get topology attachment

Get a topology attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopologyApi()
id = 789 # int | The id of the report attachment

try:
    # Get topology attachment
    api_response = api_instance.get_topology_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopologyApi->get_topology_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TopologyAttachmentDto**](TopologyAttachmentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology_attachment_filters**
> TopologyAttachmentFilters get_topology_attachment_filters(id)

Get attachment topology filters

Get topology attachment filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopologyApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment topology filters
    api_response = api_instance.get_topology_attachment_filters(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopologyApi->get_topology_attachment_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TopologyAttachmentFilters**](TopologyAttachmentFilters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology_attachment_resources**
> TopologyAttachmentResource get_topology_attachment_resources(id)

Get resources

Get Topology resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopologyApi()
id = 789 # int | The id of the report attachment

try:
    # Get resources
    api_response = api_instance.get_topology_attachment_resources(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopologyApi->get_topology_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TopologyAttachmentResource**](TopologyAttachmentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology_attachment_settings**
> TopologyAttachmentSettings get_topology_attachment_settings(id)

Get attachment settings

Get topology attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopologyApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment settings
    api_response = api_instance.get_topology_attachment_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopologyApi->get_topology_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TopologyAttachmentSettings**](TopologyAttachmentSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology_attachment_visualization_settings**
> TopologyVisualization get_topology_attachment_visualization_settings(id)

Get attachment visualization settings

Get topology attachment visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopologyApi()
id = 789 # int | The id of the report attachment

try:
    # Get attachment visualization settings
    api_response = api_instance.get_topology_attachment_visualization_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopologyApi->get_topology_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**TopologyVisualization**](TopologyVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_topology_attachment_settings**
> TopologyAttachmentSettings partial_update_topology_attachment_settings(id, settings)

Partial update attachment settings

Partial update topology attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopologyApi()
id = 789 # int | The id of the report attachment
settings = swagger_client.TopologyAttachmentSettings() # TopologyAttachmentSettings | Topology attachment settings

try:
    # Partial update attachment settings
    api_response = api_instance.partial_update_topology_attachment_settings(id, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopologyApi->partial_update_topology_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **settings** | [**TopologyAttachmentSettings**](TopologyAttachmentSettings.md)| Topology attachment settings | 

### Return type

[**TopologyAttachmentSettings**](TopologyAttachmentSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_topology_attachment_filters**
> TopologyAttachmentFilters update_topology_attachment_filters(id, filters)

Update topology filters

Update topology attachment filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopologyApi()
id = 789 # int | The id of the report attachment
filters = swagger_client.TopologyAttachmentFilters() # TopologyAttachmentFilters | Topology attachment filters

try:
    # Update topology filters
    api_response = api_instance.update_topology_attachment_filters(id, filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopologyApi->update_topology_attachment_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **filters** | [**TopologyAttachmentFilters**](TopologyAttachmentFilters.md)| Topology attachment filters | 

### Return type

[**TopologyAttachmentFilters**](TopologyAttachmentFilters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_topology_attachment_resources**
> TopologyAttachmentResource update_topology_attachment_resources(id, resources)

Update resources

Update Topology resources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopologyApi()
id = 789 # int | The id of the report attachment
resources = swagger_client.TopologyAttachmentResource() # TopologyAttachmentResource | Topology attachment resources

try:
    # Update resources
    api_response = api_instance.update_topology_attachment_resources(id, resources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopologyApi->update_topology_attachment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **resources** | [**TopologyAttachmentResource**](TopologyAttachmentResource.md)| Topology attachment resources | 

### Return type

[**TopologyAttachmentResource**](TopologyAttachmentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_topology_attachment_settings**
> TopologyAttachmentSettings update_topology_attachment_settings(id, settings)

Update attachment settings

Update topology attachment settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopologyApi()
id = 789 # int | The id of the report attachment
settings = swagger_client.TopologyAttachmentSettings() # TopologyAttachmentSettings | Topology attachment settings

try:
    # Update attachment settings
    api_response = api_instance.update_topology_attachment_settings(id, settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopologyApi->update_topology_attachment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **settings** | [**TopologyAttachmentSettings**](TopologyAttachmentSettings.md)| Topology attachment settings | 

### Return type

[**TopologyAttachmentSettings**](TopologyAttachmentSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_topology_attachment_visualization_settings**
> TopologyVisualization update_topology_attachment_visualization_settings(id, visualizations)

Update visualization settings

Update topology visualization settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportAttachmentsTopologyApi()
id = 789 # int | The id of the report attachment
visualizations = swagger_client.TopologyVisualization() # TopologyVisualization | Topology attachment visualization settings

try:
    # Update visualization settings
    api_response = api_instance.update_topology_attachment_visualization_settings(id, visualizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportAttachmentsTopologyApi->update_topology_attachment_visualization_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **visualizations** | [**TopologyVisualization**](TopologyVisualization.md)| Topology attachment visualization settings | 

### Return type

[**TopologyVisualization**](TopologyVisualization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

