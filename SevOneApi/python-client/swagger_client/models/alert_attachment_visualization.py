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

from swagger_client.models.graph_bar_setting import GraphBarSetting  # noqa: F401,E501
from swagger_client.models.graph_pie_setting import GraphPieSetting  # noqa: F401,E501
from swagger_client.models.visualization_table_setting import VisualizationTableSetting  # noqa: F401,E501


class AlertAttachmentVisualization(object):
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
        'bar': 'GraphBarSetting',
        'pie': 'GraphPieSetting',
        'table': 'VisualizationTableSetting'
    }

    attribute_map = {
        'bar': 'bar',
        'pie': 'pie',
        'table': 'table'
    }

    def __init__(self, bar=None, pie=None, table=None):  # noqa: E501
        """AlertAttachmentVisualization - a model defined in Swagger"""  # noqa: E501

        self._bar = None
        self._pie = None
        self._table = None
        self.discriminator = None

        if bar is not None:
            self.bar = bar
        if pie is not None:
            self.pie = pie
        if table is not None:
            self.table = table

    @property
    def bar(self):
        """Gets the bar of this AlertAttachmentVisualization.  # noqa: E501


        :return: The bar of this AlertAttachmentVisualization.  # noqa: E501
        :rtype: GraphBarSetting
        """
        return self._bar

    @bar.setter
    def bar(self, bar):
        """Sets the bar of this AlertAttachmentVisualization.


        :param bar: The bar of this AlertAttachmentVisualization.  # noqa: E501
        :type: GraphBarSetting
        """

        self._bar = bar

    @property
    def pie(self):
        """Gets the pie of this AlertAttachmentVisualization.  # noqa: E501


        :return: The pie of this AlertAttachmentVisualization.  # noqa: E501
        :rtype: GraphPieSetting
        """
        return self._pie

    @pie.setter
    def pie(self, pie):
        """Sets the pie of this AlertAttachmentVisualization.


        :param pie: The pie of this AlertAttachmentVisualization.  # noqa: E501
        :type: GraphPieSetting
        """

        self._pie = pie

    @property
    def table(self):
        """Gets the table of this AlertAttachmentVisualization.  # noqa: E501


        :return: The table of this AlertAttachmentVisualization.  # noqa: E501
        :rtype: VisualizationTableSetting
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this AlertAttachmentVisualization.


        :param table: The table of this AlertAttachmentVisualization.  # noqa: E501
        :type: VisualizationTableSetting
        """

        self._table = table

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
        if issubclass(AlertAttachmentVisualization, dict):
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
        if not isinstance(other, AlertAttachmentVisualization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
