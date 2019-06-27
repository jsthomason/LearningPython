# swagger_client.ReportsApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report**](ReportsApi.md#create_report) | **POST** /api/v2/reports | Create report
[**create_report1**](ReportsApi.md#create_report1) | **POST** /api/v1/reports | Create report
[**delete_report_by_id**](ReportsApi.md#delete_report_by_id) | **DELETE** /api/v2/reports/{id} | Delete report
[**delete_report_by_id1**](ReportsApi.md#delete_report_by_id1) | **DELETE** /api/v1/reports/{id} | Delete report
[**get_all_report_folders**](ReportsApi.md#get_all_report_folders) | **GET** /api/v2/reports/folders | Get all report folders
[**get_all_report_folders1**](ReportsApi.md#get_all_report_folders1) | **GET** /api/v1/reports/folders | Get all report folders
[**get_all_reports**](ReportsApi.md#get_all_reports) | **GET** /api/v2/reports | Get all reports
[**get_all_reports1**](ReportsApi.md#get_all_reports1) | **GET** /api/v1/reports | Get all reports
[**get_report**](ReportsApi.md#get_report) | **GET** /api/v2/reports/{id} | Get report
[**get_report1**](ReportsApi.md#get_report1) | **GET** /api/v1/reports/{id} | Get report
[**update_report_by_id**](ReportsApi.md#update_report_by_id) | **PUT** /api/v2/reports/{id} | Update report
[**update_report_by_id1**](ReportsApi.md#update_report_by_id1) | **PUT** /api/v1/reports/{id} | Update report


# **create_report**
> ReportDto create_report(report)

Create report

Creates a new report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
report = swagger_client.ReportRequestDto() # ReportRequestDto | Report object that will be added to the database

try:
    # Create report
    api_response = api_instance.create_report(report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->create_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report** | [**ReportRequestDto**](ReportRequestDto.md)| Report object that will be added to the database | 

### Return type

[**ReportDto**](ReportDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_report1**
> ReportDto create_report1(report)

Create report

Creates a new report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
report = swagger_client.ReportRequestDto() # ReportRequestDto | Report object that will be added to the database

try:
    # Create report
    api_response = api_instance.create_report1(report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->create_report1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report** | [**ReportRequestDto**](ReportRequestDto.md)| Report object that will be added to the database | 

### Return type

[**ReportDto**](ReportDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report_by_id**
> ResponseEntity delete_report_by_id(id)

Delete report

Deletes an existing report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
id = 789 # int | The id of the report to be deleted

try:
    # Delete report
    api_response = api_instance.delete_report_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->delete_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report_by_id1**
> ResponseEntity delete_report_by_id1(id)

Delete report

Deletes an existing report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
id = 789 # int | The id of the report to be deleted

try:
    # Delete report
    api_response = api_instance.delete_report_by_id1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->delete_report_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report to be deleted | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_report_folders**
> PagerReportFolderDto get_all_report_folders(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get all report folders

Endpoint for retrieving all report folders that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get all report folders
    api_response = api_instance.get_all_report_folders(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_all_report_folders: %s\n" % e)
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

[**PagerReportFolderDto**](PagerReportFolderDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_report_folders1**
> PagerReportFolderDto get_all_report_folders1(page=page, size=size)

Get all report folders

Endpoint for retrieving all report folders that supports pagination

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)

try:
    # Get all report folders
    api_response = api_instance.get_all_report_folders1(page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_all_report_folders1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]

### Return type

[**PagerReportFolderDto**](PagerReportFolderDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_reports**
> PagerReportDto get_all_reports(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields, user_id=user_id, name=name)

Get all reports

Endpoint for retrieving all reports that supports pagination.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)
user_id = 789 # int | Filter by owner id (optional)
name = 'name_example' # str | Filter by report name (optional)

try:
    # Get all reports
    api_response = api_instance.get_all_reports(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields, user_id=user_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_all_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **include_count** | **bool**| Whether to query for total elements count; defaults to true, set to false for performance boost | [optional] 
 **sort_by** | **str**| String array of format \&quot;parameter, -parameter, natural\\*parameter, -natural\\*parameter\&quot;, where minus is for descending, natural* is for natural sort | [optional] 
 **fields** | **str**| String array of format \&quot;id,name,objects(id,pluginId)\&quot;; Defines which fields are returned  | [optional] 
 **user_id** | **int**| Filter by owner id | [optional] 
 **name** | **str**| Filter by report name | [optional] 

### Return type

[**PagerReportDto**](PagerReportDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_reports1**
> PagerReportDto get_all_reports1(page=page, size=size, user_id=user_id, name=name)

Get all reports

Endpoint for retrieving all reports that supports pagination.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
user_id = 789 # int | Filter by owner id (optional)
name = 'name_example' # str | Filter by report name (optional)

try:
    # Get all reports
    api_response = api_instance.get_all_reports1(page=page, size=size, user_id=user_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_all_reports1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the requested page, defaults to 0 | [optional] [default to 0]
 **size** | **int**| The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) | [optional] [default to 20]
 **user_id** | **int**| Filter by owner id | [optional] 
 **name** | **str**| Filter by report name | [optional] 

### Return type

[**PagerReportDto**](PagerReportDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report**
> ReportDto get_report(id)

Get report

Endpoint for retrieving all report info.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
id = 789 # int | Report Id

try:
    # Get report
    api_response = api_instance.get_report(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Report Id | 

### Return type

[**ReportDto**](ReportDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report1**
> ReportDto get_report1(id)

Get report

Endpoint for retrieving all report info.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
id = 789 # int | Report Id

try:
    # Get report
    api_response = api_instance.get_report1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_report1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Report Id | 

### Return type

[**ReportDto**](ReportDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_by_id**
> ReportDto update_report_by_id(id, report)

Update report

Updates an existing report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
id = 789 # int | The id of the report to be updated
report = swagger_client.ReportRequestDto() # ReportRequestDto | Report to be updated

try:
    # Update report
    api_response = api_instance.update_report_by_id(id, report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->update_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report to be updated | 
 **report** | [**ReportRequestDto**](ReportRequestDto.md)| Report to be updated | 

### Return type

[**ReportDto**](ReportDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_by_id1**
> ReportDto update_report_by_id1(id, report)

Update report

Updates an existing report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
id = 789 # int | The id of the report to be updated
report = swagger_client.ReportRequestDto() # ReportRequestDto | Report to be updated

try:
    # Update report
    api_response = api_instance.update_report_by_id1(id, report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->update_report_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report to be updated | 
 **report** | [**ReportRequestDto**](ReportRequestDto.md)| Report to be updated | 

### Return type

[**ReportDto**](ReportDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

