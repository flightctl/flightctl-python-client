# coding: utf-8

"""
    Open Device Management API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: undefined
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flightctl.models.git_config_provider_spec import GitConfigProviderSpec

class TestGitConfigProviderSpec(unittest.TestCase):
    """GitConfigProviderSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GitConfigProviderSpec:
        """Test GitConfigProviderSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GitConfigProviderSpec`
        """
        model = GitConfigProviderSpec()
        if include_optional:
            return GitConfigProviderSpec(
                name = '',
                git_ref = flightctl.models.git_config_provider_spec_git_ref.GitConfigProviderSpec_gitRef(
                    repository = '', 
                    target_revision = '', 
                    path = '', 
                    mount_path = '/', )
            )
        else:
            return GitConfigProviderSpec(
                name = '',
                git_ref = flightctl.models.git_config_provider_spec_git_ref.GitConfigProviderSpec_gitRef(
                    repository = '', 
                    target_revision = '', 
                    path = '', 
                    mount_path = '/', ),
        )
        """

    def testGitConfigProviderSpec(self):
        """Test GitConfigProviderSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
