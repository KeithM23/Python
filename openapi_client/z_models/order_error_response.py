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


class OrderErrorResponse(object):
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
        'order_id': 'str',
        'billing': 'Billing',
        'shipping': 'Shipping',
        'transactions': 'list[TransactionResponse]',
        'additional_details': 'AdditionalDetails',
        'error': 'Error',
    }

    attribute_map = {
        'client_request_id': 'clientRequestId',  # noqa: E501
        'api_trace_id': 'apiTraceId',  # noqa: E501
        'response_type': 'responseType',  # noqa: E501
        'order_id': 'orderId',  # noqa: E501
        'billing': 'billing',  # noqa: E501
        'shipping': 'shipping',  # noqa: E501
        'transactions': 'transactions',  # noqa: E501
        'additional_details': 'additionalDetails',  # noqa: E501
        'error': 'error',  # noqa: E501
    }

    def __init__(self, client_request_id=None, api_trace_id=None, response_type=None, order_id=None, billing=None, shipping=None, transactions=None, additional_details=None, error=None):  # noqa: E501
        """OrderErrorResponse - a model defined in OpenAPI



        Keyword Args:
            client_request_id (str): Echoes back the value in the request header for tracking.. [optional]  # noqa: E501
            api_trace_id (str): Request identifier in API, can be used to request logs from the support team.. [optional]  # noqa: E501
            response_type (ResponseType): [optional]  # noqa: E501
            order_id (str): Client order ID if supplied by client, otherwise the order ID.. [optional]  # noqa: E501
            billing (Billing): [optional]  # noqa: E501
            shipping (Shipping): [optional]  # noqa: E501
            transactions (list[TransactionResponse]): Required for some payment methods (for example, Klarna).. [optional]  # noqa: E501
            additional_details (AdditionalDetails): [optional]  # noqa: E501
            error (Error): [optional]  # noqa: E501
        """

        self._client_request_id = None
        self._api_trace_id = None
        self._response_type = None
        self._order_id = None
        self._billing = None
        self._shipping = None
        self._transactions = None
        self._additional_details = None
        self._error = None
        self.discriminator = None

        if client_request_id is not None:
            self.client_request_id = client_request_id  # noqa: E501
        if api_trace_id is not None:
            self.api_trace_id = api_trace_id  # noqa: E501
        if response_type is not None:
            self.response_type = response_type  # noqa: E501
        if order_id is not None:
            self.order_id = order_id  # noqa: E501
        if billing is not None:
            self.billing = billing  # noqa: E501
        if shipping is not None:
            self.shipping = shipping  # noqa: E501
        if transactions is not None:
            self.transactions = transactions  # noqa: E501
        if additional_details is not None:
            self.additional_details = additional_details  # noqa: E501
        if error is not None:
            self.error = error  # noqa: E501

    @property
    def client_request_id(self):
        """Gets the client_request_id of this OrderErrorResponse.  # noqa: E501

        Echoes back the value in the request header for tracking.  # noqa: E501

        :return: The client_request_id of this OrderErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(
            self,
            client_request_id):
        """Sets the client_request_id of this OrderErrorResponse.

        Echoes back the value in the request header for tracking.  # noqa: E501

        :param client_request_id: The client_request_id of this OrderErrorResponse.  # noqa: E501
        :type: str
        """

        self._client_request_id = (
            client_request_id)

    @property
    def api_trace_id(self):
        """Gets the api_trace_id of this OrderErrorResponse.  # noqa: E501

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :return: The api_trace_id of this OrderErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_trace_id

    @api_trace_id.setter
    def api_trace_id(
            self,
            api_trace_id):
        """Sets the api_trace_id of this OrderErrorResponse.

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :param api_trace_id: The api_trace_id of this OrderErrorResponse.  # noqa: E501
        :type: str
        """

        self._api_trace_id = (
            api_trace_id)

    @property
    def response_type(self):
        """Gets the response_type of this OrderErrorResponse.  # noqa: E501


        :return: The response_type of this OrderErrorResponse.  # noqa: E501
        :rtype: ResponseType
        """
        return self._response_type

    @response_type.setter
    def response_type(
            self,
            response_type):
        """Sets the response_type of this OrderErrorResponse.


        :param response_type: The response_type of this OrderErrorResponse.  # noqa: E501
        :type: ResponseType
        """

        self._response_type = (
            response_type)

    @property
    def order_id(self):
        """Gets the order_id of this OrderErrorResponse.  # noqa: E501

        Client order ID if supplied by client, otherwise the order ID.  # noqa: E501

        :return: The order_id of this OrderErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(
            self,
            order_id):
        """Sets the order_id of this OrderErrorResponse.

        Client order ID if supplied by client, otherwise the order ID.  # noqa: E501

        :param order_id: The order_id of this OrderErrorResponse.  # noqa: E501
        :type: str
        """

        self._order_id = (
            order_id)

    @property
    def billing(self):
        """Gets the billing of this OrderErrorResponse.  # noqa: E501


        :return: The billing of this OrderErrorResponse.  # noqa: E501
        :rtype: Billing
        """
        return self._billing

    @billing.setter
    def billing(
            self,
            billing):
        """Sets the billing of this OrderErrorResponse.


        :param billing: The billing of this OrderErrorResponse.  # noqa: E501
        :type: Billing
        """

        self._billing = (
            billing)

    @property
    def shipping(self):
        """Gets the shipping of this OrderErrorResponse.  # noqa: E501


        :return: The shipping of this OrderErrorResponse.  # noqa: E501
        :rtype: Shipping
        """
        return self._shipping

    @shipping.setter
    def shipping(
            self,
            shipping):
        """Sets the shipping of this OrderErrorResponse.


        :param shipping: The shipping of this OrderErrorResponse.  # noqa: E501
        :type: Shipping
        """

        self._shipping = (
            shipping)

    @property
    def transactions(self):
        """Gets the transactions of this OrderErrorResponse.  # noqa: E501

        Required for some payment methods (for example, Klarna).  # noqa: E501

        :return: The transactions of this OrderErrorResponse.  # noqa: E501
        :rtype: list[TransactionResponse]
        """
        return self._transactions

    @transactions.setter
    def transactions(
            self,
            transactions):
        """Sets the transactions of this OrderErrorResponse.

        Required for some payment methods (for example, Klarna).  # noqa: E501

        :param transactions: The transactions of this OrderErrorResponse.  # noqa: E501
        :type: list[TransactionResponse]
        """

        self._transactions = (
            transactions)

    @property
    def additional_details(self):
        """Gets the additional_details of this OrderErrorResponse.  # noqa: E501


        :return: The additional_details of this OrderErrorResponse.  # noqa: E501
        :rtype: AdditionalDetails
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(
            self,
            additional_details):
        """Sets the additional_details of this OrderErrorResponse.


        :param additional_details: The additional_details of this OrderErrorResponse.  # noqa: E501
        :type: AdditionalDetails
        """

        self._additional_details = (
            additional_details)

    @property
    def error(self):
        """Gets the error of this OrderErrorResponse.  # noqa: E501


        :return: The error of this OrderErrorResponse.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(
            self,
            error):
        """Sets the error of this OrderErrorResponse.


        :param error: The error of this OrderErrorResponse.  # noqa: E501
        :type: Error
        """

        self._error = (
            error)

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
        if not isinstance(other, OrderErrorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
