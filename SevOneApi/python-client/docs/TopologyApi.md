# swagger_client.TopologyApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_constraint**](TopologyApi.md#create_constraint) | **POST** /api/v2/topology/constraints | Create constraint
[**create_topology_link**](TopologyApi.md#create_topology_link) | **POST** /api/v2/topology/links | Create topology link
[**delete_constraint_by_id**](TopologyApi.md#delete_constraint_by_id) | **DELETE** /api/v2/topology/constraints/{id} | Delete constraint
[**delete_topology_full_link**](TopologyApi.md#delete_topology_full_link) | **DELETE** /api/v2/topology/links/{connectionId} | Delete topology full link
[**delete_topology_half_link**](TopologyApi.md#delete_topology_half_link) | **DELETE** /api/v2/topology/links/{connectionId}/halflinks/{deviceId} | Delete topology link
[**get_constraint**](TopologyApi.md#get_constraint) | **GET** /api/v2/topology/constraints/{id} | Get constraint
[**get_constraints**](TopologyApi.md#get_constraints) | **GET** /api/v2/topology/constraints | Get constraints
[**get_topology_full_link**](TopologyApi.md#get_topology_full_link) | **GET** /api/v2/topology/links/{connectionId} | Get topology full link
[**update_constraint_by_id**](TopologyApi.md#update_constraint_by_id) | **PUT** /api/v2/topology/constraints/{id} | Update constraint


# **create_constraint**
> ConstraintDto create_constraint(constraint)

Create constraint

Create the relationship constraint for topology links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
constraint = swagger_client.ConstraintDto() # ConstraintDto | constraint

try:
    # Create constraint
    api_response = api_instance.create_constraint(constraint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->create_constraint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **constraint** | [**ConstraintDto**](ConstraintDto.md)| constraint | 

### Return type

[**ConstraintDto**](ConstraintDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_topology_link**
> CreateLinkData create_topology_link(link_data)

Create topology link

Create topology link

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
link_data = swagger_client.CreateLinkData() # CreateLinkData | linkData

try:
    # Create topology link
    api_response = api_instance.create_topology_link(link_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->create_topology_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_data** | [**CreateLinkData**](CreateLinkData.md)| linkData | 

### Return type

[**CreateLinkData**](CreateLinkData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_constraint_by_id**
> ResponseEntity delete_constraint_by_id(id)

Delete constraint

Deletes the relationship constraint for topology links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
id = 789 # int | The id of the Constraint to be deleted

try:
    # Delete constraint
    api_response = api_instance.delete_constraint_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->delete_constraint_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the Constraint to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_topology_full_link**
> ResponseEntity delete_topology_full_link(connection_id)

Delete topology full link

Delete topology full link

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
connection_id = 789 # int | connectionId

try:
    # Delete topology full link
    api_response = api_instance.delete_topology_full_link(connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->delete_topology_full_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **int**| connectionId | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_topology_half_link**
> ResponseEntity delete_topology_half_link(connection_id, device_id)

Delete topology link

Delete topology half link

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
connection_id = 789 # int | connectionId
device_id = 789 # int | deviceId

try:
    # Delete topology link
    api_response = api_instance.delete_topology_half_link(connection_id, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->delete_topology_half_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **int**| connectionId | 
 **device_id** | **int**| deviceId | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_constraint**
> ConstraintDto get_constraint(id)

Get constraint

Get the relationship constraint for topology links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
id = 789 # int | Constraint Id

try:
    # Get constraint
    api_response = api_instance.get_constraint(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->get_constraint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Constraint Id | 

### Return type

[**ConstraintDto**](ConstraintDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_constraints**
> PagerConstraintDto get_constraints(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get constraints

Get the relationship constraints for topology links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get constraints
    api_response = api_instance.get_constraints(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->get_constraints: %s\n" % e)
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

[**PagerConstraintDto**](PagerConstraintDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology_full_link**
> list[LinkData] get_topology_full_link(connection_id)

Get topology full link

Get topology full link

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
connection_id = 789 # int | connectionId

try:
    # Get topology full link
    api_response = api_instance.get_topology_full_link(connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->get_topology_full_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **int**| connectionId | 

### Return type

[**list[LinkData]**](LinkData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_constraint_by_id**
> ConstraintDto update_constraint_by_id(id, constraint_dto)

Update constraint

Update the relationship constraint for topology links

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
id = 789 # int | The id of the Constraint to be updated
constraint_dto = swagger_client.ConstraintDto() # ConstraintDto | Constraint to be updated

try:
    # Update constraint
    api_response = api_instance.update_constraint_by_id(id, constraint_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->update_constraint_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the Constraint to be updated | 
 **constraint_dto** | [**ConstraintDto**](ConstraintDto.md)| Constraint to be updated | 

### Return type

[**ConstraintDto**](ConstraintDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

