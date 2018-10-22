# coding: utf-8

"""
    Payment Gateway API Specification

    Payment Gateway API for payment processing.   # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.amount import Amount  # noqa: F401,E501
from swagger_client.models.basket_item import BasketItem  # noqa: F401,E501
from swagger_client.models.industry_specific_extensions import IndustrySpecificExtensions  # noqa: F401,E501
from swagger_client.models.order import Order  # noqa: F401,E501
from swagger_client.models.payment_method import PaymentMethod  # noqa: F401,E501
from swagger_client.models.primary_transaction_additional_details import PrimaryTransactionAdditionalDetails  # noqa: F401,E501
from swagger_client.models.split_shipment import SplitShipment  # noqa: F401,E501
from swagger_client.models.stored_credential import StoredCredential  # noqa: F401,E501
from swagger_client.models.transaction_type import TransactionType  # noqa: F401,E501


class PrimaryTransaction(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'transaction_type': 'TransactionType',
        'store_id': 'str',
        'client_transaction_id': 'str',
        'amount': 'Amount',
        'payment_method': 'PaymentMethod',
        'order': 'Order',
        'basket_items': 'list[BasketItem]',
        'split_shipment': 'SplitShipment',
        'additional_details': 'PrimaryTransactionAdditionalDetails',
        'industry_specific_extensions': 'IndustrySpecificExtensions',
        'stored_credentials': 'StoredCredential'
    }

    attribute_map = {
        'transaction_type': 'transactionType',
        'store_id': 'storeId',
        'client_transaction_id': 'clientTransactionId',
        'amount': 'amount',
        'payment_method': 'paymentMethod',
        'order': 'order',
        'basket_items': 'basketItems',
        'split_shipment': 'splitShipment',
        'additional_details': 'additionalDetails',
        'industry_specific_extensions': 'industrySpecificExtensions',
        'stored_credentials': 'storedCredentials'
    }

    def __init__(self, transaction_type=None, store_id=None, client_transaction_id=None, amount=None, payment_method=None, order=None, basket_items=None, split_shipment=None, additional_details=None, industry_specific_extensions=None, stored_credentials=None):  # noqa: E501
        """PrimaryTransaction - a model defined in Swagger"""  # noqa: E501

        self._transaction_type = None
        self._store_id = None
        self._client_transaction_id = None
        self._amount = None
        self._payment_method = None
        self._order = None
        self._basket_items = None
        self._split_shipment = None
        self._additional_details = None
        self._industry_specific_extensions = None
        self._stored_credentials = None
        self.discriminator = None

        self.transaction_type = transaction_type
        if store_id is not None:
            self.store_id = store_id
        if client_transaction_id is not None:
            self.client_transaction_id = client_transaction_id
        self.amount = amount
        self.payment_method = payment_method
        if order is not None:
            self.order = order
        if basket_items is not None:
            self.basket_items = basket_items
        if split_shipment is not None:
            self.split_shipment = split_shipment
        if additional_details is not None:
            self.additional_details = additional_details
        if industry_specific_extensions is not None:
            self.industry_specific_extensions = industry_specific_extensions
        if stored_credentials is not None:
            self.stored_credentials = stored_credentials

    @property
    def transaction_type(self):
        """Gets the transaction_type of this PrimaryTransaction.  # noqa: E501


        :return: The transaction_type of this PrimaryTransaction.  # noqa: E501
        :rtype: TransactionType
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this PrimaryTransaction.


        :param transaction_type: The transaction_type of this PrimaryTransaction.  # noqa: E501
        :type: TransactionType
        """
        if transaction_type is None:
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501

        self._transaction_type = transaction_type

    @property
    def store_id(self):
        """Gets the store_id of this PrimaryTransaction.  # noqa: E501

        An optional Outlet ID for clients that support multiple stores in the same app.  # noqa: E501

        :return: The store_id of this PrimaryTransaction.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this PrimaryTransaction.

        An optional Outlet ID for clients that support multiple stores in the same app.  # noqa: E501

        :param store_id: The store_id of this PrimaryTransaction.  # noqa: E501
        :type: str
        """

        self._store_id = store_id

    @property
    def client_transaction_id(self):
        """Gets the client_transaction_id of this PrimaryTransaction.  # noqa: E501

        The unique client Transaction ID from the Request header, if supplied.  # noqa: E501

        :return: The client_transaction_id of this PrimaryTransaction.  # noqa: E501
        :rtype: str
        """
        return self._client_transaction_id

    @client_transaction_id.setter
    def client_transaction_id(self, client_transaction_id):
        """Sets the client_transaction_id of this PrimaryTransaction.

        The unique client Transaction ID from the Request header, if supplied.  # noqa: E501

        :param client_transaction_id: The client_transaction_id of this PrimaryTransaction.  # noqa: E501
        :type: str
        """

        self._client_transaction_id = client_transaction_id

    @property
    def amount(self):
        """Gets the amount of this PrimaryTransaction.  # noqa: E501


        :return: The amount of this PrimaryTransaction.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PrimaryTransaction.


        :param amount: The amount of this PrimaryTransaction.  # noqa: E501
        :type: Amount
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def payment_method(self):
        """Gets the payment_method of this PrimaryTransaction.  # noqa: E501


        :return: The payment_method of this PrimaryTransaction.  # noqa: E501
        :rtype: PaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PrimaryTransaction.


        :param payment_method: The payment_method of this PrimaryTransaction.  # noqa: E501
        :type: PaymentMethod
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501

        self._payment_method = payment_method

    @property
    def order(self):
        """Gets the order of this PrimaryTransaction.  # noqa: E501


        :return: The order of this PrimaryTransaction.  # noqa: E501
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this PrimaryTransaction.


        :param order: The order of this PrimaryTransaction.  # noqa: E501
        :type: Order
        """

        self._order = order

    @property
    def basket_items(self):
        """Gets the basket_items of this PrimaryTransaction.  # noqa: E501

        Required for some payment methods (for example, Klarna)  # noqa: E501

        :return: The basket_items of this PrimaryTransaction.  # noqa: E501
        :rtype: list[BasketItem]
        """
        return self._basket_items

    @basket_items.setter
    def basket_items(self, basket_items):
        """Sets the basket_items of this PrimaryTransaction.

        Required for some payment methods (for example, Klarna)  # noqa: E501

        :param basket_items: The basket_items of this PrimaryTransaction.  # noqa: E501
        :type: list[BasketItem]
        """

        self._basket_items = basket_items

    @property
    def split_shipment(self):
        """Gets the split_shipment of this PrimaryTransaction.  # noqa: E501


        :return: The split_shipment of this PrimaryTransaction.  # noqa: E501
        :rtype: SplitShipment
        """
        return self._split_shipment

    @split_shipment.setter
    def split_shipment(self, split_shipment):
        """Sets the split_shipment of this PrimaryTransaction.


        :param split_shipment: The split_shipment of this PrimaryTransaction.  # noqa: E501
        :type: SplitShipment
        """

        self._split_shipment = split_shipment

    @property
    def additional_details(self):
        """Gets the additional_details of this PrimaryTransaction.  # noqa: E501


        :return: The additional_details of this PrimaryTransaction.  # noqa: E501
        :rtype: PrimaryTransactionAdditionalDetails
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(self, additional_details):
        """Sets the additional_details of this PrimaryTransaction.


        :param additional_details: The additional_details of this PrimaryTransaction.  # noqa: E501
        :type: PrimaryTransactionAdditionalDetails
        """

        self._additional_details = additional_details

    @property
    def industry_specific_extensions(self):
        """Gets the industry_specific_extensions of this PrimaryTransaction.  # noqa: E501


        :return: The industry_specific_extensions of this PrimaryTransaction.  # noqa: E501
        :rtype: IndustrySpecificExtensions
        """
        return self._industry_specific_extensions

    @industry_specific_extensions.setter
    def industry_specific_extensions(self, industry_specific_extensions):
        """Sets the industry_specific_extensions of this PrimaryTransaction.


        :param industry_specific_extensions: The industry_specific_extensions of this PrimaryTransaction.  # noqa: E501
        :type: IndustrySpecificExtensions
        """

        self._industry_specific_extensions = industry_specific_extensions

    @property
    def stored_credentials(self):
        """Gets the stored_credentials of this PrimaryTransaction.  # noqa: E501


        :return: The stored_credentials of this PrimaryTransaction.  # noqa: E501
        :rtype: StoredCredential
        """
        return self._stored_credentials

    @stored_credentials.setter
    def stored_credentials(self, stored_credentials):
        """Sets the stored_credentials of this PrimaryTransaction.


        :param stored_credentials: The stored_credentials of this PrimaryTransaction.  # noqa: E501
        :type: StoredCredential
        """

        self._stored_credentials = stored_credentials

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, PrimaryTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other