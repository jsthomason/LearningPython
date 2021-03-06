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

from swagger_client.models.indicator_type_dto_v1 import IndicatorTypeDtoV1  # noqa: F401,E501
from swagger_client.models.object_type_dto_v1 import ObjectTypeDtoV1  # noqa: F401,E501


class ObjectTypeDtoV1(object):
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
        'extended_info': 'dict(str, dict(str, str))',
        'id': 'int',
        'indicator_types': 'list[IndicatorTypeDtoV1]',
        'is_editable': 'bool',
        'is_enabled': 'bool',
        'name': 'str',
        'object_types': 'list[ObjectTypeDtoV1]',
        'parent_object_type_id': 'int',
        'plugin_id': 'int'
    }

    attribute_map = {
        'extended_info': 'extendedInfo',
        'id': 'id',
        'indicator_types': 'indicatorTypes',
        'is_editable': 'isEditable',
        'is_enabled': 'isEnabled',
        'name': 'name',
        'object_types': 'objectTypes',
        'parent_object_type_id': 'parentObjectTypeId',
        'plugin_id': 'pluginId'
    }

    def __init__(self, extended_info=None, id=None, indicator_types=None, is_editable=None, is_enabled=None, name=None, object_types=None, parent_object_type_id=None, plugin_id=None):  # noqa: E501
        """ObjectTypeDtoV1 - a model defined in Swagger"""  # noqa: E501

        self._extended_info = None
        self._id = None
        self._indicator_types = None
        self._is_editable = None
        self._is_enabled = None
        self._name = None
        self._object_types = None
        self._parent_object_type_id = None
        self._plugin_id = None
        self.discriminator = None

        if extended_info is not None:
            self.extended_info = extended_info
        if id is not None:
            self.id = id
        if indicator_types is not None:
            self.indicator_types = indicator_types
        if is_editable is not None:
            self.is_editable = is_editable
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if name is not None:
            self.name = name
        if object_types is not None:
            self.object_types = object_types
        if parent_object_type_id is not None:
            self.parent_object_type_id = parent_object_type_id
        if plugin_id is not None:
            self.plugin_id = plugin_id

    @property
    def extended_info(self):
        """Gets the extended_info of this ObjectTypeDtoV1.  # noqa: E501


        :return: The extended_info of this ObjectTypeDtoV1.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._extended_info

    @extended_info.setter
    def extended_info(self, extended_info):
        """Sets the extended_info of this ObjectTypeDtoV1.


        :param extended_info: The extended_info of this ObjectTypeDtoV1.  # noqa: E501
        :type: dict(str, dict(str, str))
        """

        self._extended_info = extended_info

    @property
    def id(self):
        """Gets the id of this ObjectTypeDtoV1.  # noqa: E501


        :return: The id of this ObjectTypeDtoV1.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ObjectTypeDtoV1.


        :param id: The id of this ObjectTypeDtoV1.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def indicator_types(self):
        """Gets the indicator_types of this ObjectTypeDtoV1.  # noqa: E501


        :return: The indicator_types of this ObjectTypeDtoV1.  # noqa: E501
        :rtype: list[IndicatorTypeDtoV1]
        """
        return self._indicator_types

    @indicator_types.setter
    def indicator_types(self, indicator_types):
        """Sets the indicator_types of this ObjectTypeDtoV1.


        :param indicator_types: The indicator_types of this ObjectTypeDtoV1.  # noqa: E501
        :type: list[IndicatorTypeDtoV1]
        """

        self._indicator_types = indicator_types

    @property
    def is_editable(self):
        """Gets the is_editable of this ObjectTypeDtoV1.  # noqa: E501


        :return: The is_editable of this ObjectTypeDtoV1.  # noqa: E501
        :rtype: bool
        """
        return self._is_editable

    @is_editable.setter
    def is_editable(self, is_editable):
        """Sets the is_editable of this ObjectTypeDtoV1.


        :param is_editable: The is_editable of this ObjectTypeDtoV1.  # noqa: E501
        :type: bool
        """

        self._is_editable = is_editable

    @property
    def is_enabled(self):
        """Gets the is_enabled of this ObjectTypeDtoV1.  # noqa: E501


        :return: The is_enabled of this ObjectTypeDtoV1.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this ObjectTypeDtoV1.


        :param is_enabled: The is_enabled of this ObjectTypeDtoV1.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def name(self):
        """Gets the name of this ObjectTypeDtoV1.  # noqa: E501


        :return: The name of this ObjectTypeDtoV1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ObjectTypeDtoV1.


        :param name: The name of this ObjectTypeDtoV1.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def object_types(self):
        """Gets the object_types of this ObjectTypeDtoV1.  # noqa: E501


        :return: The object_types of this ObjectTypeDtoV1.  # noqa: E501
        :rtype: list[ObjectTypeDtoV1]
        """
        return self._object_types

    @object_types.setter
    def object_types(self, object_types):
        """Sets the object_types of this ObjectTypeDtoV1.


        :param object_types: The object_types of this ObjectTypeDtoV1.  # noqa: E501
        :type: list[ObjectTypeDtoV1]
        """

        self._object_types = object_types

    @property
    def parent_object_type_id(self):
        """Gets the parent_object_type_id of this ObjectTypeDtoV1.  # noqa: E501


        :return: The parent_object_type_id of this ObjectTypeDtoV1.  # noqa: E501
        :rtype: int
        """
        return self._parent_object_type_id

    @parent_object_type_id.setter
    def parent_object_type_id(self, parent_object_type_id):
        """Sets the parent_object_type_id of this ObjectTypeDtoV1.


        :param parent_object_type_id: The parent_object_type_id of this ObjectTypeDtoV1.  # noqa: E501
        :type: int
        """

        self._parent_object_type_id = parent_object_type_id

    @property
    def plugin_id(self):
        """Gets the plugin_id of this ObjectTypeDtoV1.  # noqa: E501


        :return: The plugin_id of this ObjectTypeDtoV1.  # noqa: E501
        :rtype: int
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this ObjectTypeDtoV1.


        :param plugin_id: The plugin_id of this ObjectTypeDtoV1.  # noqa: E501
        :type: int
        """

        self._plugin_id = plugin_id

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
        if issubclass(ObjectTypeDtoV1, dict):
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
        if not isinstance(other, ObjectTypeDtoV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
