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

from swagger_client.models.internal_object_dto import InternalObjectDto  # noqa: F401,E501


class ConnectionDto(object):
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
        'data': 'list[InternalObjectDto]',
        'id': 'int',
        'node_a_id': 'int',
        'node_b_id': 'int',
        'type': 'str'
    }

    attribute_map = {
        'data': 'data',
        'id': 'id',
        'node_a_id': 'nodeAId',
        'node_b_id': 'nodeBId',
        'type': 'type'
    }

    def __init__(self, data=None, id=None, node_a_id=None, node_b_id=None, type=None):  # noqa: E501
        """ConnectionDto - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._id = None
        self._node_a_id = None
        self._node_b_id = None
        self._type = None
        self.discriminator = None

        self.data = data
        if id is not None:
            self.id = id
        self.node_a_id = node_a_id
        self.node_b_id = node_b_id
        self.type = type

    @property
    def data(self):
        """Gets the data of this ConnectionDto.  # noqa: E501


        :return: The data of this ConnectionDto.  # noqa: E501
        :rtype: list[InternalObjectDto]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ConnectionDto.


        :param data: The data of this ConnectionDto.  # noqa: E501
        :type: list[InternalObjectDto]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def id(self):
        """Gets the id of this ConnectionDto.  # noqa: E501


        :return: The id of this ConnectionDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConnectionDto.


        :param id: The id of this ConnectionDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def node_a_id(self):
        """Gets the node_a_id of this ConnectionDto.  # noqa: E501


        :return: The node_a_id of this ConnectionDto.  # noqa: E501
        :rtype: int
        """
        return self._node_a_id

    @node_a_id.setter
    def node_a_id(self, node_a_id):
        """Sets the node_a_id of this ConnectionDto.


        :param node_a_id: The node_a_id of this ConnectionDto.  # noqa: E501
        :type: int
        """
        if node_a_id is None:
            raise ValueError("Invalid value for `node_a_id`, must not be `None`")  # noqa: E501

        self._node_a_id = node_a_id

    @property
    def node_b_id(self):
        """Gets the node_b_id of this ConnectionDto.  # noqa: E501


        :return: The node_b_id of this ConnectionDto.  # noqa: E501
        :rtype: int
        """
        return self._node_b_id

    @node_b_id.setter
    def node_b_id(self, node_b_id):
        """Sets the node_b_id of this ConnectionDto.


        :param node_b_id: The node_b_id of this ConnectionDto.  # noqa: E501
        :type: int
        """
        if node_b_id is None:
            raise ValueError("Invalid value for `node_b_id`, must not be `None`")  # noqa: E501

        self._node_b_id = node_b_id

    @property
    def type(self):
        """Gets the type of this ConnectionDto.  # noqa: E501


        :return: The type of this ConnectionDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConnectionDto.


        :param type: The type of this ConnectionDto.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Device", "DeviceGroup", "Object", "ObjectGroup", "StatusMap"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(ConnectionDto, dict):
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
        if not isinstance(other, ConnectionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
