# coding: utf-8

"""
    SevOne API Documentation

    Supported endpoints by the new RESTful API  # noqa: E501

    OpenAPI spec version: 2.1.18, Hash: db562e6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ApiKeyDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'api_key': 'str',
        'application_name': 'str',
        'creation_date': 'int',
        'expiration_date': 'int',
        'user': 'str'
    }

    attribute_map = {
        'api_key': 'apiKey',
        'application_name': 'applicationName',
        'creation_date': 'creationDate',
        'expiration_date': 'expirationDate',
        'user': 'user'
    }

    def __init__(self, api_key=None, application_name=None, creation_date=None, expiration_date=None, user=None):  # noqa: E501
        """ApiKeyDto - a model defined in Swagger"""  # noqa: E501

        self._api_key = None
        self._application_name = None
        self._creation_date = None
        self._expiration_date = None
        self._user = None
        self.discriminator = None

        if api_key is not None:
            self.api_key = api_key
        if application_name is not None:
            self.application_name = application_name
        if creation_date is not None:
            self.creation_date = creation_date
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if user is not None:
            self.user = user

    @property
    def api_key(self):
        """Gets the api_key of this ApiKeyDto.  # noqa: E501


        :return: The api_key of this ApiKeyDto.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this ApiKeyDto.


        :param api_key: The api_key of this ApiKeyDto.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def application_name(self):
        """Gets the application_name of this ApiKeyDto.  # noqa: E501


        :return: The application_name of this ApiKeyDto.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this ApiKeyDto.


        :param application_name: The application_name of this ApiKeyDto.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def creation_date(self):
        """Gets the creation_date of this ApiKeyDto.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The creation_date of this ApiKeyDto.  # noqa: E501
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ApiKeyDto.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param creation_date: The creation_date of this ApiKeyDto.  # noqa: E501
        :type: int
        """

        self._creation_date = creation_date

    @property
    def expiration_date(self):
        """Gets the expiration_date of this ApiKeyDto.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The expiration_date of this ApiKeyDto.  # noqa: E501
        :rtype: int
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this ApiKeyDto.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param expiration_date: The expiration_date of this ApiKeyDto.  # noqa: E501
        :type: int
        """

        self._expiration_date = expiration_date

    @property
    def user(self):
        """Gets the user of this ApiKeyDto.  # noqa: E501


        :return: The user of this ApiKeyDto.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ApiKeyDto.


        :param user: The user of this ApiKeyDto.  # noqa: E501
        :type: str
        """

        self._user = user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ApiKeyDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiKeyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other