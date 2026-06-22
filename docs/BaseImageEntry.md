# BaseImageEntry

A curated base image entry available in an OCI registry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Human-readable label shown in the UI (e.g., \&quot;CentOS\&quot;). | [optional] 
**image_name** | **str** | Image path within the registry (e.g., \&quot;centos-bootc/centos-bootc\&quot;). | 
**tags** | **List[str]** | Selectable tags for this image (e.g., [\&quot;stream9\&quot;, \&quot;stream10\&quot;]). | 

## Example

```python
from flightctl.models.base_image_entry import BaseImageEntry

# TODO update the JSON string below
json = "{}"
# create an instance of BaseImageEntry from a JSON string
base_image_entry_instance = BaseImageEntry.from_json(json)
# print the JSON string representation of the object
print(BaseImageEntry.to_json())

# convert the object into a dict
base_image_entry_dict = base_image_entry_instance.to_dict()
# create an instance of BaseImageEntry from a dict
base_image_entry_from_dict = BaseImageEntry.from_dict(base_image_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


