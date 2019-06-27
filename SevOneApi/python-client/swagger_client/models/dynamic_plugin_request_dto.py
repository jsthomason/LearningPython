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

from swagger_client.models.dynamic_plugin_field_dto import DynamicPluginFieldDto  # noqa: F401,E501


class DynamicPluginRequestDto(object):
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
        'fields': 'list[DynamicPluginFieldDto]',
        'name': 'str',
        'technology': 'str'
    }

    attribute_map = {
        'fields': 'fields',
        'name': 'name',
        'technology': 'technology'
    }

    def __init__(self, fields=None, name=None, technology=None):  # noqa: E501
        """DynamicPluginRequestDto - a model defined in Swagger"""  # noqa: E501

        self._fields = None
        self._name = None
        self._technology = None
        self.discriminator = None

        if fields is not None:
            self.fields = fields
        if name is not None:
            self.name = name
        if technology is not None:
            self.technology = technology

    @property
    def fields(self):
        """Gets the fields of this DynamicPluginRequestDto.  # noqa: E501


        :return: The fields of this DynamicPluginRequestDto.  # noqa: E501
        :rtype: list[DynamicPluginFieldDto]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this DynamicPluginRequestDto.


        :param fields: The fields of this DynamicPluginRequestDto.  # noqa: E501
        :type: list[DynamicPluginFieldDto]
        """

        self._fields = fields

    @property
    def name(self):
        """Gets the name of this DynamicPluginRequestDto.  # noqa: E501


        :return: The name of this DynamicPluginRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DynamicPluginRequestDto.


        :param name: The name of this DynamicPluginRequestDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def technology(self):
        """Gets the technology of this DynamicPluginRequestDto.  # noqa: E501


        :return: The technology of this DynamicPluginRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._technology

    @technology.setter
    def technology(self, technology):
        """Sets the technology of this DynamicPluginRequestDto.


        :param technology: The technology of this DynamicPluginRequestDto.  # noqa: E501
        :type: str
        """

        self._technology = technology

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
        if issubclass(DynamicPluginRequestDto, dict):
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
        if not isinstance(other, DynamicPluginRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
