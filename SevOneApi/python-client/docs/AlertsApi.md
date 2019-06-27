# swagger_client.AlertsApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_alert**](AlertsApi.md#assign_alert) | **PATCH** /api/v1/alerts/{id}/assign/{username} | Assign alert
[**assign_alert1**](AlertsApi.md#assign_alert1) | **PATCH** /api/v2/alerts/{id}/assign/{username} | Assign alert
[**clear_alert**](AlertsApi.md#clear_alert) | **PATCH** /api/v1/alerts/{id}/clear | Clear alert
[**clear_alert1**](AlertsApi.md#clear_alert1) | **PATCH** /api/v2/alerts/{id}/clear | Clear alert
[**create_alert**](AlertsApi.md#create_alert) | **POST** /api/v1/alerts | Create Alert
[**create_alert1**](AlertsApi.md#create_alert1) | **POST** /api/v2/alerts | Create Alert
[**create_alert_forced**](AlertsApi.md#create_alert_forced) | **POST** /api/v1/alerts/force | Create Alert Forced
[**create_alert_forced1**](AlertsApi.md#create_alert_forced1) | **POST** /api/v2/alerts/force | Create Alert Forced
[**delete_alert_by_id**](AlertsApi.md#delete_alert_by_id) | **DELETE** /api/v1/alerts/{id} | Delete alert
[**delete_alert_by_id1**](AlertsApi.md#delete_alert_by_id1) | **DELETE** /api/v2/alerts/{id} | Delete alert
[**filter_alerts**](AlertsApi.md#filter_alerts) | **POST** /api/v1/alerts/filter | Filter alerts
[**filter_alerts1**](AlertsApi.md#filter_alerts1) | **POST** /api/v2/alerts/filter | Filter alerts
[**get_alert**](AlertsApi.md#get_alert) | **GET** /api/v1/alerts/{id} | Get alert
[**get_alert1**](AlertsApi.md#get_alert1) | **GET** /api/v2/alerts/{id} | Get alert
[**get_all_alerts**](AlertsApi.md#get_all_alerts) | **GET** /api/v1/alerts | Get all alert
[**get_all_alerts1**](AlertsApi.md#get_all_alerts1) | **GET** /api/v2/alerts | Get all alert
[**get_device_alerts**](AlertsApi.md#get_device_alerts) | **GET** /api/v1/alerts/devices/{id} | Get all alert
[**get_device_alerts1**](AlertsApi.md#get_device_alerts1) | **GET** /api/v2/alerts/devices/{id} | Get all alert
[**get_flow_falcon_device_alerts**](AlertsApi.md#get_flow_falcon_device_alerts) | **GET** /api/v1/alerts/netflow-device/{id} | Get all alerts by FlowFalcon Device Id
[**get_flow_falcon_device_alerts1**](AlertsApi.md#get_flow_falcon_device_alerts1) | **GET** /api/v2/alerts/netflow-device/{id} | Get all alerts by FlowFalcon Device Id
[**get_max_severity_alert_for_objects**](AlertsApi.md#get_max_severity_alert_for_objects) | **POST** /api/v1/alerts/objects | Get max severity alert/object
[**get_max_severity_alert_for_objects1**](AlertsApi.md#get_max_severity_alert_for_objects1) | **POST** /api/v2/alerts/objects | Get max severity alert/object
[**ignore_alert**](AlertsApi.md#ignore_alert) | **PATCH** /api/v1/alerts/{id}/ignore/{ignoreTime} | Ignore alert
[**ignore_alert1**](AlertsApi.md#ignore_alert1) | **PATCH** /api/v2/alerts/{id}/ignore/{ignoreTime} | Ignore alert
[**patch_alert**](AlertsApi.md#patch_alert) | **PATCH** /api/v1/alerts/{id} | Update alert
[**patch_alert1**](AlertsApi.md#patch_alert1) | **PATCH** /api/v2/alerts/{id} | Update alert
[**update_alert**](AlertsApi.md#update_alert) | **PUT** /api/v1/alerts/{id} | Update alert
[**update_alert1**](AlertsApi.md#update_alert1) | **PUT** /api/v2/alerts/{id} | Update alert


# **assign_alert**
> ResponseEntity assign_alert(id, username)

Assign alert

Assign alert to user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | Alert Id 
username = 'username_example' # str | Username

try:
    # Assign alert
    api_response = api_instance.assign_alert(id, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->assign_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Alert Id  | 
 **username** | **str**| Username | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_alert1**
> ResponseEntity assign_alert1(id, username)

Assign alert

Assign alert to user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | Alert Id 
username = 'username_example' # str | Username

try:
    # Assign alert
    api_response = api_instance.assign_alert1(id, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->assign_alert1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Alert Id  | 
 **username** | **str**| Username | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_alert**
> ResponseEntity clear_alert(id, dto)

Clear alert

Clear alert

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | Alert Id 
dto = swagger_client.AlertClearDto() # AlertClearDto | Clear Message

try:
    # Clear alert
    api_response = api_instance.clear_alert(id, dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->clear_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Alert Id  | 
 **dto** | [**AlertClearDto**](AlertClearDto.md)| Clear Message | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_alert1**
> ResponseEntity clear_alert1(id, dto)

Clear alert

Clear alert

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | Alert Id 
dto = swagger_client.AlertClearDto() # AlertClearDto | Clear Message

try:
    # Clear alert
    api_response = api_instance.clear_alert1(id, dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->clear_alert1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Alert Id  | 
 **dto** | [**AlertClearDto**](AlertClearDto.md)| Clear Message | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alert**
> str create_alert(alert)

Create Alert

Create an alert

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
alert = swagger_client.AlertCreateDto() # AlertCreateDto | alert

try:
    # Create Alert
    api_response = api_instance.create_alert(alert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->create_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert** | [**AlertCreateDto**](AlertCreateDto.md)| alert | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alert1**
> str create_alert1(alert)

Create Alert

Create an alert

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
alert = swagger_client.AlertCreateDto() # AlertCreateDto | alert

try:
    # Create Alert
    api_response = api_instance.create_alert1(alert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->create_alert1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert** | [**AlertCreateDto**](AlertCreateDto.md)| alert | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alert_forced**
> AlertCreateDto create_alert_forced(alert)

Create Alert Forced

Create an alert forced so you get its id immediately

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
alert = swagger_client.AlertCreateDto() # AlertCreateDto | alert

try:
    # Create Alert Forced
    api_response = api_instance.create_alert_forced(alert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->create_alert_forced: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert** | [**AlertCreateDto**](AlertCreateDto.md)| alert | 

### Return type

[**AlertCreateDto**](AlertCreateDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alert_forced1**
> AlertCreateDto create_alert_forced1(alert)

Create Alert Forced

Create an alert forced so you get its id immediately

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
alert = swagger_client.AlertCreateDto() # AlertCreateDto | alert

try:
    # Create Alert Forced
    api_response = api_instance.create_alert_forced1(alert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->create_alert_forced1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert** | [**AlertCreateDto**](AlertCreateDto.md)| alert | 

### Return type

[**AlertCreateDto**](AlertCreateDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_by_id**
> ResponseEntity delete_alert_by_id(id)

Delete alert

Deletes an existing alert

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | The id of the alert to be deleted

try:
    # Delete alert
    api_response = api_instance.delete_alert_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->delete_alert_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the alert to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_by_id1**
> ResponseEntity delete_alert_by_id1(id)

Delete alert

Deletes an existing alert

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | The id of the alert to be deleted

try:
    # Delete alert
    api_response = api_instance.delete_alert_by_id1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->delete_alert_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the alert to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_alerts**
> PagerAlertDto filter_alerts(alert, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Filter alerts

Endpoint for filtering all alerts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
alert = swagger_client.AlertFilterDto() # AlertFilterDto | AlertFilterDto
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Filter alerts
    api_response = api_instance.filter_alerts(alert, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->filter_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert** | [**AlertFilterDto**](AlertFilterDto.md)| AlertFilterDto | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerAlertDto**](PagerAlertDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_alerts1**
> PagerAlertDto filter_alerts1(alert, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Filter alerts

Endpoint for filtering all alerts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
alert = swagger_client.AlertFilterDto() # AlertFilterDto | AlertFilterDto
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Filter alerts
    api_response = api_instance.filter_alerts1(alert, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->filter_alerts1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert** | [**AlertFilterDto**](AlertFilterDto.md)| AlertFilterDto | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**PagerAlertDto**](PagerAlertDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert**
> AlertDto get_alert(id)

Get alert

Endpoint for retrieving all alert info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | Alert Id

try:
    # Get alert
    api_response = api_instance.get_alert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Alert Id | 

### Return type

[**AlertDto**](AlertDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert1**
> AlertDto get_alert1(id)

Get alert

Endpoint for retrieving all alert info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | Alert Id

try:
    # Get alert
    api_response = api_instance.get_alert1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_alert1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Alert Id | 

### Return type

[**AlertDto**](AlertDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_alerts**
> PagerAlertDto get_all_alerts(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all alert

Endpoint for retrieving all alert with support for pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all alert
    api_response = api_instance.get_all_alerts(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_all_alerts: %s\n" % e)
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

[**PagerAlertDto**](PagerAlertDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_alerts1**
> PagerAlertDto get_all_alerts1(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all alert

Endpoint for retrieving all alert with support for pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all alert
    api_response = api_instance.get_all_alerts1(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_all_alerts1: %s\n" % e)
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

[**PagerAlertDto**](PagerAlertDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_alerts**
> DeviceAlertsDto get_device_alerts(id, alert_status=alert_status, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all alert

Endpoint for retrieving all alert for the device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | The id of the device
alert_status = 'open' # str | Fetch alert which are open/close/both (optional) (default to open)
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all alert
    api_response = api_instance.get_device_alerts(id, alert_status=alert_status, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_device_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device | 
 **alert_status** | **str**| Fetch alert which are open/close/both | [optional] [default to open]
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**DeviceAlertsDto**](DeviceAlertsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_alerts1**
> DeviceAlertsDto get_device_alerts1(id, alert_status=alert_status, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all alert

Endpoint for retrieving all alert for the device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | The id of the device
alert_status = 'open' # str | Fetch alert which are open/close/both (optional) (default to open)
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all alert
    api_response = api_instance.get_device_alerts1(id, alert_status=alert_status, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_device_alerts1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the device | 
 **alert_status** | **str**| Fetch alert which are open/close/both | [optional] [default to open]
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**DeviceAlertsDto**](DeviceAlertsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_falcon_device_alerts**
> NetflowDeviceAlertsDto get_flow_falcon_device_alerts(id, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all alerts by FlowFalcon Device Id

Endpoint for retrieving all alerts for flowFalcon device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | id
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all alerts by FlowFalcon Device Id
    api_response = api_instance.get_flow_falcon_device_alerts(id, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_flow_falcon_device_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**NetflowDeviceAlertsDto**](NetflowDeviceAlertsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_falcon_device_alerts1**
> NetflowDeviceAlertsDto get_flow_falcon_device_alerts1(id, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all alerts by FlowFalcon Device Id

Endpoint for retrieving all alerts for flowFalcon device

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | id
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all alerts by FlowFalcon Device Id
    api_response = api_instance.get_flow_falcon_device_alerts1(id, page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_flow_falcon_device_alerts1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 

### Return type

[**NetflowDeviceAlertsDto**](NetflowDeviceAlertsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_max_severity_alert_for_objects**
> list[Severity] get_max_severity_alert_for_objects(ids)

Get max severity alert/object

Endpoint for retrieving max severity alert/object for each objectKey

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
ids = [swagger_client.DeviceObjectId()] # list[DeviceObjectId] | List of ObjectKeys

try:
    # Get max severity alert/object
    api_response = api_instance.get_max_severity_alert_for_objects(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_max_severity_alert_for_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[DeviceObjectId]**](DeviceObjectId.md)| List of ObjectKeys | 

### Return type

[**list[Severity]**](Severity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_max_severity_alert_for_objects1**
> list[Severity] get_max_severity_alert_for_objects1(ids)

Get max severity alert/object

Endpoint for retrieving max severity alert/object for each objectKey

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
ids = [swagger_client.DeviceObjectId()] # list[DeviceObjectId] | List of ObjectKeys

try:
    # Get max severity alert/object
    api_response = api_instance.get_max_severity_alert_for_objects1(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_max_severity_alert_for_objects1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[DeviceObjectId]**](DeviceObjectId.md)| List of ObjectKeys | 

### Return type

[**list[Severity]**](Severity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ignore_alert**
> ResponseEntity ignore_alert(id, ignore_time, comment=comment)

Ignore alert

Ignore alert until time (long)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | Alert Id 
ignore_time = 789 # int | Ignore until (Unix timestamp with milliseconds proximity) 
comment = swagger_client.AlertClearDto() # AlertClearDto | Ignore comment (optional)

try:
    # Ignore alert
    api_response = api_instance.ignore_alert(id, ignore_time, comment=comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->ignore_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Alert Id  | 
 **ignore_time** | **int**| Ignore until (Unix timestamp with milliseconds proximity)  | 
 **comment** | [**AlertClearDto**](AlertClearDto.md)| Ignore comment | [optional] 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ignore_alert1**
> ResponseEntity ignore_alert1(id, ignore_time, comment=comment)

Ignore alert

Ignore alert until time (long)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | Alert Id 
ignore_time = 789 # int | Ignore until (Unix timestamp with milliseconds proximity) 
comment = swagger_client.AlertClearDto() # AlertClearDto | Ignore comment (optional)

try:
    # Ignore alert
    api_response = api_instance.ignore_alert1(id, ignore_time, comment=comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->ignore_alert1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Alert Id  | 
 **ignore_time** | **int**| Ignore until (Unix timestamp with milliseconds proximity)  | 
 **comment** | [**AlertClearDto**](AlertClearDto.md)| Ignore comment | [optional] 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_alert**
> AlertDto patch_alert(id, alert)

Update alert

Updates an existing alert

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | The id of the alert to update
alert = swagger_client.AlertDto() # AlertDto | Alert to be updated

try:
    # Update alert
    api_response = api_instance.patch_alert(id, alert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->patch_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the alert to update | 
 **alert** | [**AlertDto**](AlertDto.md)| Alert to be updated | 

### Return type

[**AlertDto**](AlertDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_alert1**
> AlertDto patch_alert1(id, alert)

Update alert

Updates an existing alert

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | The id of the alert to update
alert = swagger_client.AlertDto() # AlertDto | Alert to be updated

try:
    # Update alert
    api_response = api_instance.patch_alert1(id, alert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->patch_alert1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the alert to update | 
 **alert** | [**AlertDto**](AlertDto.md)| Alert to be updated | 

### Return type

[**AlertDto**](AlertDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert**
> AlertDto update_alert(id, alert)

Update alert

Updates an existing alert

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | The id of the alert to update
alert = swagger_client.AlertDto() # AlertDto | Alert to be updated

try:
    # Update alert
    api_response = api_instance.update_alert(id, alert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->update_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the alert to update | 
 **alert** | [**AlertDto**](AlertDto.md)| Alert to be updated | 

### Return type

[**AlertDto**](AlertDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert1**
> AlertDto update_alert1(id, alert)

Update alert

Updates an existing alert

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertsApi()
id = 789 # int | The id of the alert to update
alert = swagger_client.AlertDto() # AlertDto | Alert to be updated

try:
    # Update alert
    api_response = api_instance.update_alert1(id, alert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->update_alert1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the alert to update | 
 **alert** | [**AlertDto**](AlertDto.md)| Alert to be updated | 

### Return type

[**AlertDto**](AlertDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

