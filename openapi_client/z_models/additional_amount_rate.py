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


class AdditionalAmountRate(object):
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
        'amount': 'float',
        'rate': 'float',
    }

    attribute_map = {
        'amount': 'amount',  # noqa: E501
        'rate': 'rate',  # noqa: E501
    }

    def __init__(self, amount, rate):  # noqa: E501
        """AdditionalAmountRate - a model defined in OpenAPI

        Args:
            amount (float): Amount in 3 decimal 12 bytes total digit.
            rate (float): Rate in 3 decimal 12 bytes total digit.

        Keyword Args:  # noqa: E501  # noqa: E501
        """

        self._amount = None
        self._rate = None
        self.discriminator = None

        self.amount = amount
        self.rate = rate

    @property
    def amount(self):
        """Gets the amount of this AdditionalAmountRate.  # noqa: E501

        Amount in 3 decimal 12 bytes total digit.  # noqa: E501

        :return: The amount of this AdditionalAmountRate.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(
            self,
            amount):
        """Sets the amount of this AdditionalAmountRate.

        Amount in 3 decimal 12 bytes total digit.  # noqa: E501

        :param amount: The amount of this AdditionalAmountRate.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = (
            amount)

    @property
    def rate(self):
        """Gets the rate of this AdditionalAmountRate.  # noqa: E501

        Rate in 3 decimal 12 bytes total digit.  # noqa: E501

        :return: The rate of this AdditionalAmountRate.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(
            self,
            rate):
        """Sets the rate of this AdditionalAmountRate.

        Rate in 3 decimal 12 bytes total digit.  # noqa: E501

        :param rate: The rate of this AdditionalAmountRate.  # noqa: E501
        :type: float
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = (
            rate)

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
        if not isinstance(other, AdditionalAmountRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
