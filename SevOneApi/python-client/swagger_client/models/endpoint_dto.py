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


class EndpointDto(object):
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
        'methods': 'list[str]',
        'path': 'str'
    }

    attribute_map = {
        'methods': 'methods',
        'path': 'path'
    }

    def __init__(self, methods=None, path=None):  # noqa: E501
        """EndpointDto - a model defined in Swagger"""  # noqa: E501

        self._methods = None
        self._path = None
        self.discriminator = None

        if methods is not None:
            self.methods = methods
        if path is not None:
            self.path = path

    @property
    def methods(self):
        """Gets the methods of this EndpointDto.  # noqa: E501


        :return: The methods of this EndpointDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this EndpointDto.


        :param methods: The methods of this EndpointDto.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["GET", "HEAD", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "TRACE"]  # noqa: E501
        if not set(methods).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `methods` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(methods) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._methods = methods

    @property
    def path(self):
        """Gets the path of this EndpointDto.  # noqa: E501


        :return: The path of this EndpointDto.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this EndpointDto.


        :param path: The path of this EndpointDto.  # noqa: E501
        :type: str
        """

        self._path = path

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
        if issubclass(EndpointDto, dict):
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
        if not isinstance(other, EndpointDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
