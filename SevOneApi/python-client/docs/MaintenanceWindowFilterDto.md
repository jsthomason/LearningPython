# MaintenanceWindowFilterDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **list[str]** | Match maintenance window with any of these actions -- SUPPRESS_ALERT_NOTIFICATIONS (SevOne will not send notification emails or traps for alerts occurring during this maintenance window), CATEGORIZE_ALERTS (Prepend &#39;Maintenance Window&#39; to alerts overlapping this maintenance window and downgrade severity levels higher than Info), EXCLUDE_DATA_FROM_BASELINES (Exclude data during the maintenance window from baseline calculations), EXCLUDE_DATA_FROM_AGGREGATION (Exclude data during the maintenance window from aggregation calculations) | [optional] 
**begin_date_after** | **str** | Match maintenance windows beginning after this time | [optional] 
**begin_date_before** | **str** | Match maintenance windows beginning before this time | [optional] 
**create_date_after** | **str** | Match maintenance windows created after this time | [optional] 
**create_date_before** | **str** | Match maintenance windows created before this time | [optional] 
**device_ids** | **list[int]** | Match maintenance windows for any of these device IDs | [optional] 
**end_date_after** | **str** | Match maintenance windows ending after this time | [optional] 
**end_date_before** | **str** | Match maintenance windows ending before this time | [optional] 
**is_retroactive** | **bool** | Match maintenance windows created after the begin time | [optional] 
**name** | **str** | Match maintenance windows whose name contains this substring | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


