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


class PaymentDevicePreAuthTransaction(object):
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
        'payment_method': 'PaymentDevicePaymentMethod',
        'store_id': 'str',
        'merchant_transaction_id': 'str',
        'transaction_origin': 'TransactionOrigin',
        'order': 'Order',
        'create_token': 'CreatePaymentToken',
        'settlement_split': 'list[SubMerchantSplit]',
        'stored_credentials': 'StoredCredential',
        'split_shipment': 'SplitShipment',
        'decremental_flag': 'bool',
    }

    attribute_map = {
        'request_type': 'requestType',  # noqa: E501
        'transaction_amount': 'transactionAmount',  # noqa: E501
        'payment_method': 'paymentMethod',  # noqa: E501
        'store_id': 'storeId',  # noqa: E501
        'merchant_transaction_id': 'merchantTransactionId',  # noqa: E501
        'transaction_origin': 'transactionOrigin',  # noqa: E501
        'order': 'order',  # noqa: E501
        'create_token': 'createToken',  # noqa: E501
        'settlement_split': 'settlementSplit',  # noqa: E501
        'stored_credentials': 'storedCredentials',  # noqa: E501
        'split_shipment': 'splitShipment',  # noqa: E501
        'decremental_flag': 'decrementalFlag',  # noqa: E501
    }

    def __init__(self, request_type, transaction_amount, payment_method, store_id=None, merchant_transaction_id=None, transaction_origin=None, order=None, create_token=None, settlement_split=None, stored_credentials=None, split_shipment=None, decremental_flag=None):  # noqa: E501
        """PaymentDevicePreAuthTransaction - a model defined in OpenAPI

        Args:
            request_type (str): Object name of the primary transaction request.
            transaction_amount (Amount):
            payment_method (PaymentDevicePaymentMethod):

        Keyword Args:  # noqa: E501  # noqa: E501  # noqa: E501
            store_id (str): An optional outlet ID for clients that support multiple stores in the same app.. [optional]  # noqa: E501
            merchant_transaction_id (str): The unique merchant transaction ID from the request header, if supplied.. [optional]  # noqa: E501
            transaction_origin (TransactionOrigin): [optional]  # noqa: E501
            order (Order): [optional]  # noqa: E501
            create_token (CreatePaymentToken): [optional]  # noqa: E501
            settlement_split (list[SubMerchantSplit]): Settle with multiple sub-merchants, sale and preAuth only.. [optional]  # noqa: E501
            stored_credentials (StoredCredential): [optional]  # noqa: E501
            split_shipment (SplitShipment): [optional]  # noqa: E501
            decremental_flag (bool): This flag can only be used in a preAuth transaction that updates the amount of a previous preAuth transaction to either increase the preAuth amount (DecrementalPreAuthFlag &#x3D; false) or decrease the preAuth amount (DecrementalPreAuthFlag &#x3D; true).. [optional] if omitted the server will use the default value of False  # noqa: E501
        """

        self._request_type = None
        self._transaction_amount = None
        self._store_id = None
        self._merchant_transaction_id = None
        self._transaction_origin = None
        self._order = None
        self._payment_method = None
        self._create_token = None
        self._settlement_split = None
        self._stored_credentials = None
        self._split_shipment = None
        self._decremental_flag = None
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
        self.payment_method = payment_method
        if create_token is not None:
            self.create_token = create_token  # noqa: E501
        if settlement_split is not None:
            self.settlement_split = settlement_split  # noqa: E501
        if stored_credentials is not None:
            self.stored_credentials = stored_credentials  # noqa: E501
        if split_shipment is not None:
            self.split_shipment = split_shipment  # noqa: E501
        if decremental_flag is not None:
            self.decremental_flag = decremental_flag  # noqa: E501

    @property
    def request_type(self):
        """Gets the request_type of this PaymentDevicePreAuthTransaction.  # noqa: E501

        Object name of the primary transaction request.  # noqa: E501

        :return: The request_type of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(
            self,
            request_type):
        """Sets the request_type of this PaymentDevicePreAuthTransaction.

        Object name of the primary transaction request.  # noqa: E501

        :param request_type: The request_type of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :type: str
        """
        if request_type is None:
            raise ValueError("Invalid value for `request_type`, must not be `None`")  # noqa: E501

        self._request_type = (
            request_type)

    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this PaymentDevicePreAuthTransaction.  # noqa: E501


        :return: The transaction_amount of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :rtype: Amount
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(
            self,
            transaction_amount):
        """Sets the transaction_amount of this PaymentDevicePreAuthTransaction.


        :param transaction_amount: The transaction_amount of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :type: Amount
        """
        if transaction_amount is None:
            raise ValueError("Invalid value for `transaction_amount`, must not be `None`")  # noqa: E501

        self._transaction_amount = (
            transaction_amount)

    @property
    def store_id(self):
        """Gets the store_id of this PaymentDevicePreAuthTransaction.  # noqa: E501

        An optional outlet ID for clients that support multiple stores in the same app.  # noqa: E501

        :return: The store_id of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(
            self,
            store_id):
        """Sets the store_id of this PaymentDevicePreAuthTransaction.

        An optional outlet ID for clients that support multiple stores in the same app.  # noqa: E501

        :param store_id: The store_id of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :type: str
        """
        if store_id is not None and len(store_id) > 20:
            raise ValueError("Invalid value for `store_id`, length must be less than or equal to `20`")  # noqa: E501

        self._store_id = (
            store_id)

    @property
    def merchant_transaction_id(self):
        """Gets the merchant_transaction_id of this PaymentDevicePreAuthTransaction.  # noqa: E501

        The unique merchant transaction ID from the request header, if supplied.  # noqa: E501

        :return: The merchant_transaction_id of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :rtype: str
        """
        return self._merchant_transaction_id

    @merchant_transaction_id.setter
    def merchant_transaction_id(
            self,
            merchant_transaction_id):
        """Sets the merchant_transaction_id of this PaymentDevicePreAuthTransaction.

        The unique merchant transaction ID from the request header, if supplied.  # noqa: E501

        :param merchant_transaction_id: The merchant_transaction_id of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :type: str
        """
        if merchant_transaction_id is not None and len(merchant_transaction_id) > 40:
            raise ValueError("Invalid value for `merchant_transaction_id`, length must be less than or equal to `40`")  # noqa: E501

        self._merchant_transaction_id = (
            merchant_transaction_id)

    @property
    def transaction_origin(self):
        """Gets the transaction_origin of this PaymentDevicePreAuthTransaction.  # noqa: E501


        :return: The transaction_origin of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :rtype: TransactionOrigin
        """
        return self._transaction_origin

    @transaction_origin.setter
    def transaction_origin(
            self,
            transaction_origin):
        """Sets the transaction_origin of this PaymentDevicePreAuthTransaction.


        :param transaction_origin: The transaction_origin of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :type: TransactionOrigin
        """

        self._transaction_origin = (
            transaction_origin)

    @property
    def order(self):
        """Gets the order of this PaymentDevicePreAuthTransaction.  # noqa: E501


        :return: The order of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(
            self,
            order):
        """Sets the order of this PaymentDevicePreAuthTransaction.


        :param order: The order of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :type: Order
        """

        self._order = (
            order)

    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentDevicePreAuthTransaction.  # noqa: E501


        :return: The payment_method of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :rtype: PaymentDevicePaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(
            self,
            payment_method):
        """Sets the payment_method of this PaymentDevicePreAuthTransaction.


        :param payment_method: The payment_method of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :type: PaymentDevicePaymentMethod
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501

        self._payment_method = (
            payment_method)

    @property
    def create_token(self):
        """Gets the create_token of this PaymentDevicePreAuthTransaction.  # noqa: E501


        :return: The create_token of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :rtype: CreatePaymentToken
        """
        return self._create_token

    @create_token.setter
    def create_token(
            self,
            create_token):
        """Sets the create_token of this PaymentDevicePreAuthTransaction.


        :param create_token: The create_token of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :type: CreatePaymentToken
        """

        self._create_token = (
            create_token)

    @property
    def settlement_split(self):
        """Gets the settlement_split of this PaymentDevicePreAuthTransaction.  # noqa: E501

        Settle with multiple sub-merchants, sale and preAuth only.  # noqa: E501

        :return: The settlement_split of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :rtype: list[SubMerchantSplit]
        """
        return self._settlement_split

    @settlement_split.setter
    def settlement_split(
            self,
            settlement_split):
        """Sets the settlement_split of this PaymentDevicePreAuthTransaction.

        Settle with multiple sub-merchants, sale and preAuth only.  # noqa: E501

        :param settlement_split: The settlement_split of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :type: list[SubMerchantSplit]
        """

        self._settlement_split = (
            settlement_split)

    @property
    def stored_credentials(self):
        """Gets the stored_credentials of this PaymentDevicePreAuthTransaction.  # noqa: E501


        :return: The stored_credentials of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :rtype: StoredCredential
        """
        return self._stored_credentials

    @stored_credentials.setter
    def stored_credentials(
            self,
            stored_credentials):
        """Sets the stored_credentials of this PaymentDevicePreAuthTransaction.


        :param stored_credentials: The stored_credentials of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :type: StoredCredential
        """

        self._stored_credentials = (
            stored_credentials)

    @property
    def split_shipment(self):
        """Gets the split_shipment of this PaymentDevicePreAuthTransaction.  # noqa: E501


        :return: The split_shipment of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :rtype: SplitShipment
        """
        return self._split_shipment

    @split_shipment.setter
    def split_shipment(
            self,
            split_shipment):
        """Sets the split_shipment of this PaymentDevicePreAuthTransaction.


        :param split_shipment: The split_shipment of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :type: SplitShipment
        """

        self._split_shipment = (
            split_shipment)

    @property
    def decremental_flag(self):
        """Gets the decremental_flag of this PaymentDevicePreAuthTransaction.  # noqa: E501

        This flag can only be used in a preAuth transaction that updates the amount of a previous preAuth transaction to either increase the preAuth amount (DecrementalPreAuthFlag = false) or decrease the preAuth amount (DecrementalPreAuthFlag = true).  # noqa: E501

        :return: The decremental_flag of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :rtype: bool
        """
        return self._decremental_flag

    @decremental_flag.setter
    def decremental_flag(
            self,
            decremental_flag):
        """Sets the decremental_flag of this PaymentDevicePreAuthTransaction.

        This flag can only be used in a preAuth transaction that updates the amount of a previous preAuth transaction to either increase the preAuth amount (DecrementalPreAuthFlag = false) or decrease the preAuth amount (DecrementalPreAuthFlag = true).  # noqa: E501

        :param decremental_flag: The decremental_flag of this PaymentDevicePreAuthTransaction.  # noqa: E501
        :type: bool
        """

        self._decremental_flag = (
            decremental_flag)

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
        if not isinstance(other, PaymentDevicePreAuthTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
