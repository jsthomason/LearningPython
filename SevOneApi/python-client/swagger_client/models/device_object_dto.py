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

from swagger_client.models.indicator_dto import IndicatorDto  # noqa: F401,E501


class DeviceObjectDto(object):
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
        'date_added': 'int',
        'description': 'str',
        'device_id': 'int',
        'enabled': 'str',
        'extended_info': 'dict(str, str)',
        'id': 'int',
        'indicators': 'list[IndicatorDto]',
        'is_deleted': 'bool',
        'is_enabled': 'bool',
        'is_visible': 'bool',
        'name': 'str',
        'plugin_id': 'int',
        'plugin_object_type_id': 'int',
        'subtype_id': 'int'
    }

    attribute_map = {
        'date_added': 'dateAdded',
        'description': 'description',
        'device_id': 'deviceId',
        'enabled': 'enabled',
        'extended_info': 'extendedInfo',
        'id': 'id',
        'indicators': 'indicators',
        'is_deleted': 'isDeleted',
        'is_enabled': 'isEnabled',
        'is_visible': 'isVisible',
        'name': 'name',
        'plugin_id': 'pluginId',
        'plugin_object_type_id': 'pluginObjectTypeId',
        'subtype_id': 'subtypeId'
    }

    def __init__(self, date_added=None, description=None, device_id=None, enabled=None, extended_info=None, id=None, indicators=None, is_deleted=None, is_enabled=None, is_visible=None, name=None, plugin_id=None, plugin_object_type_id=None, subtype_id=None):  # noqa: E501
        """DeviceObjectDto - a model defined in Swagger"""  # noqa: E501

        self._date_added = None
        self._description = None
        self._device_id = None
        self._enabled = None
        self._extended_info = None
        self._id = None
        self._indicators = None
        self._is_deleted = None
        self._is_enabled = None
        self._is_visible = None
        self._name = None
        self._plugin_id = None
        self._plugin_object_type_id = None
        self._subtype_id = None
        self.discriminator = None

        if date_added is not None:
            self.date_added = date_added
        if description is not None:
            self.description = description
        if device_id is not None:
            self.device_id = device_id
        if enabled is not None:
            self.enabled = enabled
        if extended_info is not None:
            self.extended_info = extended_info
        if id is not None:
            self.id = id
        if indicators is not None:
            self.indicators = indicators
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if is_visible is not None:
            self.is_visible = is_visible
        if name is not None:
            self.name = name
        if plugin_id is not None:
            self.plugin_id = plugin_id
        if plugin_object_type_id is not None:
            self.plugin_object_type_id = plugin_object_type_id
        if subtype_id is not None:
            self.subtype_id = subtype_id

    @property
    def date_added(self):
        """Gets the date_added of this DeviceObjectDto.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The date_added of this DeviceObjectDto.  # noqa: E501
        :rtype: int
        """
        return self._date_added

    @date_added.setter
    def date_added(self, date_added):
        """Sets the date_added of this DeviceObjectDto.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param date_added: The date_added of this DeviceObjectDto.  # noqa: E501
        :type: int
        """

        self._date_added = date_added

    @property
    def description(self):
        """Gets the description of this DeviceObjectDto.  # noqa: E501


        :return: The description of this DeviceObjectDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceObjectDto.


        :param description: The description of this DeviceObjectDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def device_id(self):
        """Gets the device_id of this DeviceObjectDto.  # noqa: E501


        :return: The device_id of this DeviceObjectDto.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DeviceObjectDto.


        :param device_id: The device_id of this DeviceObjectDto.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def enabled(self):
        """Gets the enabled of this DeviceObjectDto.  # noqa: E501


        :return: The enabled of this DeviceObjectDto.  # noqa: E501
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this DeviceObjectDto.


        :param enabled: The enabled of this DeviceObjectDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "AUTO"]  # noqa: E501
        if enabled not in allowed_values:
            raise ValueError(
                "Invalid value for `enabled` ({0}), must be one of {1}"  # noqa: E501
                .format(enabled, allowed_values)
            )

        self._enabled = enabled

    @property
    def extended_info(self):
        """Gets the extended_info of this DeviceObjectDto.  # noqa: E501


        :return: The extended_info of this DeviceObjectDto.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extended_info

    @extended_info.setter
    def extended_info(self, extended_info):
        """Sets the extended_info of this DeviceObjectDto.


        :param extended_info: The extended_info of this DeviceObjectDto.  # noqa: E501
        :type: dict(str, str)
        """

        self._extended_info = extended_info

    @property
    def id(self):
        """Gets the id of this DeviceObjectDto.  # noqa: E501


        :return: The id of this DeviceObjectDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceObjectDto.


        :param id: The id of this DeviceObjectDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def indicators(self):
        """Gets the indicators of this DeviceObjectDto.  # noqa: E501


        :return: The indicators of this DeviceObjectDto.  # noqa: E501
        :rtype: list[IndicatorDto]
        """
        return self._indicators

    @indicators.setter
    def indicators(self, indicators):
        """Sets the indicators of this DeviceObjectDto.


        :param indicators: The indicators of this DeviceObjectDto.  # noqa: E501
        :type: list[IndicatorDto]
        """

        self._indicators = indicators

    @property
    def is_deleted(self):
        """Gets the is_deleted of this DeviceObjectDto.  # noqa: E501


        :return: The is_deleted of this DeviceObjectDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this DeviceObjectDto.


        :param is_deleted: The is_deleted of this DeviceObjectDto.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def is_enabled(self):
        """Gets the is_enabled of this DeviceObjectDto.  # noqa: E501

        This field is deprecated and would be removed in a newer version of the API. Please use 'enabled' field instead.  # noqa: E501

        :return: The is_enabled of this DeviceObjectDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this DeviceObjectDto.

        This field is deprecated and would be removed in a newer version of the API. Please use 'enabled' field instead.  # noqa: E501

        :param is_enabled: The is_enabled of this DeviceObjectDto.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def is_visible(self):
        """Gets the is_visible of this DeviceObjectDto.  # noqa: E501


        :return: The is_visible of this DeviceObjectDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        """Sets the is_visible of this DeviceObjectDto.


        :param is_visible: The is_visible of this DeviceObjectDto.  # noqa: E501
        :type: bool
        """

        self._is_visible = is_visible

    @property
    def name(self):
        """Gets the name of this DeviceObjectDto.  # noqa: E501


        :return: The name of this DeviceObjectDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceObjectDto.


        :param name: The name of this DeviceObjectDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def plugin_id(self):
        """Gets the plugin_id of this DeviceObjectDto.  # noqa: E501


        :return: The plugin_id of this DeviceObjectDto.  # noqa: E501
        :rtype: int
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this DeviceObjectDto.


        :param plugin_id: The plugin_id of this DeviceObjectDto.  # noqa: E501
        :type: int
        """

        self._plugin_id = plugin_id

    @property
    def plugin_object_type_id(self):
        """Gets the plugin_object_type_id of this DeviceObjectDto.  # noqa: E501


        :return: The plugin_object_type_id of this DeviceObjectDto.  # noqa: E501
        :rtype: int
        """
        return self._plugin_object_type_id

    @plugin_object_type_id.setter
    def plugin_object_type_id(self, plugin_object_type_id):
        """Sets the plugin_object_type_id of this DeviceObjectDto.


        :param plugin_object_type_id: The plugin_object_type_id of this DeviceObjectDto.  # noqa: E501
        :type: int
        """

        self._plugin_object_type_id = plugin_object_type_id

    @property
    def subtype_id(self):
        """Gets the subtype_id of this DeviceObjectDto.  # noqa: E501


        :return: The subtype_id of this DeviceObjectDto.  # noqa: E501
        :rtype: int
        """
        return self._subtype_id

    @subtype_id.setter
    def subtype_id(self, subtype_id):
        """Sets the subtype_id of this DeviceObjectDto.


        :param subtype_id: The subtype_id of this DeviceObjectDto.  # noqa: E501
        :type: int
        """

        self._subtype_id = subtype_id

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
        if issubclass(DeviceObjectDto, dict):
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
        if not isinstance(other, DeviceObjectDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
