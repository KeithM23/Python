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


class PaymentTokenizationResponse(object):
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
        'request_status': 'str',
        'request_time': 'int',
        'brand': 'str',
        'country': 'str',
        'payment_token': 'PaymentTokenDetails',
        'payment_card': 'PaymentCard',
        'processor': 'ProcessorData',
        'order_id': 'str',
        'ipg_transaction_id': 'str',
        'merchant_transaction_id': 'str',
    }

    attribute_map = {
        'client_request_id': 'clientRequestId',  # noqa: E501
        'api_trace_id': 'apiTraceId',  # noqa: E501
        'response_type': 'responseType',  # noqa: E501
        'request_status': 'requestStatus',  # noqa: E501
        'request_time': 'requestTime',  # noqa: E501
        'brand': 'brand',  # noqa: E501
        'country': 'country',  # noqa: E501
        'payment_token': 'paymentToken',  # noqa: E501
        'payment_card': 'paymentCard',  # noqa: E501
        'processor': 'processor',  # noqa: E501
        'order_id': 'orderId',  # noqa: E501
        'ipg_transaction_id': 'ipgTransactionId',  # noqa: E501
        'merchant_transaction_id': 'merchantTransactionId',  # noqa: E501
    }

    def __init__(self, client_request_id=None, api_trace_id=None, response_type=None, request_status=None, request_time=None, brand=None, country=None, payment_token=None, payment_card=None, processor=None, order_id=None, ipg_transaction_id=None, merchant_transaction_id=None):  # noqa: E501
        """PaymentTokenizationResponse - a model defined in OpenAPI



        Keyword Args:
            client_request_id (str): Echoes back the value in the request header for tracking.. [optional]  # noqa: E501
            api_trace_id (str): Request identifier in API, can be used to request logs from the support team.. [optional]  # noqa: E501
            response_type (ResponseType): [optional]  # noqa: E501
            request_status (str): The status of the request.. [optional]  # noqa: E501
            request_time (int): Time of the request.. [optional]  # noqa: E501
            brand (str): Card brand.. [optional]  # noqa: E501
            country (str): Country of the card issued.. [optional]  # noqa: E501
            payment_token (PaymentTokenDetails): [optional]  # noqa: E501
            payment_card (PaymentCard): [optional]  # noqa: E501
            processor (ProcessorData): [optional]  # noqa: E501
            order_id (str): Client order ID if supplied by client, otherwise the order ID.. [optional]  # noqa: E501
            ipg_transaction_id (str): The response transaction ID.. [optional]  # noqa: E501
            merchant_transaction_id (str): The unique merchant transaction ID from the request header, if supplied.. [optional]  # noqa: E501
        """

        self._client_request_id = None
        self._api_trace_id = None
        self._response_type = None
        self._request_status = None
        self._request_time = None
        self._brand = None
        self._country = None
        self._payment_token = None
        self._payment_card = None
        self._processor = None
        self._order_id = None
        self._ipg_transaction_id = None
        self._merchant_transaction_id = None
        self.discriminator = None

        if client_request_id is not None:
            self.client_request_id = client_request_id  # noqa: E501
        if api_trace_id is not None:
            self.api_trace_id = api_trace_id  # noqa: E501
        if response_type is not None:
            self.response_type = response_type  # noqa: E501
        if request_status is not None:
            self.request_status = request_status  # noqa: E501
        if request_time is not None:
            self.request_time = request_time  # noqa: E501
        if brand is not None:
            self.brand = brand  # noqa: E501
        if country is not None:
            self.country = country  # noqa: E501
        if payment_token is not None:
            self.payment_token = payment_token  # noqa: E501
        if payment_card is not None:
            self.payment_card = payment_card  # noqa: E501
        if processor is not None:
            self.processor = processor  # noqa: E501
        if order_id is not None:
            self.order_id = order_id  # noqa: E501
        if ipg_transaction_id is not None:
            self.ipg_transaction_id = ipg_transaction_id  # noqa: E501
        if merchant_transaction_id is not None:
            self.merchant_transaction_id = merchant_transaction_id  # noqa: E501

    @property
    def client_request_id(self):
        """Gets the client_request_id of this PaymentTokenizationResponse.  # noqa: E501

        Echoes back the value in the request header for tracking.  # noqa: E501

        :return: The client_request_id of this PaymentTokenizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(
            self,
            client_request_id):
        """Sets the client_request_id of this PaymentTokenizationResponse.

        Echoes back the value in the request header for tracking.  # noqa: E501

        :param client_request_id: The client_request_id of this PaymentTokenizationResponse.  # noqa: E501
        :type: str
        """

        self._client_request_id = (
            client_request_id)

    @property
    def api_trace_id(self):
        """Gets the api_trace_id of this PaymentTokenizationResponse.  # noqa: E501

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :return: The api_trace_id of this PaymentTokenizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_trace_id

    @api_trace_id.setter
    def api_trace_id(
            self,
            api_trace_id):
        """Sets the api_trace_id of this PaymentTokenizationResponse.

        Request identifier in API, can be used to request logs from the support team.  # noqa: E501

        :param api_trace_id: The api_trace_id of this PaymentTokenizationResponse.  # noqa: E501
        :type: str
        """

        self._api_trace_id = (
            api_trace_id)

    @property
    def response_type(self):
        """Gets the response_type of this PaymentTokenizationResponse.  # noqa: E501


        :return: The response_type of this PaymentTokenizationResponse.  # noqa: E501
        :rtype: ResponseType
        """
        return self._response_type

    @response_type.setter
    def response_type(
            self,
            response_type):
        """Sets the response_type of this PaymentTokenizationResponse.


        :param response_type: The response_type of this PaymentTokenizationResponse.  # noqa: E501
        :type: ResponseType
        """

        self._response_type = (
            response_type)

    @property
    def request_status(self):
        """Gets the request_status of this PaymentTokenizationResponse.  # noqa: E501

        The status of the request.  # noqa: E501

        :return: The request_status of this PaymentTokenizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_status

    @request_status.setter
    def request_status(
            self,
            request_status):
        """Sets the request_status of this PaymentTokenizationResponse.

        The status of the request.  # noqa: E501

        :param request_status: The request_status of this PaymentTokenizationResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["DELETED", "FAILED", "SUCCESS", "APPROVED", "WAITING", "VALIDATION_FAILED", "DECLINED"]  # noqa: E501
        if request_status not in allowed_values:
            raise ValueError(
                "Invalid value for `request_status` ({0}), must be one of {1}"  # noqa: E501
                .format(request_status, allowed_values)
            )

        self._request_status = (
            request_status)

    @property
    def request_time(self):
        """Gets the request_time of this PaymentTokenizationResponse.  # noqa: E501

        Time of the request.  # noqa: E501

        :return: The request_time of this PaymentTokenizationResponse.  # noqa: E501
        :rtype: int
        """
        return self._request_time

    @request_time.setter
    def request_time(
            self,
            request_time):
        """Sets the request_time of this PaymentTokenizationResponse.

        Time of the request.  # noqa: E501

        :param request_time: The request_time of this PaymentTokenizationResponse.  # noqa: E501
        :type: int
        """

        self._request_time = (
            request_time)

    @property
    def brand(self):
        """Gets the brand of this PaymentTokenizationResponse.  # noqa: E501

        Card brand.  # noqa: E501

        :return: The brand of this PaymentTokenizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(
            self,
            brand):
        """Sets the brand of this PaymentTokenizationResponse.

        Card brand.  # noqa: E501

        :param brand: The brand of this PaymentTokenizationResponse.  # noqa: E501
        :type: str
        """

        self._brand = (
            brand)

    @property
    def country(self):
        """Gets the country of this PaymentTokenizationResponse.  # noqa: E501

        Country of the card issued.  # noqa: E501

        :return: The country of this PaymentTokenizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(
            self,
            country):
        """Sets the country of this PaymentTokenizationResponse.

        Country of the card issued.  # noqa: E501

        :param country: The country of this PaymentTokenizationResponse.  # noqa: E501
        :type: str
        """

        self._country = (
            country)

    @property
    def payment_token(self):
        """Gets the payment_token of this PaymentTokenizationResponse.  # noqa: E501


        :return: The payment_token of this PaymentTokenizationResponse.  # noqa: E501
        :rtype: PaymentTokenDetails
        """
        return self._payment_token

    @payment_token.setter
    def payment_token(
            self,
            payment_token):
        """Sets the payment_token of this PaymentTokenizationResponse.


        :param payment_token: The payment_token of this PaymentTokenizationResponse.  # noqa: E501
        :type: PaymentTokenDetails
        """

        self._payment_token = (
            payment_token)

    @property
    def payment_card(self):
        """Gets the payment_card of this PaymentTokenizationResponse.  # noqa: E501


        :return: The payment_card of this PaymentTokenizationResponse.  # noqa: E501
        :rtype: PaymentCard
        """
        return self._payment_card

    @payment_card.setter
    def payment_card(
            self,
            payment_card):
        """Sets the payment_card of this PaymentTokenizationResponse.


        :param payment_card: The payment_card of this PaymentTokenizationResponse.  # noqa: E501
        :type: PaymentCard
        """

        self._payment_card = (
            payment_card)

    @property
    def processor(self):
        """Gets the processor of this PaymentTokenizationResponse.  # noqa: E501


        :return: The processor of this PaymentTokenizationResponse.  # noqa: E501
        :rtype: ProcessorData
        """
        return self._processor

    @processor.setter
    def processor(
            self,
            processor):
        """Sets the processor of this PaymentTokenizationResponse.


        :param processor: The processor of this PaymentTokenizationResponse.  # noqa: E501
        :type: ProcessorData
        """

        self._processor = (
            processor)

    @property
    def order_id(self):
        """Gets the order_id of this PaymentTokenizationResponse.  # noqa: E501

        Client order ID if supplied by client, otherwise the order ID.  # noqa: E501

        :return: The order_id of this PaymentTokenizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(
            self,
            order_id):
        """Sets the order_id of this PaymentTokenizationResponse.

        Client order ID if supplied by client, otherwise the order ID.  # noqa: E501

        :param order_id: The order_id of this PaymentTokenizationResponse.  # noqa: E501
        :type: str
        """

        self._order_id = (
            order_id)

    @property
    def ipg_transaction_id(self):
        """Gets the ipg_transaction_id of this PaymentTokenizationResponse.  # noqa: E501

        The response transaction ID.  # noqa: E501

        :return: The ipg_transaction_id of this PaymentTokenizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._ipg_transaction_id

    @ipg_transaction_id.setter
    def ipg_transaction_id(
            self,
            ipg_transaction_id):
        """Sets the ipg_transaction_id of this PaymentTokenizationResponse.

        The response transaction ID.  # noqa: E501

        :param ipg_transaction_id: The ipg_transaction_id of this PaymentTokenizationResponse.  # noqa: E501
        :type: str
        """
        if ipg_transaction_id is not None and len(ipg_transaction_id) > 14:
            raise ValueError("Invalid value for `ipg_transaction_id`, length must be less than or equal to `14`")  # noqa: E501

        self._ipg_transaction_id = (
            ipg_transaction_id)

    @property
    def merchant_transaction_id(self):
        """Gets the merchant_transaction_id of this PaymentTokenizationResponse.  # noqa: E501

        The unique merchant transaction ID from the request header, if supplied.  # noqa: E501

        :return: The merchant_transaction_id of this PaymentTokenizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._merchant_transaction_id

    @merchant_transaction_id.setter
    def merchant_transaction_id(
            self,
            merchant_transaction_id):
        """Sets the merchant_transaction_id of this PaymentTokenizationResponse.

        The unique merchant transaction ID from the request header, if supplied.  # noqa: E501

        :param merchant_transaction_id: The merchant_transaction_id of this PaymentTokenizationResponse.  # noqa: E501
        :type: str
        """
        if merchant_transaction_id is not None and len(merchant_transaction_id) > 40:
            raise ValueError("Invalid value for `merchant_transaction_id`, length must be less than or equal to `40`")  # noqa: E501

        self._merchant_transaction_id = (
            merchant_transaction_id)

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
        if not isinstance(other, PaymentTokenizationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
