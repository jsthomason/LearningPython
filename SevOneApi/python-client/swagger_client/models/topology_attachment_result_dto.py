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

from swagger_client.models.node_data import NodeData  # noqa: F401,E501
from swagger_client.models.reporting_link_data import ReportingLinkData  # noqa: F401,E501


class TopologyAttachmentResultDto(object):
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
        'focal_device_id': 'int',
        'link_data': 'list[ReportingLinkData]',
        'node_data': 'list[NodeData]'
    }

    attribute_map = {
        'focal_device_id': 'focalDeviceId',
        'link_data': 'linkData',
        'node_data': 'nodeData'
    }

    def __init__(self, focal_device_id=None, link_data=None, node_data=None):  # noqa: E501
        """TopologyAttachmentResultDto - a model defined in Swagger"""  # noqa: E501

        self._focal_device_id = None
        self._link_data = None
        self._node_data = None
        self.discriminator = None

        if focal_device_id is not None:
            self.focal_device_id = focal_device_id
        if link_data is not None:
            self.link_data = link_data
        if node_data is not None:
            self.node_data = node_data

    @property
    def focal_device_id(self):
        """Gets the focal_device_id of this TopologyAttachmentResultDto.  # noqa: E501


        :return: The focal_device_id of this TopologyAttachmentResultDto.  # noqa: E501
        :rtype: int
        """
        return self._focal_device_id

    @focal_device_id.setter
    def focal_device_id(self, focal_device_id):
        """Sets the focal_device_id of this TopologyAttachmentResultDto.


        :param focal_device_id: The focal_device_id of this TopologyAttachmentResultDto.  # noqa: E501
        :type: int
        """

        self._focal_device_id = focal_device_id

    @property
    def link_data(self):
        """Gets the link_data of this TopologyAttachmentResultDto.  # noqa: E501


        :return: The link_data of this TopologyAttachmentResultDto.  # noqa: E501
        :rtype: list[ReportingLinkData]
        """
        return self._link_data

    @link_data.setter
    def link_data(self, link_data):
        """Sets the link_data of this TopologyAttachmentResultDto.


        :param link_data: The link_data of this TopologyAttachmentResultDto.  # noqa: E501
        :type: list[ReportingLinkData]
        """

        self._link_data = link_data

    @property
    def node_data(self):
        """Gets the node_data of this TopologyAttachmentResultDto.  # noqa: E501


        :return: The node_data of this TopologyAttachmentResultDto.  # noqa: E501
        :rtype: list[NodeData]
        """
        return self._node_data

    @node_data.setter
    def node_data(self, node_data):
        """Sets the node_data of this TopologyAttachmentResultDto.


        :param node_data: The node_data of this TopologyAttachmentResultDto.  # noqa: E501
        :type: list[NodeData]
        """

        self._node_data = node_data

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
        if issubclass(TopologyAttachmentResultDto, dict):
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
        if not isinstance(other, TopologyAttachmentResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other