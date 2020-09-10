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


class BrandingStyleConfigurationResponse(object):
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
        'client_request_id': 'str',
        'api_trace_id': 'str',
        'response_type': 'ResponseType',
        'stores': 'list[BrandingStyleConfigurationResult]',
    }

    attribute_map = {
        'client_request_id': 'clientRequestId',  # noqa: E501
        'api_trace_id': 'apiTraceId',  # noqa: E501
        'response_type': 'responseType',  # noqa: E501
        'stores': 'stores',  # noqa: E501
    }

    def __init__(self, client_request_id=None, api_trace_id=None, response_type=None, stores=None):  # noqa: E501
        """BrandingStyleConfigurationResponse - a model defined in OpenAPI



        Keyword Args:
            client_request_id (str): Echoes back the value in the request header for tracking.. [optional]  # noqa: E501
            api_trace_id (str): Request identifier in API, can be used to request logs from the support team.. [optional]  # noqa: E501
            response_type (ResponseType): [optional]  # noqa: E501
            stores (list[BrandingStyleConfigurationResult]): [optional]  # noqa: E501
        """

        self._client_request_id = None
        self._api_trace_id = None
        self._response_type = None
        self._stores = None
        self.discriminator = None

        if client_request_id is not None:
            self.client_request_id = client_request_id  # noqa: E501
        if api_trace_id is not None:
            self.api_trace_id = api_trace_id  # noqa: E501
        if response_type is not None:
            self.response_type = response_type  # noqa: E501
        if stores is not None:
            self.stores = stores  # noqa: E501

    @property
    def client_request_id(self):
        """Gets the client_request_id of this BrandingStyleConfigurationResponse.  # noqa: E501

        Echoes back the value in the request header for tracking.  # noqa: E501

        :return: The client_request_id of this BrandingStyleConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(
            self,
            client_request_id):
        """Sets the client_request_id of this BrandingStyleConfigurationResponse.

        Echoes back the value in the request header for tracking.  # noqa: E501

        :param client_request_id: The client_request_id of this BrandingStyleConfigurationResponse.  # noqa: E501
        :type: str
        """

        self._client_request_id = (
            client_request_id)

    @property
    def api_trace_id(self):
        """Gets the api_trace_id of this BrandingStyleConfigurationResponse.  # noqa: E501

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :return: The api_trace_id of this BrandingStyleConfigurationResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_trace_id

    @api_trace_id.setter
    def api_trace_id(
            self,
            api_trace_id):
        """Sets the api_trace_id of this BrandingStyleConfigurationResponse.

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :param api_trace_id: The api_trace_id of this BrandingStyleConfigurationResponse.  # noqa: E501
        :type: str
        """

        self._api_trace_id = (
            api_trace_id)

    @property
    def response_type(self):
        """Gets the response_type of this BrandingStyleConfigurationResponse.  # noqa: E501


        :return: The response_type of this BrandingStyleConfigurationResponse.  # noqa: E501
        :rtype: ResponseType
        """
        return self._response_type

    @response_type.setter
    def response_type(
            self,
            response_type):
        """Sets the response_type of this BrandingStyleConfigurationResponse.


        :param response_type: The response_type of this BrandingStyleConfigurationResponse.  # noqa: E501
        :type: ResponseType
        """

        self._response_type = (
            response_type)

    @property
    def stores(self):
        """Gets the stores of this BrandingStyleConfigurationResponse.  # noqa: E501


        :return: The stores of this BrandingStyleConfigurationResponse.  # noqa: E501
        :rtype: list[BrandingStyleConfigurationResult]
        """
        return self._stores

    @stores.setter
    def stores(
            self,
            stores):
        """Sets the stores of this BrandingStyleConfigurationResponse.


        :param stores: The stores of this BrandingStyleConfigurationResponse.  # noqa: E501
        :type: list[BrandingStyleConfigurationResult]
        """

        self._stores = (
            stores)

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
        if not isinstance(other, BrandingStyleConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
