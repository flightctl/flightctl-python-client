# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flightctl.models.hook_action_spec import HookActionSpec

class TestHookActionSpec(unittest.TestCase):
    """HookActionSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HookActionSpec:
        """Test HookActionSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HookActionSpec`
        """
        model = HookActionSpec()
        if include_optional:
            return HookActionSpec(
                timeout = '68072888001528021798096225500h'
            )
        else:
            return HookActionSpec(
        )
        """

    def testHookActionSpec(self):
        """Test HookActionSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
