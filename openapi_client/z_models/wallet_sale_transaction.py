# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.13.0.20200810.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class WalletSaleTransaction(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'request_type': 'str',
        'transaction_amount': 'Amount',
        'wallet_payment_method': 'WalletPaymentMethod',
        'store_id': 'str',
        'merchant_transaction_id': 'str',
        'transaction_origin': 'TransactionOrigin',
        'order': 'Order',
        'payment_facilitator': 'PaymentFacilitator',
    }

    attribute_map = {
        'request_type': 'requestType',  # noqa: E501
        'transaction_amount': 'transactionAmount',  # noqa: E501
        'wallet_payment_method': 'walletPaymentMethod',  # noqa: E501
        'store_id': 'storeId',  # noqa: E501
        'merchant_transaction_id': 'merchantTransactionId',  # noqa: E501
        'transaction_origin': 'transactionOrigin',  # noqa: E501
        'order': 'order',  # noqa: E501
        'payment_facilitator': 'paymentFacilitator',  # noqa: E501
    }

    def __init__(self, request_type, transaction_amount, wallet_payment_method, store_id=None, merchant_transaction_id=None, transaction_origin=None, order=None, payment_facilitator=None):  # noqa: E501
        """WalletSaleTransaction - a model defined in OpenAPI

        Args:
            request_type (str): Object name of the primary transaction request.
            transaction_amount (Amount):
            wallet_payment_method (WalletPaymentMethod):

        Keyword Args:  # noqa: E501  # noqa: E501  # noqa: E501
            store_id (str): An optional outlet ID for clients that support multiple stores in the same app.. [optional]  # noqa: E501
            merchant_transaction_id (str): The unique merchant transaction ID from the request header, if supplied.. [optional]  # noqa: E501
            transaction_origin (TransactionOrigin): [optional]  # noqa: E501
            order (Order): [optional]  # noqa: E501
            payment_facilitator (PaymentFacilitator): [optional]  # noqa: E501
        """

        self._request_type = None
        self._transaction_amount = None
        self._store_id = None
        self._merchant_transaction_id = None
        self._transaction_origin = None
        self._order = None
        self._wallet_payment_method = None
        self._payment_facilitator = None
        self.discriminator = None

        self.request_type = request_type
        self.transaction_amount = transaction_amount
        if store_id is not None:
            self.store_id = store_id  # noqa: E501
        if merchant_transaction_id is not None:
            self.merchant_transaction_id = merchant_transaction_id  # noqa: E501
        if transaction_origin is not None:
            self.transaction_origin = transaction_origin  # noqa: E501
        if order is not None:
            self.order = order  # noqa: E501
        self.wallet_payment_method = wallet_payment_method
        if payment_facilitator is not None:
            self.payment_facilitator = payment_facilitator  # noqa: E501

    @property
    def request_type(self):
        """Gets the request_type of this WalletSaleTransaction.  # noqa: E501

        Object name of the primary transaction request.  # noqa: E501

        :return: The request_type of this WalletSaleTransaction.  # noqa: E501
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(
            self,
            request_type):
        """Sets the request_type of this WalletSaleTransaction.

        Object name of the primary transaction request.  # noqa: E501

        :param request_type: The request_type of this WalletSaleTransaction.  # noqa: E501
        :type: str
        """
        if request_type is None:
            raise ValueError("Invalid value for `request_type`, must not be `None`")  # noqa: E501

        self._request_type = (
            request_type)

    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this WalletSaleTransaction.  # noqa: E501


        :return: The transaction_amount of this WalletSaleTransaction.  # noqa: E501
        :rtype: Amount
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(
            self,
            transaction_amount):
        """Sets the transaction_amount of this WalletSaleTransaction.


        :param transaction_amount: The transaction_amount of this WalletSaleTransaction.  # noqa: E501
        :type: Amount
        """
        if transaction_amount is None:
            raise ValueError("Invalid value for `transaction_amount`, must not be `None`")  # noqa: E501

        self._transaction_amount = (
            transaction_amount)

    @property
    def store_id(self):
        """Gets the store_id of this WalletSaleTransaction.  # noqa: E501

        An optional outlet ID for clients that support multiple stores in the same app.  # noqa: E501

        :return: The store_id of this WalletSaleTransaction.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(
            self,
            store_id):
        """Sets the store_id of this WalletSaleTransaction.

        An optional outlet ID for clients that support multiple stores in the same app.  # noqa: E501

        :param store_id: The store_id of this WalletSaleTransaction.  # noqa: E501
        :type: str
        """
        if store_id is not None and len(store_id) > 20:
            raise ValueError("Invalid value for `store_id`, length must be less than or equal to `20`")  # noqa: E501

        self._store_id = (
            store_id)

    @property
    def merchant_transaction_id(self):
        """Gets the merchant_transaction_id of this WalletSaleTransaction.  # noqa: E501

        The unique merchant transaction ID from the request header, if supplied.  # noqa: E501

        :return: The merchant_transaction_id of this WalletSaleTransaction.  # noqa: E501
        :rtype: str
        """
        return self._merchant_transaction_id

    @merchant_transaction_id.setter
    def merchant_transaction_id(
            self,
            merchant_transaction_id):
        """Sets the merchant_transaction_id of this WalletSaleTransaction.

        The unique merchant transaction ID from the request header, if supplied.  # noqa: E501

        :param merchant_transaction_id: The merchant_transaction_id of this WalletSaleTransaction.  # noqa: E501
        :type: str
        """
        if merchant_transaction_id is not None and len(merchant_transaction_id) > 40:
            raise ValueError("Invalid value for `merchant_transaction_id`, length must be less than or equal to `40`")  # noqa: E501

        self._merchant_transaction_id = (
            merchant_transaction_id)

    @property
    def transaction_origin(self):
        """Gets the transaction_origin of this WalletSaleTransaction.  # noqa: E501


        :return: The transaction_origin of this WalletSaleTransaction.  # noqa: E501
        :rtype: TransactionOrigin
        """
        return self._transaction_origin

    @transaction_origin.setter
    def transaction_origin(
            self,
            transaction_origin):
        """Sets the transaction_origin of this WalletSaleTransaction.


        :param transaction_origin: The transaction_origin of this WalletSaleTransaction.  # noqa: E501
        :type: TransactionOrigin
        """

        self._transaction_origin = (
            transaction_origin)

    @property
    def order(self):
        """Gets the order of this WalletSaleTransaction.  # noqa: E501


        :return: The order of this WalletSaleTransaction.  # noqa: E501
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(
            self,
            order):
        """Sets the order of this WalletSaleTransaction.


        :param order: The order of this WalletSaleTransaction.  # noqa: E501
        :type: Order
        """

        self._order = (
            order)

    @property
    def wallet_payment_method(self):
        """Gets the wallet_payment_method of this WalletSaleTransaction.  # noqa: E501


        :return: The wallet_payment_method of this WalletSaleTransaction.  # noqa: E501
        :rtype: WalletPaymentMethod
        """
        return self._wallet_payment_method

    @wallet_payment_method.setter
    def wallet_payment_method(
            self,
            wallet_payment_method):
        """Sets the wallet_payment_method of this WalletSaleTransaction.


        :param wallet_payment_method: The wallet_payment_method of this WalletSaleTransaction.  # noqa: E501
        :type: WalletPaymentMethod
        """
        if wallet_payment_method is None:
            raise ValueError("Invalid value for `wallet_payment_method`, must not be `None`")  # noqa: E501

        self._wallet_payment_method = (
            wallet_payment_method)

    @property
    def payment_facilitator(self):
        """Gets the payment_facilitator of this WalletSaleTransaction.  # noqa: E501


        :return: The payment_facilitator of this WalletSaleTransaction.  # noqa: E501
        :rtype: PaymentFacilitator
        """
        return self._payment_facilitator

    @payment_facilitator.setter
    def payment_facilitator(
            self,
            payment_facilitator):
        """Sets the payment_facilitator of this WalletSaleTransaction.


        :param payment_facilitator: The payment_facilitator of this WalletSaleTransaction.  # noqa: E501
        :type: PaymentFacilitator
        """

        self._payment_facilitator = (
            payment_facilitator)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WalletSaleTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
