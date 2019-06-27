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


class NetFlowFilterEntityCreateDto(object):
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
        'field_id': 'int',
        'is_negated': 'bool',
        'operation': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'field_id': 'fieldId',
        'is_negated': 'isNegated',
        'operation': 'operation',
        'values': 'values'
    }

    def __init__(self, field_id=None, is_negated=None, operation=None, values=None):  # noqa: E501
        """NetFlowFilterEntityCreateDto - a model defined in Swagger"""  # noqa: E501

        self._field_id = None
        self._is_negated = None
        self._operation = None
        self._values = None
        self.discriminator = None

        if field_id is not None:
            self.field_id = field_id
        if is_negated is not None:
            self.is_negated = is_negated
        if operation is not None:
            self.operation = operation
        if values is not None:
            self.values = values

    @property
    def field_id(self):
        """Gets the field_id of this NetFlowFilterEntityCreateDto.  # noqa: E501


        :return: The field_id of this NetFlowFilterEntityCreateDto.  # noqa: E501
        :rtype: int
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this NetFlowFilterEntityCreateDto.


        :param field_id: The field_id of this NetFlowFilterEntityCreateDto.  # noqa: E501
        :type: int
        """

        self._field_id = field_id

    @property
    def is_negated(self):
        """Gets the is_negated of this NetFlowFilterEntityCreateDto.  # noqa: E501


        :return: The is_negated of this NetFlowFilterEntityCreateDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_negated

    @is_negated.setter
    def is_negated(self, is_negated):
        """Sets the is_negated of this NetFlowFilterEntityCreateDto.


        :param is_negated: The is_negated of this NetFlowFilterEntityCreateDto.  # noqa: E501
        :type: bool
        """

        self._is_negated = is_negated

    @property
    def operation(self):
        """Gets the operation of this NetFlowFilterEntityCreateDto.  # noqa: E501


        :return: The operation of this NetFlowFilterEntityCreateDto.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this NetFlowFilterEntityCreateDto.


        :param operation: The operation of this NetFlowFilterEntityCreateDto.  # noqa: E501
        :type: str
        """

        self._operation = operation

    @property
    def values(self):
        """Gets the values of this NetFlowFilterEntityCreateDto.  # noqa: E501


        :return: The values of this NetFlowFilterEntityCreateDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this NetFlowFilterEntityCreateDto.


        :param values: The values of this NetFlowFilterEntityCreateDto.  # noqa: E501
        :type: list[str]
        """

        self._values = values

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
        if issubclass(NetFlowFilterEntityCreateDto, dict):
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
        if not isinstance(other, NetFlowFilterEntityCreateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
