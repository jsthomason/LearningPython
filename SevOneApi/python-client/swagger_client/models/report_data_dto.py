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

from swagger_client.models.data_point_dto import DataPointDto  # noqa: F401,E501


class ReportDataDto(object):
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
        'avg_y': 'float',
        'data': 'list[DataPointDto]',
        'max_x': 'int',
        'max_y': 'float',
        'max_y_cap': 'float',
        'min_x': 'int',
        'min_y': 'float',
        'percentiles': 'float',
        'post_data': 'DataPointDto',
        'pre_data': 'DataPointDto',
        'total': 'float',
        'trend_value_a': 'float',
        'trend_value_b': 'float',
        'unit': 'str'
    }

    attribute_map = {
        'avg_y': 'avgY',
        'data': 'data',
        'max_x': 'maxX',
        'max_y': 'maxY',
        'max_y_cap': 'maxYCap',
        'min_x': 'minX',
        'min_y': 'minY',
        'percentiles': 'percentiles',
        'post_data': 'postData',
        'pre_data': 'preData',
        'total': 'total',
        'trend_value_a': 'trendValueA',
        'trend_value_b': 'trendValueB',
        'unit': 'unit'
    }

    def __init__(self, avg_y=None, data=None, max_x=None, max_y=None, max_y_cap=None, min_x=None, min_y=None, percentiles=None, post_data=None, pre_data=None, total=None, trend_value_a=None, trend_value_b=None, unit=None):  # noqa: E501
        """ReportDataDto - a model defined in Swagger"""  # noqa: E501

        self._avg_y = None
        self._data = None
        self._max_x = None
        self._max_y = None
        self._max_y_cap = None
        self._min_x = None
        self._min_y = None
        self._percentiles = None
        self._post_data = None
        self._pre_data = None
        self._total = None
        self._trend_value_a = None
        self._trend_value_b = None
        self._unit = None
        self.discriminator = None

        if avg_y is not None:
            self.avg_y = avg_y
        if data is not None:
            self.data = data
        if max_x is not None:
            self.max_x = max_x
        if max_y is not None:
            self.max_y = max_y
        if max_y_cap is not None:
            self.max_y_cap = max_y_cap
        if min_x is not None:
            self.min_x = min_x
        if min_y is not None:
            self.min_y = min_y
        if percentiles is not None:
            self.percentiles = percentiles
        if post_data is not None:
            self.post_data = post_data
        if pre_data is not None:
            self.pre_data = pre_data
        if total is not None:
            self.total = total
        if trend_value_a is not None:
            self.trend_value_a = trend_value_a
        if trend_value_b is not None:
            self.trend_value_b = trend_value_b
        if unit is not None:
            self.unit = unit

    @property
    def avg_y(self):
        """Gets the avg_y of this ReportDataDto.  # noqa: E501


        :return: The avg_y of this ReportDataDto.  # noqa: E501
        :rtype: float
        """
        return self._avg_y

    @avg_y.setter
    def avg_y(self, avg_y):
        """Sets the avg_y of this ReportDataDto.


        :param avg_y: The avg_y of this ReportDataDto.  # noqa: E501
        :type: float
        """

        self._avg_y = avg_y

    @property
    def data(self):
        """Gets the data of this ReportDataDto.  # noqa: E501


        :return: The data of this ReportDataDto.  # noqa: E501
        :rtype: list[DataPointDto]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ReportDataDto.


        :param data: The data of this ReportDataDto.  # noqa: E501
        :type: list[DataPointDto]
        """

        self._data = data

    @property
    def max_x(self):
        """Gets the max_x of this ReportDataDto.  # noqa: E501


        :return: The max_x of this ReportDataDto.  # noqa: E501
        :rtype: int
        """
        return self._max_x

    @max_x.setter
    def max_x(self, max_x):
        """Sets the max_x of this ReportDataDto.


        :param max_x: The max_x of this ReportDataDto.  # noqa: E501
        :type: int
        """

        self._max_x = max_x

    @property
    def max_y(self):
        """Gets the max_y of this ReportDataDto.  # noqa: E501


        :return: The max_y of this ReportDataDto.  # noqa: E501
        :rtype: float
        """
        return self._max_y

    @max_y.setter
    def max_y(self, max_y):
        """Sets the max_y of this ReportDataDto.


        :param max_y: The max_y of this ReportDataDto.  # noqa: E501
        :type: float
        """

        self._max_y = max_y

    @property
    def max_y_cap(self):
        """Gets the max_y_cap of this ReportDataDto.  # noqa: E501


        :return: The max_y_cap of this ReportDataDto.  # noqa: E501
        :rtype: float
        """
        return self._max_y_cap

    @max_y_cap.setter
    def max_y_cap(self, max_y_cap):
        """Sets the max_y_cap of this ReportDataDto.


        :param max_y_cap: The max_y_cap of this ReportDataDto.  # noqa: E501
        :type: float
        """

        self._max_y_cap = max_y_cap

    @property
    def min_x(self):
        """Gets the min_x of this ReportDataDto.  # noqa: E501


        :return: The min_x of this ReportDataDto.  # noqa: E501
        :rtype: int
        """
        return self._min_x

    @min_x.setter
    def min_x(self, min_x):
        """Sets the min_x of this ReportDataDto.


        :param min_x: The min_x of this ReportDataDto.  # noqa: E501
        :type: int
        """

        self._min_x = min_x

    @property
    def min_y(self):
        """Gets the min_y of this ReportDataDto.  # noqa: E501


        :return: The min_y of this ReportDataDto.  # noqa: E501
        :rtype: float
        """
        return self._min_y

    @min_y.setter
    def min_y(self, min_y):
        """Sets the min_y of this ReportDataDto.


        :param min_y: The min_y of this ReportDataDto.  # noqa: E501
        :type: float
        """

        self._min_y = min_y

    @property
    def percentiles(self):
        """Gets the percentiles of this ReportDataDto.  # noqa: E501


        :return: The percentiles of this ReportDataDto.  # noqa: E501
        :rtype: float
        """
        return self._percentiles

    @percentiles.setter
    def percentiles(self, percentiles):
        """Sets the percentiles of this ReportDataDto.


        :param percentiles: The percentiles of this ReportDataDto.  # noqa: E501
        :type: float
        """

        self._percentiles = percentiles

    @property
    def post_data(self):
        """Gets the post_data of this ReportDataDto.  # noqa: E501


        :return: The post_data of this ReportDataDto.  # noqa: E501
        :rtype: DataPointDto
        """
        return self._post_data

    @post_data.setter
    def post_data(self, post_data):
        """Sets the post_data of this ReportDataDto.


        :param post_data: The post_data of this ReportDataDto.  # noqa: E501
        :type: DataPointDto
        """

        self._post_data = post_data

    @property
    def pre_data(self):
        """Gets the pre_data of this ReportDataDto.  # noqa: E501


        :return: The pre_data of this ReportDataDto.  # noqa: E501
        :rtype: DataPointDto
        """
        return self._pre_data

    @pre_data.setter
    def pre_data(self, pre_data):
        """Sets the pre_data of this ReportDataDto.


        :param pre_data: The pre_data of this ReportDataDto.  # noqa: E501
        :type: DataPointDto
        """

        self._pre_data = pre_data

    @property
    def total(self):
        """Gets the total of this ReportDataDto.  # noqa: E501


        :return: The total of this ReportDataDto.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ReportDataDto.


        :param total: The total of this ReportDataDto.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def trend_value_a(self):
        """Gets the trend_value_a of this ReportDataDto.  # noqa: E501


        :return: The trend_value_a of this ReportDataDto.  # noqa: E501
        :rtype: float
        """
        return self._trend_value_a

    @trend_value_a.setter
    def trend_value_a(self, trend_value_a):
        """Sets the trend_value_a of this ReportDataDto.


        :param trend_value_a: The trend_value_a of this ReportDataDto.  # noqa: E501
        :type: float
        """

        self._trend_value_a = trend_value_a

    @property
    def trend_value_b(self):
        """Gets the trend_value_b of this ReportDataDto.  # noqa: E501


        :return: The trend_value_b of this ReportDataDto.  # noqa: E501
        :rtype: float
        """
        return self._trend_value_b

    @trend_value_b.setter
    def trend_value_b(self, trend_value_b):
        """Sets the trend_value_b of this ReportDataDto.


        :param trend_value_b: The trend_value_b of this ReportDataDto.  # noqa: E501
        :type: float
        """

        self._trend_value_b = trend_value_b

    @property
    def unit(self):
        """Gets the unit of this ReportDataDto.  # noqa: E501


        :return: The unit of this ReportDataDto.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ReportDataDto.


        :param unit: The unit of this ReportDataDto.  # noqa: E501
        :type: str
        """

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
        if issubclass(ReportDataDto, dict):
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
        if not isinstance(other, ReportDataDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
