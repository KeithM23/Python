# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.8.0.20190731.002
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.payment_url_api import PaymentURLApi  # noqa: E501
from openapi_client.rest import ApiException


class TestPaymentURLApi(unittest.TestCase):
    """PaymentURLApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.payment_url_api.PaymentURLApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_payment_url(self):
        """Test case for create_payment_url

        Create a payment URL.  # noqa: E501
        """
        pass

    def test_delete_payment_url(self):
        """Test case for delete_payment_url

        Delete a payment URL.  # noqa: E501
        """
        pass

    def test_payment_url_detail(self):
        """Test case for payment_url_detail

        Retrieve the state of payment URL.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
