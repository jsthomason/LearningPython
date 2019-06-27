# swagger_client.NetFlowApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_filter**](NetFlowApi.md#create_filter) | **POST** /api/v2/netflow/filters | Create Netflow filters
[**create_filter_entities**](NetFlowApi.md#create_filter_entities) | **POST** /api/v2/netflow/filters/{id}/rules | Create Netflow filters rules
[**create_mappings**](NetFlowApi.md#create_mappings) | **POST** /api/v2/netflow/objectMappings | Create object mapping
[**create_subnet**](NetFlowApi.md#create_subnet) | **POST** /api/v2/netflow/segments/{id}/subnets | Create subnet
[**create_subnet_category**](NetFlowApi.md#create_subnet_category) | **POST** /api/v2/netflow/segments | Create Network Segment
[**delet_subnet_by_id**](NetFlowApi.md#delet_subnet_by_id) | **DELETE** /api/v2/netflow/segments/subnets/{id} | Delete subnet
[**delet_subnet_category_by_id**](NetFlowApi.md#delet_subnet_category_by_id) | **DELETE** /api/v2/netflow/segments/{id} | Delete Network Segment
[**delete_filter**](NetFlowApi.md#delete_filter) | **DELETE** /api/v2/netflow/filters/{id} | Delete Netflow filter
[**delete_filter_entity**](NetFlowApi.md#delete_filter_entity) | **DELETE** /api/v2/netflow/filters/{id}/rules/{ruleId} | Delete Netflow filter rule
[**delete_object_mapping_by_id**](NetFlowApi.md#delete_object_mapping_by_id) | **DELETE** /api/v2/netflow/objectMappings/{id} | Delete Object Mapping by Id
[**filter_net_flow_device_interfaces**](NetFlowApi.md#filter_net_flow_device_interfaces) | **POST** /api/v2/netflow/devices/interfaces/filter | Get NetFlow device interfaces
[**filter_net_flow_devices**](NetFlowApi.md#filter_net_flow_devices) | **POST** /api/v2/netflow/devices/filter | Get all NetFlow devices
[**filter_netflow_fields**](NetFlowApi.md#filter_netflow_fields) | **POST** /api/v2/netflow/fields/filter | Filter netflow fields
[**filter_netflow_views**](NetFlowApi.md#filter_netflow_views) | **POST** /api/v2/netflow/views/filter | Filter views
[**filter_view_indicators**](NetFlowApi.md#filter_view_indicators) | **POST** /api/v2/netflow/views/{viewId}/fields/filter | Filter netflow view fields
[**get_directions**](NetFlowApi.md#get_directions) | **GET** /api/v2/netflow/devices/{netflowDeviceId}/interfaces/{interfaceId}/directions | Get directions by NetFlow device id and interface id
[**get_filter_by_id**](NetFlowApi.md#get_filter_by_id) | **GET** /api/v2/netflow/filters/{id} | Get Netflow filters
[**get_filter_entities_by_id**](NetFlowApi.md#get_filter_entities_by_id) | **GET** /api/v2/netflow/filters/{id}/rules | Get Netflow filter rules
[**get_filters**](NetFlowApi.md#get_filters) | **GET** /api/v2/netflow/filters | Get Netflow filters
[**get_interfaces**](NetFlowApi.md#get_interfaces) | **GET** /api/v2/netflow/devices/{netflowDeviceId}/interfaces | Get interfaces by NetFlow device id
[**get_mapping_by_indicator**](NetFlowApi.md#get_mapping_by_indicator) | **POST** /api/v2/netflow/objectMappings/filterByIndicator | Get flow interface to device indicator mapping by indicators
[**get_mapping_by_interfaces**](NetFlowApi.md#get_mapping_by_interfaces) | **POST** /api/v2/netflow/objectMappings/filterByInterface | Get flow interface to device indicator mapping by interface
[**get_mappings**](NetFlowApi.md#get_mappings) | **GET** /api/v2/netflow/objectMappings | Get flow interface to device indicator mappings
[**get_net_flow_devices**](NetFlowApi.md#get_net_flow_devices) | **GET** /api/v2/netflow/devices | Get all NetFlow devices
[**get_net_flow_modes**](NetFlowApi.md#get_net_flow_modes) | **GET** /api/v2/netflow/settings | Get the status of NetFlow settings
[**get_netflow_categories**](NetFlowApi.md#get_netflow_categories) | **GET** /api/v2/netflow/views/categories | Get netflow view categories
[**get_netflow_fields**](NetFlowApi.md#get_netflow_fields) | **GET** /api/v2/netflow/fields | Get netflow fields
[**get_network_segments**](NetFlowApi.md#get_network_segments) | **GET** /api/v2/netflow/segments | Get Network Segments
[**get_protocols**](NetFlowApi.md#get_protocols) | **GET** /api/v2/netflow/protocols | Get protocols
[**get_report_columns_using_get**](NetFlowApi.md#get_report_columns_using_get) | **GET** /api/v2/netflow/views/{viewId}/reportColumns | getReportColumns
[**get_services_by_port**](NetFlowApi.md#get_services_by_port) | **GET** /api/v2/netflow/services | Get services by port
[**get_subnet_category_by_id**](NetFlowApi.md#get_subnet_category_by_id) | **GET** /api/v2/netflow/segments/{id} | Get Network Segment By Id
[**get_subnets**](NetFlowApi.md#get_subnets) | **GET** /api/v2/netflow/segments/subnets | Get subnets
[**get_subnets_by_category_id**](NetFlowApi.md#get_subnets_by_category_id) | **GET** /api/v2/netflow/segments/{id}/subnets | Get subnets
[**get_view_indicators**](NetFlowApi.md#get_view_indicators) | **GET** /api/v2/netflow/views/{viewId}/fields | Get the keys and metrics in a FlowFalcon view
[**get_views**](NetFlowApi.md#get_views) | **GET** /api/v2/netflow/views | Get views


# **create_filter**
> NetFlowFilterDto create_filter(dto)

Create Netflow filters

Create a netflow filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
dto = swagger_client.NetFlowFilterCreateDto() # NetFlowFilterCreateDto | dto

try:
    # Create Netflow filters
    api_response = api_instance.create_filter(dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->create_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dto** | [**NetFlowFilterCreateDto**](NetFlowFilterCreateDto.md)| dto | 

### Return type

[**NetFlowFilterDto**](NetFlowFilterDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_filter_entities**
> NetFlowFilterEntityDto create_filter_entities(dto, id)

Create Netflow filters rules

Create a netflow filter rules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
dto = swagger_client.NetFlowFilterEntityCreateDto() # NetFlowFilterEntityCreateDto | dto
id = 789 # int | Filter Id

try:
    # Create Netflow filters rules
    api_response = api_instance.create_filter_entities(dto, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->create_filter_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dto** | [**NetFlowFilterEntityCreateDto**](NetFlowFilterEntityCreateDto.md)| dto | 
 **id** | **int**| Filter Id | 

### Return type

[**NetFlowFilterEntityDto**](NetFlowFilterEntityDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mappings**
> FlowDeviceMappingDto create_mappings(new_object_mapping)

Create object mapping

Create object mapping

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
new_object_mapping = swagger_client.FlowDeviceMappingDto() # FlowDeviceMappingDto | newObjectMapping

try:
    # Create object mapping
    api_response = api_instance.create_mappings(new_object_mapping)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->create_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_object_mapping** | [**FlowDeviceMappingDto**](FlowDeviceMappingDto.md)| newObjectMapping | 

### Return type

[**FlowDeviceMappingDto**](FlowDeviceMappingDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subnet**
> NetFlowSubnetDto create_subnet(dto, id)

Create subnet

Create a subnet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
dto = swagger_client.NetFlowSubnetCreateDto() # NetFlowSubnetCreateDto | dto
id = 789 # int | Segment Id

try:
    # Create subnet
    api_response = api_instance.create_subnet(dto, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->create_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dto** | [**NetFlowSubnetCreateDto**](NetFlowSubnetCreateDto.md)| dto | 
 **id** | **int**| Segment Id | 

### Return type

[**NetFlowSubnetDto**](NetFlowSubnetDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subnet_category**
> NetFlowSubnetCategoryDto create_subnet_category(dto)

Create Network Segment

Create a Network Segment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
dto = swagger_client.NetFlowSubnetCategoryCreateDto() # NetFlowSubnetCategoryCreateDto | dto

try:
    # Create Network Segment
    api_response = api_instance.create_subnet_category(dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->create_subnet_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dto** | [**NetFlowSubnetCategoryCreateDto**](NetFlowSubnetCategoryCreateDto.md)| dto | 

### Return type

[**NetFlowSubnetCategoryDto**](NetFlowSubnetCategoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delet_subnet_by_id**
> ResponseEntity delet_subnet_by_id(id)

Delete subnet

Deletes an existing subnet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | The id of the subnet to be deleted

try:
    # Delete subnet
    api_response = api_instance.delet_subnet_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->delet_subnet_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the subnet to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delet_subnet_category_by_id**
> ResponseEntity delet_subnet_category_by_id(id)

Delete Network Segment

Deletes an existing Network Segment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | The id of the segment to be deleted

try:
    # Delete Network Segment
    api_response = api_instance.delet_subnet_category_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->delet_subnet_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the segment to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_filter**
> ResponseEntity delete_filter(id)

Delete Netflow filter

Deletes an existing netflow filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | The id of the filter to be deleted

try:
    # Delete Netflow filter
    api_response = api_instance.delete_filter(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->delete_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the filter to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_filter_entity**
> ResponseEntity delete_filter_entity(id, rule_id)

Delete Netflow filter rule

Deletes an existing netflow filter rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | The id of the filter that has the rule
rule_id = 789 # int | The id of the filter rule to be deleted

try:
    # Delete Netflow filter rule
    api_response = api_instance.delete_filter_entity(id, rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->delete_filter_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the filter that has the rule | 
 **rule_id** | **int**| The id of the filter rule to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object_mapping_by_id**
> ResponseEntity delete_object_mapping_by_id(id)

Delete Object Mapping by Id

Deletes an existing Object mapping 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | The id of the the object mapping to be deleted

try:
    # Delete Object Mapping by Id
    api_response = api_instance.delete_object_mapping_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->delete_object_mapping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the the object mapping to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_net_flow_device_interfaces**
> PagerNetFlowInterfaceDto filter_net_flow_device_interfaces(filter, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get NetFlow device interfaces

Endpoint for retrieving all NetFlow device interfaces that match the criteria

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
filter = swagger_client.NetFlowInterfaceFilterDto() # NetFlowInterfaceFilterDto | Netflow Device object that will be used for filtering
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get NetFlow device interfaces
    api_response = api_instance.filter_net_flow_device_interfaces(filter, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->filter_net_flow_device_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**NetFlowInterfaceFilterDto**](NetFlowInterfaceFilterDto.md)| Netflow Device object that will be used for filtering | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerNetFlowInterfaceDto**](PagerNetFlowInterfaceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_net_flow_devices**
> PagerNetFlowDeviceDto filter_net_flow_devices(filter, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all NetFlow devices

Endpoint for retrieving all NetFlow devices that match the criteria

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
filter = swagger_client.NetFlowDeviceFilterDto() # NetFlowDeviceFilterDto | Netflow Device object that will be used for filtering
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all NetFlow devices
    api_response = api_instance.filter_net_flow_devices(filter, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->filter_net_flow_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**NetFlowDeviceFilterDto**](NetFlowDeviceFilterDto.md)| Netflow Device object that will be used for filtering | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerNetFlowDeviceDto**](PagerNetFlowDeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_netflow_fields**
> PagerNetFlowFieldDto filter_netflow_fields(net_flow_field_filter_dto, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Filter netflow fields

Filter netflow fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
net_flow_field_filter_dto = swagger_client.NetFlowFieldFilterDto() # NetFlowFieldFilterDto | Netflow Fileds filtering params
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Filter netflow fields
    api_response = api_instance.filter_netflow_fields(net_flow_field_filter_dto, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->filter_netflow_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **net_flow_field_filter_dto** | [**NetFlowFieldFilterDto**](NetFlowFieldFilterDto.md)| Netflow Fileds filtering params | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerNetFlowFieldDto**](PagerNetFlowFieldDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_netflow_views**
> PagerNetFlowAggregationTemplateDto filter_netflow_views(net_flow_view_filter_dto, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Filter views

Filter netflow views

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
net_flow_view_filter_dto = swagger_client.NetFlowViewFilterDto() # NetFlowViewFilterDto | Netflow View filtering params
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Filter views
    api_response = api_instance.filter_netflow_views(net_flow_view_filter_dto, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->filter_netflow_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **net_flow_view_filter_dto** | [**NetFlowViewFilterDto**](NetFlowViewFilterDto.md)| Netflow View filtering params | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerNetFlowAggregationTemplateDto**](PagerNetFlowAggregationTemplateDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_view_indicators**
> PagerNetFlowFieldDto filter_view_indicators(view_id, net_flow_field_filter_dto, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Filter netflow view fields

Filter netflow view fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
view_id = 789 # int | viewId
net_flow_field_filter_dto = swagger_client.NetFlowFieldFilterDto() # NetFlowFieldFilterDto | Netflow view fileds filtering params
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Filter netflow view fields
    api_response = api_instance.filter_view_indicators(view_id, net_flow_field_filter_dto, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->filter_view_indicators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**| viewId | 
 **net_flow_field_filter_dto** | [**NetFlowFieldFilterDto**](NetFlowFieldFilterDto.md)| Netflow view fileds filtering params | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerNetFlowFieldDto**](PagerNetFlowFieldDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_directions**
> list[NetFlowDirectionDto] get_directions(netflow_device_id, interface_id)

Get directions by NetFlow device id and interface id

Get directions by NetFlow device id and interface id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
netflow_device_id = 789 # int | netflowDeviceId
interface_id = 789 # int | interfaceId

try:
    # Get directions by NetFlow device id and interface id
    api_response = api_instance.get_directions(netflow_device_id, interface_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_directions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **netflow_device_id** | **int**| netflowDeviceId | 
 **interface_id** | **int**| interfaceId | 

### Return type

[**list[NetFlowDirectionDto]**](NetFlowDirectionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filter_by_id**
> list[NetFlowFilterDto] get_filter_by_id(id)

Get Netflow filters

Get filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | Filter Id

try:
    # Get Netflow filters
    api_response = api_instance.get_filter_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_filter_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Filter Id | 

### Return type

[**list[NetFlowFilterDto]**](NetFlowFilterDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filter_entities_by_id**
> list[NetFlowFilterEntityDto] get_filter_entities_by_id(id)

Get Netflow filter rules

Get filters rules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | Filter Id

try:
    # Get Netflow filter rules
    api_response = api_instance.get_filter_entities_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_filter_entities_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Filter Id | 

### Return type

[**list[NetFlowFilterEntityDto]**](NetFlowFilterEntityDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filters**
> list[NetFlowFilterDto] get_filters()

Get Netflow filters

Get filters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()

try:
    # Get Netflow filters
    api_response = api_instance.get_filters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_filters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NetFlowFilterDto]**](NetFlowFilterDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interfaces**
> list[NetFlowInterfaceDto] get_interfaces(netflow_device_id)

Get interfaces by NetFlow device id

Get interfaces by NetFlow device id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
netflow_device_id = 789 # int | netflowDeviceId

try:
    # Get interfaces by NetFlow device id
    api_response = api_instance.get_interfaces(netflow_device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **netflow_device_id** | **int**| netflowDeviceId | 

### Return type

[**list[NetFlowInterfaceDto]**](NetFlowInterfaceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapping_by_indicator**
> PagerFlowDeviceMappingDto get_mapping_by_indicator(dtos, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields, include_automatic=include_automatic)

Get flow interface to device indicator mapping by indicators

Get flow interface to device indicator mapping by indicators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
dtos = [swagger_client.DeviceIndicatorDto()] # list[DeviceIndicatorDto] | dtos
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)
include_automatic = false # bool | Include automatic mappings (optional) (default to false)

try:
    # Get flow interface to device indicator mapping by indicators
    api_response = api_instance.get_mapping_by_indicator(dtos, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields, include_automatic=include_automatic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_mapping_by_indicator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtos** | [**list[DeviceIndicatorDto]**](DeviceIndicatorDto.md)| dtos | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 
 **include_automatic** | **bool**| Include automatic mappings | [optional] [default to false]

### Return type

[**PagerFlowDeviceMappingDto**](PagerFlowDeviceMappingDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapping_by_interfaces**
> PagerFlowDeviceMappingDto get_mapping_by_interfaces(dtos, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields, include_automatic=include_automatic)

Get flow interface to device indicator mapping by interface

Get flow interface to device indicator mapping by interfaces

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
dtos = [swagger_client.FlowInterfaceDto()] # list[FlowInterfaceDto] | dtos
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)
include_automatic = false # bool | Include automatic mappings (optional) (default to false)

try:
    # Get flow interface to device indicator mapping by interface
    api_response = api_instance.get_mapping_by_interfaces(dtos, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields, include_automatic=include_automatic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_mapping_by_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtos** | [**list[FlowInterfaceDto]**](FlowInterfaceDto.md)| dtos | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 
 **include_automatic** | **bool**| Include automatic mappings | [optional] [default to false]

### Return type

[**PagerFlowDeviceMappingDto**](PagerFlowDeviceMappingDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mappings**
> PagerFlowDeviceMappingDto get_mappings(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields, include_automatic=include_automatic)

Get flow interface to device indicator mappings

Get flow interface to device indicator mappings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)
include_automatic = false # bool | Include automatic mappings (optional) (default to false)

try:
    # Get flow interface to device indicator mappings
    api_response = api_instance.get_mappings(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields, include_automatic=include_automatic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 
 **include_automatic** | **bool**| Include automatic mappings | [optional] [default to false]

### Return type

[**PagerFlowDeviceMappingDto**](PagerFlowDeviceMappingDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_net_flow_devices**
> PagerNetFlowDeviceDto get_net_flow_devices(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all NetFlow devices

Endpoint for retrieving all NetFlow devices with support for pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all NetFlow devices
    api_response = api_instance.get_net_flow_devices(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_net_flow_devices: %s\n" % e)
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

[**PagerNetFlowDeviceDto**](PagerNetFlowDeviceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_net_flow_modes**
> NetFlowModesDto get_net_flow_modes()

Get the status of NetFlow settings

Endpoint for retrieving the status of NetFlow settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()

try:
    # Get the status of NetFlow settings
    api_response = api_instance.get_net_flow_modes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_net_flow_modes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NetFlowModesDto**](NetFlowModesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_netflow_categories**
> PagerNetFlowViewCategoryDto get_netflow_categories(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get netflow view categories

Get netflow view categories

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get netflow view categories
    api_response = api_instance.get_netflow_categories(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_netflow_categories: %s\n" % e)
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

[**PagerNetFlowViewCategoryDto**](PagerNetFlowViewCategoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_netflow_fields**
> PagerNetFlowFieldDto get_netflow_fields(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get netflow fields

Get netflow fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get netflow fields
    api_response = api_instance.get_netflow_fields(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_netflow_fields: %s\n" % e)
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

[**PagerNetFlowFieldDto**](PagerNetFlowFieldDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_segments**
> list[NetFlowSubnetCategoryDto] get_network_segments()

Get Network Segments

Get Networks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()

try:
    # Get Network Segments
    api_response = api_instance.get_network_segments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_network_segments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NetFlowSubnetCategoryDto]**](NetFlowSubnetCategoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_protocols**
> list[NetFlowProtocolDto] get_protocols()

Get protocols

Get protocols

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()

try:
    # Get protocols
    api_response = api_instance.get_protocols()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_protocols: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NetFlowProtocolDto]**](NetFlowProtocolDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_columns_using_get**
> list[NetflowReportingColumnDto] get_report_columns_using_get(view_id)

getReportColumns

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
view_id = 789 # int | viewId

try:
    # getReportColumns
    api_response = api_instance.get_report_columns_using_get(view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_report_columns_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**| viewId | 

### Return type

[**list[NetflowReportingColumnDto]**](NetflowReportingColumnDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services_by_port**
> list[NetFlowApplicationDto] get_services_by_port()

Get services by port

Get applications by port

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()

try:
    # Get services by port
    api_response = api_instance.get_services_by_port()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_services_by_port: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NetFlowApplicationDto]**](NetFlowApplicationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subnet_category_by_id**
> NetFlowSubnetCategoryDto get_subnet_category_by_id(id)

Get Network Segment By Id

et Network Segment By Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | Segment Id

try:
    # Get Network Segment By Id
    api_response = api_instance.get_subnet_category_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_subnet_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Segment Id | 

### Return type

[**NetFlowSubnetCategoryDto**](NetFlowSubnetCategoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subnets**
> list[NetFlowSubnetDto] get_subnets()

Get subnets

Get subnets

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()

try:
    # Get subnets
    api_response = api_instance.get_subnets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_subnets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NetFlowSubnetDto]**](NetFlowSubnetDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subnets_by_category_id**
> list[NetFlowSubnetDto] get_subnets_by_category_id(id)

Get subnets

Get subnets

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
id = 789 # int | Segment Id

try:
    # Get subnets
    api_response = api_instance.get_subnets_by_category_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_subnets_by_category_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Segment Id | 

### Return type

[**list[NetFlowSubnetDto]**](NetFlowSubnetDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view_indicators**
> FlowFalconViewIndicatorsDto get_view_indicators(view_id, include_members=include_members)

Get the keys and metrics in a FlowFalcon view

Endpoint for retrieving the keys and metrics in a FlowFalcon view

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
view_id = 789 # int | viewId
include_members = false # bool | Include members, defaults to false (optional) (default to false)

try:
    # Get the keys and metrics in a FlowFalcon view
    api_response = api_instance.get_view_indicators(view_id, include_members=include_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_view_indicators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **int**| viewId | 
 **include_members** | **bool**| Include members, defaults to false | [optional] [default to false]

### Return type

[**FlowFalconViewIndicatorsDto**](FlowFalconViewIndicatorsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_views**
> PagerNetFlowAggregationTemplateDto get_views(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get views

Get views

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NetFlowApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get views
    api_response = api_instance.get_views(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetFlowApi->get_views: %s\n" % e)
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

[**PagerNetFlowAggregationTemplateDto**](PagerNetFlowAggregationTemplateDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

