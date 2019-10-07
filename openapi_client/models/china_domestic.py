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


class ChinaDomestic(object):
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
        'product_code': 'str',
        'product_quantity': 'int',
        'product_price': 'float',
        'product_description': 'str',
        'redirect_url': 'str',
        'limit_card_function_to_debit': 'bool',
        'customer_id': 'str',
        'bank_id': 'str'
    }

    attribute_map = {
        'product_code': 'productCode',
        'product_quantity': 'productQuantity',
        'product_price': 'productPrice',
        'product_description': 'productDescription',
        'redirect_url': 'redirectURL',
        'limit_card_function_to_debit': 'limitCardFunctionToDebit',
        'customer_id': 'customerId',
        'bank_id': 'bankId'
    }

    def __init__(self, product_code=None, product_quantity=None, product_price=None, product_description=None, redirect_url=None, limit_card_function_to_debit=None, customer_id=None, bank_id=None):  # noqa: E501
        """ChinaDomestic - a model defined in OpenAPI"""  # noqa: E501

        self._product_code = None
        self._product_quantity = None
        self._product_price = None
        self._product_description = None
        self._redirect_url = None
        self._limit_card_function_to_debit = None
        self._customer_id = None
        self._bank_id = None
        self.discriminator = None

        self.product_code = product_code
        self.product_quantity = product_quantity
        self.product_price = product_price
        self.product_description = product_description
        self.redirect_url = redirect_url
        if limit_card_function_to_debit is not None:
            self.limit_card_function_to_debit = limit_card_function_to_debit
        if customer_id is not None:
            self.customer_id = customer_id
        if bank_id is not None:
            self.bank_id = bank_id

    @property
    def product_code(self):
        """Gets the product_code of this ChinaDomestic.  # noqa: E501

        Use this to indicate the product code according to the product category list.  # noqa: E501

        :return: The product_code of this ChinaDomestic.  # noqa: E501
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """Sets the product_code of this ChinaDomestic.

        Use this to indicate the product code according to the product category list.  # noqa: E501

        :param product_code: The product_code of this ChinaDomestic.  # noqa: E501
        :type: str
        """
        if product_code is None:
            raise ValueError("Invalid value for `product_code`, must not be `None`")  # noqa: E501
        if product_code is not None and len(product_code) > 32:
            raise ValueError("Invalid value for `product_code`, length must be less than or equal to `32`")  # noqa: E501
        if product_code is not None and not re.search(r'^(?!\s*$).+', product_code):  # noqa: E501
            raise ValueError(r"Invalid value for `product_code`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._product_code = product_code

    @property
    def product_quantity(self):
        """Gets the product_quantity of this ChinaDomestic.  # noqa: E501

        The quantity.  # noqa: E501

        :return: The product_quantity of this ChinaDomestic.  # noqa: E501
        :rtype: int
        """
        return self._product_quantity

    @product_quantity.setter
    def product_quantity(self, product_quantity):
        """Sets the product_quantity of this ChinaDomestic.

        The quantity.  # noqa: E501

        :param product_quantity: The product_quantity of this ChinaDomestic.  # noqa: E501
        :type: int
        """
        if product_quantity is None:
            raise ValueError("Invalid value for `product_quantity`, must not be `None`")  # noqa: E501
        if product_quantity is not None and product_quantity < 1:  # noqa: E501
            raise ValueError("Invalid value for `product_quantity`, must be a value greater than or equal to `1`")  # noqa: E501

        self._product_quantity = product_quantity

    @property
    def product_price(self):
        """Gets the product_price of this ChinaDomestic.  # noqa: E501

        Rate amount in 3 decimal 12 bytes total digit.  # noqa: E501

        :return: The product_price of this ChinaDomestic.  # noqa: E501
        :rtype: float
        """
        return self._product_price

    @product_price.setter
    def product_price(self, product_price):
        """Sets the product_price of this ChinaDomestic.

        Rate amount in 3 decimal 12 bytes total digit.  # noqa: E501

        :param product_price: The product_price of this ChinaDomestic.  # noqa: E501
        :type: float
        """
        if product_price is None:
            raise ValueError("Invalid value for `product_price`, must not be `None`")  # noqa: E501

        self._product_price = product_price

    @property
    def product_description(self):
        """Gets the product_description of this ChinaDomestic.  # noqa: E501

        The product description.  # noqa: E501

        :return: The product_description of this ChinaDomestic.  # noqa: E501
        :rtype: str
        """
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        """Sets the product_description of this ChinaDomestic.

        The product description.  # noqa: E501

        :param product_description: The product_description of this ChinaDomestic.  # noqa: E501
        :type: str
        """
        if product_description is None:
            raise ValueError("Invalid value for `product_description`, must not be `None`")  # noqa: E501
        if product_description is not None and len(product_description) > 100:
            raise ValueError("Invalid value for `product_description`, length must be less than or equal to `100`")  # noqa: E501
        if product_description is not None and not re.search(r'^(?!\s*$).+', product_description):  # noqa: E501
            raise ValueError(r"Invalid value for `product_description`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._product_description = product_description

    @property
    def redirect_url(self):
        """Gets the redirect_url of this ChinaDomestic.  # noqa: E501

        Use this to indicate the product code according to the product category list.  # noqa: E501

        :return: The redirect_url of this ChinaDomestic.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this ChinaDomestic.

        Use this to indicate the product code according to the product category list.  # noqa: E501

        :param redirect_url: The redirect_url of this ChinaDomestic.  # noqa: E501
        :type: str
        """
        if redirect_url is None:
            raise ValueError("Invalid value for `redirect_url`, must not be `None`")  # noqa: E501
        if redirect_url is not None and len(redirect_url) > 1024:
            raise ValueError("Invalid value for `redirect_url`, length must be less than or equal to `1024`")  # noqa: E501
        if redirect_url is not None and not re.search(r'^(?!\s*$).+', redirect_url):  # noqa: E501
            raise ValueError(r"Invalid value for `redirect_url`, must be a follow pattern or equal to `/^(?!\s*$).+/`")  # noqa: E501

        self._redirect_url = redirect_url

    @property
    def limit_card_function_to_debit(self):
        """Gets the limit_card_function_to_debit of this ChinaDomestic.  # noqa: E501

        Use this to limit card functions to debit cards.  # noqa: E501

        :return: The limit_card_function_to_debit of this ChinaDomestic.  # noqa: E501
        :rtype: bool
        """
        return self._limit_card_function_to_debit

    @limit_card_function_to_debit.setter
    def limit_card_function_to_debit(self, limit_card_function_to_debit):
        """Sets the limit_card_function_to_debit of this ChinaDomestic.

        Use this to limit card functions to debit cards.  # noqa: E501

        :param limit_card_function_to_debit: The limit_card_function_to_debit of this ChinaDomestic.  # noqa: E501
        :type: bool
        """

        self._limit_card_function_to_debit = limit_card_function_to_debit

    @property
    def customer_id(self):
        """Gets the customer_id of this ChinaDomestic.  # noqa: E501

        Use this to indicate the CUP customer ID if known.  # noqa: E501

        :return: The customer_id of this ChinaDomestic.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ChinaDomestic.

        Use this to indicate the CUP customer ID if known.  # noqa: E501

        :param customer_id: The customer_id of this ChinaDomestic.  # noqa: E501
        :type: str
        """
        if customer_id is not None and len(customer_id) > 32:
            raise ValueError("Invalid value for `customer_id`, length must be less than or equal to `32`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def bank_id(self):
        """Gets the bank_id of this ChinaDomestic.  # noqa: E501

        Use this to indicate the CUP bank ID if known.  # noqa: E501

        :return: The bank_id of this ChinaDomestic.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this ChinaDomestic.

        Use this to indicate the CUP bank ID if known.  # noqa: E501

        :param bank_id: The bank_id of this ChinaDomestic.  # noqa: E501
        :type: str
        """
        if bank_id is not None and len(bank_id) > 8:
            raise ValueError("Invalid value for `bank_id`, length must be less than or equal to `8`")  # noqa: E501

        self._bank_id = bank_id

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
        if not isinstance(other, ChinaDomestic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
