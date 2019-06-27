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


class GroupMetricsIndicatorTypesV1(object):
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
        'aggregations': 'list[str]',
        'ids': 'list[int]',
        'object_type_id': 'int',
        'plugin_id': 'int'
    }

    attribute_map = {
        'aggregations': 'aggregations',
        'ids': 'ids',
        'object_type_id': 'objectTypeId',
        'plugin_id': 'pluginId'
    }

    def __init__(self, aggregations=None, ids=None, object_type_id=None, plugin_id=None):  # noqa: E501
        """GroupMetricsIndicatorTypesV1 - a model defined in Swagger"""  # noqa: E501

        self._aggregations = None
        self._ids = None
        self._object_type_id = None
        self._plugin_id = None
        self.discriminator = None

        self.aggregations = aggregations
        if ids is not None:
            self.ids = ids
        self.object_type_id = object_type_id
        self.plugin_id = plugin_id

    @property
    def aggregations(self):
        """Gets the aggregations of this GroupMetricsIndicatorTypesV1.  # noqa: E501

        Allowed values are `avg`, `avgPer`, `min`, `minPer`, `max`, `maxPer`  # noqa: E501

        :return: The aggregations of this GroupMetricsIndicatorTypesV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._aggregations

    @aggregations.setter
    def aggregations(self, aggregations):
        """Sets the aggregations of this GroupMetricsIndicatorTypesV1.

        Allowed values are `avg`, `avgPer`, `min`, `minPer`, `max`, `maxPer`  # noqa: E501

        :param aggregations: The aggregations of this GroupMetricsIndicatorTypesV1.  # noqa: E501
        :type: list[str]
        """
        if aggregations is None:
            raise ValueError("Invalid value for `aggregations`, must not be `None`")  # noqa: E501
        allowed_values = ["avg", "max", "min", "avgPer", "maxPer", "minPer"]  # noqa: E501
        if not set(aggregations).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `aggregations` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(aggregations) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._aggregations = aggregations

    @property
    def ids(self):
        """Gets the ids of this GroupMetricsIndicatorTypesV1.  # noqa: E501


        :return: The ids of this GroupMetricsIndicatorTypesV1.  # noqa: E501
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this GroupMetricsIndicatorTypesV1.


        :param ids: The ids of this GroupMetricsIndicatorTypesV1.  # noqa: E501
        :type: list[int]
        """

        self._ids = ids

    @property
    def object_type_id(self):
        """Gets the object_type_id of this GroupMetricsIndicatorTypesV1.  # noqa: E501


        :return: The object_type_id of this GroupMetricsIndicatorTypesV1.  # noqa: E501
        :rtype: int
        """
        return self._object_type_id

    @object_type_id.setter
    def object_type_id(self, object_type_id):
        """Sets the object_type_id of this GroupMetricsIndicatorTypesV1.


        :param object_type_id: The object_type_id of this GroupMetricsIndicatorTypesV1.  # noqa: E501
        :type: int
        """
        if object_type_id is None:
            raise ValueError("Invalid value for `object_type_id`, must not be `None`")  # noqa: E501

        self._object_type_id = object_type_id

    @property
    def plugin_id(self):
        """Gets the plugin_id of this GroupMetricsIndicatorTypesV1.  # noqa: E501


        :return: The plugin_id of this GroupMetricsIndicatorTypesV1.  # noqa: E501
        :rtype: int
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this GroupMetricsIndicatorTypesV1.


        :param plugin_id: The plugin_id of this GroupMetricsIndicatorTypesV1.  # noqa: E501
        :type: int
        """
        if plugin_id is None:
            raise ValueError("Invalid value for `plugin_id`, must not be `None`")  # noqa: E501

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
        if issubclass(GroupMetricsIndicatorTypesV1, dict):
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
        if not isinstance(other, GroupMetricsIndicatorTypesV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
