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


class SharedSecretConfigurationRequest(object):
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
        'shared_secret': 'str'
    }

    attribute_map = {
        'shared_secret': 'sharedSecret'
    }

    def __init__(self, shared_secret=None):  # noqa: E501
        """SharedSecretConfigurationRequest - a model defined in OpenAPI"""  # noqa: E501

        self._shared_secret = None
        self.discriminator = None

        self.shared_secret = shared_secret

    @property
    def shared_secret(self):
        """Gets the shared_secret of this SharedSecretConfigurationRequest.  # noqa: E501

        Shared secret/password for Connect.  # noqa: E501

        :return: The shared_secret of this SharedSecretConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._shared_secret

    @shared_secret.setter
    def shared_secret(self, shared_secret):
        """Sets the shared_secret of this SharedSecretConfigurationRequest.

        Shared secret/password for Connect.  # noqa: E501

        :param shared_secret: The shared_secret of this SharedSecretConfigurationRequest.  # noqa: E501
        :type: str
        """
        if shared_secret is None:
            raise ValueError("Invalid value for `shared_secret`, must not be `None`")  # noqa: E501
        if shared_secret is not None and not re.search(r'[^ ]{7,16}', shared_secret):  # noqa: E501
            raise ValueError(r"Invalid value for `shared_secret`, must be a follow pattern or equal to `/[^ ]{7,16}/`")  # noqa: E501

        self._shared_secret = shared_secret

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
        if not isinstance(other, SharedSecretConfigurationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
