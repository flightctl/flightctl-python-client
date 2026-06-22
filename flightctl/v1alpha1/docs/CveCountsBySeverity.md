# CveCountsBySeverity

Counts of distinct CVEs in the organization by highest severity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total distinct CVEs across the organization. | 
**critical** | **int** | Count of distinct Critical CVEs. | 
**high** | **int** | Count of distinct High CVEs. | 
**medium** | **int** | Count of distinct Medium CVEs. | 
**low** | **int** | Count of distinct Low CVEs. | 
**var_none** | **int** | Count of distinct CVEs with no exploitable impact (CVSS score 0). | 
**unknown** | **int** | Count of distinct CVEs with unknown or unscored severity. | 

## Example

```python
from flightctl.v1alpha1.models.cve_counts_by_severity import CveCountsBySeverity

# TODO update the JSON string below
json = "{}"
# create an instance of CveCountsBySeverity from a JSON string
cve_counts_by_severity_instance = CveCountsBySeverity.from_json(json)
# print the JSON string representation of the object
print(CveCountsBySeverity.to_json())

# convert the object into a dict
cve_counts_by_severity_dict = cve_counts_by_severity_instance.to_dict()
# create an instance of CveCountsBySeverity from a dict
cve_counts_by_severity_from_dict = CveCountsBySeverity.from_dict(cve_counts_by_severity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


