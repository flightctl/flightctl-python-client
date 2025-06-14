# flightctl
[Flight Control](https://flightctl.io) is a service for declarative management of fleets of edge devices and their workloads.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1alpha1
- Package version: 1.0.0
- Generator version: 7.11.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://flightctl.io](https://flightctl.io)

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/flightctl/python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/flightctl/python-client.git`)

Then import the package:
```python
import flightctl
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import flightctl
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import flightctl
from flightctl.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flightctl.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with flightctl.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flightctl.AuthenticationApi(api_client)

    try:
        api_response = api_instance.auth_config()
        print("The response of AuthenticationApi->auth_config:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->auth_config: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**auth_config**](docs/AuthenticationApi.md#auth_config) | **GET** /api/v1/auth/config | 
*AuthenticationApi* | [**auth_validate**](docs/AuthenticationApi.md#auth_validate) | **GET** /api/v1/auth/validate | 
*CertificatesigningrequestApi* | [**create_certificate_signing_request**](docs/CertificatesigningrequestApi.md#create_certificate_signing_request) | **POST** /api/v1/certificatesigningrequests | 
*CertificatesigningrequestApi* | [**delete_certificate_signing_request**](docs/CertificatesigningrequestApi.md#delete_certificate_signing_request) | **DELETE** /api/v1/certificatesigningrequests/{name} | 
*CertificatesigningrequestApi* | [**get_certificate_signing_request**](docs/CertificatesigningrequestApi.md#get_certificate_signing_request) | **GET** /api/v1/certificatesigningrequests/{name} | 
*CertificatesigningrequestApi* | [**list_certificate_signing_requests**](docs/CertificatesigningrequestApi.md#list_certificate_signing_requests) | **GET** /api/v1/certificatesigningrequests | 
*CertificatesigningrequestApi* | [**patch_certificate_signing_request**](docs/CertificatesigningrequestApi.md#patch_certificate_signing_request) | **PATCH** /api/v1/certificatesigningrequests/{name} | 
*CertificatesigningrequestApi* | [**replace_certificate_signing_request**](docs/CertificatesigningrequestApi.md#replace_certificate_signing_request) | **PUT** /api/v1/certificatesigningrequests/{name} | 
*CertificatesigningrequestApi* | [**update_certificate_signing_request_approval**](docs/CertificatesigningrequestApi.md#update_certificate_signing_request_approval) | **PUT** /api/v1/certificatesigningrequests/{name}/approval | 
*DeviceApi* | [**create_device**](docs/DeviceApi.md#create_device) | **POST** /api/v1/devices | 
*DeviceApi* | [**decommission_device**](docs/DeviceApi.md#decommission_device) | **PUT** /api/v1/devices/{name}/decommission | 
*DeviceApi* | [**delete_device**](docs/DeviceApi.md#delete_device) | **DELETE** /api/v1/devices/{name} | 
*DeviceApi* | [**get_device**](docs/DeviceApi.md#get_device) | **GET** /api/v1/devices/{name} | 
*DeviceApi* | [**get_device_status**](docs/DeviceApi.md#get_device_status) | **GET** /api/v1/devices/{name}/status | 
*DeviceApi* | [**get_rendered_device**](docs/DeviceApi.md#get_rendered_device) | **GET** /api/v1/devices/{name}/rendered | 
*DeviceApi* | [**list_devices**](docs/DeviceApi.md#list_devices) | **GET** /api/v1/devices | 
*DeviceApi* | [**patch_device**](docs/DeviceApi.md#patch_device) | **PATCH** /api/v1/devices/{name} | 
*DeviceApi* | [**patch_device_status**](docs/DeviceApi.md#patch_device_status) | **PATCH** /api/v1/devices/{name}/status | 
*DeviceApi* | [**replace_device**](docs/DeviceApi.md#replace_device) | **PUT** /api/v1/devices/{name} | 
*DeviceApi* | [**replace_device_status**](docs/DeviceApi.md#replace_device_status) | **PUT** /api/v1/devices/{name}/status | 
*EnrollmentrequestApi* | [**approve_enrollment_request**](docs/EnrollmentrequestApi.md#approve_enrollment_request) | **PUT** /api/v1/enrollmentrequests/{name}/approval | 
*EnrollmentrequestApi* | [**create_enrollment_request**](docs/EnrollmentrequestApi.md#create_enrollment_request) | **POST** /api/v1/enrollmentrequests | 
*EnrollmentrequestApi* | [**delete_enrollment_request**](docs/EnrollmentrequestApi.md#delete_enrollment_request) | **DELETE** /api/v1/enrollmentrequests/{name} | 
*EnrollmentrequestApi* | [**get_enrollment_config**](docs/EnrollmentrequestApi.md#get_enrollment_config) | **GET** /api/v1/enrollmentconfig | 
*EnrollmentrequestApi* | [**get_enrollment_request**](docs/EnrollmentrequestApi.md#get_enrollment_request) | **GET** /api/v1/enrollmentrequests/{name} | 
*EnrollmentrequestApi* | [**get_enrollment_request_status**](docs/EnrollmentrequestApi.md#get_enrollment_request_status) | **GET** /api/v1/enrollmentrequests/{name}/status | 
*EnrollmentrequestApi* | [**list_enrollment_requests**](docs/EnrollmentrequestApi.md#list_enrollment_requests) | **GET** /api/v1/enrollmentrequests | 
*EnrollmentrequestApi* | [**patch_enrollment_request**](docs/EnrollmentrequestApi.md#patch_enrollment_request) | **PATCH** /api/v1/enrollmentrequests/{name} | 
*EnrollmentrequestApi* | [**patch_enrollment_request_status**](docs/EnrollmentrequestApi.md#patch_enrollment_request_status) | **PATCH** /api/v1/enrollmentrequests/{name}/status | 
*EnrollmentrequestApi* | [**replace_enrollment_request**](docs/EnrollmentrequestApi.md#replace_enrollment_request) | **PUT** /api/v1/enrollmentrequests/{name} | 
*EnrollmentrequestApi* | [**replace_enrollment_request_status**](docs/EnrollmentrequestApi.md#replace_enrollment_request_status) | **PUT** /api/v1/enrollmentrequests/{name}/status | 
*EventApi* | [**list_events**](docs/EventApi.md#list_events) | **GET** /api/v1/events | 
*FleetApi* | [**create_fleet**](docs/FleetApi.md#create_fleet) | **POST** /api/v1/fleets | 
*FleetApi* | [**delete_fleet**](docs/FleetApi.md#delete_fleet) | **DELETE** /api/v1/fleets/{name} | 
*FleetApi* | [**delete_template_version**](docs/FleetApi.md#delete_template_version) | **DELETE** /api/v1/fleets/{fleet}/templateversions/{name} | 
*FleetApi* | [**get_fleet**](docs/FleetApi.md#get_fleet) | **GET** /api/v1/fleets/{name} | 
*FleetApi* | [**get_fleet_status**](docs/FleetApi.md#get_fleet_status) | **GET** /api/v1/fleets/{name}/status | 
*FleetApi* | [**get_template_version**](docs/FleetApi.md#get_template_version) | **GET** /api/v1/fleets/{fleet}/templateversions/{name} | 
*FleetApi* | [**list_fleets**](docs/FleetApi.md#list_fleets) | **GET** /api/v1/fleets | 
*FleetApi* | [**list_template_versions**](docs/FleetApi.md#list_template_versions) | **GET** /api/v1/fleets/{fleet}/templateversions | 
*FleetApi* | [**patch_fleet**](docs/FleetApi.md#patch_fleet) | **PATCH** /api/v1/fleets/{name} | 
*FleetApi* | [**patch_fleet_status**](docs/FleetApi.md#patch_fleet_status) | **PATCH** /api/v1/fleets/{name}/status | 
*FleetApi* | [**replace_fleet**](docs/FleetApi.md#replace_fleet) | **PUT** /api/v1/fleets/{name} | 
*FleetApi* | [**replace_fleet_status**](docs/FleetApi.md#replace_fleet_status) | **PUT** /api/v1/fleets/{name}/status | 
*LabelApi* | [**list_labels**](docs/LabelApi.md#list_labels) | **GET** /api/v1/labels | 
*RepositoryApi* | [**create_repository**](docs/RepositoryApi.md#create_repository) | **POST** /api/v1/repositories | 
*RepositoryApi* | [**delete_repository**](docs/RepositoryApi.md#delete_repository) | **DELETE** /api/v1/repositories/{name} | 
*RepositoryApi* | [**get_repository**](docs/RepositoryApi.md#get_repository) | **GET** /api/v1/repositories/{name} | 
*RepositoryApi* | [**list_repositories**](docs/RepositoryApi.md#list_repositories) | **GET** /api/v1/repositories | 
*RepositoryApi* | [**patch_repository**](docs/RepositoryApi.md#patch_repository) | **PATCH** /api/v1/repositories/{name} | 
*RepositoryApi* | [**replace_repository**](docs/RepositoryApi.md#replace_repository) | **PUT** /api/v1/repositories/{name} | 
*ResourcesyncApi* | [**create_resource_sync**](docs/ResourcesyncApi.md#create_resource_sync) | **POST** /api/v1/resourcesyncs | 
*ResourcesyncApi* | [**delete_resource_sync**](docs/ResourcesyncApi.md#delete_resource_sync) | **DELETE** /api/v1/resourcesyncs/{name} | 
*ResourcesyncApi* | [**get_resource_sync**](docs/ResourcesyncApi.md#get_resource_sync) | **GET** /api/v1/resourcesyncs/{name} | 
*ResourcesyncApi* | [**list_resource_syncs**](docs/ResourcesyncApi.md#list_resource_syncs) | **GET** /api/v1/resourcesyncs | 
*ResourcesyncApi* | [**patch_resource_sync**](docs/ResourcesyncApi.md#patch_resource_sync) | **PATCH** /api/v1/resourcesyncs/{name} | 
*ResourcesyncApi* | [**replace_resource_sync**](docs/ResourcesyncApi.md#replace_resource_sync) | **PUT** /api/v1/resourcesyncs/{name} | 
*VersionApi* | [**get_version**](docs/VersionApi.md#get_version) | **GET** /api/version | 


## Documentation For Models

 - [AbsolutePath](docs/AbsolutePath.md)
 - [AppType](docs/AppType.md)
 - [ApplicationContent](docs/ApplicationContent.md)
 - [ApplicationEnvVars](docs/ApplicationEnvVars.md)
 - [ApplicationProviderSpec](docs/ApplicationProviderSpec.md)
 - [ApplicationStatusType](docs/ApplicationStatusType.md)
 - [ApplicationVolume](docs/ApplicationVolume.md)
 - [ApplicationVolumeProviderSpec](docs/ApplicationVolumeProviderSpec.md)
 - [ApplicationVolumeStatus](docs/ApplicationVolumeStatus.md)
 - [ApplicationsSummaryStatusType](docs/ApplicationsSummaryStatusType.md)
 - [AuthConfig](docs/AuthConfig.md)
 - [Batch](docs/Batch.md)
 - [BatchLimit](docs/BatchLimit.md)
 - [BatchSequence](docs/BatchSequence.md)
 - [CertificateSigningRequest](docs/CertificateSigningRequest.md)
 - [CertificateSigningRequestList](docs/CertificateSigningRequestList.md)
 - [CertificateSigningRequestSpec](docs/CertificateSigningRequestSpec.md)
 - [CertificateSigningRequestStatus](docs/CertificateSigningRequestStatus.md)
 - [Condition](docs/Condition.md)
 - [ConditionStatus](docs/ConditionStatus.md)
 - [ConditionType](docs/ConditionType.md)
 - [ConfigProviderSpec](docs/ConfigProviderSpec.md)
 - [CpuResourceMonitorSpec](docs/CpuResourceMonitorSpec.md)
 - [Device](docs/Device.md)
 - [DeviceApplicationStatus](docs/DeviceApplicationStatus.md)
 - [DeviceApplicationsSummaryStatus](docs/DeviceApplicationsSummaryStatus.md)
 - [DeviceConfigStatus](docs/DeviceConfigStatus.md)
 - [DeviceConsole](docs/DeviceConsole.md)
 - [DeviceDecommission](docs/DeviceDecommission.md)
 - [DeviceDecommissionTargetType](docs/DeviceDecommissionTargetType.md)
 - [DeviceIntegrityStatus](docs/DeviceIntegrityStatus.md)
 - [DeviceIntegrityStatusSummaryType](docs/DeviceIntegrityStatusSummaryType.md)
 - [DeviceLifecycleHookType](docs/DeviceLifecycleHookType.md)
 - [DeviceLifecycleStatus](docs/DeviceLifecycleStatus.md)
 - [DeviceLifecycleStatusType](docs/DeviceLifecycleStatusType.md)
 - [DeviceList](docs/DeviceList.md)
 - [DeviceOsSpec](docs/DeviceOsSpec.md)
 - [DeviceOsStatus](docs/DeviceOsStatus.md)
 - [DeviceResourceStatus](docs/DeviceResourceStatus.md)
 - [DeviceResourceStatusType](docs/DeviceResourceStatusType.md)
 - [DeviceSpec](docs/DeviceSpec.md)
 - [DeviceSpecSystemd](docs/DeviceSpecSystemd.md)
 - [DeviceStatus](docs/DeviceStatus.md)
 - [DeviceSummaryStatus](docs/DeviceSummaryStatus.md)
 - [DeviceSummaryStatusType](docs/DeviceSummaryStatusType.md)
 - [DeviceSystemInfo](docs/DeviceSystemInfo.md)
 - [DeviceUpdatePolicySpec](docs/DeviceUpdatePolicySpec.md)
 - [DeviceUpdatedStatus](docs/DeviceUpdatedStatus.md)
 - [DeviceUpdatedStatusType](docs/DeviceUpdatedStatusType.md)
 - [DevicesSummary](docs/DevicesSummary.md)
 - [DiskResourceMonitorSpec](docs/DiskResourceMonitorSpec.md)
 - [DisruptionBudget](docs/DisruptionBudget.md)
 - [EncodingType](docs/EncodingType.md)
 - [EnrollmentConfig](docs/EnrollmentConfig.md)
 - [EnrollmentRequest](docs/EnrollmentRequest.md)
 - [EnrollmentRequestApproval](docs/EnrollmentRequestApproval.md)
 - [EnrollmentRequestApprovalStatus](docs/EnrollmentRequestApprovalStatus.md)
 - [EnrollmentRequestList](docs/EnrollmentRequestList.md)
 - [EnrollmentRequestSpec](docs/EnrollmentRequestSpec.md)
 - [EnrollmentRequestStatus](docs/EnrollmentRequestStatus.md)
 - [EnrollmentService](docs/EnrollmentService.md)
 - [EnrollmentServiceAuth](docs/EnrollmentServiceAuth.md)
 - [EnrollmentServiceService](docs/EnrollmentServiceService.md)
 - [Event](docs/Event.md)
 - [EventDetails](docs/EventDetails.md)
 - [EventList](docs/EventList.md)
 - [EventSource](docs/EventSource.md)
 - [FileContent](docs/FileContent.md)
 - [FileMetadata](docs/FileMetadata.md)
 - [FileOperation](docs/FileOperation.md)
 - [FileSpec](docs/FileSpec.md)
 - [Fleet](docs/Fleet.md)
 - [FleetList](docs/FleetList.md)
 - [FleetRolloutStatus](docs/FleetRolloutStatus.md)
 - [FleetSpec](docs/FleetSpec.md)
 - [FleetSpecTemplate](docs/FleetSpecTemplate.md)
 - [FleetStatus](docs/FleetStatus.md)
 - [GenericRepoSpec](docs/GenericRepoSpec.md)
 - [GitConfigProviderSpec](docs/GitConfigProviderSpec.md)
 - [GitConfigProviderSpecGitRef](docs/GitConfigProviderSpecGitRef.md)
 - [HookAction](docs/HookAction.md)
 - [HookActionRun](docs/HookActionRun.md)
 - [HookCondition](docs/HookCondition.md)
 - [HookConditionPathOp](docs/HookConditionPathOp.md)
 - [HttpConfig](docs/HttpConfig.md)
 - [HttpConfigProviderSpec](docs/HttpConfigProviderSpec.md)
 - [HttpConfigProviderSpecHttpRef](docs/HttpConfigProviderSpecHttpRef.md)
 - [HttpRepoSpec](docs/HttpRepoSpec.md)
 - [ImageApplicationProviderSpec](docs/ImageApplicationProviderSpec.md)
 - [ImagePullPolicy](docs/ImagePullPolicy.md)
 - [ImageVolumeProviderSpec](docs/ImageVolumeProviderSpec.md)
 - [ImageVolumeSource](docs/ImageVolumeSource.md)
 - [InlineApplicationProviderSpec](docs/InlineApplicationProviderSpec.md)
 - [InlineConfigProviderSpec](docs/InlineConfigProviderSpec.md)
 - [KubernetesSecretProviderSpec](docs/KubernetesSecretProviderSpec.md)
 - [KubernetesSecretProviderSpecSecretRef](docs/KubernetesSecretProviderSpecSecretRef.md)
 - [LabelSelector](docs/LabelSelector.md)
 - [ListMeta](docs/ListMeta.md)
 - [MatchExpression](docs/MatchExpression.md)
 - [MemoryResourceMonitorSpec](docs/MemoryResourceMonitorSpec.md)
 - [ObjectMeta](docs/ObjectMeta.md)
 - [ObjectReference](docs/ObjectReference.md)
 - [PatchRequestInner](docs/PatchRequestInner.md)
 - [RelativePath](docs/RelativePath.md)
 - [RepoSpecType](docs/RepoSpecType.md)
 - [Repository](docs/Repository.md)
 - [RepositoryList](docs/RepositoryList.md)
 - [RepositorySpec](docs/RepositorySpec.md)
 - [RepositoryStatus](docs/RepositoryStatus.md)
 - [ResourceAlertRule](docs/ResourceAlertRule.md)
 - [ResourceAlertSeverityType](docs/ResourceAlertSeverityType.md)
 - [ResourceKind](docs/ResourceKind.md)
 - [ResourceMonitor](docs/ResourceMonitor.md)
 - [ResourceMonitorSpec](docs/ResourceMonitorSpec.md)
 - [ResourceSync](docs/ResourceSync.md)
 - [ResourceSyncList](docs/ResourceSyncList.md)
 - [ResourceSyncSpec](docs/ResourceSyncSpec.md)
 - [ResourceSyncStatus](docs/ResourceSyncStatus.md)
 - [ResourceUpdatedDetails](docs/ResourceUpdatedDetails.md)
 - [RolloutDeviceSelection](docs/RolloutDeviceSelection.md)
 - [RolloutPolicy](docs/RolloutPolicy.md)
 - [RolloutStrategy](docs/RolloutStrategy.md)
 - [SshConfig](docs/SshConfig.md)
 - [SshRepoSpec](docs/SshRepoSpec.md)
 - [Status](docs/Status.md)
 - [TemplateVersion](docs/TemplateVersion.md)
 - [TemplateVersionList](docs/TemplateVersionList.md)
 - [TemplateVersionSpec](docs/TemplateVersionSpec.md)
 - [TemplateVersionStatus](docs/TemplateVersionStatus.md)
 - [UpdateSchedule](docs/UpdateSchedule.md)
 - [Version](docs/Version.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

team@flightctl.io


