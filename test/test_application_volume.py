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

from flightctl.models.application_volume import ApplicationVolume

class TestApplicationVolume(unittest.TestCase):
    """ApplicationVolume unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApplicationVolume:
        """Test ApplicationVolume
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApplicationVolume`
        """
        model = ApplicationVolume()
        if include_optional:
            return ApplicationVolume(
                name = '',
                image = flightctl.models.image_volume_source.ImageVolumeSource(
                    reference = '', 
                    pull_policy = 'IfNotPresent', )
            )
        else:
            return ApplicationVolume(
                name = '',
                image = flightctl.models.image_volume_source.ImageVolumeSource(
                    reference = '', 
                    pull_policy = 'IfNotPresent', ),
        )
        """

    def testApplicationVolume(self):
        """Test ApplicationVolume"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
