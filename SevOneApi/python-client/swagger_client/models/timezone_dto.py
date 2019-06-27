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


class TimezoneDto(object):
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
        'country': 'str',
        'country_code': 'str',
        'display_name': 'str',
        'offset': 'int',
        'timezone': 'str'
    }

    attribute_map = {
        'country': 'country',
        'country_code': 'countryCode',
        'display_name': 'displayName',
        'offset': 'offset',
        'timezone': 'timezone'
    }

    def __init__(self, country=None, country_code=None, display_name=None, offset=None, timezone=None):  # noqa: E501
        """TimezoneDto - a model defined in Swagger"""  # noqa: E501

        self._country = None
        self._country_code = None
        self._display_name = None
        self._offset = None
        self._timezone = None
        self.discriminator = None

        if country is not None:
            self.country = country
        if country_code is not None:
            self.country_code = country_code
        if display_name is not None:
            self.display_name = display_name
        if offset is not None:
            self.offset = offset
        if timezone is not None:
            self.timezone = timezone

    @property
    def country(self):
        """Gets the country of this TimezoneDto.  # noqa: E501


        :return: The country of this TimezoneDto.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this TimezoneDto.


        :param country: The country of this TimezoneDto.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def country_code(self):
        """Gets the country_code of this TimezoneDto.  # noqa: E501


        :return: The country_code of this TimezoneDto.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this TimezoneDto.


        :param country_code: The country_code of this TimezoneDto.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def display_name(self):
        """Gets the display_name of this TimezoneDto.  # noqa: E501


        :return: The display_name of this TimezoneDto.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this TimezoneDto.


        :param display_name: The display_name of this TimezoneDto.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def offset(self):
        """Gets the offset of this TimezoneDto.  # noqa: E501

        UTC offset in milliseconds  # noqa: E501

        :return: The offset of this TimezoneDto.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TimezoneDto.

        UTC offset in milliseconds  # noqa: E501

        :param offset: The offset of this TimezoneDto.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def timezone(self):
        """Gets the timezone of this TimezoneDto.  # noqa: E501


        :return: The timezone of this TimezoneDto.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this TimezoneDto.


        :param timezone: The timezone of this TimezoneDto.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

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
        if issubclass(TimezoneDto, dict):
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
        if not isinstance(other, TimezoneDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other