# UpdateSchedule

Defines the schedule for automatic updates, including timing and optional timeout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_zone** | **str** | Time zone identifiers follow the IANA format AREA/LOCATION, where AREA represents a continent or ocean, and LOCATION specifies a particular site within that area, for example America/New_York, Europe/Paris. Only unambiguous 3-character time zones are supported (\&quot;GMT\&quot;, \&quot;UTC\&quot;). | [optional] [default to 'Local']
**at** | **str** | Cron expression format for scheduling times. The format is &#x60;* * * * *&#x60;: - Minutes: &#x60;*&#x60; matches 0-59. - Hours: &#x60;*&#x60; matches 0-23. - Day of Month: &#x60;*&#x60; matches 1-31. - Month: &#x60;*&#x60; matches 1-12. - Day of Week: &#x60;*&#x60; matches 0-6. Supported operators: - &#x60;*&#x60;: Matches any value (e.g., &#x60;*&#x60; in hours matches every hour). - &#x60;-&#x60;: Range (e.g., &#x60;0-8&#x60; for 12 AM to 8 AM). - &#x60;,&#x60;: List (e.g., &#x60;1,12&#x60; for 1st and 12th minute). - &#x60;/&#x60;: Step (e.g., &#x60;*/12&#x60; for every 12th minute). - Single value (e.g., &#x60;8&#x60; matches the 8th minute). Example: &#x60;* 0-8,16-23 * * *&#x60;. | 
**start_grace_duration** | **str** | The maximum duration allowed for the action to complete. The duration should be specified as a positive integer followed by a time unit. Supported time units are: &#x60;s&#x60; for seconds, &#x60;m&#x60; for minutes, &#x60;h&#x60; for hours. | [optional] [default to '0s']

## Example

```python
from flightctl.models.update_schedule import UpdateSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSchedule from a JSON string
update_schedule_instance = UpdateSchedule.from_json(json)
# print the JSON string representation of the object
print(UpdateSchedule.to_json())

# convert the object into a dict
update_schedule_dict = update_schedule_instance.to_dict()
# create an instance of UpdateSchedule from a dict
update_schedule_from_dict = UpdateSchedule.from_dict(update_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


