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

from swagger_client.models.timespan_between import TimespanBetween  # noqa: F401,E501


class AlertFilterDto(object):
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
        'acknowledged_by': 'str',
        'assigned_to': 'list[int]',
        'clear_message': 'str',
        'closed': 'int',
        'closed_key': 'int',
        'comments': 'str',
        'device_id': 'list[int]',
        'end_time': 'int',
        'id': 'int',
        'ids': 'list[int]',
        'ignore_comment': 'str',
        'ignore_uid': 'int',
        'ignore_until': 'int',
        'indicator_id': 'list[int]',
        'is_maintenance_alert': 'bool',
        'last_processed': 'int',
        'message': 'str',
        'number': 'int',
        'object_id': 'list[int]',
        'origin': 'str',
        'plugin_name': 'str',
        'poll_id': 'list[int]',
        'severity': 'int',
        'start_time': 'int',
        'threshold_id': 'list[int]',
        'timespan_between': 'TimespanBetween'
    }

    attribute_map = {
        'acknowledged_by': 'acknowledgedBy',
        'assigned_to': 'assignedTo',
        'clear_message': 'clearMessage',
        'closed': 'closed',
        'closed_key': 'closedKey',
        'comments': 'comments',
        'device_id': 'deviceId',
        'end_time': 'endTime',
        'id': 'id',
        'ids': 'ids',
        'ignore_comment': 'ignoreComment',
        'ignore_uid': 'ignoreUid',
        'ignore_until': 'ignoreUntil',
        'indicator_id': 'indicatorId',
        'is_maintenance_alert': 'isMaintenanceAlert',
        'last_processed': 'lastProcessed',
        'message': 'message',
        'number': 'number',
        'object_id': 'objectId',
        'origin': 'origin',
        'plugin_name': 'pluginName',
        'poll_id': 'pollId',
        'severity': 'severity',
        'start_time': 'startTime',
        'threshold_id': 'thresholdId',
        'timespan_between': 'timespanBetween'
    }

    def __init__(self, acknowledged_by=None, assigned_to=None, clear_message=None, closed=None, closed_key=None, comments=None, device_id=None, end_time=None, id=None, ids=None, ignore_comment=None, ignore_uid=None, ignore_until=None, indicator_id=None, is_maintenance_alert=None, last_processed=None, message=None, number=None, object_id=None, origin=None, plugin_name=None, poll_id=None, severity=None, start_time=None, threshold_id=None, timespan_between=None):  # noqa: E501
        """AlertFilterDto - a model defined in Swagger"""  # noqa: E501

        self._acknowledged_by = None
        self._assigned_to = None
        self._clear_message = None
        self._closed = None
        self._closed_key = None
        self._comments = None
        self._device_id = None
        self._end_time = None
        self._id = None
        self._ids = None
        self._ignore_comment = None
        self._ignore_uid = None
        self._ignore_until = None
        self._indicator_id = None
        self._is_maintenance_alert = None
        self._last_processed = None
        self._message = None
        self._number = None
        self._object_id = None
        self._origin = None
        self._plugin_name = None
        self._poll_id = None
        self._severity = None
        self._start_time = None
        self._threshold_id = None
        self._timespan_between = None
        self.discriminator = None

        if acknowledged_by is not None:
            self.acknowledged_by = acknowledged_by
        if assigned_to is not None:
            self.assigned_to = assigned_to
        if clear_message is not None:
            self.clear_message = clear_message
        if closed is not None:
            self.closed = closed
        if closed_key is not None:
            self.closed_key = closed_key
        if comments is not None:
            self.comments = comments
        if device_id is not None:
            self.device_id = device_id
        if end_time is not None:
            self.end_time = end_time
        if id is not None:
            self.id = id
        if ids is not None:
            self.ids = ids
        if ignore_comment is not None:
            self.ignore_comment = ignore_comment
        if ignore_uid is not None:
            self.ignore_uid = ignore_uid
        if ignore_until is not None:
            self.ignore_until = ignore_until
        if indicator_id is not None:
            self.indicator_id = indicator_id
        if is_maintenance_alert is not None:
            self.is_maintenance_alert = is_maintenance_alert
        if last_processed is not None:
            self.last_processed = last_processed
        if message is not None:
            self.message = message
        if number is not None:
            self.number = number
        if object_id is not None:
            self.object_id = object_id
        if origin is not None:
            self.origin = origin
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if poll_id is not None:
            self.poll_id = poll_id
        if severity is not None:
            self.severity = severity
        if start_time is not None:
            self.start_time = start_time
        if threshold_id is not None:
            self.threshold_id = threshold_id
        if timespan_between is not None:
            self.timespan_between = timespan_between

    @property
    def acknowledged_by(self):
        """Gets the acknowledged_by of this AlertFilterDto.  # noqa: E501


        :return: The acknowledged_by of this AlertFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._acknowledged_by

    @acknowledged_by.setter
    def acknowledged_by(self, acknowledged_by):
        """Sets the acknowledged_by of this AlertFilterDto.


        :param acknowledged_by: The acknowledged_by of this AlertFilterDto.  # noqa: E501
        :type: str
        """

        self._acknowledged_by = acknowledged_by

    @property
    def assigned_to(self):
        """Gets the assigned_to of this AlertFilterDto.  # noqa: E501


        :return: The assigned_to of this AlertFilterDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """Sets the assigned_to of this AlertFilterDto.


        :param assigned_to: The assigned_to of this AlertFilterDto.  # noqa: E501
        :type: list[int]
        """

        self._assigned_to = assigned_to

    @property
    def clear_message(self):
        """Gets the clear_message of this AlertFilterDto.  # noqa: E501


        :return: The clear_message of this AlertFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._clear_message

    @clear_message.setter
    def clear_message(self, clear_message):
        """Sets the clear_message of this AlertFilterDto.


        :param clear_message: The clear_message of this AlertFilterDto.  # noqa: E501
        :type: str
        """

        self._clear_message = clear_message

    @property
    def closed(self):
        """Gets the closed of this AlertFilterDto.  # noqa: E501


        :return: The closed of this AlertFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this AlertFilterDto.


        :param closed: The closed of this AlertFilterDto.  # noqa: E501
        :type: int
        """

        self._closed = closed

    @property
    def closed_key(self):
        """Gets the closed_key of this AlertFilterDto.  # noqa: E501


        :return: The closed_key of this AlertFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._closed_key

    @closed_key.setter
    def closed_key(self, closed_key):
        """Sets the closed_key of this AlertFilterDto.


        :param closed_key: The closed_key of this AlertFilterDto.  # noqa: E501
        :type: int
        """

        self._closed_key = closed_key

    @property
    def comments(self):
        """Gets the comments of this AlertFilterDto.  # noqa: E501


        :return: The comments of this AlertFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this AlertFilterDto.


        :param comments: The comments of this AlertFilterDto.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def device_id(self):
        """Gets the device_id of this AlertFilterDto.  # noqa: E501


        :return: The device_id of this AlertFilterDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this AlertFilterDto.


        :param device_id: The device_id of this AlertFilterDto.  # noqa: E501
        :type: list[int]
        """

        self._device_id = device_id

    @property
    def end_time(self):
        """Gets the end_time of this AlertFilterDto.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The end_time of this AlertFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this AlertFilterDto.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param end_time: The end_time of this AlertFilterDto.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def id(self):
        """Gets the id of this AlertFilterDto.  # noqa: E501


        :return: The id of this AlertFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertFilterDto.


        :param id: The id of this AlertFilterDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def ids(self):
        """Gets the ids of this AlertFilterDto.  # noqa: E501


        :return: The ids of this AlertFilterDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this AlertFilterDto.


        :param ids: The ids of this AlertFilterDto.  # noqa: E501
        :type: list[int]
        """

        self._ids = ids

    @property
    def ignore_comment(self):
        """Gets the ignore_comment of this AlertFilterDto.  # noqa: E501


        :return: The ignore_comment of this AlertFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._ignore_comment

    @ignore_comment.setter
    def ignore_comment(self, ignore_comment):
        """Sets the ignore_comment of this AlertFilterDto.


        :param ignore_comment: The ignore_comment of this AlertFilterDto.  # noqa: E501
        :type: str
        """

        self._ignore_comment = ignore_comment

    @property
    def ignore_uid(self):
        """Gets the ignore_uid of this AlertFilterDto.  # noqa: E501


        :return: The ignore_uid of this AlertFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._ignore_uid

    @ignore_uid.setter
    def ignore_uid(self, ignore_uid):
        """Sets the ignore_uid of this AlertFilterDto.


        :param ignore_uid: The ignore_uid of this AlertFilterDto.  # noqa: E501
        :type: int
        """

        self._ignore_uid = ignore_uid

    @property
    def ignore_until(self):
        """Gets the ignore_until of this AlertFilterDto.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The ignore_until of this AlertFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._ignore_until

    @ignore_until.setter
    def ignore_until(self, ignore_until):
        """Sets the ignore_until of this AlertFilterDto.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param ignore_until: The ignore_until of this AlertFilterDto.  # noqa: E501
        :type: int
        """

        self._ignore_until = ignore_until

    @property
    def indicator_id(self):
        """Gets the indicator_id of this AlertFilterDto.  # noqa: E501


        :return: The indicator_id of this AlertFilterDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._indicator_id

    @indicator_id.setter
    def indicator_id(self, indicator_id):
        """Sets the indicator_id of this AlertFilterDto.


        :param indicator_id: The indicator_id of this AlertFilterDto.  # noqa: E501
        :type: list[int]
        """

        self._indicator_id = indicator_id

    @property
    def is_maintenance_alert(self):
        """Gets the is_maintenance_alert of this AlertFilterDto.  # noqa: E501


        :return: The is_maintenance_alert of this AlertFilterDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_maintenance_alert

    @is_maintenance_alert.setter
    def is_maintenance_alert(self, is_maintenance_alert):
        """Sets the is_maintenance_alert of this AlertFilterDto.


        :param is_maintenance_alert: The is_maintenance_alert of this AlertFilterDto.  # noqa: E501
        :type: bool
        """

        self._is_maintenance_alert = is_maintenance_alert

    @property
    def last_processed(self):
        """Gets the last_processed of this AlertFilterDto.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The last_processed of this AlertFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._last_processed

    @last_processed.setter
    def last_processed(self, last_processed):
        """Sets the last_processed of this AlertFilterDto.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param last_processed: The last_processed of this AlertFilterDto.  # noqa: E501
        :type: int
        """

        self._last_processed = last_processed

    @property
    def message(self):
        """Gets the message of this AlertFilterDto.  # noqa: E501


        :return: The message of this AlertFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AlertFilterDto.


        :param message: The message of this AlertFilterDto.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def number(self):
        """Gets the number of this AlertFilterDto.  # noqa: E501


        :return: The number of this AlertFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this AlertFilterDto.


        :param number: The number of this AlertFilterDto.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def object_id(self):
        """Gets the object_id of this AlertFilterDto.  # noqa: E501


        :return: The object_id of this AlertFilterDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this AlertFilterDto.


        :param object_id: The object_id of this AlertFilterDto.  # noqa: E501
        :type: list[int]
        """

        self._object_id = object_id

    @property
    def origin(self):
        """Gets the origin of this AlertFilterDto.  # noqa: E501


        :return: The origin of this AlertFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this AlertFilterDto.


        :param origin: The origin of this AlertFilterDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["system", "trap", "flow"]  # noqa: E501
        if origin not in allowed_values:
            raise ValueError(
                "Invalid value for `origin` ({0}), must be one of {1}"  # noqa: E501
                .format(origin, allowed_values)
            )

        self._origin = origin

    @property
    def plugin_name(self):
        """Gets the plugin_name of this AlertFilterDto.  # noqa: E501


        :return: The plugin_name of this AlertFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this AlertFilterDto.


        :param plugin_name: The plugin_name of this AlertFilterDto.  # noqa: E501
        :type: str
        """

        self._plugin_name = plugin_name

    @property
    def poll_id(self):
        """Gets the poll_id of this AlertFilterDto.  # noqa: E501


        :return: The poll_id of this AlertFilterDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._poll_id

    @poll_id.setter
    def poll_id(self, poll_id):
        """Sets the poll_id of this AlertFilterDto.


        :param poll_id: The poll_id of this AlertFilterDto.  # noqa: E501
        :type: list[int]
        """

        self._poll_id = poll_id

    @property
    def severity(self):
        """Gets the severity of this AlertFilterDto.  # noqa: E501


        :return: The severity of this AlertFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this AlertFilterDto.


        :param severity: The severity of this AlertFilterDto.  # noqa: E501
        :type: int
        """

        self._severity = severity

    @property
    def start_time(self):
        """Gets the start_time of this AlertFilterDto.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The start_time of this AlertFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this AlertFilterDto.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param start_time: The start_time of this AlertFilterDto.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def threshold_id(self):
        """Gets the threshold_id of this AlertFilterDto.  # noqa: E501


        :return: The threshold_id of this AlertFilterDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._threshold_id

    @threshold_id.setter
    def threshold_id(self, threshold_id):
        """Sets the threshold_id of this AlertFilterDto.


        :param threshold_id: The threshold_id of this AlertFilterDto.  # noqa: E501
        :type: list[int]
        """

        self._threshold_id = threshold_id

    @property
    def timespan_between(self):
        """Gets the timespan_between of this AlertFilterDto.  # noqa: E501


        :return: The timespan_between of this AlertFilterDto.  # noqa: E501
        :rtype: TimespanBetween
        """
        return self._timespan_between

    @timespan_between.setter
    def timespan_between(self, timespan_between):
        """Sets the timespan_between of this AlertFilterDto.


        :param timespan_between: The timespan_between of this AlertFilterDto.  # noqa: E501
        :type: TimespanBetween
        """

        self._timespan_between = timespan_between

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
        if issubclass(AlertFilterDto, dict):
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
        if not isinstance(other, AlertFilterDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other