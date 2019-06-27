# swagger_client.PeersApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_incorporate_mode_using_patch**](PeersApi.md#edit_incorporate_mode_using_patch) | **PATCH** /api/v1/peers/incorporateMode | Edit peer status
[**edit_incorporate_mode_using_patch1**](PeersApi.md#edit_incorporate_mode_using_patch1) | **PATCH** /api/v2/peers/incorporateMode | Edit peer status
[**get_cluster_settings**](PeersApi.md#get_cluster_settings) | **GET** /api/v1/peers/clusterSettings | Get cluster settings
[**get_cluster_settings1**](PeersApi.md#get_cluster_settings1) | **GET** /api/v2/peers/clusterSettings | Get cluster settings
[**get_current_peer_using_get**](PeersApi.md#get_current_peer_using_get) | **GET** /api/v1/peers/current | Current peer
[**get_current_peer_using_get1**](PeersApi.md#get_current_peer_using_get1) | **GET** /api/v2/peers/current | Current peer
[**get_incorporate_mode_using_get**](PeersApi.md#get_incorporate_mode_using_get) | **GET** /api/v1/peers/incorporateMode | Get peer status
[**get_incorporate_mode_using_get1**](PeersApi.md#get_incorporate_mode_using_get1) | **GET** /api/v2/peers/incorporateMode | Get peer status
[**get_peer_using_get**](PeersApi.md#get_peer_using_get) | **GET** /api/v1/peers/{id} | Get peer
[**get_peer_using_get1**](PeersApi.md#get_peer_using_get1) | **GET** /api/v2/peers/{id} | Get peer
[**get_peers_using_get**](PeersApi.md#get_peers_using_get) | **GET** /api/v1/peers | Get peers
[**get_peers_using_get1**](PeersApi.md#get_peers_using_get1) | **GET** /api/v2/peers | Get peers
[**get_settings**](PeersApi.md#get_settings) | **GET** /api/v1/peers/{id}/settings | Get settings
[**get_settings1**](PeersApi.md#get_settings1) | **GET** /api/v2/peers/{id}/settings | Get settings


# **edit_incorporate_mode_using_patch**
> IncorporateResponse edit_incorporate_mode_using_patch(status)

Edit peer status

Edit current peer status - activate or deactivate incorporate mode

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
status = swagger_client.PeerStatus() # PeerStatus | status

try:
    # Edit peer status
    api_response = api_instance.edit_incorporate_mode_using_patch(status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->edit_incorporate_mode_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**PeerStatus**](PeerStatus.md)| status | 

### Return type

[**IncorporateResponse**](IncorporateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_incorporate_mode_using_patch1**
> IncorporateResponse edit_incorporate_mode_using_patch1(status)

Edit peer status

Edit current peer status - activate or deactivate incorporate mode

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
status = swagger_client.PeerStatus() # PeerStatus | status

try:
    # Edit peer status
    api_response = api_instance.edit_incorporate_mode_using_patch1(status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->edit_incorporate_mode_using_patch1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**PeerStatus**](PeerStatus.md)| status | 

### Return type

[**IncorporateResponse**](IncorporateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_settings**
> dict(str, object) get_cluster_settings(filter=filter)

Get cluster settings

Get cluster settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
filter = 'filter_example' # str | Filter to retrieve only subset of cluster settings (optional)

try:
    # Get cluster settings
    api_response = api_instance.get_cluster_settings(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_cluster_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to retrieve only subset of cluster settings | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_settings1**
> dict(str, object) get_cluster_settings1(filter=filter)

Get cluster settings

Get cluster settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
filter = 'filter_example' # str | Filter to retrieve only subset of cluster settings (optional)

try:
    # Get cluster settings
    api_response = api_instance.get_cluster_settings1(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_cluster_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to retrieve only subset of cluster settings | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_peer_using_get**
> PeerDto get_current_peer_using_get()

Current peer

Gets current peer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()

try:
    # Current peer
    api_response = api_instance.get_current_peer_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_current_peer_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PeerDto**](PeerDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_peer_using_get1**
> PeerDto get_current_peer_using_get1()

Current peer

Gets current peer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()

try:
    # Current peer
    api_response = api_instance.get_current_peer_using_get1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_current_peer_using_get1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PeerDto**](PeerDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_incorporate_mode_using_get**
> IncorporateResponse get_incorporate_mode_using_get()

Get peer status

Gets incorporate mode status for current peer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()

try:
    # Get peer status
    api_response = api_instance.get_incorporate_mode_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_incorporate_mode_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IncorporateResponse**](IncorporateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_incorporate_mode_using_get1**
> IncorporateResponse get_incorporate_mode_using_get1()

Get peer status

Gets incorporate mode status for current peer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()

try:
    # Get peer status
    api_response = api_instance.get_incorporate_mode_using_get1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_incorporate_mode_using_get1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IncorporateResponse**](IncorporateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peer_using_get**
> PeerDto get_peer_using_get(id)

Get peer

Gets peer by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
id = 789 # int | The id of the peer

try:
    # Get peer
    api_response = api_instance.get_peer_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_peer_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the peer | 

### Return type

[**PeerDto**](PeerDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peer_using_get1**
> PeerDto get_peer_using_get1(id)

Get peer

Gets peer by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
id = 789 # int | The id of the peer

try:
    # Get peer
    api_response = api_instance.get_peer_using_get1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_peer_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the peer | 

### Return type

[**PeerDto**](PeerDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peers_using_get**
> PagerPeerDto get_peers_using_get(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get peers

Gets all peers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get peers
    api_response = api_instance.get_peers_using_get(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_peers_using_get: %s\n" % e)
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

[**PagerPeerDto**](PagerPeerDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peers_using_get1**
> PagerPeerDto get_peers_using_get1(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)

Get peers

Gets all peers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
page = 0 # int | The number of the requested page, defaults to 0 (optional) (default to 0)
size = 20 # int | The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default) (optional) (default to 20)
include_count = true # bool | Whether to query for total elements count; defaults to true, set to false for performance boost (optional)
sort_by = 'sort_by_example' # str | String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort (optional)
fields = 'fields_example' # str | String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned  (optional)

try:
    # Get peers
    api_response = api_instance.get_peers_using_get1(page=page, size=size, include_count=include_count, sort_by=sort_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_peers_using_get1: %s\n" % e)
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

[**PagerPeerDto**](PagerPeerDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> dict(str, object) get_settings(id, filter=filter)

Get settings

Get settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
id = 789 # int | The id of the peer
filter = 'filter_example' # str | Filter to retrieve only subset of settings (optional)

try:
    # Get settings
    api_response = api_instance.get_settings(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the peer | 
 **filter** | **str**| Filter to retrieve only subset of settings | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings1**
> dict(str, object) get_settings1(id, filter=filter)

Get settings

Get settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PeersApi()
id = 789 # int | The id of the peer
filter = 'filter_example' # str | Filter to retrieve only subset of settings (optional)

try:
    # Get settings
    api_response = api_instance.get_settings1(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeersApi->get_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the peer | 
 **filter** | **str**| Filter to retrieve only subset of settings | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

