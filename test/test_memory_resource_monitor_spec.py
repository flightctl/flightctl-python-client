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

from flightctl.models.memory_resource_monitor_spec import MemoryResourceMonitorSpec

class TestMemoryResourceMonitorSpec(unittest.TestCase):
    """MemoryResourceMonitorSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MemoryResourceMonitorSpec:
        """Test MemoryResourceMonitorSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MemoryResourceMonitorSpec`
        """
        model = MemoryResourceMonitorSpec()
        if include_optional:
            return MemoryResourceMonitorSpec(
                alert_rules = [
                    flightctl.models.resource_alert_rule.ResourceAlertRule(
                        severity = 'Warning', 
                        duration = '4s', 
                        percentage = 1.337, 
                        description = '', )
                    ],
                sampling_interval = '68072888001528021798096225500h',
                monitor_type = ''
            )
        else:
            return MemoryResourceMonitorSpec(
                alert_rules = [
                    flightctl.models.resource_alert_rule.ResourceAlertRule(
                        severity = 'Warning', 
                        duration = '4s', 
                        percentage = 1.337, 
                        description = '', )
                    ],
                sampling_interval = '68072888001528021798096225500h',
                monitor_type = '',
        )
        """

    def testMemoryResourceMonitorSpec(self):
        """Test MemoryResourceMonitorSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
