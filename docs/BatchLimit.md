# BatchLimit

The maximum number or percentage of devices to update in the batch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from flightctl.models.batch_limit import BatchLimit

# TODO update the JSON string below
json = "{}"
# create an instance of BatchLimit from a JSON string
batch_limit_instance = BatchLimit.from_json(json)
# print the JSON string representation of the object
print(BatchLimit.to_json())

# convert the object into a dict
batch_limit_dict = batch_limit_instance.to_dict()
# create an instance of BatchLimit from a dict
batch_limit_from_dict = BatchLimit.from_dict(batch_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


