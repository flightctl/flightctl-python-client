# InternalTaskPermanentlyFailedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_type** | **str** | The type of detail for discriminator purposes. | 
**error_message** | **str** | The error message describing the permanent failure. | 
**retry_count** | **int** | Number of times the task was retried before being marked as permanently failed. | 
**original_event** | [**Event**](Event.md) |  | 

## Example

```python
from flightctl.models.internal_task_permanently_failed_details import InternalTaskPermanentlyFailedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTaskPermanentlyFailedDetails from a JSON string
internal_task_permanently_failed_details_instance = InternalTaskPermanentlyFailedDetails.from_json(json)
# print the JSON string representation of the object
print(InternalTaskPermanentlyFailedDetails.to_json())

# convert the object into a dict
internal_task_permanently_failed_details_dict = internal_task_permanently_failed_details_instance.to_dict()
# create an instance of InternalTaskPermanentlyFailedDetails from a dict
internal_task_permanently_failed_details_from_dict = InternalTaskPermanentlyFailedDetails.from_dict(internal_task_permanently_failed_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


