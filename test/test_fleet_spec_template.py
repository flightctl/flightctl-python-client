# coding: utf-8

"""
    Flight Control API

    [Flight Control](https://flightctl.io) is a service for declarative management of fleets of edge devices and their workloads. 

    The version of the OpenAPI document: v1alpha1
    Contact: team@flightctl.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flightctl.models.fleet_spec_template import FleetSpecTemplate

class TestFleetSpecTemplate(unittest.TestCase):
    """FleetSpecTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FleetSpecTemplate:
        """Test FleetSpecTemplate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FleetSpecTemplate`
        """
        model = FleetSpecTemplate()
        if include_optional:
            return FleetSpecTemplate(
                metadata = flightctl.models.object_meta.ObjectMeta(
                    creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    name = '', 
                    labels = {
                        'key' : ''
                        }, 
                    generation = 56, 
                    owner = '', 
                    annotations = {
                        'key' : ''
                        }, 
                    resource_version = '', ),
                spec = flightctl.models.device_spec.DeviceSpec(
                    update_policy = flightctl.models.device_update_policy_spec.DeviceUpdatePolicySpec(
                        download_schedule = flightctl.models.update_schedule.UpdateSchedule(
                            time_zone = 'Local', 
                            at = '', 
                            start_grace_duration = '0s', ), 
                        update_schedule = flightctl.models.update_schedule.UpdateSchedule(
                            time_zone = 'Local', 
                            at = '', 
                            start_grace_duration = '0s', ), ), 
                    os = flightctl.models.device_os_spec.DeviceOsSpec(
                        image = '', ), 
                    config = [
                        null
                        ], 
                    applications = [
                        flightctl.models.application_provider_spec.ApplicationProviderSpec()
                        ], 
                    systemd = flightctl.models.device_spec_systemd.DeviceSpec_systemd(
                        match_patterns = [
                            'ge34w9Wa*CLfoo\\yJX2gCb'
                            ], ), 
                    resources = [
                        null
                        ], 
                    consoles = [
                        flightctl.models.device_console.DeviceConsole(
                            session_metadata = '', 
                            session_id = '', )
                        ], 
                    decommissioning = flightctl.models.device_decommission.DeviceDecommission(
                        target = 'Unenroll', ), )
            )
        else:
            return FleetSpecTemplate(
                spec = flightctl.models.device_spec.DeviceSpec(
                    update_policy = flightctl.models.device_update_policy_spec.DeviceUpdatePolicySpec(
                        download_schedule = flightctl.models.update_schedule.UpdateSchedule(
                            time_zone = 'Local', 
                            at = '', 
                            start_grace_duration = '0s', ), 
                        update_schedule = flightctl.models.update_schedule.UpdateSchedule(
                            time_zone = 'Local', 
                            at = '', 
                            start_grace_duration = '0s', ), ), 
                    os = flightctl.models.device_os_spec.DeviceOsSpec(
                        image = '', ), 
                    config = [
                        null
                        ], 
                    applications = [
                        flightctl.models.application_provider_spec.ApplicationProviderSpec()
                        ], 
                    systemd = flightctl.models.device_spec_systemd.DeviceSpec_systemd(
                        match_patterns = [
                            'ge34w9Wa*CLfoo\\yJX2gCb'
                            ], ), 
                    resources = [
                        null
                        ], 
                    consoles = [
                        flightctl.models.device_console.DeviceConsole(
                            session_metadata = '', 
                            session_id = '', )
                        ], 
                    decommissioning = flightctl.models.device_decommission.DeviceDecommission(
                        target = 'Unenroll', ), ),
        )
        """

    def testFleetSpecTemplate(self):
        """Test FleetSpecTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
