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


class MapImageDto(object):
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
        'id': 'int',
        'image_mime_type': 'str',
        'image_size': 'int',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'image_mime_type': 'imageMimeType',
        'image_size': 'imageSize',
        'name': 'name'
    }

    def __init__(self, id=None, image_mime_type=None, image_size=None, name=None):  # noqa: E501
        """MapImageDto - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._image_mime_type = None
        self._image_size = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if image_mime_type is not None:
            self.image_mime_type = image_mime_type
        if image_size is not None:
            self.image_size = image_size
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this MapImageDto.  # noqa: E501


        :return: The id of this MapImageDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MapImageDto.


        :param id: The id of this MapImageDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def image_mime_type(self):
        """Gets the image_mime_type of this MapImageDto.  # noqa: E501


        :return: The image_mime_type of this MapImageDto.  # noqa: E501
        :rtype: str
        """
        return self._image_mime_type

    @image_mime_type.setter
    def image_mime_type(self, image_mime_type):
        """Sets the image_mime_type of this MapImageDto.


        :param image_mime_type: The image_mime_type of this MapImageDto.  # noqa: E501
        :type: str
        """

        self._image_mime_type = image_mime_type

    @property
    def image_size(self):
        """Gets the image_size of this MapImageDto.  # noqa: E501


        :return: The image_size of this MapImageDto.  # noqa: E501
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        """Sets the image_size of this MapImageDto.


        :param image_size: The image_size of this MapImageDto.  # noqa: E501
        :type: int
        """

        self._image_size = image_size

    @property
    def name(self):
        """Gets the name of this MapImageDto.  # noqa: E501


        :return: The name of this MapImageDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MapImageDto.


        :param name: The name of this MapImageDto.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(MapImageDto, dict):
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
        if not isinstance(other, MapImageDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other