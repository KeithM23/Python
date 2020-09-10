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


class AccessTokenResponse(object):
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
        'token_id': 'str',
        'status': 'str',
        'issued_on': 'str',
        'expires_in_seconds': 'str',
        'public_key_base64': 'str',
        'algorithm': 'str',
        'client_request_id': 'str'
    }

    attribute_map = {
        'token_id': 'tokenId',
        'status': 'status',
        'issued_on': 'issuedOn',
        'expires_in_seconds': 'expiresInSeconds',
        'public_key_base64': 'publicKeyBase64',
        'algorithm': 'algorithm',
        'client_request_id': 'clientRequestId'
    }

    def __init__(self, token_id=None, status=None, issued_on=None, expires_in_seconds=None, public_key_base64=None, algorithm=None, client_request_id=None):  # noqa: E501
        """AccessTokenResponse - a model defined in OpenAPI"""  # noqa: E501

        self._token_id = None
        self._status = None
        self._issued_on = None
        self._expires_in_seconds = None
        self._public_key_base64 = None
        self._algorithm = None
        self._client_request_id = None
        self.discriminator = None

        if token_id is not None:
            self.token_id = token_id
        if status is not None:
            self.status = status
        if issued_on is not None:
            self.issued_on = issued_on
        if expires_in_seconds is not None:
            self.expires_in_seconds = expires_in_seconds
        if public_key_base64 is not None:
            self.public_key_base64 = public_key_base64
        if algorithm is not None:
            self.algorithm = algorithm
        if client_request_id is not None:
            self.client_request_id = client_request_id

    @property
    def token_id(self):
        """Gets the token_id of this AccessTokenResponse.  # noqa: E501

        Access token for authentication.  # noqa: E501

        :return: The token_id of this AccessTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this AccessTokenResponse.

        Access token for authentication.  # noqa: E501

        :param token_id: The token_id of this AccessTokenResponse.  # noqa: E501
        :type: str
        """

        self._token_id = token_id

    @property
    def status(self):
        """Gets the status of this AccessTokenResponse.  # noqa: E501

        The token status.  # noqa: E501

        :return: The status of this AccessTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccessTokenResponse.

        The token status.  # noqa: E501

        :param status: The status of this AccessTokenResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def issued_on(self):
        """Gets the issued_on of this AccessTokenResponse.  # noqa: E501

        Access token issued time in milliseconds.  # noqa: E501

        :return: The issued_on of this AccessTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._issued_on

    @issued_on.setter
    def issued_on(self, issued_on):
        """Sets the issued_on of this AccessTokenResponse.

        Access token issued time in milliseconds.  # noqa: E501

        :param issued_on: The issued_on of this AccessTokenResponse.  # noqa: E501
        :type: str
        """

        self._issued_on = issued_on

    @property
    def expires_in_seconds(self):
        """Gets the expires_in_seconds of this AccessTokenResponse.  # noqa: E501

        Access token expiration time.  # noqa: E501

        :return: The expires_in_seconds of this AccessTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._expires_in_seconds

    @expires_in_seconds.setter
    def expires_in_seconds(self, expires_in_seconds):
        """Sets the expires_in_seconds of this AccessTokenResponse.

        Access token expiration time.  # noqa: E501

        :param expires_in_seconds: The expires_in_seconds of this AccessTokenResponse.  # noqa: E501
        :type: str
        """

        self._expires_in_seconds = expires_in_seconds

    @property
    def public_key_base64(self):
        """Gets the public_key_base64 of this AccessTokenResponse.  # noqa: E501

        Public key to encrypt data.  # noqa: E501

        :return: The public_key_base64 of this AccessTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._public_key_base64

    @public_key_base64.setter
    def public_key_base64(self, public_key_base64):
        """Sets the public_key_base64 of this AccessTokenResponse.

        Public key to encrypt data.  # noqa: E501

        :param public_key_base64: The public_key_base64 of this AccessTokenResponse.  # noqa: E501
        :type: str
        """

        self._public_key_base64 = public_key_base64

    @property
    def algorithm(self):
        """Gets the algorithm of this AccessTokenResponse.  # noqa: E501

        Encyption algorithym. One way ECDH 256 bit key.  # noqa: E501

        :return: The algorithm of this AccessTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this AccessTokenResponse.

        Encyption algorithym. One way ECDH 256 bit key.  # noqa: E501

        :param algorithm: The algorithm of this AccessTokenResponse.  # noqa: E501
        :type: str
        """

        self._algorithm = algorithm

    @property
    def client_request_id(self):
        """Gets the client_request_id of this AccessTokenResponse.  # noqa: E501

        Echoes back the value from the request header for tracking.  # noqa: E501

        :return: The client_request_id of this AccessTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        """Sets the client_request_id of this AccessTokenResponse.

        Echoes back the value from the request header for tracking.  # noqa: E501

        :param client_request_id: The client_request_id of this AccessTokenResponse.  # noqa: E501
        :type: str
        """

        self._client_request_id = client_request_id

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
        if not isinstance(other, AccessTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
