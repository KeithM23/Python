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


class FundingTransactionType(object):
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
        'disbursement_type': 'str',
        'sender_info': 'SenderInfo',
        'receiver_info': 'ReceiverInfo'
    }

    attribute_map = {
        'disbursement_type': 'disbursementType',
        'sender_info': 'senderInfo',
        'receiver_info': 'receiverInfo'
    }

    def __init__(self, disbursement_type=None, sender_info=None, receiver_info=None):  # noqa: E501
        """FundingTransactionType - a model defined in OpenAPI"""  # noqa: E501

        self._disbursement_type = None
        self._sender_info = None
        self._receiver_info = None
        self.discriminator = None

        self.disbursement_type = disbursement_type
        self.sender_info = sender_info
        self.receiver_info = receiver_info

    @property
    def disbursement_type(self):
        """Gets the disbursement_type of this FundingTransactionType.  # noqa: E501

        The type of disbursement.  # noqa: E501

        :return: The disbursement_type of this FundingTransactionType.  # noqa: E501
        :rtype: str
        """
        return self._disbursement_type

    @disbursement_type.setter
    def disbursement_type(self, disbursement_type):
        """Sets the disbursement_type of this FundingTransactionType.

        The type of disbursement.  # noqa: E501

        :param disbursement_type: The disbursement_type of this FundingTransactionType.  # noqa: E501
        :type: str
        """
        if disbursement_type is None:
            raise ValueError("Invalid value for `disbursement_type`, must not be `None`")  # noqa: E501

        self._disbursement_type = disbursement_type

    @property
    def sender_info(self):
        """Gets the sender_info of this FundingTransactionType.  # noqa: E501


        :return: The sender_info of this FundingTransactionType.  # noqa: E501
        :rtype: SenderInfo
        """
        return self._sender_info

    @sender_info.setter
    def sender_info(self, sender_info):
        """Sets the sender_info of this FundingTransactionType.


        :param sender_info: The sender_info of this FundingTransactionType.  # noqa: E501
        :type: SenderInfo
        """
        if sender_info is None:
            raise ValueError("Invalid value for `sender_info`, must not be `None`")  # noqa: E501

        self._sender_info = sender_info

    @property
    def receiver_info(self):
        """Gets the receiver_info of this FundingTransactionType.  # noqa: E501


        :return: The receiver_info of this FundingTransactionType.  # noqa: E501
        :rtype: ReceiverInfo
        """
        return self._receiver_info

    @receiver_info.setter
    def receiver_info(self, receiver_info):
        """Sets the receiver_info of this FundingTransactionType.


        :param receiver_info: The receiver_info of this FundingTransactionType.  # noqa: E501
        :type: ReceiverInfo
        """
        if receiver_info is None:
            raise ValueError("Invalid value for `receiver_info`, must not be `None`")  # noqa: E501

        self._receiver_info = receiver_info

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
        if not isinstance(other, FundingTransactionType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
