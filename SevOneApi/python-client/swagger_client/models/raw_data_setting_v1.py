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


class RawDataSettingV1(object):
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
        'fit_time_span_to': 'str',
        'percentiles': 'int',
        'projection_time': 'int',
        'reduce_data': 'bool',
        'standard_deviation': 'int',
        'time_over_time_only': 'bool',
        'time_over_time_type': 'str',
        'time_over_time_units': 'str',
        'time_over_time_value': 'int',
        'trend': 'str',
        'trend_type': 'str',
        'use_baseline': 'bool',
        'use_percentiles': 'str',
        'use_time_over_time': 'bool'
    }

    attribute_map = {
        'fit_time_span_to': 'fitTimeSpanTo',
        'percentiles': 'percentiles',
        'projection_time': 'projectionTime',
        'reduce_data': 'reduceData',
        'standard_deviation': 'standardDeviation',
        'time_over_time_only': 'timeOverTimeOnly',
        'time_over_time_type': 'timeOverTimeType',
        'time_over_time_units': 'timeOverTimeUnits',
        'time_over_time_value': 'timeOverTimeValue',
        'trend': 'trend',
        'trend_type': 'trendType',
        'use_baseline': 'useBaseline',
        'use_percentiles': 'usePercentiles',
        'use_time_over_time': 'useTimeOverTime'
    }

    def __init__(self, fit_time_span_to=None, percentiles=None, projection_time=None, reduce_data=None, standard_deviation=None, time_over_time_only=None, time_over_time_type=None, time_over_time_units=None, time_over_time_value=None, trend=None, trend_type=None, use_baseline=None, use_percentiles=None, use_time_over_time=None):  # noqa: E501
        """RawDataSettingV1 - a model defined in Swagger"""  # noqa: E501

        self._fit_time_span_to = None
        self._percentiles = None
        self._projection_time = None
        self._reduce_data = None
        self._standard_deviation = None
        self._time_over_time_only = None
        self._time_over_time_type = None
        self._time_over_time_units = None
        self._time_over_time_value = None
        self._trend = None
        self._trend_type = None
        self._use_baseline = None
        self._use_percentiles = None
        self._use_time_over_time = None
        self.discriminator = None

        if fit_time_span_to is not None:
            self.fit_time_span_to = fit_time_span_to
        if percentiles is not None:
            self.percentiles = percentiles
        if projection_time is not None:
            self.projection_time = projection_time
        if reduce_data is not None:
            self.reduce_data = reduce_data
        if standard_deviation is not None:
            self.standard_deviation = standard_deviation
        if time_over_time_only is not None:
            self.time_over_time_only = time_over_time_only
        if time_over_time_type is not None:
            self.time_over_time_type = time_over_time_type
        if time_over_time_units is not None:
            self.time_over_time_units = time_over_time_units
        if time_over_time_value is not None:
            self.time_over_time_value = time_over_time_value
        if trend is not None:
            self.trend = trend
        if trend_type is not None:
            self.trend_type = trend_type
        if use_baseline is not None:
            self.use_baseline = use_baseline
        if use_percentiles is not None:
            self.use_percentiles = use_percentiles
        if use_time_over_time is not None:
            self.use_time_over_time = use_time_over_time

    @property
    def fit_time_span_to(self):
        """Gets the fit_time_span_to of this RawDataSettingV1.  # noqa: E501


        :return: The fit_time_span_to of this RawDataSettingV1.  # noqa: E501
        :rtype: str
        """
        return self._fit_time_span_to

    @fit_time_span_to.setter
    def fit_time_span_to(self, fit_time_span_to):
        """Sets the fit_time_span_to of this RawDataSettingV1.


        :param fit_time_span_to: The fit_time_span_to of this RawDataSettingV1.  # noqa: E501
        :type: str
        """
        allowed_values = ["second", "seconds", "minute", "minutes", "hour", "hours", "sixhour", "sixhours", "day", "days", "week", "weeks", "month", "months", "quarter", "quarters", "year", "years"]  # noqa: E501
        if fit_time_span_to not in allowed_values:
            raise ValueError(
                "Invalid value for `fit_time_span_to` ({0}), must be one of {1}"  # noqa: E501
                .format(fit_time_span_to, allowed_values)
            )

        self._fit_time_span_to = fit_time_span_to

    @property
    def percentiles(self):
        """Gets the percentiles of this RawDataSettingV1.  # noqa: E501


        :return: The percentiles of this RawDataSettingV1.  # noqa: E501
        :rtype: int
        """
        return self._percentiles

    @percentiles.setter
    def percentiles(self, percentiles):
        """Sets the percentiles of this RawDataSettingV1.


        :param percentiles: The percentiles of this RawDataSettingV1.  # noqa: E501
        :type: int
        """

        self._percentiles = percentiles

    @property
    def projection_time(self):
        """Gets the projection_time of this RawDataSettingV1.  # noqa: E501


        :return: The projection_time of this RawDataSettingV1.  # noqa: E501
        :rtype: int
        """
        return self._projection_time

    @projection_time.setter
    def projection_time(self, projection_time):
        """Sets the projection_time of this RawDataSettingV1.


        :param projection_time: The projection_time of this RawDataSettingV1.  # noqa: E501
        :type: int
        """

        self._projection_time = projection_time

    @property
    def reduce_data(self):
        """Gets the reduce_data of this RawDataSettingV1.  # noqa: E501


        :return: The reduce_data of this RawDataSettingV1.  # noqa: E501
        :rtype: bool
        """
        return self._reduce_data

    @reduce_data.setter
    def reduce_data(self, reduce_data):
        """Sets the reduce_data of this RawDataSettingV1.


        :param reduce_data: The reduce_data of this RawDataSettingV1.  # noqa: E501
        :type: bool
        """

        self._reduce_data = reduce_data

    @property
    def standard_deviation(self):
        """Gets the standard_deviation of this RawDataSettingV1.  # noqa: E501


        :return: The standard_deviation of this RawDataSettingV1.  # noqa: E501
        :rtype: int
        """
        return self._standard_deviation

    @standard_deviation.setter
    def standard_deviation(self, standard_deviation):
        """Sets the standard_deviation of this RawDataSettingV1.


        :param standard_deviation: The standard_deviation of this RawDataSettingV1.  # noqa: E501
        :type: int
        """

        self._standard_deviation = standard_deviation

    @property
    def time_over_time_only(self):
        """Gets the time_over_time_only of this RawDataSettingV1.  # noqa: E501


        :return: The time_over_time_only of this RawDataSettingV1.  # noqa: E501
        :rtype: bool
        """
        return self._time_over_time_only

    @time_over_time_only.setter
    def time_over_time_only(self, time_over_time_only):
        """Sets the time_over_time_only of this RawDataSettingV1.


        :param time_over_time_only: The time_over_time_only of this RawDataSettingV1.  # noqa: E501
        :type: bool
        """

        self._time_over_time_only = time_over_time_only

    @property
    def time_over_time_type(self):
        """Gets the time_over_time_type of this RawDataSettingV1.  # noqa: E501


        :return: The time_over_time_type of this RawDataSettingV1.  # noqa: E501
        :rtype: str
        """
        return self._time_over_time_type

    @time_over_time_type.setter
    def time_over_time_type(self, time_over_time_type):
        """Sets the time_over_time_type of this RawDataSettingV1.


        :param time_over_time_type: The time_over_time_type of this RawDataSettingV1.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "average", "minimum", "maximum", "total"]  # noqa: E501
        if time_over_time_type not in allowed_values:
            raise ValueError(
                "Invalid value for `time_over_time_type` ({0}), must be one of {1}"  # noqa: E501
                .format(time_over_time_type, allowed_values)
            )

        self._time_over_time_type = time_over_time_type

    @property
    def time_over_time_units(self):
        """Gets the time_over_time_units of this RawDataSettingV1.  # noqa: E501


        :return: The time_over_time_units of this RawDataSettingV1.  # noqa: E501
        :rtype: str
        """
        return self._time_over_time_units

    @time_over_time_units.setter
    def time_over_time_units(self, time_over_time_units):
        """Sets the time_over_time_units of this RawDataSettingV1.


        :param time_over_time_units: The time_over_time_units of this RawDataSettingV1.  # noqa: E501
        :type: str
        """
        allowed_values = ["second", "seconds", "minute", "minutes", "hour", "hours", "sixhour", "sixhours", "day", "days", "week", "weeks", "month", "months", "quarter", "quarters", "year", "years"]  # noqa: E501
        if time_over_time_units not in allowed_values:
            raise ValueError(
                "Invalid value for `time_over_time_units` ({0}), must be one of {1}"  # noqa: E501
                .format(time_over_time_units, allowed_values)
            )

        self._time_over_time_units = time_over_time_units

    @property
    def time_over_time_value(self):
        """Gets the time_over_time_value of this RawDataSettingV1.  # noqa: E501


        :return: The time_over_time_value of this RawDataSettingV1.  # noqa: E501
        :rtype: int
        """
        return self._time_over_time_value

    @time_over_time_value.setter
    def time_over_time_value(self, time_over_time_value):
        """Sets the time_over_time_value of this RawDataSettingV1.


        :param time_over_time_value: The time_over_time_value of this RawDataSettingV1.  # noqa: E501
        :type: int
        """

        self._time_over_time_value = time_over_time_value

    @property
    def trend(self):
        """Gets the trend of this RawDataSettingV1.  # noqa: E501


        :return: The trend of this RawDataSettingV1.  # noqa: E501
        :rtype: str
        """
        return self._trend

    @trend.setter
    def trend(self, trend):
        """Sets the trend of this RawDataSettingV1.


        :param trend: The trend of this RawDataSettingV1.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "standard", "historical", "projected"]  # noqa: E501
        if trend not in allowed_values:
            raise ValueError(
                "Invalid value for `trend` ({0}), must be one of {1}"  # noqa: E501
                .format(trend, allowed_values)
            )

        self._trend = trend

    @property
    def trend_type(self):
        """Gets the trend_type of this RawDataSettingV1.  # noqa: E501


        :return: The trend_type of this RawDataSettingV1.  # noqa: E501
        :rtype: str
        """
        return self._trend_type

    @trend_type.setter
    def trend_type(self, trend_type):
        """Sets the trend_type of this RawDataSettingV1.


        :param trend_type: The trend_type of this RawDataSettingV1.  # noqa: E501
        :type: str
        """
        allowed_values = ["linear", "exponential", "logarithmic", "power", "none"]  # noqa: E501
        if trend_type not in allowed_values:
            raise ValueError(
                "Invalid value for `trend_type` ({0}), must be one of {1}"  # noqa: E501
                .format(trend_type, allowed_values)
            )

        self._trend_type = trend_type

    @property
    def use_baseline(self):
        """Gets the use_baseline of this RawDataSettingV1.  # noqa: E501


        :return: The use_baseline of this RawDataSettingV1.  # noqa: E501
        :rtype: bool
        """
        return self._use_baseline

    @use_baseline.setter
    def use_baseline(self, use_baseline):
        """Sets the use_baseline of this RawDataSettingV1.


        :param use_baseline: The use_baseline of this RawDataSettingV1.  # noqa: E501
        :type: bool
        """

        self._use_baseline = use_baseline

    @property
    def use_percentiles(self):
        """Gets the use_percentiles of this RawDataSettingV1.  # noqa: E501


        :return: The use_percentiles of this RawDataSettingV1.  # noqa: E501
        :rtype: str
        """
        return self._use_percentiles

    @use_percentiles.setter
    def use_percentiles(self, use_percentiles):
        """Sets the use_percentiles of this RawDataSettingV1.


        :param use_percentiles: The use_percentiles of this RawDataSettingV1.  # noqa: E501
        :type: str
        """

        self._use_percentiles = use_percentiles

    @property
    def use_time_over_time(self):
        """Gets the use_time_over_time of this RawDataSettingV1.  # noqa: E501


        :return: The use_time_over_time of this RawDataSettingV1.  # noqa: E501
        :rtype: bool
        """
        return self._use_time_over_time

    @use_time_over_time.setter
    def use_time_over_time(self, use_time_over_time):
        """Sets the use_time_over_time of this RawDataSettingV1.


        :param use_time_over_time: The use_time_over_time of this RawDataSettingV1.  # noqa: E501
        :type: bool
        """

        self._use_time_over_time = use_time_over_time

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
        if issubclass(RawDataSettingV1, dict):
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
        if not isinstance(other, RawDataSettingV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
