# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flightctl.models.hook_condition_path_op import HookConditionPathOp

class TestHookConditionPathOp(unittest.TestCase):
    """HookConditionPathOp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HookConditionPathOp:
        """Test HookConditionPathOp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HookConditionPathOp`
        """
        model = HookConditionPathOp()
        if include_optional:
            return HookConditionPathOp(
                path = '',
                op = [
                    'created'
                    ]
            )
        else:
            return HookConditionPathOp(
                path = '',
                op = [
                    'created'
                    ],
        )
        """

    def testHookConditionPathOp(self):
        """Test HookConditionPathOp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
