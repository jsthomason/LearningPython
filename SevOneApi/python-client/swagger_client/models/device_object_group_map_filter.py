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


class DeviceObjectGroupMapFilter(object):
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
        'automatic': 'bool',
        'device_ids': 'list[int]',
        'device_object_ids': 'list[DeviceObjectId]',
        'ids': 'list[int]',
        'object_group_ids': 'list[int]',
        'plugin_ids': 'list[int]'
    }

    attribute_map = {
        'automatic': 'automatic',
        'device_ids': 'deviceIds',
        'device_object_ids': 'deviceObjectIds',
        'ids': 'ids',
        'object_group_ids': 'objectGroupIds',
        'plugin_ids': 'pluginIds'
    }

    def __init__(self, automatic=None, device_ids=None, device_object_ids=None, ids=None, object_group_ids=None, plugin_ids=None):  # noqa: E501
        """DeviceObjectGroupMapFilter - a model defined in Swagger"""  # noqa: E501

        self._automatic = None
        self._device_ids = None
        self._device_object_ids = None
        self._ids = None
        self._object_group_ids = None
        self._plugin_ids = None
        self.discriminator = None

        if automatic is not None:
            self.automatic = automatic
        if device_ids is not None:
            self.device_ids = device_ids
        if device_object_ids is not None:
            self.device_object_ids = device_object_ids
        if ids is not None:
            self.ids = ids
        if object_group_ids is not None:
            self.object_group_ids = object_group_ids
        if plugin_ids is not None:
            self.plugin_ids = plugin_ids

    @property
    def automatic(self):
        """Gets the automatic of this DeviceObjectGroupMapFilter.  # noqa: E501


        :return: The automatic of this DeviceObjectGroupMapFilter.  # noqa: E501
        :rtype: bool
        """
        return self._automatic

    @automatic.setter
    def automatic(self, automatic):
        """Sets the automatic of this DeviceObjectGroupMapFilter.


        :param automatic: The automatic of this DeviceObjectGroupMapFilter.  # noqa: E501
        :type: bool
        """

        self._automatic = automatic

    @property
    def device_ids(self):
        """Gets the device_ids of this DeviceObjectGroupMapFilter.  # noqa: E501


        :return: The device_ids of this DeviceObjectGroupMapFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._device_ids

    @device_ids.setter
    def device_ids(self, device_ids):
        """Sets the device_ids of this DeviceObjectGroupMapFilter.


        :param device_ids: The device_ids of this DeviceObjectGroupMapFilter.  # noqa: E501
        :type: list[int]
        """

        self._device_ids = device_ids

    @property
    def device_object_ids(self):
        """Gets the device_object_ids of this DeviceObjectGroupMapFilter.  # noqa: E501


        :return: The device_object_ids of this DeviceObjectGroupMapFilter.  # noqa: E501
        :rtype: list[DeviceObjectId]
        """
        return self._device_object_ids

    @device_object_ids.setter
    def device_object_ids(self, device_object_ids):
        """Sets the device_object_ids of this DeviceObjectGroupMapFilter.


        :param device_object_ids: The device_object_ids of this DeviceObjectGroupMapFilter.  # noqa: E501
        :type: list[DeviceObjectId]
        """

        self._device_object_ids = device_object_ids

    @property
    def ids(self):
        """Gets the ids of this DeviceObjectGroupMapFilter.  # noqa: E501


        :return: The ids of this DeviceObjectGroupMapFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this DeviceObjectGroupMapFilter.


        :param ids: The ids of this DeviceObjectGroupMapFilter.  # noqa: E501
        :type: list[int]
        """

        self._ids = ids

    @property
    def object_group_ids(self):
        """Gets the object_group_ids of this DeviceObjectGroupMapFilter.  # noqa: E501


        :return: The object_group_ids of this DeviceObjectGroupMapFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._object_group_ids

    @object_group_ids.setter
    def object_group_ids(self, object_group_ids):
        """Sets the object_group_ids of this DeviceObjectGroupMapFilter.


        :param object_group_ids: The object_group_ids of this DeviceObjectGroupMapFilter.  # noqa: E501
        :type: list[int]
        """

        self._object_group_ids = object_group_ids

    @property
    def plugin_ids(self):
        """Gets the plugin_ids of this DeviceObjectGroupMapFilter.  # noqa: E501


        :return: The plugin_ids of this DeviceObjectGroupMapFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._plugin_ids

    @plugin_ids.setter
    def plugin_ids(self, plugin_ids):
        """Sets the plugin_ids of this DeviceObjectGroupMapFilter.


        :param plugin_ids: The plugin_ids of this DeviceObjectGroupMapFilter.  # noqa: E501
        :type: list[int]
        """

        self._plugin_ids = plugin_ids

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
        if issubclass(DeviceObjectGroupMapFilter, dict):
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
        if not isinstance(other, DeviceObjectGroupMapFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
