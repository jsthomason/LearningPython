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

from swagger_client.models.attachment_filters import AttachmentFilters  # noqa: F401,E501
from swagger_client.models.flow_falcon_resource import FlowFalconResource  # noqa: F401,E501
from swagger_client.models.flow_falcon_settings import FlowFalconSettings  # noqa: F401,E501
from swagger_client.models.flow_falcon_visualization import FlowFalconVisualization  # noqa: F401,E501
from swagger_client.models.time_setting import TimeSetting  # noqa: F401,E501


class FlowFalconAttachmentDto(object):
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
        'filters': 'AttachmentFilters',
        'name': 'str',
        'resource': 'FlowFalconResource',
        'settings': 'FlowFalconSettings',
        'time': 'TimeSetting',
        'visualization': 'FlowFalconVisualization'
    }

    attribute_map = {
        'filters': 'filters',
        'name': 'name',
        'resource': 'resource',
        'settings': 'settings',
        'time': 'time',
        'visualization': 'visualization'
    }

    def __init__(self, filters=None, name=None, resource=None, settings=None, time=None, visualization=None):  # noqa: E501
        """FlowFalconAttachmentDto - a model defined in Swagger"""  # noqa: E501

        self._filters = None
        self._name = None
        self._resource = None
        self._settings = None
        self._time = None
        self._visualization = None
        self.discriminator = None

        if filters is not None:
            self.filters = filters
        self.name = name
        self.resource = resource
        self.settings = settings
        self.time = time
        if visualization is not None:
            self.visualization = visualization

    @property
    def filters(self):
        """Gets the filters of this FlowFalconAttachmentDto.  # noqa: E501


        :return: The filters of this FlowFalconAttachmentDto.  # noqa: E501
        :rtype: AttachmentFilters
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this FlowFalconAttachmentDto.


        :param filters: The filters of this FlowFalconAttachmentDto.  # noqa: E501
        :type: AttachmentFilters
        """

        self._filters = filters

    @property
    def name(self):
        """Gets the name of this FlowFalconAttachmentDto.  # noqa: E501


        :return: The name of this FlowFalconAttachmentDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FlowFalconAttachmentDto.


        :param name: The name of this FlowFalconAttachmentDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def resource(self):
        """Gets the resource of this FlowFalconAttachmentDto.  # noqa: E501


        :return: The resource of this FlowFalconAttachmentDto.  # noqa: E501
        :rtype: FlowFalconResource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this FlowFalconAttachmentDto.


        :param resource: The resource of this FlowFalconAttachmentDto.  # noqa: E501
        :type: FlowFalconResource
        """
        if resource is None:
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource

    @property
    def settings(self):
        """Gets the settings of this FlowFalconAttachmentDto.  # noqa: E501


        :return: The settings of this FlowFalconAttachmentDto.  # noqa: E501
        :rtype: FlowFalconSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this FlowFalconAttachmentDto.


        :param settings: The settings of this FlowFalconAttachmentDto.  # noqa: E501
        :type: FlowFalconSettings
        """
        if settings is None:
            raise ValueError("Invalid value for `settings`, must not be `None`")  # noqa: E501

        self._settings = settings

    @property
    def time(self):
        """Gets the time of this FlowFalconAttachmentDto.  # noqa: E501


        :return: The time of this FlowFalconAttachmentDto.  # noqa: E501
        :rtype: TimeSetting
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this FlowFalconAttachmentDto.


        :param time: The time of this FlowFalconAttachmentDto.  # noqa: E501
        :type: TimeSetting
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def visualization(self):
        """Gets the visualization of this FlowFalconAttachmentDto.  # noqa: E501


        :return: The visualization of this FlowFalconAttachmentDto.  # noqa: E501
        :rtype: FlowFalconVisualization
        """
        return self._visualization

    @visualization.setter
    def visualization(self, visualization):
        """Sets the visualization of this FlowFalconAttachmentDto.


        :param visualization: The visualization of this FlowFalconAttachmentDto.  # noqa: E501
        :type: FlowFalconVisualization
        """

        self._visualization = visualization

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
        if issubclass(FlowFalconAttachmentDto, dict):
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
        if not isinstance(other, FlowFalconAttachmentDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
