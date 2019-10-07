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


class FraudRegistrationCard(object):
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
        'cardholder_name': 'str',
        'card_number': 'str',
        'exp_date': 'str',
        'cvv_present': 'str',
        'issuer': 'str',
        'card_reissued_number': 'str'
    }

    attribute_map = {
        'cardholder_name': 'cardholderName',
        'card_number': 'cardNumber',
        'exp_date': 'expDate',
        'cvv_present': 'cvvPresent',
        'issuer': 'issuer',
        'card_reissued_number': 'cardReissuedNumber'
    }

    def __init__(self, cardholder_name=None, card_number=None, exp_date=None, cvv_present=None, issuer=None, card_reissued_number=None):  # noqa: E501
        """FraudRegistrationCard - a model defined in OpenAPI"""  # noqa: E501

        self._cardholder_name = None
        self._card_number = None
        self._exp_date = None
        self._cvv_present = None
        self._issuer = None
        self._card_reissued_number = None
        self.discriminator = None

        if cardholder_name is not None:
            self.cardholder_name = cardholder_name
        if card_number is not None:
            self.card_number = card_number
        if exp_date is not None:
            self.exp_date = exp_date
        if cvv_present is not None:
            self.cvv_present = cvv_present
        if issuer is not None:
            self.issuer = issuer
        if card_reissued_number is not None:
            self.card_reissued_number = card_reissued_number

    @property
    def cardholder_name(self):
        """Gets the cardholder_name of this FraudRegistrationCard.  # noqa: E501

        The cardholder name as it appears on the card.  # noqa: E501

        :return: The cardholder_name of this FraudRegistrationCard.  # noqa: E501
        :rtype: str
        """
        return self._cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, cardholder_name):
        """Sets the cardholder_name of this FraudRegistrationCard.

        The cardholder name as it appears on the card.  # noqa: E501

        :param cardholder_name: The cardholder_name of this FraudRegistrationCard.  # noqa: E501
        :type: str
        """

        self._cardholder_name = cardholder_name

    @property
    def card_number(self):
        """Gets the card_number of this FraudRegistrationCard.  # noqa: E501

        Use this field to send clear PAN or tokens other than TransArmor Token.  # noqa: E501

        :return: The card_number of this FraudRegistrationCard.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this FraudRegistrationCard.

        Use this field to send clear PAN or tokens other than TransArmor Token.  # noqa: E501

        :param card_number: The card_number of this FraudRegistrationCard.  # noqa: E501
        :type: str
        """

        self._card_number = card_number

    @property
    def exp_date(self):
        """Gets the exp_date of this FraudRegistrationCard.  # noqa: E501

        Payment method expiration date. Format is MMYYYY.  # noqa: E501

        :return: The exp_date of this FraudRegistrationCard.  # noqa: E501
        :rtype: str
        """
        return self._exp_date

    @exp_date.setter
    def exp_date(self, exp_date):
        """Sets the exp_date of this FraudRegistrationCard.

        Payment method expiration date. Format is MMYYYY.  # noqa: E501

        :param exp_date: The exp_date of this FraudRegistrationCard.  # noqa: E501
        :type: str
        """

        self._exp_date = exp_date

    @property
    def cvv_present(self):
        """Gets the cvv_present of this FraudRegistrationCard.  # noqa: E501

        CVV present indicator.  # noqa: E501

        :return: The cvv_present of this FraudRegistrationCard.  # noqa: E501
        :rtype: str
        """
        return self._cvv_present

    @cvv_present.setter
    def cvv_present(self, cvv_present):
        """Sets the cvv_present of this FraudRegistrationCard.

        CVV present indicator.  # noqa: E501

        :param cvv_present: The cvv_present of this FraudRegistrationCard.  # noqa: E501
        :type: str
        """

        self._cvv_present = cvv_present

    @property
    def issuer(self):
        """Gets the issuer of this FraudRegistrationCard.  # noqa: E501

        The company (usually a bank) that issued the card.  # noqa: E501

        :return: The issuer of this FraudRegistrationCard.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this FraudRegistrationCard.

        The company (usually a bank) that issued the card.  # noqa: E501

        :param issuer: The issuer of this FraudRegistrationCard.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def card_reissued_number(self):
        """Gets the card_reissued_number of this FraudRegistrationCard.  # noqa: E501

        A number that distinguishes between two plastic cards with the same card number in the event of the card being re-issued.  # noqa: E501

        :return: The card_reissued_number of this FraudRegistrationCard.  # noqa: E501
        :rtype: str
        """
        return self._card_reissued_number

    @card_reissued_number.setter
    def card_reissued_number(self, card_reissued_number):
        """Sets the card_reissued_number of this FraudRegistrationCard.

        A number that distinguishes between two plastic cards with the same card number in the event of the card being re-issued.  # noqa: E501

        :param card_reissued_number: The card_reissued_number of this FraudRegistrationCard.  # noqa: E501
        :type: str
        """

        self._card_reissued_number = card_reissued_number

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
        if not isinstance(other, FraudRegistrationCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
