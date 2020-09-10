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


class ReferencedOrderPaymentSchedulesRequestAllOf(object):
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
        'referenced_order_id': 'str',
    }

    attribute_map = {
        'referenced_order_id': 'referencedOrderId',  # noqa: E501
    }

    def __init__(self, referenced_order_id):  # noqa: E501
        """ReferencedOrderPaymentSchedulesRequestAllOf - a model defined in OpenAPI

        Args:
            referenced_order_id (str): Order ID used to create recurring payment from existing transaction.

        Keyword Args:  # noqa: E501
        """

        self._referenced_order_id = None
        self.discriminator = None

        self.referenced_order_id = referenced_order_id

    @property
    def referenced_order_id(self):
        """Gets the referenced_order_id of this ReferencedOrderPaymentSchedulesRequestAllOf.  # noqa: E501

        Order ID used to create recurring payment from existing transaction.  # noqa: E501

        :return: The referenced_order_id of this ReferencedOrderPaymentSchedulesRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._referenced_order_id

    @referenced_order_id.setter
    def referenced_order_id(
            self,
            referenced_order_id):
        """Sets the referenced_order_id of this ReferencedOrderPaymentSchedulesRequestAllOf.

        Order ID used to create recurring payment from existing transaction.  # noqa: E501

        :param referenced_order_id: The referenced_order_id of this ReferencedOrderPaymentSchedulesRequestAllOf.  # noqa: E501
        :type: str
        """
        if referenced_order_id is None:
            raise ValueError("Invalid value for `referenced_order_id`, must not be `None`")  # noqa: E501
        if referenced_order_id is not None and not re.search(r'^(?!\s*$).+', referenced_order_id):  # noqa: E501
            raise ValueError(r"Invalid value for `referenced_order_id`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._referenced_order_id = (
            referenced_order_id)

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
        if not isinstance(other, ReferencedOrderPaymentSchedulesRequestAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
