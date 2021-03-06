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


class DynamicPluginFieldDto(object):
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
        'default_entry': 'str',
        'description': 'str',
        'enum_list': 'str',
        'max_length': 'int',
        'name': 'str',
        'type': 'str',
        'value_range': 'str'
    }

    attribute_map = {
        'default_entry': 'defaultEntry',
        'description': 'description',
        'enum_list': 'enumList',
        'max_length': 'maxLength',
        'name': 'name',
        'type': 'type',
        'value_range': 'valueRange'
    }

    def __init__(self, default_entry=None, description=None, enum_list=None, max_length=None, name=None, type=None, value_range=None):  # noqa: E501
        """DynamicPluginFieldDto - a model defined in Swagger"""  # noqa: E501

        self._default_entry = None
        self._description = None
        self._enum_list = None
        self._max_length = None
        self._name = None
        self._type = None
        self._value_range = None
        self.discriminator = None

        if default_entry is not None:
            self.default_entry = default_entry
        if description is not None:
            self.description = description
        if enum_list is not None:
            self.enum_list = enum_list
        if max_length is not None:
            self.max_length = max_length
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if value_range is not None:
            self.value_range = value_range

    @property
    def default_entry(self):
        """Gets the default_entry of this DynamicPluginFieldDto.  # noqa: E501


        :return: The default_entry of this DynamicPluginFieldDto.  # noqa: E501
        :rtype: str
        """
        return self._default_entry

    @default_entry.setter
    def default_entry(self, default_entry):
        """Sets the default_entry of this DynamicPluginFieldDto.


        :param default_entry: The default_entry of this DynamicPluginFieldDto.  # noqa: E501
        :type: str
        """

        self._default_entry = default_entry

    @property
    def description(self):
        """Gets the description of this DynamicPluginFieldDto.  # noqa: E501


        :return: The description of this DynamicPluginFieldDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DynamicPluginFieldDto.


        :param description: The description of this DynamicPluginFieldDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enum_list(self):
        """Gets the enum_list of this DynamicPluginFieldDto.  # noqa: E501


        :return: The enum_list of this DynamicPluginFieldDto.  # noqa: E501
        :rtype: str
        """
        return self._enum_list

    @enum_list.setter
    def enum_list(self, enum_list):
        """Sets the enum_list of this DynamicPluginFieldDto.


        :param enum_list: The enum_list of this DynamicPluginFieldDto.  # noqa: E501
        :type: str
        """

        self._enum_list = enum_list

    @property
    def max_length(self):
        """Gets the max_length of this DynamicPluginFieldDto.  # noqa: E501


        :return: The max_length of this DynamicPluginFieldDto.  # noqa: E501
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this DynamicPluginFieldDto.


        :param max_length: The max_length of this DynamicPluginFieldDto.  # noqa: E501
        :type: int
        """

        self._max_length = max_length

    @property
    def name(self):
        """Gets the name of this DynamicPluginFieldDto.  # noqa: E501


        :return: The name of this DynamicPluginFieldDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DynamicPluginFieldDto.


        :param name: The name of this DynamicPluginFieldDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this DynamicPluginFieldDto.  # noqa: E501


        :return: The type of this DynamicPluginFieldDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DynamicPluginFieldDto.


        :param type: The type of this DynamicPluginFieldDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["BOOLEAN", "INTEGER", "FLOAT", "LIST", "TEXT", "SECRET"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def value_range(self):
        """Gets the value_range of this DynamicPluginFieldDto.  # noqa: E501


        :return: The value_range of this DynamicPluginFieldDto.  # noqa: E501
        :rtype: str
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        """Sets the value_range of this DynamicPluginFieldDto.


        :param value_range: The value_range of this DynamicPluginFieldDto.  # noqa: E501
        :type: str
        """

        self._value_range = value_range

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
        if issubclass(DynamicPluginFieldDto, dict):
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
        if not isinstance(other, DynamicPluginFieldDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
