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

from swagger_client.models.capacity_threshold import CapacityThreshold  # noqa: F401,E501


class TopNSetting(object):
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
        'capacity_threshold': 'CapacityThreshold',
        'display_only_exceeding_objects': 'bool',
        'display_r_values': 'bool',
        'sort_by': 'int',
        'sort_order': 'str',
        'template_id': 'int'
    }

    attribute_map = {
        'capacity_threshold': 'capacityThreshold',
        'display_only_exceeding_objects': 'displayOnlyExceedingObjects',
        'display_r_values': 'displayRValues',
        'sort_by': 'sortBy',
        'sort_order': 'sortOrder',
        'template_id': 'templateId'
    }

    def __init__(self, capacity_threshold=None, display_only_exceeding_objects=None, display_r_values=None, sort_by=None, sort_order=None, template_id=None):  # noqa: E501
        """TopNSetting - a model defined in Swagger"""  # noqa: E501

        self._capacity_threshold = None
        self._display_only_exceeding_objects = None
        self._display_r_values = None
        self._sort_by = None
        self._sort_order = None
        self._template_id = None
        self.discriminator = None

        if capacity_threshold is not None:
            self.capacity_threshold = capacity_threshold
        if display_only_exceeding_objects is not None:
            self.display_only_exceeding_objects = display_only_exceeding_objects
        if display_r_values is not None:
            self.display_r_values = display_r_values
        if sort_by is not None:
            self.sort_by = sort_by
        if sort_order is not None:
            self.sort_order = sort_order
        if template_id is not None:
            self.template_id = template_id

    @property
    def capacity_threshold(self):
        """Gets the capacity_threshold of this TopNSetting.  # noqa: E501


        :return: The capacity_threshold of this TopNSetting.  # noqa: E501
        :rtype: CapacityThreshold
        """
        return self._capacity_threshold

    @capacity_threshold.setter
    def capacity_threshold(self, capacity_threshold):
        """Sets the capacity_threshold of this TopNSetting.


        :param capacity_threshold: The capacity_threshold of this TopNSetting.  # noqa: E501
        :type: CapacityThreshold
        """

        self._capacity_threshold = capacity_threshold

    @property
    def display_only_exceeding_objects(self):
        """Gets the display_only_exceeding_objects of this TopNSetting.  # noqa: E501


        :return: The display_only_exceeding_objects of this TopNSetting.  # noqa: E501
        :rtype: bool
        """
        return self._display_only_exceeding_objects

    @display_only_exceeding_objects.setter
    def display_only_exceeding_objects(self, display_only_exceeding_objects):
        """Sets the display_only_exceeding_objects of this TopNSetting.


        :param display_only_exceeding_objects: The display_only_exceeding_objects of this TopNSetting.  # noqa: E501
        :type: bool
        """

        self._display_only_exceeding_objects = display_only_exceeding_objects

    @property
    def display_r_values(self):
        """Gets the display_r_values of this TopNSetting.  # noqa: E501


        :return: The display_r_values of this TopNSetting.  # noqa: E501
        :rtype: bool
        """
        return self._display_r_values

    @display_r_values.setter
    def display_r_values(self, display_r_values):
        """Sets the display_r_values of this TopNSetting.


        :param display_r_values: The display_r_values of this TopNSetting.  # noqa: E501
        :type: bool
        """

        self._display_r_values = display_r_values

    @property
    def sort_by(self):
        """Gets the sort_by of this TopNSetting.  # noqa: E501


        :return: The sort_by of this TopNSetting.  # noqa: E501
        :rtype: int
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this TopNSetting.


        :param sort_by: The sort_by of this TopNSetting.  # noqa: E501
        :type: int
        """

        self._sort_by = sort_by

    @property
    def sort_order(self):
        """Gets the sort_order of this TopNSetting.  # noqa: E501


        :return: The sort_order of this TopNSetting.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this TopNSetting.


        :param sort_order: The sort_order of this TopNSetting.  # noqa: E501
        :type: str
        """
        allowed_values = ["DESC", "ASC"]  # noqa: E501
        if sort_order not in allowed_values:
            raise ValueError(
                "Invalid value for `sort_order` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_order, allowed_values)
            )

        self._sort_order = sort_order

    @property
    def template_id(self):
        """Gets the template_id of this TopNSetting.  # noqa: E501


        :return: The template_id of this TopNSetting.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this TopNSetting.


        :param template_id: The template_id of this TopNSetting.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

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
        if issubclass(TopNSetting, dict):
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
        if not isinstance(other, TopNSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
