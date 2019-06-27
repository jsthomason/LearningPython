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


class PluginIndicatorTypeFilterDto(object):
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
        'allow_maximum_value': 'bool',
        'data_units': 'str',
        'description': 'str',
        'display_units': 'str',
        'format': 'str',
        'id': 'int',
        'ids': 'list[int]',
        'is_default': 'bool',
        'is_enabled': 'bool',
        'name': 'str',
        'plugin_id': 'int',
        'plugin_object_type_id': 'int',
        'synthetic_expression': 'str',
        'synthetic_maximum_expression': 'str'
    }

    attribute_map = {
        'allow_maximum_value': 'allowMaximumValue',
        'data_units': 'dataUnits',
        'description': 'description',
        'display_units': 'displayUnits',
        'format': 'format',
        'id': 'id',
        'ids': 'ids',
        'is_default': 'isDefault',
        'is_enabled': 'isEnabled',
        'name': 'name',
        'plugin_id': 'pluginId',
        'plugin_object_type_id': 'pluginObjectTypeId',
        'synthetic_expression': 'syntheticExpression',
        'synthetic_maximum_expression': 'syntheticMaximumExpression'
    }

    def __init__(self, allow_maximum_value=None, data_units=None, description=None, display_units=None, format=None, id=None, ids=None, is_default=None, is_enabled=None, name=None, plugin_id=None, plugin_object_type_id=None, synthetic_expression=None, synthetic_maximum_expression=None):  # noqa: E501
        """PluginIndicatorTypeFilterDto - a model defined in Swagger"""  # noqa: E501

        self._allow_maximum_value = None
        self._data_units = None
        self._description = None
        self._display_units = None
        self._format = None
        self._id = None
        self._ids = None
        self._is_default = None
        self._is_enabled = None
        self._name = None
        self._plugin_id = None
        self._plugin_object_type_id = None
        self._synthetic_expression = None
        self._synthetic_maximum_expression = None
        self.discriminator = None

        if allow_maximum_value is not None:
            self.allow_maximum_value = allow_maximum_value
        if data_units is not None:
            self.data_units = data_units
        if description is not None:
            self.description = description
        if display_units is not None:
            self.display_units = display_units
        if format is not None:
            self.format = format
        if id is not None:
            self.id = id
        if ids is not None:
            self.ids = ids
        if is_default is not None:
            self.is_default = is_default
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if name is not None:
            self.name = name
        if plugin_id is not None:
            self.plugin_id = plugin_id
        if plugin_object_type_id is not None:
            self.plugin_object_type_id = plugin_object_type_id
        if synthetic_expression is not None:
            self.synthetic_expression = synthetic_expression
        if synthetic_maximum_expression is not None:
            self.synthetic_maximum_expression = synthetic_maximum_expression

    @property
    def allow_maximum_value(self):
        """Gets the allow_maximum_value of this PluginIndicatorTypeFilterDto.  # noqa: E501


        :return: The allow_maximum_value of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :rtype: bool
        """
        return self._allow_maximum_value

    @allow_maximum_value.setter
    def allow_maximum_value(self, allow_maximum_value):
        """Sets the allow_maximum_value of this PluginIndicatorTypeFilterDto.


        :param allow_maximum_value: The allow_maximum_value of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :type: bool
        """

        self._allow_maximum_value = allow_maximum_value

    @property
    def data_units(self):
        """Gets the data_units of this PluginIndicatorTypeFilterDto.  # noqa: E501


        :return: The data_units of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._data_units

    @data_units.setter
    def data_units(self, data_units):
        """Sets the data_units of this PluginIndicatorTypeFilterDto.


        :param data_units: The data_units of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :type: str
        """

        self._data_units = data_units

    @property
    def description(self):
        """Gets the description of this PluginIndicatorTypeFilterDto.  # noqa: E501


        :return: The description of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PluginIndicatorTypeFilterDto.


        :param description: The description of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_units(self):
        """Gets the display_units of this PluginIndicatorTypeFilterDto.  # noqa: E501


        :return: The display_units of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._display_units

    @display_units.setter
    def display_units(self, display_units):
        """Sets the display_units of this PluginIndicatorTypeFilterDto.


        :param display_units: The display_units of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :type: str
        """

        self._display_units = display_units

    @property
    def format(self):
        """Gets the format of this PluginIndicatorTypeFilterDto.  # noqa: E501


        :return: The format of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this PluginIndicatorTypeFilterDto.


        :param format: The format of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["GAUGE", "COUNTER32", "COUNTER64"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def id(self):
        """Gets the id of this PluginIndicatorTypeFilterDto.  # noqa: E501


        :return: The id of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PluginIndicatorTypeFilterDto.


        :param id: The id of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def ids(self):
        """Gets the ids of this PluginIndicatorTypeFilterDto.  # noqa: E501


        :return: The ids of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this PluginIndicatorTypeFilterDto.


        :param ids: The ids of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :type: list[int]
        """

        self._ids = ids

    @property
    def is_default(self):
        """Gets the is_default of this PluginIndicatorTypeFilterDto.  # noqa: E501


        :return: The is_default of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this PluginIndicatorTypeFilterDto.


        :param is_default: The is_default of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def is_enabled(self):
        """Gets the is_enabled of this PluginIndicatorTypeFilterDto.  # noqa: E501


        :return: The is_enabled of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this PluginIndicatorTypeFilterDto.


        :param is_enabled: The is_enabled of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def name(self):
        """Gets the name of this PluginIndicatorTypeFilterDto.  # noqa: E501


        :return: The name of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PluginIndicatorTypeFilterDto.


        :param name: The name of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def plugin_id(self):
        """Gets the plugin_id of this PluginIndicatorTypeFilterDto.  # noqa: E501


        :return: The plugin_id of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this PluginIndicatorTypeFilterDto.


        :param plugin_id: The plugin_id of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :type: int
        """

        self._plugin_id = plugin_id

    @property
    def plugin_object_type_id(self):
        """Gets the plugin_object_type_id of this PluginIndicatorTypeFilterDto.  # noqa: E501


        :return: The plugin_object_type_id of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._plugin_object_type_id

    @plugin_object_type_id.setter
    def plugin_object_type_id(self, plugin_object_type_id):
        """Sets the plugin_object_type_id of this PluginIndicatorTypeFilterDto.


        :param plugin_object_type_id: The plugin_object_type_id of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :type: int
        """

        self._plugin_object_type_id = plugin_object_type_id

    @property
    def synthetic_expression(self):
        """Gets the synthetic_expression of this PluginIndicatorTypeFilterDto.  # noqa: E501


        :return: The synthetic_expression of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._synthetic_expression

    @synthetic_expression.setter
    def synthetic_expression(self, synthetic_expression):
        """Sets the synthetic_expression of this PluginIndicatorTypeFilterDto.


        :param synthetic_expression: The synthetic_expression of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :type: str
        """

        self._synthetic_expression = synthetic_expression

    @property
    def synthetic_maximum_expression(self):
        """Gets the synthetic_maximum_expression of this PluginIndicatorTypeFilterDto.  # noqa: E501


        :return: The synthetic_maximum_expression of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._synthetic_maximum_expression

    @synthetic_maximum_expression.setter
    def synthetic_maximum_expression(self, synthetic_maximum_expression):
        """Sets the synthetic_maximum_expression of this PluginIndicatorTypeFilterDto.


        :param synthetic_maximum_expression: The synthetic_maximum_expression of this PluginIndicatorTypeFilterDto.  # noqa: E501
        :type: str
        """

        self._synthetic_maximum_expression = synthetic_maximum_expression

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
        if issubclass(PluginIndicatorTypeFilterDto, dict):
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
        if not isinstance(other, PluginIndicatorTypeFilterDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
