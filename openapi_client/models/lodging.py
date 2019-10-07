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


class Lodging(object):
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
        'arrival_date': 'date',
        'departure_date': 'date',
        'folio_number': 'str',
        'extra_charges': 'list[LodgingExtraCharges]',
        'no_show_indicator': 'bool'
    }

    attribute_map = {
        'arrival_date': 'arrivalDate',
        'departure_date': 'departureDate',
        'folio_number': 'folioNumber',
        'extra_charges': 'extraCharges',
        'no_show_indicator': 'noShowIndicator'
    }

    def __init__(self, arrival_date=None, departure_date=None, folio_number=None, extra_charges=None, no_show_indicator=None):  # noqa: E501
        """Lodging - a model defined in OpenAPI"""  # noqa: E501

        self._arrival_date = None
        self._departure_date = None
        self._folio_number = None
        self._extra_charges = None
        self._no_show_indicator = None
        self.discriminator = None

        if arrival_date is not None:
            self.arrival_date = arrival_date
        if departure_date is not None:
            self.departure_date = departure_date
        if folio_number is not None:
            self.folio_number = folio_number
        if extra_charges is not None:
            self.extra_charges = extra_charges
        if no_show_indicator is not None:
            self.no_show_indicator = no_show_indicator

    @property
    def arrival_date(self):
        """Gets the arrival_date of this Lodging.  # noqa: E501

        Date of arrival.  # noqa: E501

        :return: The arrival_date of this Lodging.  # noqa: E501
        :rtype: date
        """
        return self._arrival_date

    @arrival_date.setter
    def arrival_date(self, arrival_date):
        """Sets the arrival_date of this Lodging.

        Date of arrival.  # noqa: E501

        :param arrival_date: The arrival_date of this Lodging.  # noqa: E501
        :type: date
        """

        self._arrival_date = arrival_date

    @property
    def departure_date(self):
        """Gets the departure_date of this Lodging.  # noqa: E501

        Date of departure.  # noqa: E501

        :return: The departure_date of this Lodging.  # noqa: E501
        :rtype: date
        """
        return self._departure_date

    @departure_date.setter
    def departure_date(self, departure_date):
        """Sets the departure_date of this Lodging.

        Date of departure.  # noqa: E501

        :param departure_date: The departure_date of this Lodging.  # noqa: E501
        :type: date
        """

        self._departure_date = departure_date

    @property
    def folio_number(self):
        """Gets the folio_number of this Lodging.  # noqa: E501

        Portfolio number.  # noqa: E501

        :return: The folio_number of this Lodging.  # noqa: E501
        :rtype: str
        """
        return self._folio_number

    @folio_number.setter
    def folio_number(self, folio_number):
        """Sets the folio_number of this Lodging.

        Portfolio number.  # noqa: E501

        :param folio_number: The folio_number of this Lodging.  # noqa: E501
        :type: str
        """
        if folio_number is not None and len(folio_number) > 20:
            raise ValueError("Invalid value for `folio_number`, length must be less than or equal to `20`")  # noqa: E501

        self._folio_number = folio_number

    @property
    def extra_charges(self):
        """Gets the extra_charges of this Lodging.  # noqa: E501

        Information about charges other than base lodging.  # noqa: E501

        :return: The extra_charges of this Lodging.  # noqa: E501
        :rtype: list[LodgingExtraCharges]
        """
        return self._extra_charges

    @extra_charges.setter
    def extra_charges(self, extra_charges):
        """Sets the extra_charges of this Lodging.

        Information about charges other than base lodging.  # noqa: E501

        :param extra_charges: The extra_charges of this Lodging.  # noqa: E501
        :type: list[LodgingExtraCharges]
        """

        self._extra_charges = extra_charges

    @property
    def no_show_indicator(self):
        """Gets the no_show_indicator of this Lodging.  # noqa: E501

        Indicates if the transaction is associated with a delayed or no-show penalty.  # noqa: E501

        :return: The no_show_indicator of this Lodging.  # noqa: E501
        :rtype: bool
        """
        return self._no_show_indicator

    @no_show_indicator.setter
    def no_show_indicator(self, no_show_indicator):
        """Sets the no_show_indicator of this Lodging.

        Indicates if the transaction is associated with a delayed or no-show penalty.  # noqa: E501

        :param no_show_indicator: The no_show_indicator of this Lodging.  # noqa: E501
        :type: bool
        """

        self._no_show_indicator = no_show_indicator

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
        if not isinstance(other, Lodging):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
