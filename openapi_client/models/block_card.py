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


class BlockCard(object):
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
        'card_number': 'str',
        'order_id': 'str',
        'merchant_transaction_id': 'str'
    }

    attribute_map = {
        'card_number': 'cardNumber',
        'order_id': 'orderId',
        'merchant_transaction_id': 'merchantTransactionId'
    }

    def __init__(self, card_number=None, order_id=None, merchant_transaction_id=None):  # noqa: E501
        """BlockCard - a model defined in OpenAPI"""  # noqa: E501

        self._card_number = None
        self._order_id = None
        self._merchant_transaction_id = None
        self.discriminator = None

        if card_number is not None:
            self.card_number = card_number
        if order_id is not None:
            self.order_id = order_id
        if merchant_transaction_id is not None:
            self.merchant_transaction_id = merchant_transaction_id

    @property
    def card_number(self):
        """Gets the card_number of this BlockCard.  # noqa: E501

        Use this field to send clear PAN or tokens other than TransArmor Token.  # noqa: E501

        :return: The card_number of this BlockCard.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this BlockCard.

        Use this field to send clear PAN or tokens other than TransArmor Token.  # noqa: E501

        :param card_number: The card_number of this BlockCard.  # noqa: E501
        :type: str
        """

        self._card_number = card_number

    @property
    def order_id(self):
        """Gets the order_id of this BlockCard.  # noqa: E501

        Client order ID.  # noqa: E501

        :return: The order_id of this BlockCard.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this BlockCard.

        Client order ID.  # noqa: E501

        :param order_id: The order_id of this BlockCard.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def merchant_transaction_id(self):
        """Gets the merchant_transaction_id of this BlockCard.  # noqa: E501

        The unique merchant transaction ID.  # noqa: E501

        :return: The merchant_transaction_id of this BlockCard.  # noqa: E501
        :rtype: str
        """
        return self._merchant_transaction_id

    @merchant_transaction_id.setter
    def merchant_transaction_id(self, merchant_transaction_id):
        """Sets the merchant_transaction_id of this BlockCard.

        The unique merchant transaction ID.  # noqa: E501

        :param merchant_transaction_id: The merchant_transaction_id of this BlockCard.  # noqa: E501
        :type: str
        """
        if merchant_transaction_id is not None and len(merchant_transaction_id) > 40:
            raise ValueError("Invalid value for `merchant_transaction_id`, length must be less than or equal to `40`")  # noqa: E501

        self._merchant_transaction_id = merchant_transaction_id

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
        if not isinstance(other, BlockCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
