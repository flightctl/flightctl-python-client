# DeviceGpu

Information about a GPU device discovered on the device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Zero-based enumeration index of the GPU on the system, assigned in PCI bus discovery order. |
**vendor** | **str** | The GPU vendor name (e.g., \&quot;NVIDIA\&quot;, \&quot;AMD\&quot;, \&quot;Intel\&quot;). | [optional]
**model** | **str** | The GPU model name (e.g., \&quot;RTX 4090\&quot;, \&quot;GA10B\&quot;). | [optional]
**pci_device_id** | **str** | PCI device ID of the GPU, as read from the PCI configuration register (e.g., \&quot;0x2717\&quot;). | [optional]
**pci_address** | **str** | PCI bus address in BDF notation (e.g., \&quot;0000:01:00.0\&quot;). | [optional]
**pci_revision_id** | **str** | PCI revision ID of the GPU (e.g., \&quot;0xa1\&quot;). | [optional]
**pci_vendor_id** | **str** | PCI vendor ID of the GPU (e.g., \&quot;0x10de\&quot; for NVIDIA). | [optional]
**memory_bytes** | **int** | The amount of GPU memory in bytes. | [optional]
**arch** | **str** | GPU microarchitecture generation name as defined in the hardware map or platform lookup table (e.g., \&quot;Ada\&quot;, \&quot;Ampere\&quot;, \&quot;Volta\&quot;, \&quot;Maxwell\&quot; for NVIDIA; \&quot;RDNA3\&quot;, \&quot;CDNA3\&quot; for AMD). This is the vendor marketing name for the GPU microarchitecture, not the host CPU ISA or a compute-capability version string. | [optional]
**features** | **List[str]** | Vendor-specific GPU capability identifiers sourced from the hardware map. Values are lowercase tokens describing supported compute or display features (e.g., \&quot;cuda\&quot;, \&quot;rocm\&quot;, \&quot;opencl\&quot;, \&quot;sriov\&quot;, \&quot;mig\&quot;). The vocabulary is extensible and determined by the hardware map; no fixed enum is enforced. | [optional]

## Example

```python
from flightctl.models.device_gpu import DeviceGpu

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceGpu from a JSON string
device_gpu_instance = DeviceGpu.from_json(json)
# print the JSON string representation of the object
print(DeviceGpu.to_json())

# convert the object into a dict
device_gpu_dict = device_gpu_instance.to_dict()
# create an instance of DeviceGpu from a dict
device_gpu_from_dict = DeviceGpu.from_dict(device_gpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
