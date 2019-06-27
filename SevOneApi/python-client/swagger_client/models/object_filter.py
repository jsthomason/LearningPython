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

from swagger_client.models.device_object_id import DeviceObjectId  # noqa: F401,E501


class ObjectFilter(object):
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
        'device_group_ids': 'list[int]',
        'device_ids': 'list[int]',
        'enabled': 'str',
        'is_deleted': 'bool',
        'is_enabled': 'bool',
        'is_visible': 'bool',
        'metadata': 'dict(str, str)',
        'name': 'str',
        'object_group_ids': 'list[int]',
        'object_ids': 'list[DeviceObjectId]',
        'peer_ids': 'list[int]',
        'plugin_ids': 'list[int]',
        'plugin_name': 'str',
        'plugin_object_type_ids': 'list[int]'
    }

    attribute_map = {
        'device_group_ids': 'deviceGroupIds',
        'device_ids': 'deviceIds',
        'enabled': 'enabled',
        'is_deleted': 'isDeleted',
        'is_enabled': 'isEnabled',
        'is_visible': 'isVisible',
        'metadata': 'metadata',
        'name': 'name',
        'object_group_ids': 'objectGroupIds',
        'object_ids': 'objectIds',
        'peer_ids': 'peerIds',
        'plugin_ids': 'pluginIds',
        'plugin_name': 'pluginName',
        'plugin_object_type_ids': 'pluginObjectTypeIds'
    }

    def __init__(self, device_group_ids=None, device_ids=None, enabled=None, is_deleted=None, is_enabled=None, is_visible=None, metadata=None, name=None, object_group_ids=None, object_ids=None, peer_ids=None, plugin_ids=None, plugin_name=None, plugin_object_type_ids=None):  # noqa: E501
        """ObjectFilter - a model defined in Swagger"""  # noqa: E501

        self._device_group_ids = None
        self._device_ids = None
        self._enabled = None
        self._is_deleted = None
        self._is_enabled = None
        self._is_visible = None
        self._metadata = None
        self._name = None
        self._object_group_ids = None
        self._object_ids = None
        self._peer_ids = None
        self._plugin_ids = None
        self._plugin_name = None
        self._plugin_object_type_ids = None
        self.discriminator = None

        if device_group_ids is not None:
            self.device_group_ids = device_group_ids
        if device_ids is not None:
            self.device_ids = device_ids
        if enabled is not None:
            self.enabled = enabled
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if is_visible is not None:
            self.is_visible = is_visible
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if object_group_ids is not None:
            self.object_group_ids = object_group_ids
        if object_ids is not None:
            self.object_ids = object_ids
        if peer_ids is not None:
            self.peer_ids = peer_ids
        if plugin_ids is not None:
            self.plugin_ids = plugin_ids
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if plugin_object_type_ids is not None:
            self.plugin_object_type_ids = plugin_object_type_ids

    @property
    def device_group_ids(self):
        """Gets the device_group_ids of this ObjectFilter.  # noqa: E501


        :return: The device_group_ids of this ObjectFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._device_group_ids

    @device_group_ids.setter
    def device_group_ids(self, device_group_ids):
        """Sets the device_group_ids of this ObjectFilter.


        :param device_group_ids: The device_group_ids of this ObjectFilter.  # noqa: E501
        :type: list[int]
        """

        self._device_group_ids = device_group_ids

    @property
    def device_ids(self):
        """Gets the device_ids of this ObjectFilter.  # noqa: E501


        :return: The device_ids of this ObjectFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._device_ids

    @device_ids.setter
    def device_ids(self, device_ids):
        """Sets the device_ids of this ObjectFilter.


        :param device_ids: The device_ids of this ObjectFilter.  # noqa: E501
        :type: list[int]
        """

        self._device_ids = device_ids

    @property
    def enabled(self):
        """Gets the enabled of this ObjectFilter.  # noqa: E501


        :return: The enabled of this ObjectFilter.  # noqa: E501
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ObjectFilter.


        :param enabled: The enabled of this ObjectFilter.  # noqa: E501
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
        """Gets the is_deleted of this ObjectFilter.  # noqa: E501


        :return: The is_deleted of this ObjectFilter.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this ObjectFilter.


        :param is_deleted: The is_deleted of this ObjectFilter.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def is_enabled(self):
        """Gets the is_enabled of this ObjectFilter.  # noqa: E501

        This field is deprecated and would be removed in a newer version of the API. Please use 'enabled' field instead.  # noqa: E501

        :return: The is_enabled of this ObjectFilter.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this ObjectFilter.

        This field is deprecated and would be removed in a newer version of the API. Please use 'enabled' field instead.  # noqa: E501

        :param is_enabled: The is_enabled of this ObjectFilter.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def is_visible(self):
        """Gets the is_visible of this ObjectFilter.  # noqa: E501


        :return: The is_visible of this ObjectFilter.  # noqa: E501
        :rtype: bool
        """
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        """Sets the is_visible of this ObjectFilter.


        :param is_visible: The is_visible of this ObjectFilter.  # noqa: E501
        :type: bool
        """

        self._is_visible = is_visible

    @property
    def metadata(self):
        """Gets the metadata of this ObjectFilter.  # noqa: E501

        Key-value pair, the key is namespaceName.attributeName, e.g. {system}.sysName  # noqa: E501

        :return: The metadata of this ObjectFilter.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ObjectFilter.

        Key-value pair, the key is namespaceName.attributeName, e.g. {system}.sysName  # noqa: E501

        :param metadata: The metadata of this ObjectFilter.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this ObjectFilter.  # noqa: E501


        :return: The name of this ObjectFilter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ObjectFilter.


        :param name: The name of this ObjectFilter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def object_group_ids(self):
        """Gets the object_group_ids of this ObjectFilter.  # noqa: E501


        :return: The object_group_ids of this ObjectFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._object_group_ids

    @object_group_ids.setter
    def object_group_ids(self, object_group_ids):
        """Sets the object_group_ids of this ObjectFilter.


        :param object_group_ids: The object_group_ids of this ObjectFilter.  # noqa: E501
        :type: list[int]
        """

        self._object_group_ids = object_group_ids

    @property
    def object_ids(self):
        """Gets the object_ids of this ObjectFilter.  # noqa: E501


        :return: The object_ids of this ObjectFilter.  # noqa: E501
        :rtype: list[DeviceObjectId]
        """
        return self._object_ids

    @object_ids.setter
    def object_ids(self, object_ids):
        """Sets the object_ids of this ObjectFilter.


        :param object_ids: The object_ids of this ObjectFilter.  # noqa: E501
        :type: list[DeviceObjectId]
        """

        self._object_ids = object_ids

    @property
    def peer_ids(self):
        """Gets the peer_ids of this ObjectFilter.  # noqa: E501


        :return: The peer_ids of this ObjectFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._peer_ids

    @peer_ids.setter
    def peer_ids(self, peer_ids):
        """Sets the peer_ids of this ObjectFilter.


        :param peer_ids: The peer_ids of this ObjectFilter.  # noqa: E501
        :type: list[int]
        """

        self._peer_ids = peer_ids

    @property
    def plugin_ids(self):
        """Gets the plugin_ids of this ObjectFilter.  # noqa: E501


        :return: The plugin_ids of this ObjectFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._plugin_ids

    @plugin_ids.setter
    def plugin_ids(self, plugin_ids):
        """Sets the plugin_ids of this ObjectFilter.


        :param plugin_ids: The plugin_ids of this ObjectFilter.  # noqa: E501
        :type: list[int]
        """

        self._plugin_ids = plugin_ids

    @property
    def plugin_name(self):
        """Gets the plugin_name of this ObjectFilter.  # noqa: E501


        :return: The plugin_name of this ObjectFilter.  # noqa: E501
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this ObjectFilter.


        :param plugin_name: The plugin_name of this ObjectFilter.  # noqa: E501
        :type: str
        """

        self._plugin_name = plugin_name

    @property
    def plugin_object_type_ids(self):
        """Gets the plugin_object_type_ids of this ObjectFilter.  # noqa: E501


        :return: The plugin_object_type_ids of this ObjectFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._plugin_object_type_ids

    @plugin_object_type_ids.setter
    def plugin_object_type_ids(self, plugin_object_type_ids):
        """Sets the plugin_object_type_ids of this ObjectFilter.


        :param plugin_object_type_ids: The plugin_object_type_ids of this ObjectFilter.  # noqa: E501
        :type: list[int]
        """

        self._plugin_object_type_ids = plugin_object_type_ids

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
        if issubclass(ObjectFilter, dict):
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
        if not isinstance(other, ObjectFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
