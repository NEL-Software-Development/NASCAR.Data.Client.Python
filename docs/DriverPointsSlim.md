# DriverPointsSlim

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points_position** | **int** | Overall points rank for season | [optional] 
**driver_id** | **int** | Unique NASCAR ID given for each driver | [optional] 
**history_driver_id** | **int** | Unique historical NASCAR ID given for each driver, used for historical data | [optional] 
**driver** | **str** | Driver full name | [optional] 
**driver_abbrev** | **str** | Abbreviated driver name | [optional] 
**car_number** | **str** | Corresponding car number for this driver during this run | [optional] 
**race_pos** | **int** | Position of vehicle in current run | [optional] 
**stage_1_position** | **int** | Finish position of vehicle for stage 1 | [optional] 
**stage_1_points** | **int** | Stage points earned for vehicle for stage 1 | [optional] 
**stage_2_position** | **int** | Finish position of vehicle for stage 2 | [optional] 
**stage_2_points** | **int** | Stage points earned for vehicle for stage 2 | [optional] 
**stage_3_position** | **int** | Finish position of vehicle for stage 3 | [optional] 
**stage_3_points** | **int** | Stage points earned for vehicle for stage 3 | [optional] 
**finish_points** | **int** | Number of points earned based on finish position for this race | [optional] 
**race_points** | **int** | Number of total points earned based on finish position and stage points for this race | [optional] 
**points** | **int** | Total regular season points | [optional] 
**delta_leader** | **int** | Number of points behind the leader | [optional] 
**delta_next** | **int** | Number of points behind the next driver | [optional] 
**in_round** | **bool** | Is this driver in the current round (true or false) | [optional] 
**is_points_eligible** | **bool** | Is driver points eligible for the series (true or false) | [optional] 
**is_post_entry** | **bool** | Is the driver a post-entry for this race | [optional] 
**is_cutline** | **bool** | Cut line below this driver, true for only one record | [optional] 
**is_locked** | **bool** | Locked into the next round | [optional] 
**is_round_eligible** | **bool** | Is eligible for the current round | [optional] 
**tv_sort_order** | **int** | The order displayed on TV (locked drivers sorted by wins desc, then current leader, then all else sorted by total points) | [optional] 
**round_race_wins** | **int** | Wins in current round (round 0, etc.) | [optional] 
**cutline_points_delta** | **int** | Difference to cutline adjacent driver (last driver locked below, and first driver out above) | [optional] 
**stage_wins** | **int** | Stage wins for current season | [optional] 
**poles** | **int** | Number of poles for current season | [optional] 
**attempts** | **int** | Number of attempts to qualify for current season | [optional] 
**wins** | **int** | Number of wins for current season | [optional] 
**top_5** | **int** | Number of top 5 finishes for current season | [optional] 
**top_10** | **int** | Number of top 10 finishes for current season | [optional] 
**is_fastest_lap_point** | **bool** | True if driver earned a point for fastest lap point | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

