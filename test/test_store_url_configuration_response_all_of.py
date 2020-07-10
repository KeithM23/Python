# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.12.0.20200605.001
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.store_url_configuration_response_all_of import StoreUrlConfigurationResponseAllOf  # noqa: E501
from openapi_client.rest import ApiException

class TestStoreUrlConfigurationResponseAllOf(unittest.TestCase):
    """StoreUrlConfigurationResponseAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StoreUrlConfigurationResponseAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.store_url_configuration_response_all_of.StoreUrlConfigurationResponseAllOf()  # noqa: E501
        if include_optional :
            return StoreUrlConfigurationResponseAllOf(
                stores = [{"id":"12099500088","status":"SUCCESS. Connect url settings was changed successfully."},{"id":"12099500044","status":"SUCCESS. Connect url settings was changed successfully."}]
            )
        else :
            return StoreUrlConfigurationResponseAllOf(
        )

    def testStoreUrlConfigurationResponseAllOf(self):
        """Test StoreUrlConfigurationResponseAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()