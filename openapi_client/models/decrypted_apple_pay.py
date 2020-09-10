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


class DecryptedApplePay(object):
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
        'account_number': 'str',
        'expiration': 'str',
        'cardholder_name': 'str',
        'brand': 'str',
        'cryptogram': 'str',
        'eci_indicator': 'str'
    }

    attribute_map = {
        'account_number': 'accountNumber',
        'expiration': 'expiration',
        'cardholder_name': 'cardholderName',
        'brand': 'brand',
        'cryptogram': 'cryptogram',
        'eci_indicator': 'eciIndicator'
    }

    def __init__(self, account_number=None, expiration=None, cardholder_name=None, brand=None, cryptogram=None, eci_indicator=None):  # noqa: E501
        """DecryptedApplePay - a model defined in OpenAPI"""  # noqa: E501

        self._account_number = None
        self._expiration = None
        self._cardholder_name = None
        self._brand = None
        self._cryptogram = None
        self._eci_indicator = None
        self.discriminator = None

        self.account_number = account_number
        self.expiration = expiration
        if cardholder_name is not None:
            self.cardholder_name = cardholder_name
        if brand is not None:
            self.brand = brand
        self.cryptogram = cryptogram
        self.eci_indicator = eci_indicator

    @property
    def account_number(self):
        """Gets the account_number of this DecryptedApplePay.  # noqa: E501

        Payment card number.  # noqa: E501

        :return: The account_number of this DecryptedApplePay.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this DecryptedApplePay.

        Payment card number.  # noqa: E501

        :param account_number: The account_number of this DecryptedApplePay.  # noqa: E501
        :type: str
        """
        if account_number is None:
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501
        if account_number is not None and not re.search(r'[0-9]{13,19}', account_number):  # noqa: E501
            raise ValueError(r"Invalid value for `account_number`, must be a follow pattern or equal to `/[0-9]{13,19}/`")  # noqa: E501

        self._account_number = account_number

    @property
    def expiration(self):
        """Gets the expiration of this DecryptedApplePay.  # noqa: E501

        Card expiration date in MMYYYY format.  # noqa: E501

        :return: The expiration of this DecryptedApplePay.  # noqa: E501
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this DecryptedApplePay.

        Card expiration date in MMYYYY format.  # noqa: E501

        :param expiration: The expiration of this DecryptedApplePay.  # noqa: E501
        :type: str
        """
        if expiration is None:
            raise ValueError("Invalid value for `expiration`, must not be `None`")  # noqa: E501
        if expiration is not None and not re.search(r'[0-9]{6}', expiration):  # noqa: E501
            raise ValueError(r"Invalid value for `expiration`, must be a follow pattern or equal to `/[0-9]{6}/`")  # noqa: E501

        self._expiration = expiration

    @property
    def cardholder_name(self):
        """Gets the cardholder_name of this DecryptedApplePay.  # noqa: E501

        Name of the cardholder.  # noqa: E501

        :return: The cardholder_name of this DecryptedApplePay.  # noqa: E501
        :rtype: str
        """
        return self._cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, cardholder_name):
        """Sets the cardholder_name of this DecryptedApplePay.

        Name of the cardholder.  # noqa: E501

        :param cardholder_name: The cardholder_name of this DecryptedApplePay.  # noqa: E501
        :type: str
        """
        if cardholder_name is not None and len(cardholder_name) > 96:
            raise ValueError("Invalid value for `cardholder_name`, length must be less than or equal to `96`")  # noqa: E501
        if cardholder_name is not None and not re.search(r'^(?!\s*$).+', cardholder_name):  # noqa: E501
            raise ValueError(r"Invalid value for `cardholder_name`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._cardholder_name = cardholder_name

    @property
    def brand(self):
        """Gets the brand of this DecryptedApplePay.  # noqa: E501

        Card brand.  # noqa: E501

        :return: The brand of this DecryptedApplePay.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this DecryptedApplePay.

        Card brand.  # noqa: E501

        :param brand: The brand of this DecryptedApplePay.  # noqa: E501
        :type: str
        """
        if brand is not None and not re.search(r'^(?!\s*$).+', brand):  # noqa: E501
            raise ValueError(r"Invalid value for `brand`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._brand = brand

    @property
    def cryptogram(self):
        """Gets the cryptogram of this DecryptedApplePay.  # noqa: E501

        The wallet cryptogram from the decrypted data.  # noqa: E501

        :return: The cryptogram of this DecryptedApplePay.  # noqa: E501
        :rtype: str
        """
        return self._cryptogram

    @cryptogram.setter
    def cryptogram(self, cryptogram):
        """Sets the cryptogram of this DecryptedApplePay.

        The wallet cryptogram from the decrypted data.  # noqa: E501

        :param cryptogram: The cryptogram of this DecryptedApplePay.  # noqa: E501
        :type: str
        """
        if cryptogram is None:
            raise ValueError("Invalid value for `cryptogram`, must not be `None`")  # noqa: E501
        if cryptogram is not None and not re.search(r'^(?!\s*$).+', cryptogram):  # noqa: E501
            raise ValueError(r"Invalid value for `cryptogram`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._cryptogram = cryptogram

    @property
    def eci_indicator(self):
        """Gets the eci_indicator of this DecryptedApplePay.  # noqa: E501

        The ECI indicator from the decrypted data.  # noqa: E501

        :return: The eci_indicator of this DecryptedApplePay.  # noqa: E501
        :rtype: str
        """
        return self._eci_indicator

    @eci_indicator.setter
    def eci_indicator(self, eci_indicator):
        """Sets the eci_indicator of this DecryptedApplePay.

        The ECI indicator from the decrypted data.  # noqa: E501

        :param eci_indicator: The eci_indicator of this DecryptedApplePay.  # noqa: E501
        :type: str
        """
        if eci_indicator is None:
            raise ValueError("Invalid value for `eci_indicator`, must not be `None`")  # noqa: E501
        if eci_indicator is not None and not re.search(r'[0-9]{2}', eci_indicator):  # noqa: E501
            raise ValueError(r"Invalid value for `eci_indicator`, must be a follow pattern or equal to `/[0-9]{2}/`")  # noqa: E501

        self._eci_indicator = eci_indicator

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
        if not isinstance(other, DecryptedApplePay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
