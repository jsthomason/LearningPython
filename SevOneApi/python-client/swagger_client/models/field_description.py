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


class FieldDescription(object):
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
        'aggregation': 'str',
        'data_units': 'str',
        'field': 'int',
        'field_type': 'str',
        'is_rate': 'bool',
        'key': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'aggregation': 'aggregation',
        'data_units': 'dataUnits',
        'field': 'field',
        'field_type': 'fieldType',
        'is_rate': 'isRate',
        'key': 'key',
        'name': 'name'
    }

    def __init__(self, aggregation=None, data_units=None, field=None, field_type=None, is_rate=None, key=None, name=None):  # noqa: E501
        """FieldDescription - a model defined in Swagger"""  # noqa: E501

        self._aggregation = None
        self._data_units = None
        self._field = None
        self._field_type = None
        self._is_rate = None
        self._key = None
        self._name = None
        self.discriminator = None

        if aggregation is not None:
            self.aggregation = aggregation
        if data_units is not None:
            self.data_units = data_units
        if field is not None:
            self.field = field
        if field_type is not None:
            self.field_type = field_type
        if is_rate is not None:
            self.is_rate = is_rate
        if key is not None:
            self.key = key
        if name is not None:
            self.name = name

    @property
    def aggregation(self):
        """Gets the aggregation of this FieldDescription.  # noqa: E501


        :return: The aggregation of this FieldDescription.  # noqa: E501
        :rtype: str
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """Sets the aggregation of this FieldDescription.


        :param aggregation: The aggregation of this FieldDescription.  # noqa: E501
        :type: str
        """

        self._aggregation = aggregation

    @property
    def data_units(self):
        """Gets the data_units of this FieldDescription.  # noqa: E501


        :return: The data_units of this FieldDescription.  # noqa: E501
        :rtype: str
        """
        return self._data_units

    @data_units.setter
    def data_units(self, data_units):
        """Sets the data_units of this FieldDescription.


        :param data_units: The data_units of this FieldDescription.  # noqa: E501
        :type: str
        """

        self._data_units = data_units

    @property
    def field(self):
        """Gets the field of this FieldDescription.  # noqa: E501


        :return: The field of this FieldDescription.  # noqa: E501
        :rtype: int
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this FieldDescription.


        :param field: The field of this FieldDescription.  # noqa: E501
        :type: int
        """

        self._field = field

    @property
    def field_type(self):
        """Gets the field_type of this FieldDescription.  # noqa: E501


        :return: The field_type of this FieldDescription.  # noqa: E501
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this FieldDescription.


        :param field_type: The field_type of this FieldDescription.  # noqa: E501
        :type: str
        """

        self._field_type = field_type

    @property
    def is_rate(self):
        """Gets the is_rate of this FieldDescription.  # noqa: E501


        :return: The is_rate of this FieldDescription.  # noqa: E501
        :rtype: bool
        """
        return self._is_rate

    @is_rate.setter
    def is_rate(self, is_rate):
        """Sets the is_rate of this FieldDescription.


        :param is_rate: The is_rate of this FieldDescription.  # noqa: E501
        :type: bool
        """

        self._is_rate = is_rate

    @property
    def key(self):
        """Gets the key of this FieldDescription.  # noqa: E501


        :return: The key of this FieldDescription.  # noqa: E501
        :rtype: bool
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this FieldDescription.


        :param key: The key of this FieldDescription.  # noqa: E501
        :type: bool
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this FieldDescription.  # noqa: E501


        :return: The name of this FieldDescription.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FieldDescription.


        :param name: The name of this FieldDescription.  # noqa: E501
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
        if issubclass(FieldDescription, dict):
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
        if not isinstance(other, FieldDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
