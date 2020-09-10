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


class Secure3D10AuthenticationUpdateRequestAllOf(object):
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
        'payer_authentication_response': 'str',
        'merchant_data': 'str',
        'security_code': 'str',
    }

    attribute_map = {
        'payer_authentication_response': 'payerAuthenticationResponse',  # noqa: E501
        'merchant_data': 'merchantData',  # noqa: E501
        'security_code': 'securityCode',  # noqa: E501
    }

    def __init__(self, payer_authentication_response, merchant_data, security_code=None):  # noqa: E501
        """Secure3D10AuthenticationUpdateRequestAllOf - a model defined in OpenAPI

        Args:
            payer_authentication_response (str): A formatted message providing results of the issuer’s cardholder authentication.
            merchant_data (str): Formatted string encoding transaction time, order ID, and return URL data.

        Keyword Args:  # noqa: E501  # noqa: E501
            security_code (str): Card security code if required by merchant.. [optional]  # noqa: E501
        """

        self._payer_authentication_response = None
        self._merchant_data = None
        self._security_code = None
        self.discriminator = None

        self.payer_authentication_response = payer_authentication_response
        self.merchant_data = merchant_data
        if security_code is not None:
            self.security_code = security_code  # noqa: E501

    @property
    def payer_authentication_response(self):
        """Gets the payer_authentication_response of this Secure3D10AuthenticationUpdateRequestAllOf.  # noqa: E501

        A formatted message providing results of the issuer’s cardholder authentication.  # noqa: E501

        :return: The payer_authentication_response of this Secure3D10AuthenticationUpdateRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._payer_authentication_response

    @payer_authentication_response.setter
    def payer_authentication_response(
            self,
            payer_authentication_response):
        """Sets the payer_authentication_response of this Secure3D10AuthenticationUpdateRequestAllOf.

        A formatted message providing results of the issuer’s cardholder authentication.  # noqa: E501

        :param payer_authentication_response: The payer_authentication_response of this Secure3D10AuthenticationUpdateRequestAllOf.  # noqa: E501
        :type: str
        """
        if payer_authentication_response is None:
            raise ValueError("Invalid value for `payer_authentication_response`, must not be `None`")  # noqa: E501
        if payer_authentication_response is not None and not re.search(r'^(?!\s*$).+', payer_authentication_response):  # noqa: E501
            raise ValueError(r"Invalid value for `payer_authentication_response`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._payer_authentication_response = (
            payer_authentication_response)

    @property
    def merchant_data(self):
        """Gets the merchant_data of this Secure3D10AuthenticationUpdateRequestAllOf.  # noqa: E501

        Formatted string encoding transaction time, order ID, and return URL data.  # noqa: E501

        :return: The merchant_data of this Secure3D10AuthenticationUpdateRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._merchant_data

    @merchant_data.setter
    def merchant_data(
            self,
            merchant_data):
        """Sets the merchant_data of this Secure3D10AuthenticationUpdateRequestAllOf.

        Formatted string encoding transaction time, order ID, and return URL data.  # noqa: E501

        :param merchant_data: The merchant_data of this Secure3D10AuthenticationUpdateRequestAllOf.  # noqa: E501
        :type: str
        """
        if merchant_data is None:
            raise ValueError("Invalid value for `merchant_data`, must not be `None`")  # noqa: E501
        if merchant_data is not None and not re.search(r'^(?!\s*$).+', merchant_data):  # noqa: E501
            raise ValueError(r"Invalid value for `merchant_data`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._merchant_data = (
            merchant_data)

    @property
    def security_code(self):
        """Gets the security_code of this Secure3D10AuthenticationUpdateRequestAllOf.  # noqa: E501

        Card security code if required by merchant.  # noqa: E501

        :return: The security_code of this Secure3D10AuthenticationUpdateRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(
            self,
            security_code):
        """Sets the security_code of this Secure3D10AuthenticationUpdateRequestAllOf.

        Card security code if required by merchant.  # noqa: E501

        :param security_code: The security_code of this Secure3D10AuthenticationUpdateRequestAllOf.  # noqa: E501
        :type: str
        """

        self._security_code = (
            security_code)

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
        if not isinstance(other, Secure3D10AuthenticationUpdateRequestAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
