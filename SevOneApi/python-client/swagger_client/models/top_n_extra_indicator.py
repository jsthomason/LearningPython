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

from swagger_client.models.top_n_data_dto import TopNDataDto  # noqa: F401,E501


class TopNExtraIndicator(object):
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
        'data': 'list[TopNDataDto]',
        'indicator_alias': 'str',
        'indicator_id': 'int',
        'indicator_type_description': 'str',
        'indicator_type_id': 'int',
        'unit': 'str'
    }

    attribute_map = {
        'data': 'data',
        'indicator_alias': 'indicatorAlias',
        'indicator_id': 'indicatorId',
        'indicator_type_description': 'indicatorTypeDescription',
        'indicator_type_id': 'indicatorTypeId',
        'unit': 'unit'
    }

    def __init__(self, data=None, indicator_alias=None, indicator_id=None, indicator_type_description=None, indicator_type_id=None, unit=None):  # noqa: E501
        """TopNExtraIndicator - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._indicator_alias = None
        self._indicator_id = None
        self._indicator_type_description = None
        self._indicator_type_id = None
        self._unit = None
        self.discriminator = None

        self.data = data
        self.indicator_alias = indicator_alias
        self.indicator_id = indicator_id
        self.indicator_type_description = indicator_type_description
        self.indicator_type_id = indicator_type_id
        self.unit = unit

    @property
    def data(self):
        """Gets the data of this TopNExtraIndicator.  # noqa: E501


        :return: The data of this TopNExtraIndicator.  # noqa: E501
        :rtype: list[TopNDataDto]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TopNExtraIndicator.


        :param data: The data of this TopNExtraIndicator.  # noqa: E501
        :type: list[TopNDataDto]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def indicator_alias(self):
        """Gets the indicator_alias of this TopNExtraIndicator.  # noqa: E501


        :return: The indicator_alias of this TopNExtraIndicator.  # noqa: E501
        :rtype: str
        """
        return self._indicator_alias

    @indicator_alias.setter
    def indicator_alias(self, indicator_alias):
        """Sets the indicator_alias of this TopNExtraIndicator.


        :param indicator_alias: The indicator_alias of this TopNExtraIndicator.  # noqa: E501
        :type: str
        """
        if indicator_alias is None:
            raise ValueError("Invalid value for `indicator_alias`, must not be `None`")  # noqa: E501

        self._indicator_alias = indicator_alias

    @property
    def indicator_id(self):
        """Gets the indicator_id of this TopNExtraIndicator.  # noqa: E501


        :return: The indicator_id of this TopNExtraIndicator.  # noqa: E501
        :rtype: int
        """
        return self._indicator_id

    @indicator_id.setter
    def indicator_id(self, indicator_id):
        """Sets the indicator_id of this TopNExtraIndicator.


        :param indicator_id: The indicator_id of this TopNExtraIndicator.  # noqa: E501
        :type: int
        """
        if indicator_id is None:
            raise ValueError("Invalid value for `indicator_id`, must not be `None`")  # noqa: E501

        self._indicator_id = indicator_id

    @property
    def indicator_type_description(self):
        """Gets the indicator_type_description of this TopNExtraIndicator.  # noqa: E501


        :return: The indicator_type_description of this TopNExtraIndicator.  # noqa: E501
        :rtype: str
        """
        return self._indicator_type_description

    @indicator_type_description.setter
    def indicator_type_description(self, indicator_type_description):
        """Sets the indicator_type_description of this TopNExtraIndicator.


        :param indicator_type_description: The indicator_type_description of this TopNExtraIndicator.  # noqa: E501
        :type: str
        """
        if indicator_type_description is None:
            raise ValueError("Invalid value for `indicator_type_description`, must not be `None`")  # noqa: E501

        self._indicator_type_description = indicator_type_description

    @property
    def indicator_type_id(self):
        """Gets the indicator_type_id of this TopNExtraIndicator.  # noqa: E501


        :return: The indicator_type_id of this TopNExtraIndicator.  # noqa: E501
        :rtype: int
        """
        return self._indicator_type_id

    @indicator_type_id.setter
    def indicator_type_id(self, indicator_type_id):
        """Sets the indicator_type_id of this TopNExtraIndicator.


        :param indicator_type_id: The indicator_type_id of this TopNExtraIndicator.  # noqa: E501
        :type: int
        """
        if indicator_type_id is None:
            raise ValueError("Invalid value for `indicator_type_id`, must not be `None`")  # noqa: E501

        self._indicator_type_id = indicator_type_id

    @property
    def unit(self):
        """Gets the unit of this TopNExtraIndicator.  # noqa: E501


        :return: The unit of this TopNExtraIndicator.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this TopNExtraIndicator.


        :param unit: The unit of this TopNExtraIndicator.  # noqa: E501
        :type: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

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
        if issubclass(TopNExtraIndicator, dict):
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
        if not isinstance(other, TopNExtraIndicator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
