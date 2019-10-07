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


class AVSResponse(object):
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
        'street_match': 'str',
        'postal_code_match': 'str'
    }

    attribute_map = {
        'street_match': 'streetMatch',
        'postal_code_match': 'postalCodeMatch'
    }

    def __init__(self, street_match=None, postal_code_match=None):  # noqa: E501
        """AVSResponse - a model defined in OpenAPI"""  # noqa: E501

        self._street_match = None
        self._postal_code_match = None
        self.discriminator = None

        if street_match is not None:
            self.street_match = street_match
        if postal_code_match is not None:
            self.postal_code_match = postal_code_match

    @property
    def street_match(self):
        """Gets the street_match of this AVSResponse.  # noqa: E501

        Response if street matches that on file.  # noqa: E501

        :return: The street_match of this AVSResponse.  # noqa: E501
        :rtype: str
        """
        return self._street_match

    @street_match.setter
    def street_match(self, street_match):
        """Sets the street_match of this AVSResponse.

        Response if street matches that on file.  # noqa: E501

        :param street_match: The street_match of this AVSResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Y", "N", "NO_INPUT_DATA", "NOT_CHECKED"]  # noqa: E501
        if street_match not in allowed_values:
            raise ValueError(
                "Invalid value for `street_match` ({0}), must be one of {1}"  # noqa: E501
                .format(street_match, allowed_values)
            )

        self._street_match = street_match

    @property
    def postal_code_match(self):
        """Gets the postal_code_match of this AVSResponse.  # noqa: E501

        Response if postal code matches that on file.  # noqa: E501

        :return: The postal_code_match of this AVSResponse.  # noqa: E501
        :rtype: str
        """
        return self._postal_code_match

    @postal_code_match.setter
    def postal_code_match(self, postal_code_match):
        """Sets the postal_code_match of this AVSResponse.

        Response if postal code matches that on file.  # noqa: E501

        :param postal_code_match: The postal_code_match of this AVSResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Y", "N", "NO_INPUT_DATA", "NOT_CHECKED"]  # noqa: E501
        if postal_code_match not in allowed_values:
            raise ValueError(
                "Invalid value for `postal_code_match` ({0}), must be one of {1}"  # noqa: E501
                .format(postal_code_match, allowed_values)
            )

        self._postal_code_match = postal_code_match

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
        if not isinstance(other, AVSResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
