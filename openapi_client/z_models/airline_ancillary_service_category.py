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


class AirlineAncillaryServiceCategory(object):
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
        'service_category': 'str',
    }

    attribute_map = {
        'service_category': 'serviceCategory',  # noqa: E501
    }

    def __init__(self, service_category):  # noqa: E501
        """AirlineAncillaryServiceCategory - a model defined in OpenAPI

        Args:
            service_category (str): Identifies the service purchased in the transaction if not a base ticket

        Keyword Args:  # noqa: E501
        """

        self._service_category = None
        self.discriminator = None

        self.service_category = service_category

    @property
    def service_category(self):
        """Gets the service_category of this AirlineAncillaryServiceCategory.  # noqa: E501

        Identifies the service purchased in the transaction if not a base ticket  # noqa: E501

        :return: The service_category of this AirlineAncillaryServiceCategory.  # noqa: E501
        :rtype: str
        """
        return self._service_category

    @service_category.setter
    def service_category(
            self,
            service_category):
        """Sets the service_category of this AirlineAncillaryServiceCategory.

        Identifies the service purchased in the transaction if not a base ticket  # noqa: E501

        :param service_category: The service_category of this AirlineAncillaryServiceCategory.  # noqa: E501
        :type: str
        """
        if service_category is None:
            raise ValueError("Invalid value for `service_category`, must not be `None`")  # noqa: E501
        allowed_values = ["BUNDLED_SERVICE", "BAGGAGE_FEE", "CHANGE_FEE", "CARGO", "CARBON_OFFSET", "FREQUENT_FLYER", "GIFT_CARD", "GROUND_TRANSPORT", "IN_FLIGHT_ENTERTAINMENT", "LOUNGE", "MEDICAL", "MEAL_BEVERAGE", "OTHER", "PASSENGER_ASSIST_FEE", "PETS", "SEAT_FEES", "STANDBY", "SERVICE_FEE", "STORE", "TRAVEL_SERVICE", "UNACCOMPANIED_TRAVEL", "UPGRADES", "WI_FI"]  # noqa: E501
        if service_category not in allowed_values:
            raise ValueError(
                "Invalid value for `service_category` ({0}), must be one of {1}"  # noqa: E501
                .format(service_category, allowed_values)
            )

        self._service_category = (
            service_category)

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
        if not isinstance(other, AirlineAncillaryServiceCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
