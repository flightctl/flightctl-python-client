# DeviceCountsBySeverity

Counts of distinct devices affected in the organization, grouped by vulnerability severity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Number of distinct devices with at least one vulnerability finding in the organization. | 
**critical** | **int** | Number of devices whose highest severity finding is critical. | 
**high** | **int** | Number of devices whose highest severity finding is high. | 
**medium** | **int** | Number of devices whose highest severity finding is medium. | 
**low** | **int** | Number of devices whose highest severity finding is low. | 
**var_none** | **int** | Number of devices whose highest severity finding is none. | 
**unknown** | **int** | Number of devices whose highest severity finding is unknown. | 

## Example

```python
from flightctl.v1alpha1.models.device_counts_by_severity import DeviceCountsBySeverity

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceCountsBySeverity from a JSON string
device_counts_by_severity_instance = DeviceCountsBySeverity.from_json(json)
# print the JSON string representation of the object
print(DeviceCountsBySeverity.to_json())

# convert the object into a dict
device_counts_by_severity_dict = device_counts_by_severity_instance.to_dict()
# create an instance of DeviceCountsBySeverity from a dict
device_counts_by_severity_from_dict = DeviceCountsBySeverity.from_dict(device_counts_by_severity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


