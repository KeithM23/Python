# coding: utf-8

"""
    Payment Gateway API Specification.

    Payment Gateway API for payment processing. Version 6.4.0.20181018.001   # noqa: E501

    OpenAPI spec version: 6.4.0.20181018.001
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AuthenticationResponseVerificationRequest(object):
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
        'store_id': 'str',
        'security_code': 'str',
        'authentication_response_verification': 'AuthenticationResponseVerification',
        'amount': 'Amount'
    }

    attribute_map = {
        'store_id': 'storeId',
        'security_code': 'securityCode',
        'authentication_response_verification': 'authenticationResponseVerification',
        'amount': 'amount'
    }

    def __init__(self, store_id=None, security_code=None, authentication_response_verification=None, amount=None):  # noqa: E501
        """AuthenticationResponseVerificationRequest - a model defined in OpenAPI"""  # noqa: E501

        self._store_id = None
        self._security_code = None
        self._authentication_response_verification = None
        self._amount = None
        self.discriminator = None

        if store_id is not None:
            self.store_id = store_id
        if security_code is not None:
            self.security_code = security_code
        if authentication_response_verification is not None:
            self.authentication_response_verification = authentication_response_verification
        if amount is not None:
            self.amount = amount

    @property
    def store_id(self):
        """Gets the store_id of this AuthenticationResponseVerificationRequest.  # noqa: E501


        :return: The store_id of this AuthenticationResponseVerificationRequest.  # noqa: E501
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this AuthenticationResponseVerificationRequest.


        :param store_id: The store_id of this AuthenticationResponseVerificationRequest.  # noqa: E501
        :type: str
        """

        self._store_id = store_id

    @property
    def security_code(self):
        """Gets the security_code of this AuthenticationResponseVerificationRequest.  # noqa: E501

        Card Security Code if required by merchant.  # noqa: E501

        :return: The security_code of this AuthenticationResponseVerificationRequest.  # noqa: E501
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code):
        """Sets the security_code of this AuthenticationResponseVerificationRequest.

        Card Security Code if required by merchant.  # noqa: E501

        :param security_code: The security_code of this AuthenticationResponseVerificationRequest.  # noqa: E501
        :type: str
        """

        self._security_code = security_code

    @property
    def authentication_response_verification(self):
        """Gets the authentication_response_verification of this AuthenticationResponseVerificationRequest.  # noqa: E501


        :return: The authentication_response_verification of this AuthenticationResponseVerificationRequest.  # noqa: E501
        :rtype: AuthenticationResponseVerification
        """
        return self._authentication_response_verification

    @authentication_response_verification.setter
    def authentication_response_verification(self, authentication_response_verification):
        """Sets the authentication_response_verification of this AuthenticationResponseVerificationRequest.


        :param authentication_response_verification: The authentication_response_verification of this AuthenticationResponseVerificationRequest.  # noqa: E501
        :type: AuthenticationResponseVerification
        """

        self._authentication_response_verification = authentication_response_verification

    @property
    def amount(self):
        """Gets the amount of this AuthenticationResponseVerificationRequest.  # noqa: E501


        :return: The amount of this AuthenticationResponseVerificationRequest.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AuthenticationResponseVerificationRequest.


        :param amount: The amount of this AuthenticationResponseVerificationRequest.  # noqa: E501
        :type: Amount
        """

        self._amount = amount

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
        if not isinstance(other, AuthenticationResponseVerificationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other