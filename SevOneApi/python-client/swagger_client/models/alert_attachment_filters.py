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

from swagger_client.models.filter_schema_details import FilterSchemaDetails  # noqa: F401,E501


class AlertAttachmentFilters(object):
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
        'alert_id': 'FilterSchemaDetails',
        'alert_types': 'FilterSchemaDetails',
        'assigned_to': 'FilterSchemaDetails',
        'is_closed': 'FilterSchemaDetails',
        'message': 'FilterSchemaDetails',
        'policy_id': 'FilterSchemaDetails',
        'severity': 'FilterSchemaDetails',
        'show_ignored': 'FilterSchemaDetails',
        'threshold_id': 'FilterSchemaDetails'
    }

    attribute_map = {
        'alert_id': 'alertId',
        'alert_types': 'alertTypes',
        'assigned_to': 'assignedTo',
        'is_closed': 'isClosed',
        'message': 'message',
        'policy_id': 'policyId',
        'severity': 'severity',
        'show_ignored': 'showIgnored',
        'threshold_id': 'thresholdId'
    }

    def __init__(self, alert_id=None, alert_types=None, assigned_to=None, is_closed=None, message=None, policy_id=None, severity=None, show_ignored=None, threshold_id=None):  # noqa: E501
        """AlertAttachmentFilters - a model defined in Swagger"""  # noqa: E501

        self._alert_id = None
        self._alert_types = None
        self._assigned_to = None
        self._is_closed = None
        self._message = None
        self._policy_id = None
        self._severity = None
        self._show_ignored = None
        self._threshold_id = None
        self.discriminator = None

        if alert_id is not None:
            self.alert_id = alert_id
        if alert_types is not None:
            self.alert_types = alert_types
        if assigned_to is not None:
            self.assigned_to = assigned_to
        if is_closed is not None:
            self.is_closed = is_closed
        if message is not None:
            self.message = message
        if policy_id is not None:
            self.policy_id = policy_id
        if severity is not None:
            self.severity = severity
        if show_ignored is not None:
            self.show_ignored = show_ignored
        if threshold_id is not None:
            self.threshold_id = threshold_id

    @property
    def alert_id(self):
        """Gets the alert_id of this AlertAttachmentFilters.  # noqa: E501


        :return: The alert_id of this AlertAttachmentFilters.  # noqa: E501
        :rtype: FilterSchemaDetails
        """
        return self._alert_id

    @alert_id.setter
    def alert_id(self, alert_id):
        """Sets the alert_id of this AlertAttachmentFilters.


        :param alert_id: The alert_id of this AlertAttachmentFilters.  # noqa: E501
        :type: FilterSchemaDetails
        """

        self._alert_id = alert_id

    @property
    def alert_types(self):
        """Gets the alert_types of this AlertAttachmentFilters.  # noqa: E501


        :return: The alert_types of this AlertAttachmentFilters.  # noqa: E501
        :rtype: FilterSchemaDetails
        """
        return self._alert_types

    @alert_types.setter
    def alert_types(self, alert_types):
        """Sets the alert_types of this AlertAttachmentFilters.


        :param alert_types: The alert_types of this AlertAttachmentFilters.  # noqa: E501
        :type: FilterSchemaDetails
        """

        self._alert_types = alert_types

    @property
    def assigned_to(self):
        """Gets the assigned_to of this AlertAttachmentFilters.  # noqa: E501


        :return: The assigned_to of this AlertAttachmentFilters.  # noqa: E501
        :rtype: FilterSchemaDetails
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """Sets the assigned_to of this AlertAttachmentFilters.


        :param assigned_to: The assigned_to of this AlertAttachmentFilters.  # noqa: E501
        :type: FilterSchemaDetails
        """

        self._assigned_to = assigned_to

    @property
    def is_closed(self):
        """Gets the is_closed of this AlertAttachmentFilters.  # noqa: E501


        :return: The is_closed of this AlertAttachmentFilters.  # noqa: E501
        :rtype: FilterSchemaDetails
        """
        return self._is_closed

    @is_closed.setter
    def is_closed(self, is_closed):
        """Sets the is_closed of this AlertAttachmentFilters.


        :param is_closed: The is_closed of this AlertAttachmentFilters.  # noqa: E501
        :type: FilterSchemaDetails
        """

        self._is_closed = is_closed

    @property
    def message(self):
        """Gets the message of this AlertAttachmentFilters.  # noqa: E501


        :return: The message of this AlertAttachmentFilters.  # noqa: E501
        :rtype: FilterSchemaDetails
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AlertAttachmentFilters.


        :param message: The message of this AlertAttachmentFilters.  # noqa: E501
        :type: FilterSchemaDetails
        """

        self._message = message

    @property
    def policy_id(self):
        """Gets the policy_id of this AlertAttachmentFilters.  # noqa: E501


        :return: The policy_id of this AlertAttachmentFilters.  # noqa: E501
        :rtype: FilterSchemaDetails
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this AlertAttachmentFilters.


        :param policy_id: The policy_id of this AlertAttachmentFilters.  # noqa: E501
        :type: FilterSchemaDetails
        """

        self._policy_id = policy_id

    @property
    def severity(self):
        """Gets the severity of this AlertAttachmentFilters.  # noqa: E501


        :return: The severity of this AlertAttachmentFilters.  # noqa: E501
        :rtype: FilterSchemaDetails
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this AlertAttachmentFilters.


        :param severity: The severity of this AlertAttachmentFilters.  # noqa: E501
        :type: FilterSchemaDetails
        """

        self._severity = severity

    @property
    def show_ignored(self):
        """Gets the show_ignored of this AlertAttachmentFilters.  # noqa: E501


        :return: The show_ignored of this AlertAttachmentFilters.  # noqa: E501
        :rtype: FilterSchemaDetails
        """
        return self._show_ignored

    @show_ignored.setter
    def show_ignored(self, show_ignored):
        """Sets the show_ignored of this AlertAttachmentFilters.


        :param show_ignored: The show_ignored of this AlertAttachmentFilters.  # noqa: E501
        :type: FilterSchemaDetails
        """

        self._show_ignored = show_ignored

    @property
    def threshold_id(self):
        """Gets the threshold_id of this AlertAttachmentFilters.  # noqa: E501


        :return: The threshold_id of this AlertAttachmentFilters.  # noqa: E501
        :rtype: FilterSchemaDetails
        """
        return self._threshold_id

    @threshold_id.setter
    def threshold_id(self, threshold_id):
        """Sets the threshold_id of this AlertAttachmentFilters.


        :param threshold_id: The threshold_id of this AlertAttachmentFilters.  # noqa: E501
        :type: FilterSchemaDetails
        """

        self._threshold_id = threshold_id

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
        if issubclass(AlertAttachmentFilters, dict):
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
        if not isinstance(other, AlertAttachmentFilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other