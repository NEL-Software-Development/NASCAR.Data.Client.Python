# RaceResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finish_position** | **int** | Finish position | [optional] 
**driver_name** | **str** | Driver name | [optional] 
**vehicle_number** | **str** | Vehicle number | [optional] 
**laps** | **int** | Total number of laps | [optional] 
**best_time** | **int** | Best lap time in milliseconds | [optional] 
**best_speed** | **float** | Best speed in MPH | [optional] 
**best_lap** | **int** | Best lap number | [optional] 
**last_lap_time** | **int** | Last lap time in milliseconds | [optional] 
**delta_next_time** | **int** | Number of milliseconds behind the next position | [optional] 
**delta_next_laps** | **int** | Number of laps behind the next position | [optional] 
**delta_leader_time** | **int** | Number of milliseconds behind the leader | [optional] 
**delta_leader_laps** | **int** | Number of laps behind the leader | [optional] 
**on_track** | **bool** | Indicates whether the vehicle is currently on track | [optional] 
**is_on_dvp** | **bool** | Indicates whether the vehicle is currently on the DVP clock | [optional] 
**status** | **str** | Vehicle status (0&#x3D;None, 1&#x3D;Active, 2&#x3D;DNS, 3&#x3D;DNF, 4&#x3D;DQ, 5&#x3D;Pace Car, 6&#x3D;Garage) | [optional] 
**comment** | **str** | Comment associated with the result | [optional] 
**avg_running_pos** | **float** | Real-time average running position, sourced from the Racing DB for the laps completed so far this run | [optional] 
**avg_speed** | **float** | Real-time average speed (MPH), sourced from the Racing DB for the laps completed so far this run | [optional] 
**fastest_laps_run** | **int** | Real-time count of laps this run in which the vehicle recorded the fastest lap of the field, sourced from the Racing DB | [optional] 
**start_position** | **int** | Start position | [optional] 
**pit_box** | **int** | Pit box assigned to the vehicle for the race | [optional] 
**disqualified** | **bool** | Indicates whether the vehicle was disqualified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

