# VmApplication

A VM workload managed by the FlightCtl agent. The VM definition may be delivered either as an OCI image/artifact or as inline application content. For inline providers, the package must contain a KubeVirt VirtualMachine YAML file named vm.yaml.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The application name must be 1–253 characters long, start with a letter or number, and contain no whitespace. | [optional] 
**app_type** | [**AppType**](AppType.md) |  | 
**annotations** | **Dict[str, str]** | Arbitrary metadata annotations. Used internally by the control plane (e.g., flightctl.io/workload-type) when transforming application types at render time. | [optional] [readonly] 
**desired_state** | [**ApplicationDesiredState**](ApplicationDesiredState.md) | Desired lifecycle state for this application, as most recently set by the stop/start device APIs. Read-only: cannot be set directly by apply; only present in the rendered application spec delivered to the agent. | [optional] [readonly] 
**restart_generation** | **int** | Counter incremented by the restart device API each time the application is restarted. Read-only: cannot be set directly by apply; only present in the rendered application spec delivered to the agent. | [optional] [readonly] 
**publish_ports** | **List[str]** | List of host-to-guest port mappings for the VM. Each entry must follow the format \&quot;hostPort:guestPort\&quot; or \&quot;hostPort:guestPort/protocol\&quot; (e.g. \&quot;8080:80\&quot; or \&quot;8080:80/tcp\&quot;). | [optional] 
**image** | **str** | Reference to an OCI image or artifact with tag. | 
**inline** | [**List[ApplicationContent]**](ApplicationContent.md) | A list of application content. | 

## Example

```python
from flightctl.models.vm_application import VmApplication

# TODO update the JSON string below
json = "{}"
# create an instance of VmApplication from a JSON string
vm_application_instance = VmApplication.from_json(json)
# print the JSON string representation of the object
print(VmApplication.to_json())

# convert the object into a dict
vm_application_dict = vm_application_instance.to_dict()
# create an instance of VmApplication from a dict
vm_application_from_dict = VmApplication.from_dict(vm_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


