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

from swagger_client.models.alert_setting import AlertSetting  # noqa: F401,E501
from swagger_client.models.result_limit_setting_v1 import ResultLimitSettingV1  # noqa: F401,E501
from swagger_client.models.source_fields_setting import SourceFieldsSetting  # noqa: F401,E501


class AlertAttachmentSettingsV1(object):
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
        'alert_setting': 'AlertSetting',
        'result_limit_setting': 'ResultLimitSettingV1',
        'source_fields_setting': 'SourceFieldsSetting'
    }

    attribute_map = {
        'alert_setting': 'alertSetting',
        'result_limit_setting': 'resultLimitSetting',
        'source_fields_setting': 'sourceFieldsSetting'
    }

    def __init__(self, alert_setting=None, result_limit_setting=None, source_fields_setting=None):  # noqa: E501
        """AlertAttachmentSettingsV1 - a model defined in Swagger"""  # noqa: E501

        self._alert_setting = None
        self._result_limit_setting = None
        self._source_fields_setting = None
        self.discriminator = None

        if alert_setting is not None:
            self.alert_setting = alert_setting
        if result_limit_setting is not None:
            self.result_limit_setting = result_limit_setting
        if source_fields_setting is not None:
            self.source_fields_setting = source_fields_setting

    @property
    def alert_setting(self):
        """Gets the alert_setting of this AlertAttachmentSettingsV1.  # noqa: E501


        :return: The alert_setting of this AlertAttachmentSettingsV1.  # noqa: E501
        :rtype: AlertSetting
        """
        return self._alert_setting

    @alert_setting.setter
    def alert_setting(self, alert_setting):
        """Sets the alert_setting of this AlertAttachmentSettingsV1.


        :param alert_setting: The alert_setting of this AlertAttachmentSettingsV1.  # noqa: E501
        :type: AlertSetting
        """

        self._alert_setting = alert_setting

    @property
    def result_limit_setting(self):
        """Gets the result_limit_setting of this AlertAttachmentSettingsV1.  # noqa: E501


        :return: The result_limit_setting of this AlertAttachmentSettingsV1.  # noqa: E501
        :rtype: ResultLimitSettingV1
        """
        return self._result_limit_setting

    @result_limit_setting.setter
    def result_limit_setting(self, result_limit_setting):
        """Sets the result_limit_setting of this AlertAttachmentSettingsV1.


        :param result_limit_setting: The result_limit_setting of this AlertAttachmentSettingsV1.  # noqa: E501
        :type: ResultLimitSettingV1
        """

        self._result_limit_setting = result_limit_setting

    @property
    def source_fields_setting(self):
        """Gets the source_fields_setting of this AlertAttachmentSettingsV1.  # noqa: E501


        :return: The source_fields_setting of this AlertAttachmentSettingsV1.  # noqa: E501
        :rtype: SourceFieldsSetting
        """
        return self._source_fields_setting

    @source_fields_setting.setter
    def source_fields_setting(self, source_fields_setting):
        """Sets the source_fields_setting of this AlertAttachmentSettingsV1.


        :param source_fields_setting: The source_fields_setting of this AlertAttachmentSettingsV1.  # noqa: E501
        :type: SourceFieldsSetting
        """

        self._source_fields_setting = source_fields_setting

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
        if issubclass(AlertAttachmentSettingsV1, dict):
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
        if not isinstance(other, AlertAttachmentSettingsV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
