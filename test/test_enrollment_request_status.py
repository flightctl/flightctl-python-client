# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flightctl.models.enrollment_request_status import EnrollmentRequestStatus

class TestEnrollmentRequestStatus(unittest.TestCase):
    """EnrollmentRequestStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnrollmentRequestStatus:
        """Test EnrollmentRequestStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnrollmentRequestStatus`
        """
        model = EnrollmentRequestStatus()
        if include_optional:
            return EnrollmentRequestStatus(
                certificate = '',
                conditions = [
                    flightctl.models.condition.Condition(
                        type = 'Approved', 
                        status = 'True', 
                        observed_generation = 56, 
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        reason = '', )
                    ],
                approval = flightctl.models.enrollment_request_approval.EnrollmentRequestApproval(
                    labels = {
                        'key' : ''
                        }, 
                    approved = True, 
                    approved_by = '', 
                    approved_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return EnrollmentRequestStatus(
                conditions = [
                    flightctl.models.condition.Condition(
                        type = 'Approved', 
                        status = 'True', 
                        observed_generation = 56, 
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        reason = '', )
                    ],
        )
        """

    def testEnrollmentRequestStatus(self):
        """Test EnrollmentRequestStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
