# swagger_client.RunReportAttachmentsApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_flow_falcon_pm**](RunReportAttachmentsApi.md#create_flow_falcon_pm) | **POST** /api/v2/reports/attachments/flow-falcon/performance-metrics/run | Create performance metrics flow falcon report
[**create_flow_falcon_top_n**](RunReportAttachmentsApi.md#create_flow_falcon_top_n) | **POST** /api/v2/reports/attachments/flow-falcon/topn/run | Create TopN flow falcon report
[**run_alert_attachment**](RunReportAttachmentsApi.md#run_alert_attachment) | **GET** /api/v2/reports/attachments/alerts/{id}/run | Run alert attachment
[**run_alert_report**](RunReportAttachmentsApi.md#run_alert_report) | **POST** /api/v2/reports/attachments/alerts/run | Run alert report
[**run_flow_falcon_attachment**](RunReportAttachmentsApi.md#run_flow_falcon_attachment) | **GET** /api/v2/reports/attachments/flow-falcon/{id}/run | Run a flow falcon attachment
[**run_flow_falcon_report**](RunReportAttachmentsApi.md#run_flow_falcon_report) | **POST** /api/v2/reports/attachments/flow-falcon/run | Run a flow falcon report
[**run_performance_metrics_attachment**](RunReportAttachmentsApi.md#run_performance_metrics_attachment) | **POST** /api/v2/reports/attachments/performance-metrics/run | Run performance metrics attachment
[**run_performance_metrics_attachment_by_id**](RunReportAttachmentsApi.md#run_performance_metrics_attachment_by_id) | **GET** /api/v2/reports/attachments/performance-metrics/{id}/run | Run performance metrics attachment
[**run_top_n_attachment**](RunReportAttachmentsApi.md#run_top_n_attachment) | **POST** /api/v2/reports/attachments/topn/run | Run topn attachment
[**run_top_n_attachment1**](RunReportAttachmentsApi.md#run_top_n_attachment1) | **GET** /api/v2/reports/attachments/topn/{id}/run | Run topn attachment
[**run_topology_attachment**](RunReportAttachmentsApi.md#run_topology_attachment) | **GET** /api/v2/reports/attachments/topology/{id}/run | Run a topology attachment
[**run_topology_report**](RunReportAttachmentsApi.md#run_topology_report) | **POST** /api/v2/reports/attachments/topology/run | Run a topology attachment


# **create_flow_falcon_pm**
> FlowFalconReportResponseDto create_flow_falcon_pm(flow_falcon_request_dto)

Create performance metrics flow falcon report

Create performance metrics flow falcon report

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunReportAttachmentsApi()
flow_falcon_request_dto = swagger_client.FlowFalconPerformanceMetricsRequestDto() # FlowFalconPerformanceMetricsRequestDto | FlowFalcon report request object

try:
    # Create performance metrics flow falcon report
    api_response = api_instance.create_flow_falcon_pm(flow_falcon_request_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunReportAttachmentsApi->create_flow_falcon_pm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_falcon_request_dto** | [**FlowFalconPerformanceMetricsRequestDto**](FlowFalconPerformanceMetricsRequestDto.md)| FlowFalcon report request object | 

### Return type

[**FlowFalconReportResponseDto**](FlowFalconReportResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_flow_falcon_top_n**
> FlowFalconReportResponseDto create_flow_falcon_top_n(flow_falcon_request_dto)

Create TopN flow falcon report

Create TopN flow falcon report

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunReportAttachmentsApi()
flow_falcon_request_dto = swagger_client.FlowFalconReportRequestDto() # FlowFalconReportRequestDto | FlowFalcon report request object

try:
    # Create TopN flow falcon report
    api_response = api_instance.create_flow_falcon_top_n(flow_falcon_request_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunReportAttachmentsApi->create_flow_falcon_top_n: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_falcon_request_dto** | [**FlowFalconReportRequestDto**](FlowFalconReportRequestDto.md)| FlowFalcon report request object | 

### Return type

[**FlowFalconReportResponseDto**](FlowFalconReportResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_alert_attachment**
> AlertReportResponseDto run_alert_attachment(id)

Run alert attachment

Run alert attachment. <br/><br/>By default the alert report would include two additional filters: alertStatus = \"open\" and showIgnored = \"off\". You can override this behavior by giving explicit values for one or both of those filters. If you want to disable them, just add filters alertStatus = \"both\" and showIgnored = \"both\".

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunReportAttachmentsApi()
id = 789 # int | The id of the report attachment

try:
    # Run alert attachment
    api_response = api_instance.run_alert_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunReportAttachmentsApi->run_alert_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 

### Return type

[**AlertReportResponseDto**](AlertReportResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_alert_report**
> AlertReportResponseDto run_alert_report(attachment)

Run alert report

Run alert report. <br/><br/>By default the alert report would include two additional filters: alertStatus = \"open\" and showIgnored = \"off\". You can override this behavior by giving explicit values for one or both of those filters. If you want to disable them, just add filters alertStatus = \"both\" and showIgnored = \"both\".

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunReportAttachmentsApi()
attachment = swagger_client.AlertAttachmentDto() # AlertAttachmentDto | Alert attachment

try:
    # Run alert report
    api_response = api_instance.run_alert_report(attachment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunReportAttachmentsApi->run_alert_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment** | [**AlertAttachmentDto**](AlertAttachmentDto.md)| Alert attachment | 

### Return type

[**AlertReportResponseDto**](AlertReportResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_flow_falcon_attachment**
> FlowFalconAttachmentDto run_flow_falcon_attachment(id)

Run a flow falcon attachment

Run a flow falcon attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunReportAttachmentsApi()
id = 789 # int | The id of the report attachment

try:
    # Run a flow falcon attachment
    api_response = api_instance.run_flow_falcon_attachment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunReportAttachmentsApi->run_flow_falcon_attachment: %s\n" % e)
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

# **run_flow_falcon_report**
> FlowFalconAttachmentResponseDto run_flow_falcon_report(dto)

Run a flow falcon report

Run a flow falcon report

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunReportAttachmentsApi()
dto = swagger_client.FlowFalconAttachmentDto() # FlowFalconAttachmentDto | FlowFalcon attachment object

try:
    # Run a flow falcon report
    api_response = api_instance.run_flow_falcon_report(dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunReportAttachmentsApi->run_flow_falcon_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dto** | [**FlowFalconAttachmentDto**](FlowFalconAttachmentDto.md)| FlowFalcon attachment object | 

### Return type

[**FlowFalconAttachmentResponseDto**](FlowFalconAttachmentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_performance_metrics_attachment**
> PerformanceMetricsResultDto run_performance_metrics_attachment(performance_metric_attachment, skip_null_points=skip_null_points, graph_width=graph_width, max_indicators=max_indicators)

Run performance metrics attachment

Run a performance metrics attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunReportAttachmentsApi()
performance_metric_attachment = swagger_client.PerformanceMetricsDto() # PerformanceMetricsDto | Performance metrics attachment object
skip_null_points = true # bool | skipNullPoints (optional) (default to true)
graph_width = 800 # int | Graph width allows overriding in auto aggregation calculation, where the aggregation interval is calculated as (endTime - startTime) / graphWidth (optional) (default to 800)
max_indicators = 56 # int | Report will fail if resources resolve to more than maxIndicators number of indicators (optional)

try:
    # Run performance metrics attachment
    api_response = api_instance.run_performance_metrics_attachment(performance_metric_attachment, skip_null_points=skip_null_points, graph_width=graph_width, max_indicators=max_indicators)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunReportAttachmentsApi->run_performance_metrics_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performance_metric_attachment** | [**PerformanceMetricsDto**](PerformanceMetricsDto.md)| Performance metrics attachment object | 
 **skip_null_points** | **bool**| skipNullPoints | [optional] [default to true]
 **graph_width** | **int**| Graph width allows overriding in auto aggregation calculation, where the aggregation interval is calculated as (endTime - startTime) / graphWidth | [optional] [default to 800]
 **max_indicators** | **int**| Report will fail if resources resolve to more than maxIndicators number of indicators | [optional] 

### Return type

[**PerformanceMetricsResultDto**](PerformanceMetricsResultDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_performance_metrics_attachment_by_id**
> PerformanceMetricsResultDto run_performance_metrics_attachment_by_id(id, skip_null_points=skip_null_points, graph_width=graph_width, max_indicators=max_indicators)

Run performance metrics attachment

Run a performance metrics attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunReportAttachmentsApi()
id = 789 # int | Performance metrics attachment id
skip_null_points = true # bool | skipNullPoints (optional) (default to true)
graph_width = 800 # int | Graph width allows overriding in auto aggregation calculation, where the aggregation interval is calculated as (endTime - startTime) / graphWidth (optional) (default to 800)
max_indicators = 56 # int | Report will fail if resources resolve to more than maxIndicators number of indicators (optional)

try:
    # Run performance metrics attachment
    api_response = api_instance.run_performance_metrics_attachment_by_id(id, skip_null_points=skip_null_points, graph_width=graph_width, max_indicators=max_indicators)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunReportAttachmentsApi->run_performance_metrics_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Performance metrics attachment id | 
 **skip_null_points** | **bool**| skipNullPoints | [optional] [default to true]
 **graph_width** | **int**| Graph width allows overriding in auto aggregation calculation, where the aggregation interval is calculated as (endTime - startTime) / graphWidth | [optional] [default to 800]
 **max_indicators** | **int**| Report will fail if resources resolve to more than maxIndicators number of indicators | [optional] 

### Return type

[**PerformanceMetricsResultDto**](PerformanceMetricsResultDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_top_n_attachment**
> TopNRunReportResultDto run_top_n_attachment(resources)

Run topn attachment

Run topn attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunReportAttachmentsApi()
resources = swagger_client.TopNRunReportRequestDto() # TopNRunReportRequestDto | TopN attachment

try:
    # Run topn attachment
    api_response = api_instance.run_top_n_attachment(resources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunReportAttachmentsApi->run_top_n_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resources** | [**TopNRunReportRequestDto**](TopNRunReportRequestDto.md)| TopN attachment | 

### Return type

[**TopNRunReportResultDto**](TopNRunReportResultDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_top_n_attachment1**
> TopNRunReportResultDto run_top_n_attachment1(id)

Run topn attachment

Run topn attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunReportAttachmentsApi()
id = 789 # int | TopN attachment id

try:
    # Run topn attachment
    api_response = api_instance.run_top_n_attachment1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunReportAttachmentsApi->run_top_n_attachment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| TopN attachment id | 

### Return type

[**TopNRunReportResultDto**](TopNRunReportResultDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_topology_attachment**
> TopologyAttachmentResponseDto run_topology_attachment(id, include_layout=include_layout, include_device_data=include_device_data)

Run a topology attachment

Run a topology attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunReportAttachmentsApi()
id = 789 # int | The id of the report attachment
include_layout = true # bool | Include topology layout data (optional) (default to true)
include_device_data = true # bool | Include device data (optional) (default to true)

try:
    # Run a topology attachment
    api_response = api_instance.run_topology_attachment(id, include_layout=include_layout, include_device_data=include_device_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunReportAttachmentsApi->run_topology_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the report attachment | 
 **include_layout** | **bool**| Include topology layout data | [optional] [default to true]
 **include_device_data** | **bool**| Include device data | [optional] [default to true]

### Return type

[**TopologyAttachmentResponseDto**](TopologyAttachmentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_topology_report**
> TopologyAttachmentResponseDto run_topology_report(dto, include_layout=include_layout, include_device_data=include_device_data)

Run a topology attachment

Run a topology attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RunReportAttachmentsApi()
dto = swagger_client.TopologyAttachmentDto() # TopologyAttachmentDto | Topology attachment object
include_layout = true # bool | Include topology layout data (optional) (default to true)
include_device_data = true # bool | Include device data (optional) (default to true)

try:
    # Run a topology attachment
    api_response = api_instance.run_topology_report(dto, include_layout=include_layout, include_device_data=include_device_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunReportAttachmentsApi->run_topology_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dto** | [**TopologyAttachmentDto**](TopologyAttachmentDto.md)| Topology attachment object | 
 **include_layout** | **bool**| Include topology layout data | [optional] [default to true]
 **include_device_data** | **bool**| Include device data | [optional] [default to true]

### Return type

[**TopologyAttachmentResponseDto**](TopologyAttachmentResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

