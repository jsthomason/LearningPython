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


class TelephonyAttachmentAggregationV1(object):
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
        'aggregation': 'str'
    }

    attribute_map = {
        'aggregation': 'aggregation'
    }

    def __init__(self, aggregation=None):  # noqa: E501
        """TelephonyAttachmentAggregationV1 - a model defined in Swagger"""  # noqa: E501

        self._aggregation = None
        self.discriminator = None

        if aggregation is not None:
            self.aggregation = aggregation

    @property
    def aggregation(self):
        """Gets the aggregation of this TelephonyAttachmentAggregationV1.  # noqa: E501


        :return: The aggregation of this TelephonyAttachmentAggregationV1.  # noqa: E501
        :rtype: str
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """Sets the aggregation of this TelephonyAttachmentAggregationV1.


        :param aggregation: The aggregation of this TelephonyAttachmentAggregationV1.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Destination", "DestinationCodec", "DestinationIP", "DestinationPhone", "DestinationPool", "PBXName", "Source", "SourceCodec", "SourceIP", "SourcePhone", "SourcePool", "Domain"]  # noqa: E501
        if aggregation not in allowed_values:
            raise ValueError(
                "Invalid value for `aggregation` ({0}), must be one of {1}"  # noqa: E501
                .format(aggregation, allowed_values)
            )

        self._aggregation = aggregation

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
        if issubclass(TelephonyAttachmentAggregationV1, dict):
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
        if not isinstance(other, TelephonyAttachmentAggregationV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
