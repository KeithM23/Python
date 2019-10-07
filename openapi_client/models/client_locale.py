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


class ClientLocale(object):
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
        'language': 'str',
        'country': 'str'
    }

    attribute_map = {
        'language': 'language',
        'country': 'country'
    }

    def __init__(self, language=None, country=None):  # noqa: E501
        """ClientLocale - a model defined in OpenAPI"""  # noqa: E501

        self._language = None
        self._country = None
        self.discriminator = None

        self.language = language
        self.country = country

    @property
    def language(self):
        """Gets the language of this ClientLocale.  # noqa: E501

        Language used by client.  # noqa: E501

        :return: The language of this ClientLocale.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ClientLocale.

        Language used by client.  # noqa: E501

        :param language: The language of this ClientLocale.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501
        if language is not None and not re.search(r'^(?!\s*$).+', language):  # noqa: E501
            raise ValueError(r"Invalid value for `language`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._language = language

    @property
    def country(self):
        """Gets the country of this ClientLocale.  # noqa: E501

        Country of the client.  # noqa: E501

        :return: The country of this ClientLocale.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ClientLocale.

        Country of the client.  # noqa: E501

        :param country: The country of this ClientLocale.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501
        if country is not None and not re.search(r'^(?!\s*$).+', country):  # noqa: E501
            raise ValueError(r"Invalid value for `country`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._country = country

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
        if not isinstance(other, ClientLocale):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
