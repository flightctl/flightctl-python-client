# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flightctl.models.device_decommission import DeviceDecommission

class TestDeviceDecommission(unittest.TestCase):
    """DeviceDecommission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceDecommission:
        """Test DeviceDecommission
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceDecommission`
        """
        model = DeviceDecommission()
        if include_optional:
            return DeviceDecommission(
                decommission_target = 'Unenroll'
            )
        else:
            return DeviceDecommission(
                decommission_target = 'Unenroll',
        )
        """

    def testDeviceDecommission(self):
        """Test DeviceDecommission"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
