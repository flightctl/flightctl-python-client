# BatchSequence

BatchSequence defines the list of batches to be executed in sequence.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence** | [**List[Batch]**](Batch.md) | A list of batch definitions. | [optional] 

## Example

```python
from flightctl.models.batch_sequence import BatchSequence

# TODO update the JSON string below
json = "{}"
# create an instance of BatchSequence from a JSON string
batch_sequence_instance = BatchSequence.from_json(json)
# print the JSON string representation of the object
print(BatchSequence.to_json())

# convert the object into a dict
batch_sequence_dict = batch_sequence_instance.to_dict()
# create an instance of BatchSequence from a dict
batch_sequence_from_dict = BatchSequence.from_dict(batch_sequence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


