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


class BancontactQR(object):
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
        'transaction_routing_means': 'str',
        'issuer_customer_reference': 'str',
    }

    attribute_map = {
        'transaction_routing_means': 'transactionRoutingMeans',  # noqa: E501
        'issuer_customer_reference': 'issuerCustomerReference',  # noqa: E501
    }

    def __init__(self, transaction_routing_means, issuer_customer_reference=None):  # noqa: E501
        """BancontactQR - a model defined in OpenAPI

        Args:
            transaction_routing_means (str): Transaction Routing Means.

        Keyword Args:  # noqa: E501
            issuer_customer_reference (str): Issuer Customer Reference.. [optional]  # noqa: E501
        """

        self._transaction_routing_means = None
        self._issuer_customer_reference = None
        self.discriminator = None

        self.transaction_routing_means = transaction_routing_means
        if issuer_customer_reference is not None:
            self.issuer_customer_reference = issuer_customer_reference  # noqa: E501

    @property
    def transaction_routing_means(self):
        """Gets the transaction_routing_means of this BancontactQR.  # noqa: E501

        Transaction Routing Means.  # noqa: E501

        :return: The transaction_routing_means of this BancontactQR.  # noqa: E501
        :rtype: str
        """
        return self._transaction_routing_means

    @transaction_routing_means.setter
    def transaction_routing_means(
            self,
            transaction_routing_means):
        """Sets the transaction_routing_means of this BancontactQR.

        Transaction Routing Means.  # noqa: E501

        :param transaction_routing_means: The transaction_routing_means of this BancontactQR.  # noqa: E501
        :type: str
        """
        if transaction_routing_means is None:
            raise ValueError("Invalid value for `transaction_routing_means`, must not be `None`")  # noqa: E501
        allowed_values = ["QR Code", "URL Intent"]  # noqa: E501
        if transaction_routing_means not in allowed_values:
            raise ValueError(
                "Invalid value for `transaction_routing_means` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_routing_means, allowed_values)
            )

        self._transaction_routing_means = (
            transaction_routing_means)

    @property
    def issuer_customer_reference(self):
        """Gets the issuer_customer_reference of this BancontactQR.  # noqa: E501

        Issuer Customer Reference.  # noqa: E501

        :return: The issuer_customer_reference of this BancontactQR.  # noqa: E501
        :rtype: str
        """
        return self._issuer_customer_reference

    @issuer_customer_reference.setter
    def issuer_customer_reference(
            self,
            issuer_customer_reference):
        """Sets the issuer_customer_reference of this BancontactQR.

        Issuer Customer Reference.  # noqa: E501

        :param issuer_customer_reference: The issuer_customer_reference of this BancontactQR.  # noqa: E501
        :type: str
        """
        if issuer_customer_reference is not None and len(issuer_customer_reference) > 254:
            raise ValueError("Invalid value for `issuer_customer_reference`, length must be less than or equal to `254`")  # noqa: E501

        self._issuer_customer_reference = (
            issuer_customer_reference)

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
        if not isinstance(other, BancontactQR):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
