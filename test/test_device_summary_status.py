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

from flightctl.models.device_summary_status import DeviceSummaryStatus

class TestDeviceSummaryStatus(unittest.TestCase):
    """DeviceSummaryStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceSummaryStatus:
        """Test DeviceSummaryStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceSummaryStatus`
        """
        model = DeviceSummaryStatus()
        if include_optional:
            return DeviceSummaryStatus(
                status = 'Online',
                info = ''
            )
        else:
            return DeviceSummaryStatus(
                status = 'Online',
        )
        """

    def testDeviceSummaryStatus(self):
        """Test DeviceSummaryStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
