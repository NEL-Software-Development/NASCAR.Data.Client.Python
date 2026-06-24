# SeasonSeries

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**race_season** | **int** | Race Season as a 4 digit year (e.g. 2024) | [optional] 
**series_id** | **int** | The series ID | [optional] 
**number_of_races** | **int** | Total number of races in the season for the series | [optional] 
**champion_driver** | **str** | Champion driver name for the season and series. | [optional] 
**champion_driver_details** | **str** | Navigation URL to get champion driver details from the NASCAR Data API. This will be null if champion_driver_api_id is not set. | [optional] 
**champion_driver_api_id** | **int** | Champion driver API ID for the season and series. This will be -1 if the driver is not known by the Data API. This can be used to get champion driver details from the NASCAR Data API. | [optional] 
**champion_owner** | **str** | Owner name related to the champion driver for the season and series. | [optional] 
**champion_crew_chief** | **str** | Crew Chief name related to the champion driver for the season and series. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

