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


class SubMerchantData(object):
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
        'mcc': 'str',
        'legal_name': 'str',
        'timezone': 'str',
        'address': 'Address',
        'document': 'Document',
        'merchant_id': 'str',
    }

    attribute_map = {
        'mcc': 'mcc',  # noqa: E501
        'legal_name': 'legalName',  # noqa: E501
        'timezone': 'timezone',  # noqa: E501
        'address': 'address',  # noqa: E501
        'document': 'document',  # noqa: E501
        'merchant_id': 'merchantId',  # noqa: E501
    }

    def __init__(self, mcc, legal_name=None, timezone=None, address=None, document=None, merchant_id=None):  # noqa: E501
        """SubMerchantData - a model defined in OpenAPI

        Args:
            mcc (str): Merchant category code.

        Keyword Args:  # noqa: E501
            legal_name (str): Store legal name.. [optional]  # noqa: E501
            timezone (str): Timezone.. [optional]  # noqa: E501
            address (Address): [optional]  # noqa: E501
            document (Document): [optional]  # noqa: E501
            merchant_id (str): Sub-merchant ID.. [optional]  # noqa: E501
        """

        self._mcc = None
        self._legal_name = None
        self._timezone = None
        self._address = None
        self._document = None
        self._merchant_id = None
        self.discriminator = None

        self.mcc = mcc
        if legal_name is not None:
            self.legal_name = legal_name  # noqa: E501
        if timezone is not None:
            self.timezone = timezone  # noqa: E501
        if address is not None:
            self.address = address  # noqa: E501
        if document is not None:
            self.document = document  # noqa: E501
        if merchant_id is not None:
            self.merchant_id = merchant_id  # noqa: E501

    @property
    def mcc(self):
        """Gets the mcc of this SubMerchantData.  # noqa: E501

        Merchant category code.  # noqa: E501

        :return: The mcc of this SubMerchantData.  # noqa: E501
        :rtype: str
        """
        return self._mcc

    @mcc.setter
    def mcc(
            self,
            mcc):
        """Sets the mcc of this SubMerchantData.

        Merchant category code.  # noqa: E501

        :param mcc: The mcc of this SubMerchantData.  # noqa: E501
        :type: str
        """
        if mcc is None:
            raise ValueError("Invalid value for `mcc`, must not be `None`")  # noqa: E501
        if mcc is not None and not re.search(r'[0-9]{4}', mcc):  # noqa: E501
            raise ValueError(r"Invalid value for `mcc`, must be a follow pattern or equal to `/[0-9]{4}/`")  # noqa: E501

        self._mcc = (
            mcc)

    @property
    def legal_name(self):
        """Gets the legal_name of this SubMerchantData.  # noqa: E501

        Store legal name.  # noqa: E501

        :return: The legal_name of this SubMerchantData.  # noqa: E501
        :rtype: str
        """
        return self._legal_name

    @legal_name.setter
    def legal_name(
            self,
            legal_name):
        """Sets the legal_name of this SubMerchantData.

        Store legal name.  # noqa: E501

        :param legal_name: The legal_name of this SubMerchantData.  # noqa: E501
        :type: str
        """
        if legal_name is not None and len(legal_name) > 100:
            raise ValueError("Invalid value for `legal_name`, length must be less than or equal to `100`")  # noqa: E501

        self._legal_name = (
            legal_name)

    @property
    def timezone(self):
        """Gets the timezone of this SubMerchantData.  # noqa: E501

        Timezone.  # noqa: E501

        :return: The timezone of this SubMerchantData.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(
            self,
            timezone):
        """Sets the timezone of this SubMerchantData.

        Timezone.  # noqa: E501

        :param timezone: The timezone of this SubMerchantData.  # noqa: E501
        :type: str
        """
        if timezone is not None and len(timezone) > 500:
            raise ValueError("Invalid value for `timezone`, length must be less than or equal to `500`")  # noqa: E501

        self._timezone = (
            timezone)

    @property
    def address(self):
        """Gets the address of this SubMerchantData.  # noqa: E501


        :return: The address of this SubMerchantData.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(
            self,
            address):
        """Sets the address of this SubMerchantData.


        :param address: The address of this SubMerchantData.  # noqa: E501
        :type: Address
        """

        self._address = (
            address)

    @property
    def document(self):
        """Gets the document of this SubMerchantData.  # noqa: E501


        :return: The document of this SubMerchantData.  # noqa: E501
        :rtype: Document
        """
        return self._document

    @document.setter
    def document(
            self,
            document):
        """Sets the document of this SubMerchantData.


        :param document: The document of this SubMerchantData.  # noqa: E501
        :type: Document
        """

        self._document = (
            document)

    @property
    def merchant_id(self):
        """Gets the merchant_id of this SubMerchantData.  # noqa: E501

        Sub-merchant ID.  # noqa: E501

        :return: The merchant_id of this SubMerchantData.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(
            self,
            merchant_id):
        """Sets the merchant_id of this SubMerchantData.

        Sub-merchant ID.  # noqa: E501

        :param merchant_id: The merchant_id of this SubMerchantData.  # noqa: E501
        :type: str
        """
        if merchant_id is not None and len(merchant_id) > 50:
            raise ValueError("Invalid value for `merchant_id`, length must be less than or equal to `50`")  # noqa: E501

        self._merchant_id = (
            merchant_id)

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
        if not isinstance(other, SubMerchantData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
