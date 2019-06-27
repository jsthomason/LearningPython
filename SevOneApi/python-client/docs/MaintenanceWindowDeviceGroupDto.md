# MaintenanceWindowDeviceGroupDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **list[str]** | List of actions for this maintenance window -- SUPPRESS_ALERT_NOTIFICATIONS (SevOne will not send notification emails or traps for alerts occurring during this maintenance window), CATEGORIZE_ALERTS (Prepend &#39;Maintenance Window&#39; to alerts overlapping this maintenance window and downgrade severity levels higher than Info), EXCLUDE_DATA_FROM_BASELINES (Exclude data during the maintenance window from baseline calculations), EXCLUDE_DATA_FROM_AGGREGATION (Exclude data during the maintenance window from aggregation calculations) | [optional] 
**id** | **str** | Maintenance window UUID -- omit to auto-generate for POST or leave unchanged for PUT | [optional] 
**maintenance_type** | **str** | Type of maintenance window | [optional] 
**mapped_entities** | [**list[MappedDeviceGroupEntityDto]**](MappedDeviceGroupEntityDto.md) |  | [optional] 
**name** | **str** | Name of maintenance window -- must be unique | 
**notes** | **str** | Free form notes | [optional] 
**schedule_instance** | [**ScheduleInstanceDto**](ScheduleInstanceDto.md) | Maintenance window must be scheduled in the future and have a duration of at least 3 minutes | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


