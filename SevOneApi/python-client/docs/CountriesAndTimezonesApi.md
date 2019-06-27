# swagger_client.CountriesAndTimezonesApi

All URIs are relative to *https://qdc-sevone.qdx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_timezones_by_countries**](CountriesAndTimezonesApi.md#get_timezones_by_countries) | **GET** /api/v1/countries/timezones | Get timezones
[**get_timezones_by_countries1**](CountriesAndTimezonesApi.md#get_timezones_by_countries1) | **GET** /api/v2/countries/timezones | Get timezones


# **get_timezones_by_countries**
> list[TimezoneDto] get_timezones_by_countries()

Get timezones

Endpoint for retrieving all timezones for the enabled countries

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CountriesAndTimezonesApi()

try:
    # Get timezones
    api_response = api_instance.get_timezones_by_countries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesAndTimezonesApi->get_timezones_by_countries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TimezoneDto]**](TimezoneDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timezones_by_countries1**
> list[TimezoneDto] get_timezones_by_countries1()

Get timezones

Endpoint for retrieving all timezones for the enabled countries

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CountriesAndTimezonesApi()

try:
    # Get timezones
    api_response = api_instance.get_timezones_by_countries1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesAndTimezonesApi->get_timezones_by_countries1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TimezoneDto]**](TimezoneDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

