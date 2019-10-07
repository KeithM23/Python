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


class PaymentCardPayerAuthTransactionAllOf(object):
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
        'payment_method': 'PaymentCardPaymentMethod',
        'currency_conversion': 'CurrencyConversion'
    }

    attribute_map = {
        'payment_method': 'paymentMethod',
        'currency_conversion': 'currencyConversion'
    }

    def __init__(self, payment_method=None, currency_conversion=None):  # noqa: E501
        """PaymentCardPayerAuthTransactionAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._payment_method = None
        self._currency_conversion = None
        self.discriminator = None

        self.payment_method = payment_method
        if currency_conversion is not None:
            self.currency_conversion = currency_conversion

    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentCardPayerAuthTransactionAllOf.  # noqa: E501


        :return: The payment_method of this PaymentCardPayerAuthTransactionAllOf.  # noqa: E501
        :rtype: PaymentCardPaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentCardPayerAuthTransactionAllOf.


        :param payment_method: The payment_method of this PaymentCardPayerAuthTransactionAllOf.  # noqa: E501
        :type: PaymentCardPaymentMethod
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501

        self._payment_method = payment_method

    @property
    def currency_conversion(self):
        """Gets the currency_conversion of this PaymentCardPayerAuthTransactionAllOf.  # noqa: E501


        :return: The currency_conversion of this PaymentCardPayerAuthTransactionAllOf.  # noqa: E501
        :rtype: CurrencyConversion
        """
        return self._currency_conversion

    @currency_conversion.setter
    def currency_conversion(self, currency_conversion):
        """Sets the currency_conversion of this PaymentCardPayerAuthTransactionAllOf.


        :param currency_conversion: The currency_conversion of this PaymentCardPayerAuthTransactionAllOf.  # noqa: E501
        :type: CurrencyConversion
        """

        self._currency_conversion = currency_conversion

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
        if not isinstance(other, PaymentCardPayerAuthTransactionAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
