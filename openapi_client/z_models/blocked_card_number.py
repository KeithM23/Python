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


class BlockedCardNumber(object):
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
        'token_identifier': 'str',
    }

    attribute_map = {
        'card_number': 'cardNumber',  # noqa: E501
        'token_identifier': 'tokenIdentifier',  # noqa: E501
    }

    def __init__(self, card_number=None, token_identifier=None):  # noqa: E501
        """BlockedCardNumber - a model defined in OpenAPI



        Keyword Args:
            card_number (str): Use this field to send clear PAN or tokens other than TransArmor Token.. [optional]  # noqa: E501
            token_identifier (str): Token identifier.. [optional]  # noqa: E501
        """

        self._card_number = None
        self._token_identifier = None
        self.discriminator = None

        if card_number is not None:
            self.card_number = card_number  # noqa: E501
        if token_identifier is not None:
            self.token_identifier = token_identifier  # noqa: E501

    @property
    def card_number(self):
        """Gets the card_number of this BlockedCardNumber.  # noqa: E501

        Use this field to send clear PAN or tokens other than TransArmor Token.  # noqa: E501

        :return: The card_number of this BlockedCardNumber.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(
            self,
            card_number):
        """Sets the card_number of this BlockedCardNumber.

        Use this field to send clear PAN or tokens other than TransArmor Token.  # noqa: E501

        :param card_number: The card_number of this BlockedCardNumber.  # noqa: E501
        :type: str
        """

        self._card_number = (
            card_number)

    @property
    def token_identifier(self):
        """Gets the token_identifier of this BlockedCardNumber.  # noqa: E501

        Token identifier.  # noqa: E501

        :return: The token_identifier of this BlockedCardNumber.  # noqa: E501
        :rtype: str
        """
        return self._token_identifier

    @token_identifier.setter
    def token_identifier(
            self,
            token_identifier):
        """Sets the token_identifier of this BlockedCardNumber.

        Token identifier.  # noqa: E501

        :param token_identifier: The token_identifier of this BlockedCardNumber.  # noqa: E501
        :type: str
        """

        self._token_identifier = (
            token_identifier)

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
        if not isinstance(other, BlockedCardNumber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
