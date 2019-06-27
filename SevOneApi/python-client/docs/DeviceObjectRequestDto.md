# DeviceObjectRequestDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | 
**plugin_id** | **int** |  | 
**plugin_object_type_id** | **int** |  | 
**poll_frequency** | **int** |  | 
**subtype_id** | **int** |  | [optional] 
**extended_info** | **dict(str, str)** |  | [optional] 
**enabled** | **str** |  | [optional] 
**is_deleted** | **bool** | false | [optional] 
**is_enabled** | **bool** | This field is deprecated and would be removed in a newer version of the API. Please use &#39;enabled&#39; field instead. | [optional] 
**is_visible** | **bool** |  | [optional] 
**indicators** | [**list[IndicatorRequestDto]**](IndicatorRequestDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


