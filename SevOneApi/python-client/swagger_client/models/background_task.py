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


class BackgroundTask(object):
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
        'response': 'object',
        'returned': 'bool',
        'status': 'str',
        'task_id': 'str',
        'time_elapsed': 'int'
    }

    attribute_map = {
        'response': 'response',
        'returned': 'returned',
        'status': 'status',
        'task_id': 'taskId',
        'time_elapsed': 'timeElapsed'
    }

    def __init__(self, response=None, returned=None, status=None, task_id=None, time_elapsed=None):  # noqa: E501
        """BackgroundTask - a model defined in Swagger"""  # noqa: E501

        self._response = None
        self._returned = None
        self._status = None
        self._task_id = None
        self._time_elapsed = None
        self.discriminator = None

        if response is not None:
            self.response = response
        if returned is not None:
            self.returned = returned
        if status is not None:
            self.status = status
        if task_id is not None:
            self.task_id = task_id
        if time_elapsed is not None:
            self.time_elapsed = time_elapsed

    @property
    def response(self):
        """Gets the response of this BackgroundTask.  # noqa: E501


        :return: The response of this BackgroundTask.  # noqa: E501
        :rtype: object
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this BackgroundTask.


        :param response: The response of this BackgroundTask.  # noqa: E501
        :type: object
        """

        self._response = response

    @property
    def returned(self):
        """Gets the returned of this BackgroundTask.  # noqa: E501


        :return: The returned of this BackgroundTask.  # noqa: E501
        :rtype: bool
        """
        return self._returned

    @returned.setter
    def returned(self, returned):
        """Sets the returned of this BackgroundTask.


        :param returned: The returned of this BackgroundTask.  # noqa: E501
        :type: bool
        """

        self._returned = returned

    @property
    def status(self):
        """Gets the status of this BackgroundTask.  # noqa: E501


        :return: The status of this BackgroundTask.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BackgroundTask.


        :param status: The status of this BackgroundTask.  # noqa: E501
        :type: str
        """
        allowed_values = ["PENDING", "IN_PROGRESS", "COMPLETED", "ERROR", "CANCELLED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def task_id(self):
        """Gets the task_id of this BackgroundTask.  # noqa: E501


        :return: The task_id of this BackgroundTask.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this BackgroundTask.


        :param task_id: The task_id of this BackgroundTask.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def time_elapsed(self):
        """Gets the time_elapsed of this BackgroundTask.  # noqa: E501


        :return: The time_elapsed of this BackgroundTask.  # noqa: E501
        :rtype: int
        """
        return self._time_elapsed

    @time_elapsed.setter
    def time_elapsed(self, time_elapsed):
        """Sets the time_elapsed of this BackgroundTask.


        :param time_elapsed: The time_elapsed of this BackgroundTask.  # noqa: E501
        :type: int
        """

        self._time_elapsed = time_elapsed

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
        if issubclass(BackgroundTask, dict):
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
        if not isinstance(other, BackgroundTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
