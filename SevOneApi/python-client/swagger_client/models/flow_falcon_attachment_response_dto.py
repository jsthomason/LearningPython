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

from swagger_client.models.flow_falcon_report_response_dto import FlowFalconReportResponseDto  # noqa: F401,E501
from swagger_client.models.time_range_dto import TimeRangeDto  # noqa: F401,E501


class FlowFalconAttachmentResponseDto(object):
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
        'performance_metrics': 'FlowFalconReportResponseDto',
        'time_ranges': 'list[TimeRangeDto]',
        'top_n': 'FlowFalconReportResponseDto'
    }

    attribute_map = {
        'performance_metrics': 'performanceMetrics',
        'time_ranges': 'timeRanges',
        'top_n': 'topN'
    }

    def __init__(self, performance_metrics=None, time_ranges=None, top_n=None):  # noqa: E501
        """FlowFalconAttachmentResponseDto - a model defined in Swagger"""  # noqa: E501

        self._performance_metrics = None
        self._time_ranges = None
        self._top_n = None
        self.discriminator = None

        if performance_metrics is not None:
            self.performance_metrics = performance_metrics
        if time_ranges is not None:
            self.time_ranges = time_ranges
        if top_n is not None:
            self.top_n = top_n

    @property
    def performance_metrics(self):
        """Gets the performance_metrics of this FlowFalconAttachmentResponseDto.  # noqa: E501


        :return: The performance_metrics of this FlowFalconAttachmentResponseDto.  # noqa: E501
        :rtype: FlowFalconReportResponseDto
        """
        return self._performance_metrics

    @performance_metrics.setter
    def performance_metrics(self, performance_metrics):
        """Sets the performance_metrics of this FlowFalconAttachmentResponseDto.


        :param performance_metrics: The performance_metrics of this FlowFalconAttachmentResponseDto.  # noqa: E501
        :type: FlowFalconReportResponseDto
        """

        self._performance_metrics = performance_metrics

    @property
    def time_ranges(self):
        """Gets the time_ranges of this FlowFalconAttachmentResponseDto.  # noqa: E501


        :return: The time_ranges of this FlowFalconAttachmentResponseDto.  # noqa: E501
        :rtype: list[TimeRangeDto]
        """
        return self._time_ranges

    @time_ranges.setter
    def time_ranges(self, time_ranges):
        """Sets the time_ranges of this FlowFalconAttachmentResponseDto.


        :param time_ranges: The time_ranges of this FlowFalconAttachmentResponseDto.  # noqa: E501
        :type: list[TimeRangeDto]
        """

        self._time_ranges = time_ranges

    @property
    def top_n(self):
        """Gets the top_n of this FlowFalconAttachmentResponseDto.  # noqa: E501


        :return: The top_n of this FlowFalconAttachmentResponseDto.  # noqa: E501
        :rtype: FlowFalconReportResponseDto
        """
        return self._top_n

    @top_n.setter
    def top_n(self, top_n):
        """Sets the top_n of this FlowFalconAttachmentResponseDto.


        :param top_n: The top_n of this FlowFalconAttachmentResponseDto.  # noqa: E501
        :type: FlowFalconReportResponseDto
        """

        self._top_n = top_n

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
        if issubclass(FlowFalconAttachmentResponseDto, dict):
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
        if not isinstance(other, FlowFalconAttachmentResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other