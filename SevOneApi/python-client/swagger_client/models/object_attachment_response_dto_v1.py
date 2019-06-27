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

from swagger_client.models.object_attachment_resource_v1 import ObjectAttachmentResourceV1  # noqa: F401,E501
from swagger_client.models.object_attachment_settings_v1 import ObjectAttachmentSettingsV1  # noqa: F401,E501
from swagger_client.models.object_attachment_visualization_v1 import ObjectAttachmentVisualizationV1  # noqa: F401,E501


class ObjectAttachmentResponseDtoV1(object):
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
        'name': 'str',
        'resource': 'ObjectAttachmentResourceV1',
        'settings': 'ObjectAttachmentSettingsV1',
        'visualization': 'ObjectAttachmentVisualizationV1'
    }

    attribute_map = {
        'name': 'name',
        'resource': 'resource',
        'settings': 'settings',
        'visualization': 'visualization'
    }

    def __init__(self, name=None, resource=None, settings=None, visualization=None):  # noqa: E501
        """ObjectAttachmentResponseDtoV1 - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._resource = None
        self._settings = None
        self._visualization = None
        self.discriminator = None

        self.name = name
        if resource is not None:
            self.resource = resource
        if settings is not None:
            self.settings = settings
        if visualization is not None:
            self.visualization = visualization

    @property
    def name(self):
        """Gets the name of this ObjectAttachmentResponseDtoV1.  # noqa: E501


        :return: The name of this ObjectAttachmentResponseDtoV1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ObjectAttachmentResponseDtoV1.


        :param name: The name of this ObjectAttachmentResponseDtoV1.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def resource(self):
        """Gets the resource of this ObjectAttachmentResponseDtoV1.  # noqa: E501


        :return: The resource of this ObjectAttachmentResponseDtoV1.  # noqa: E501
        :rtype: ObjectAttachmentResourceV1
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this ObjectAttachmentResponseDtoV1.


        :param resource: The resource of this ObjectAttachmentResponseDtoV1.  # noqa: E501
        :type: ObjectAttachmentResourceV1
        """

        self._resource = resource

    @property
    def settings(self):
        """Gets the settings of this ObjectAttachmentResponseDtoV1.  # noqa: E501


        :return: The settings of this ObjectAttachmentResponseDtoV1.  # noqa: E501
        :rtype: ObjectAttachmentSettingsV1
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this ObjectAttachmentResponseDtoV1.


        :param settings: The settings of this ObjectAttachmentResponseDtoV1.  # noqa: E501
        :type: ObjectAttachmentSettingsV1
        """

        self._settings = settings

    @property
    def visualization(self):
        """Gets the visualization of this ObjectAttachmentResponseDtoV1.  # noqa: E501


        :return: The visualization of this ObjectAttachmentResponseDtoV1.  # noqa: E501
        :rtype: ObjectAttachmentVisualizationV1
        """
        return self._visualization

    @visualization.setter
    def visualization(self, visualization):
        """Sets the visualization of this ObjectAttachmentResponseDtoV1.


        :param visualization: The visualization of this ObjectAttachmentResponseDtoV1.  # noqa: E501
        :type: ObjectAttachmentVisualizationV1
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
        if issubclass(ObjectAttachmentResponseDtoV1, dict):
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
        if not isinstance(other, ObjectAttachmentResponseDtoV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
