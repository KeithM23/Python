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
from openapi_client.api.fraud_detect_api import FraudDetectApi  # noqa: E501
from openapi_client.rest import ApiException


class TestFraudDetectApi(unittest.TestCase):
    """FraudDetectApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.fraud_detect_api.FraudDetectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_fraud_client_registration_post(self):
        """Test case for fraud_client_registration_post

        Client registration for fraud detect transaction.  # noqa: E501
        """
        pass

    def test_fraud_payment_registration_post(self):
        """Test case for fraud_payment_registration_post

        Payment registration for fraud detect transaction.  # noqa: E501
        """
        pass

    def test_score_only(self):
        """Test case for score_only

        Score a transaction for fraud.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
