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


class WalletPreAuthTransactionAllOf(object):
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
        'wallet_payment_method': 'WalletPaymentMethod',
        'split_shipment': 'SplitShipment',
        'payment_facilitator': 'PaymentFacilitator'
    }

    attribute_map = {
        'wallet_payment_method': 'walletPaymentMethod',
        'split_shipment': 'splitShipment',
        'payment_facilitator': 'paymentFacilitator'
    }

    def __init__(self, wallet_payment_method=None, split_shipment=None, payment_facilitator=None):  # noqa: E501
        """WalletPreAuthTransactionAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._wallet_payment_method = None
        self._split_shipment = None
        self._payment_facilitator = None
        self.discriminator = None

        self.wallet_payment_method = wallet_payment_method
        if split_shipment is not None:
            self.split_shipment = split_shipment
        if payment_facilitator is not None:
            self.payment_facilitator = payment_facilitator

    @property
    def wallet_payment_method(self):
        """Gets the wallet_payment_method of this WalletPreAuthTransactionAllOf.  # noqa: E501


        :return: The wallet_payment_method of this WalletPreAuthTransactionAllOf.  # noqa: E501
        :rtype: WalletPaymentMethod
        """
        return self._wallet_payment_method

    @wallet_payment_method.setter
    def wallet_payment_method(self, wallet_payment_method):
        """Sets the wallet_payment_method of this WalletPreAuthTransactionAllOf.


        :param wallet_payment_method: The wallet_payment_method of this WalletPreAuthTransactionAllOf.  # noqa: E501
        :type: WalletPaymentMethod
        """
        if wallet_payment_method is None:
            raise ValueError("Invalid value for `wallet_payment_method`, must not be `None`")  # noqa: E501

        self._wallet_payment_method = wallet_payment_method

    @property
    def split_shipment(self):
        """Gets the split_shipment of this WalletPreAuthTransactionAllOf.  # noqa: E501


        :return: The split_shipment of this WalletPreAuthTransactionAllOf.  # noqa: E501
        :rtype: SplitShipment
        """
        return self._split_shipment

    @split_shipment.setter
    def split_shipment(self, split_shipment):
        """Sets the split_shipment of this WalletPreAuthTransactionAllOf.


        :param split_shipment: The split_shipment of this WalletPreAuthTransactionAllOf.  # noqa: E501
        :type: SplitShipment
        """

        self._split_shipment = split_shipment

    @property
    def payment_facilitator(self):
        """Gets the payment_facilitator of this WalletPreAuthTransactionAllOf.  # noqa: E501


        :return: The payment_facilitator of this WalletPreAuthTransactionAllOf.  # noqa: E501
        :rtype: PaymentFacilitator
        """
        return self._payment_facilitator

    @payment_facilitator.setter
    def payment_facilitator(self, payment_facilitator):
        """Sets the payment_facilitator of this WalletPreAuthTransactionAllOf.


        :param payment_facilitator: The payment_facilitator of this WalletPreAuthTransactionAllOf.  # noqa: E501
        :type: PaymentFacilitator
        """

        self._payment_facilitator = payment_facilitator

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
        if not isinstance(other, WalletPreAuthTransactionAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
