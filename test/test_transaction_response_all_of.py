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
from openapi_client.models.transaction_response_all_of import TransactionResponseAllOf  # noqa: E501
from openapi_client.rest import ApiException

class TestTransactionResponseAllOf(unittest.TestCase):
    """TransactionResponseAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TransactionResponseAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.transaction_response_all_of.TransactionResponseAllOf()  # noqa: E501
        if include_optional :
            return TransactionResponseAllOf(
                ipg_transaction_id = '838916029301', 
                order_id = '123456', 
                transaction_type = 'SALE', 
                payment_token = {"value":"234ljl124l12","reusable":true,"declineDuplicates":false,"last4":"4997","brand":"VISA","accountVerification":true,"type":"PAYMENT_CARD"}, 
                transaction_origin = 'ECOM', 
                payment_method_details = {"paymentCard":{"number":"5424180279791732","expiryDate":{"month":"03","year":"21"},"securityCode":"977"},"paymentMethodType":"PAYMENT_CARD"}, 
                country = 'USA', 
                terminal_id = '123456', 
                merchant_id = '199950008', 
                merchant_transaction_id = 'lsk23532djljff3', 
                transaction_time = 1518811817, 
                approved_amount = {"total":10.24,"currency":"USD","components":{"subtotal":8.0,"localTax":1.0,"shipping":1.24}}, 
                transaction_status = 'APPROVED', 
                transaction_state = 'AUTHORIZED', 
                secure3d_response = {"responseCode3dSecure":"3"}, 
                redirect_url = 'http://pay.issuer-bank.com/sessionID=123&sharedKey=456', 
                authentication_response = {"type":"3D_SECURE","version":"2.1","redirectURL":"http://pay.issuer-bank.com/sessionID=123&sharedKey=456","secure3dMethod":"&lt;!DOCTYPE iframe SYSTEM \"about:legacy-compat\"&gt; &lt;iframe id=\"tdsMmethodTgtFrame\" name=\"tdsMmethodTgtFrame\"\n                         style=\"width: 1px; height: 1px; display: none;\" src=\"javascript:false;\" xmlns=\"http://www.w3.org/1999/xhtml\"&gt;\n                &lt;!--.--&gt; &lt;/iframe&gt;&lt;form id=\"tdsMmethodForm\" name=\"tdsMmethodForm\"\n                         action=\"https://localhost.modirum.com:8543/dstests/ACSEmu2\" method=\"post\"\n                         target=\"tdsMmethodTgtFrame\" xmlns=\"http://www.w3.org/1999/xhtml\"&gt; &lt;input type=\"hidden\" name=\"3DSMethodData\"\n                         value=\"eyAidGhyZWVEU1NlcnZlclRyYW5zSUQiIDogIjAwMDAwMDAwLTU2NzYtNTY2My04MDAwLTAwMDAw\n                &amp;#10;MDAwNDFhOSIsICJ0aHJlZURTTWV0aG9kTm90aWZpY2F0aW9uVVJMIiA6ICJodHRwczovL2xvY\n                         2Fs&amp;#10;aG9zdC5tb2RpcnVtLmNvbTo4NTQzL21kcGF5bXBpL01lcmNoYW50U2VydmVyP21uPVkmdHhpZD0x\n                &amp;#10;NjgwOSZkaWdlc3Q9aSUyQnhhUEF5NWFOcVJRbllqNmozbWFDZlFJbTdFdjJYTmkwNn\n                         h6YmZNJTJG&amp;#10;R3MlM0QiIH0\"/&gt; &lt;input type=\"hidden\" name=\"threeDSMethodData\"\n                         value=\"eyAidGhyZWVEU1NlcnZlclRyYW5zSUQiIDogIjAwMDAwMDAwLTU2NzYtNTY2My04MDAwLTAwMDA\n                         w&amp;#10;MDAwNDFhOSIsICJ0aHJlZURTTWV0aG9kTm90aWZpY2F0aW9uVVJMIiA6ICJodHRwczovL2xvY\n                         2Fs&amp;#10;aG9zdC5tb2RpcnVtLmNvbTo4NTQzL21kcGF5bXBpL01lcmNoYW50U2VydmVyP21uPVkmd\n                         HhpZD0x&amp;#10;NjgwOSZkaWdlc3Q9aSUyQnhhUEF5NWFOcVJRbllqNmozbWFDZlFJbTdFdjJYTmkwNn\n                         h6YmZNJTJG&amp;#10;R3MlM0QiIH0\"/&gt;\n                &lt;/form&gt;&lt;script type=\"text/javascript\" xmlns=\"http://www.w3.org/1999/xhtml\"&gt;\n                         document.getElementById(\"tdsMmethodForm\").submit(); &lt;/script&gt;","secure3dTransId":"3ac7caa7-aa42-2663-791b-2ac05a542c4a"}, 
                scheme_transaction_id = '019078743804756', 
                processor = {"responseCode":"00","responseMessage":"APPROVED","authorizationCode":"OK7118","network":"NYCE"}, 
                additional_details = {"comments":"This is a comment","invoiceNumber":"551294633441","purchaseOrderNumber":"1223456"}, 
                account_updater_response = {"updatedCard":"4012000066660018","updatedExpirationDate":"1220","updatedAccountStatus":"A","updatedAccountErrorCode":"VAU002"}, 
                ach_response = {"responseCode":"49","approvalCode":"ASF2","referenceNumber":"1234567","preferredFlag":"Y","transactionStatus":"1"}
            )
        else :
            return TransactionResponseAllOf(
        )

    def testTransactionResponseAllOf(self):
        """Test TransactionResponseAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()