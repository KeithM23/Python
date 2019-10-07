# coding: utf-8

"""
    Payment Gateway API Specification.

    The documentation here is designed to provide all of the technical guidance required to consume and integrate with our APIs for payment processing. To learn more about our APIs please visit https://docs.firstdata.com/org/gateway.  # noqa: E501

    The version of the OpenAPI document: 6.8.0.20190731.002
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PaymentDevicePreAuthTransactionAllOf(object):
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
        'payment_method': 'PaymentDevicePaymentMethod',
        'create_token': 'CreatePaymentToken',
        'settlement_split': 'list[SubMerchantSplit]',
        'stored_credentials': 'StoredCredential',
        'split_shipment': 'SplitShipment'
    }

    attribute_map = {
        'payment_method': 'paymentMethod',
        'create_token': 'createToken',
        'settlement_split': 'settlementSplit',
        'stored_credentials': 'storedCredentials',
        'split_shipment': 'splitShipment'
    }

    def __init__(self, payment_method=None, create_token=None, settlement_split=None, stored_credentials=None, split_shipment=None):  # noqa: E501
        """PaymentDevicePreAuthTransactionAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._payment_method = None
        self._create_token = None
        self._settlement_split = None
        self._stored_credentials = None
        self._split_shipment = None
        self.discriminator = None

        self.payment_method = payment_method
        if create_token is not None:
            self.create_token = create_token
        if settlement_split is not None:
            self.settlement_split = settlement_split
        if stored_credentials is not None:
            self.stored_credentials = stored_credentials
        if split_shipment is not None:
            self.split_shipment = split_shipment

    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentDevicePreAuthTransactionAllOf.  # noqa: E501


        :return: The payment_method of this PaymentDevicePreAuthTransactionAllOf.  # noqa: E501
        :rtype: PaymentDevicePaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentDevicePreAuthTransactionAllOf.


        :param payment_method: The payment_method of this PaymentDevicePreAuthTransactionAllOf.  # noqa: E501
        :type: PaymentDevicePaymentMethod
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501

        self._payment_method = payment_method

    @property
    def create_token(self):
        """Gets the create_token of this PaymentDevicePreAuthTransactionAllOf.  # noqa: E501


        :return: The create_token of this PaymentDevicePreAuthTransactionAllOf.  # noqa: E501
        :rtype: CreatePaymentToken
        """
        return self._create_token

    @create_token.setter
    def create_token(self, create_token):
        """Sets the create_token of this PaymentDevicePreAuthTransactionAllOf.


        :param create_token: The create_token of this PaymentDevicePreAuthTransactionAllOf.  # noqa: E501
        :type: CreatePaymentToken
        """

        self._create_token = create_token

    @property
    def settlement_split(self):
        """Gets the settlement_split of this PaymentDevicePreAuthTransactionAllOf.  # noqa: E501

        Settle with multiple sub-merchants, sale and preAuth only.  # noqa: E501

        :return: The settlement_split of this PaymentDevicePreAuthTransactionAllOf.  # noqa: E501
        :rtype: list[SubMerchantSplit]
        """
        return self._settlement_split

    @settlement_split.setter
    def settlement_split(self, settlement_split):
        """Sets the settlement_split of this PaymentDevicePreAuthTransactionAllOf.

        Settle with multiple sub-merchants, sale and preAuth only.  # noqa: E501

        :param settlement_split: The settlement_split of this PaymentDevicePreAuthTransactionAllOf.  # noqa: E501
        :type: list[SubMerchantSplit]
        """

        self._settlement_split = settlement_split

    @property
    def stored_credentials(self):
        """Gets the stored_credentials of this PaymentDevicePreAuthTransactionAllOf.  # noqa: E501


        :return: The stored_credentials of this PaymentDevicePreAuthTransactionAllOf.  # noqa: E501
        :rtype: StoredCredential
        """
        return self._stored_credentials

    @stored_credentials.setter
    def stored_credentials(self, stored_credentials):
        """Sets the stored_credentials of this PaymentDevicePreAuthTransactionAllOf.


        :param stored_credentials: The stored_credentials of this PaymentDevicePreAuthTransactionAllOf.  # noqa: E501
        :type: StoredCredential
        """

        self._stored_credentials = stored_credentials

    @property
    def split_shipment(self):
        """Gets the split_shipment of this PaymentDevicePreAuthTransactionAllOf.  # noqa: E501


        :return: The split_shipment of this PaymentDevicePreAuthTransactionAllOf.  # noqa: E501
        :rtype: SplitShipment
        """
        return self._split_shipment

    @split_shipment.setter
    def split_shipment(self, split_shipment):
        """Sets the split_shipment of this PaymentDevicePreAuthTransactionAllOf.


        :param split_shipment: The split_shipment of this PaymentDevicePreAuthTransactionAllOf.  # noqa: E501
        :type: SplitShipment
        """

        self._split_shipment = split_shipment

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
        if not isinstance(other, PaymentDevicePreAuthTransactionAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
