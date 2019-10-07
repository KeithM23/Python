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


class EncryptedSamsungPay(object):
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
        'data': 'str',
        'version': 'str'
    }

    attribute_map = {
        'data': 'data',
        'version': 'version'
    }

    def __init__(self, data=None, version=None):  # noqa: E501
        """EncryptedSamsungPay - a model defined in OpenAPI"""  # noqa: E501

        self._data = None
        self._version = None
        self.discriminator = None

        self.data = data
        if version is not None:
            self.version = version

    @property
    def data(self):
        """Gets the data of this EncryptedSamsungPay.  # noqa: E501

        The encrypted wallet payload.  # noqa: E501

        :return: The data of this EncryptedSamsungPay.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this EncryptedSamsungPay.

        The encrypted wallet payload.  # noqa: E501

        :param data: The data of this EncryptedSamsungPay.  # noqa: E501
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501
        if data is not None and not re.search(r'^(?!\s*$).+', data):  # noqa: E501
            raise ValueError(r"Invalid value for `data`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._data = data

    @property
    def version(self):
        """Gets the version of this EncryptedSamsungPay.  # noqa: E501

        Identifies under which encryption/signing scheme this message has been created. In this way, the protocol can evolve over time if needed. For Google Payments transactions, this should be set to ECv1.  # noqa: E501

        :return: The version of this EncryptedSamsungPay.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this EncryptedSamsungPay.

        Identifies under which encryption/signing scheme this message has been created. In this way, the protocol can evolve over time if needed. For Google Payments transactions, this should be set to ECv1.  # noqa: E501

        :param version: The version of this EncryptedSamsungPay.  # noqa: E501
        :type: str
        """
        if version is not None and not re.search(r'^(?!\s*$).+', version):  # noqa: E501
            raise ValueError(r"Invalid value for `version`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, EncryptedSamsungPay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other