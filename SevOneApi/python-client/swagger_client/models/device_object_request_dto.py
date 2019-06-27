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

from swagger_client.models.indicator_request_dto import IndicatorRequestDto  # noqa: F401,E501


class DeviceObjectRequestDto(object):
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
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'plugin_id': 'int',
        'plugin_object_type_id': 'int',
        'poll_frequency': 'int',
        'subtype_id': 'int',
        'extended_info': 'dict(str, str)',
        'enabled': 'str',
        'is_deleted': 'bool',
        'is_enabled': 'bool',
        'is_visible': 'bool',
        'indicators': 'list[IndicatorRequestDto]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'plugin_id': 'pluginId',
        'plugin_object_type_id': 'pluginObjectTypeId',
        'poll_frequency': 'pollFrequency',
        'subtype_id': 'subtypeId',
        'extended_info': 'extendedInfo',
        'enabled': 'enabled',
        'is_deleted': 'isDeleted',
        'is_enabled': 'isEnabled',
        'is_visible': 'isVisible',
        'indicators': 'indicators'
    }

    def __init__(self, id=None, name=None, description=None, plugin_id=None, plugin_object_type_id=None, poll_frequency=None, subtype_id=None, extended_info=None, enabled=None, is_deleted=None, is_enabled=None, is_visible=None, indicators=None):  # noqa: E501
        """DeviceObjectRequestDto - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._plugin_id = None
        self._plugin_object_type_id = None
        self._poll_frequency = None
        self._subtype_id = None
        self._extended_info = None
        self._enabled = None
        self._is_deleted = None
        self._is_enabled = None
        self._is_visible = None
        self._indicators = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.description = description
        self.plugin_id = plugin_id
        self.plugin_object_type_id = plugin_object_type_id
        self.poll_frequency = poll_frequency
        if subtype_id is not None:
            self.subtype_id = subtype_id
        if extended_info is not None:
            self.extended_info = extended_info
        if enabled is not None:
            self.enabled = enabled
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if is_visible is not None:
            self.is_visible = is_visible
        if indicators is not None:
            self.indicators = indicators

    @property
    def id(self):
        """Gets the id of this DeviceObjectRequestDto.  # noqa: E501


        :return: The id of this DeviceObjectRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceObjectRequestDto.


        :param id: The id of this DeviceObjectRequestDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DeviceObjectRequestDto.  # noqa: E501


        :return: The name of this DeviceObjectRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceObjectRequestDto.


        :param name: The name of this DeviceObjectRequestDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this DeviceObjectRequestDto.  # noqa: E501


        :return: The description of this DeviceObjectRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceObjectRequestDto.


        :param description: The description of this DeviceObjectRequestDto.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def plugin_id(self):
        """Gets the plugin_id of this DeviceObjectRequestDto.  # noqa: E501


        :return: The plugin_id of this DeviceObjectRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this DeviceObjectRequestDto.


        :param plugin_id: The plugin_id of this DeviceObjectRequestDto.  # noqa: E501
        :type: int
        """
        if plugin_id is None:
            raise ValueError("Invalid value for `plugin_id`, must not be `None`")  # noqa: E501

        self._plugin_id = plugin_id

    @property
    def plugin_object_type_id(self):
        """Gets the plugin_object_type_id of this DeviceObjectRequestDto.  # noqa: E501


        :return: The plugin_object_type_id of this DeviceObjectRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._plugin_object_type_id

    @plugin_object_type_id.setter
    def plugin_object_type_id(self, plugin_object_type_id):
        """Sets the plugin_object_type_id of this DeviceObjectRequestDto.


        :param plugin_object_type_id: The plugin_object_type_id of this DeviceObjectRequestDto.  # noqa: E501
        :type: int
        """
        if plugin_object_type_id is None:
            raise ValueError("Invalid value for `plugin_object_type_id`, must not be `None`")  # noqa: E501

        self._plugin_object_type_id = plugin_object_type_id

    @property
    def poll_frequency(self):
        """Gets the poll_frequency of this DeviceObjectRequestDto.  # noqa: E501


        :return: The poll_frequency of this DeviceObjectRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._poll_frequency

    @poll_frequency.setter
    def poll_frequency(self, poll_frequency):
        """Sets the poll_frequency of this DeviceObjectRequestDto.


        :param poll_frequency: The poll_frequency of this DeviceObjectRequestDto.  # noqa: E501
        :type: int
        """
        if poll_frequency is None:
            raise ValueError("Invalid value for `poll_frequency`, must not be `None`")  # noqa: E501

        self._poll_frequency = poll_frequency

    @property
    def subtype_id(self):
        """Gets the subtype_id of this DeviceObjectRequestDto.  # noqa: E501


        :return: The subtype_id of this DeviceObjectRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._subtype_id

    @subtype_id.setter
    def subtype_id(self, subtype_id):
        """Sets the subtype_id of this DeviceObjectRequestDto.


        :param subtype_id: The subtype_id of this DeviceObjectRequestDto.  # noqa: E501
        :type: int
        """

        self._subtype_id = subtype_id

    @property
    def extended_info(self):
        """Gets the extended_info of this DeviceObjectRequestDto.  # noqa: E501


        :return: The extended_info of this DeviceObjectRequestDto.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extended_info

    @extended_info.setter
    def extended_info(self, extended_info):
        """Sets the extended_info of this DeviceObjectRequestDto.


        :param extended_info: The extended_info of this DeviceObjectRequestDto.  # noqa: E501
        :type: dict(str, str)
        """

        self._extended_info = extended_info

    @property
    def enabled(self):
        """Gets the enabled of this DeviceObjectRequestDto.  # noqa: E501


        :return: The enabled of this DeviceObjectRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this DeviceObjectRequestDto.


        :param enabled: The enabled of this DeviceObjectRequestDto.  # noqa: E501
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
    def is_deleted(self):
        """Gets the is_deleted of this DeviceObjectRequestDto.  # noqa: E501

        false  # noqa: E501

        :return: The is_deleted of this DeviceObjectRequestDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this DeviceObjectRequestDto.

        false  # noqa: E501

        :param is_deleted: The is_deleted of this DeviceObjectRequestDto.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def is_enabled(self):
        """Gets the is_enabled of this DeviceObjectRequestDto.  # noqa: E501

        This field is deprecated and would be removed in a newer version of the API. Please use 'enabled' field instead.  # noqa: E501

        :return: The is_enabled of this DeviceObjectRequestDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this DeviceObjectRequestDto.

        This field is deprecated and would be removed in a newer version of the API. Please use 'enabled' field instead.  # noqa: E501

        :param is_enabled: The is_enabled of this DeviceObjectRequestDto.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def is_visible(self):
        """Gets the is_visible of this DeviceObjectRequestDto.  # noqa: E501


        :return: The is_visible of this DeviceObjectRequestDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        """Sets the is_visible of this DeviceObjectRequestDto.


        :param is_visible: The is_visible of this DeviceObjectRequestDto.  # noqa: E501
        :type: bool
        """

        self._is_visible = is_visible

    @property
    def indicators(self):
        """Gets the indicators of this DeviceObjectRequestDto.  # noqa: E501


        :return: The indicators of this DeviceObjectRequestDto.  # noqa: E501
        :rtype: list[IndicatorRequestDto]
        """
        return self._indicators

    @indicators.setter
    def indicators(self, indicators):
        """Sets the indicators of this DeviceObjectRequestDto.


        :param indicators: The indicators of this DeviceObjectRequestDto.  # noqa: E501
        :type: list[IndicatorRequestDto]
        """

        self._indicators = indicators

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
        if issubclass(DeviceObjectRequestDto, dict):
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
        if not isinstance(other, DeviceObjectRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
