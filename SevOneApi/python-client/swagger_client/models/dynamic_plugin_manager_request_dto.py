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


class DynamicPluginManagerRequestDto(object):
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
        'plugin_manager_name': 'str',
        'plugin_manager_identifier': 'str'
    }

    attribute_map = {
        'plugin_manager_name': 'pluginManagerName',
        'plugin_manager_identifier': 'pluginManagerIdentifier'
    }

    def __init__(self, plugin_manager_name=None, plugin_manager_identifier=None):  # noqa: E501
        """DynamicPluginManagerRequestDto - a model defined in Swagger"""  # noqa: E501

        self._plugin_manager_name = None
        self._plugin_manager_identifier = None
        self.discriminator = None

        if plugin_manager_name is not None:
            self.plugin_manager_name = plugin_manager_name
        if plugin_manager_identifier is not None:
            self.plugin_manager_identifier = plugin_manager_identifier

    @property
    def plugin_manager_name(self):
        """Gets the plugin_manager_name of this DynamicPluginManagerRequestDto.  # noqa: E501


        :return: The plugin_manager_name of this DynamicPluginManagerRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._plugin_manager_name

    @plugin_manager_name.setter
    def plugin_manager_name(self, plugin_manager_name):
        """Sets the plugin_manager_name of this DynamicPluginManagerRequestDto.


        :param plugin_manager_name: The plugin_manager_name of this DynamicPluginManagerRequestDto.  # noqa: E501
        :type: str
        """

        self._plugin_manager_name = plugin_manager_name

    @property
    def plugin_manager_identifier(self):
        """Gets the plugin_manager_identifier of this DynamicPluginManagerRequestDto.  # noqa: E501


        :return: The plugin_manager_identifier of this DynamicPluginManagerRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._plugin_manager_identifier

    @plugin_manager_identifier.setter
    def plugin_manager_identifier(self, plugin_manager_identifier):
        """Sets the plugin_manager_identifier of this DynamicPluginManagerRequestDto.


        :param plugin_manager_identifier: The plugin_manager_identifier of this DynamicPluginManagerRequestDto.  # noqa: E501
        :type: str
        """

        self._plugin_manager_identifier = plugin_manager_identifier

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
        if issubclass(DynamicPluginManagerRequestDto, dict):
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
        if not isinstance(other, DynamicPluginManagerRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other