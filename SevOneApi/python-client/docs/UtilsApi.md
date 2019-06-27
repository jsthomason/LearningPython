# swagger_client.UtilsApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_unit_infos**](UtilsApi.md#get_unit_infos) | **GET** /api/v2/utils/unitinfos | Get unitinfos


# **get_unit_infos**
> list[UnitInfoDto] get_unit_infos()

Get unitinfos

Get unitinfos

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilsApi()

try:
    # Get unitinfos
    api_response = api_instance.get_unit_infos()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilsApi->get_unit_infos: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UnitInfoDto]**](UnitInfoDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

