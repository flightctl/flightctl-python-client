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

from flightctl.models.application_volume_status import ApplicationVolumeStatus

class TestApplicationVolumeStatus(unittest.TestCase):
    """ApplicationVolumeStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApplicationVolumeStatus:
        """Test ApplicationVolumeStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApplicationVolumeStatus`
        """
        model = ApplicationVolumeStatus()
        if include_optional:
            return ApplicationVolumeStatus(
                name = '',
                reference = ''
            )
        else:
            return ApplicationVolumeStatus(
                name = '',
                reference = '',
        )
        """

    def testApplicationVolumeStatus(self):
        """Test ApplicationVolumeStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
