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
from openapi_client.models.payment_card_verification_request import PaymentCardVerificationRequest  # noqa: E501
from openapi_client.rest import ApiException

class TestPaymentCardVerificationRequest(unittest.TestCase):
    """PaymentCardVerificationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentCardVerificationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.payment_card_verification_request.PaymentCardVerificationRequest()  # noqa: E501
        if include_optional :
            return PaymentCardVerificationRequest(
                request_type = 'PaymentCardVerificationRequest', 
                billing_address = {"address1":"123 Main St.","city":"Sandy Springs","region":"Georgia","postalCode":"30303","country":"USA"}, 
                store_id = '12345500000', 
                additional_details = {"comments":"This is a comment","invoiceNumber":"551294633441","purchaseOrderNumber":"1223456","operatorId":"OPERATOR_ID_123XXX","salesSystemId":"W-EU-H3866-FLS2","ipgDeferredAuth":true,"highRiskPurchaseIndicator":true}, 
                payment_card = {"number":"5424180279791732","expiryDate":{"month":"03","year":"21"},"securityCode":"977"}
            )
        else :
            return PaymentCardVerificationRequest(
                request_type = 'PaymentCardVerificationRequest',
                payment_card = {"number":"5424180279791732","expiryDate":{"month":"03","year":"21"},"securityCode":"977"},
        )

    def testPaymentCardVerificationRequest(self):
        """Test PaymentCardVerificationRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()