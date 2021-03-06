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


class ReportDto(object):
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
        'description': 'str',
        'email_to': 'str',
        'folder_id': 'int',
        'id': 'int',
        'is_emailed': 'bool',
        'is_ftped': 'bool',
        'is_private': 'bool',
        'is_read_only': 'bool',
        'is_temporary': 'bool',
        'last_accessed': 'int',
        'last_modified': 'int',
        'message': 'str',
        'migrated': 'int',
        'name': 'str',
        'next_run': 'int',
        'number_of_columns': 'int',
        'run_unit': 'str',
        'run_value': 'int',
        'template_type': 'str',
        'timezone': 'str',
        'user_id': 'int',
        'user_role_id': 'int'
    }

    attribute_map = {
        'description': 'description',
        'email_to': 'emailTo',
        'folder_id': 'folderId',
        'id': 'id',
        'is_emailed': 'isEmailed',
        'is_ftped': 'isFtped',
        'is_private': 'isPrivate',
        'is_read_only': 'isReadOnly',
        'is_temporary': 'isTemporary',
        'last_accessed': 'lastAccessed',
        'last_modified': 'lastModified',
        'message': 'message',
        'migrated': 'migrated',
        'name': 'name',
        'next_run': 'nextRun',
        'number_of_columns': 'numberOfColumns',
        'run_unit': 'runUnit',
        'run_value': 'runValue',
        'template_type': 'templateType',
        'timezone': 'timezone',
        'user_id': 'userId',
        'user_role_id': 'userRoleId'
    }

    def __init__(self, description=None, email_to=None, folder_id=None, id=None, is_emailed=None, is_ftped=None, is_private=None, is_read_only=None, is_temporary=None, last_accessed=None, last_modified=None, message=None, migrated=None, name=None, next_run=None, number_of_columns=None, run_unit=None, run_value=None, template_type=None, timezone=None, user_id=None, user_role_id=None):  # noqa: E501
        """ReportDto - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._email_to = None
        self._folder_id = None
        self._id = None
        self._is_emailed = None
        self._is_ftped = None
        self._is_private = None
        self._is_read_only = None
        self._is_temporary = None
        self._last_accessed = None
        self._last_modified = None
        self._message = None
        self._migrated = None
        self._name = None
        self._next_run = None
        self._number_of_columns = None
        self._run_unit = None
        self._run_value = None
        self._template_type = None
        self._timezone = None
        self._user_id = None
        self._user_role_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if email_to is not None:
            self.email_to = email_to
        if folder_id is not None:
            self.folder_id = folder_id
        if id is not None:
            self.id = id
        if is_emailed is not None:
            self.is_emailed = is_emailed
        if is_ftped is not None:
            self.is_ftped = is_ftped
        if is_private is not None:
            self.is_private = is_private
        if is_read_only is not None:
            self.is_read_only = is_read_only
        if is_temporary is not None:
            self.is_temporary = is_temporary
        if last_accessed is not None:
            self.last_accessed = last_accessed
        if last_modified is not None:
            self.last_modified = last_modified
        if message is not None:
            self.message = message
        if migrated is not None:
            self.migrated = migrated
        if name is not None:
            self.name = name
        if next_run is not None:
            self.next_run = next_run
        if number_of_columns is not None:
            self.number_of_columns = number_of_columns
        if run_unit is not None:
            self.run_unit = run_unit
        if run_value is not None:
            self.run_value = run_value
        if template_type is not None:
            self.template_type = template_type
        if timezone is not None:
            self.timezone = timezone
        if user_id is not None:
            self.user_id = user_id
        if user_role_id is not None:
            self.user_role_id = user_role_id

    @property
    def description(self):
        """Gets the description of this ReportDto.  # noqa: E501


        :return: The description of this ReportDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReportDto.


        :param description: The description of this ReportDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def email_to(self):
        """Gets the email_to of this ReportDto.  # noqa: E501


        :return: The email_to of this ReportDto.  # noqa: E501
        :rtype: str
        """
        return self._email_to

    @email_to.setter
    def email_to(self, email_to):
        """Sets the email_to of this ReportDto.


        :param email_to: The email_to of this ReportDto.  # noqa: E501
        :type: str
        """

        self._email_to = email_to

    @property
    def folder_id(self):
        """Gets the folder_id of this ReportDto.  # noqa: E501


        :return: The folder_id of this ReportDto.  # noqa: E501
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this ReportDto.


        :param folder_id: The folder_id of this ReportDto.  # noqa: E501
        :type: int
        """

        self._folder_id = folder_id

    @property
    def id(self):
        """Gets the id of this ReportDto.  # noqa: E501


        :return: The id of this ReportDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReportDto.


        :param id: The id of this ReportDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_emailed(self):
        """Gets the is_emailed of this ReportDto.  # noqa: E501


        :return: The is_emailed of this ReportDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_emailed

    @is_emailed.setter
    def is_emailed(self, is_emailed):
        """Sets the is_emailed of this ReportDto.


        :param is_emailed: The is_emailed of this ReportDto.  # noqa: E501
        :type: bool
        """

        self._is_emailed = is_emailed

    @property
    def is_ftped(self):
        """Gets the is_ftped of this ReportDto.  # noqa: E501


        :return: The is_ftped of this ReportDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_ftped

    @is_ftped.setter
    def is_ftped(self, is_ftped):
        """Sets the is_ftped of this ReportDto.


        :param is_ftped: The is_ftped of this ReportDto.  # noqa: E501
        :type: bool
        """

        self._is_ftped = is_ftped

    @property
    def is_private(self):
        """Gets the is_private of this ReportDto.  # noqa: E501


        :return: The is_private of this ReportDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """Sets the is_private of this ReportDto.


        :param is_private: The is_private of this ReportDto.  # noqa: E501
        :type: bool
        """

        self._is_private = is_private

    @property
    def is_read_only(self):
        """Gets the is_read_only of this ReportDto.  # noqa: E501


        :return: The is_read_only of this ReportDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only):
        """Sets the is_read_only of this ReportDto.


        :param is_read_only: The is_read_only of this ReportDto.  # noqa: E501
        :type: bool
        """

        self._is_read_only = is_read_only

    @property
    def is_temporary(self):
        """Gets the is_temporary of this ReportDto.  # noqa: E501


        :return: The is_temporary of this ReportDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_temporary

    @is_temporary.setter
    def is_temporary(self, is_temporary):
        """Sets the is_temporary of this ReportDto.


        :param is_temporary: The is_temporary of this ReportDto.  # noqa: E501
        :type: bool
        """

        self._is_temporary = is_temporary

    @property
    def last_accessed(self):
        """Gets the last_accessed of this ReportDto.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The last_accessed of this ReportDto.  # noqa: E501
        :rtype: int
        """
        return self._last_accessed

    @last_accessed.setter
    def last_accessed(self, last_accessed):
        """Sets the last_accessed of this ReportDto.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param last_accessed: The last_accessed of this ReportDto.  # noqa: E501
        :type: int
        """

        self._last_accessed = last_accessed

    @property
    def last_modified(self):
        """Gets the last_modified of this ReportDto.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The last_modified of this ReportDto.  # noqa: E501
        :rtype: int
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this ReportDto.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param last_modified: The last_modified of this ReportDto.  # noqa: E501
        :type: int
        """

        self._last_modified = last_modified

    @property
    def message(self):
        """Gets the message of this ReportDto.  # noqa: E501


        :return: The message of this ReportDto.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ReportDto.


        :param message: The message of this ReportDto.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def migrated(self):
        """Gets the migrated of this ReportDto.  # noqa: E501


        :return: The migrated of this ReportDto.  # noqa: E501
        :rtype: int
        """
        return self._migrated

    @migrated.setter
    def migrated(self, migrated):
        """Sets the migrated of this ReportDto.


        :param migrated: The migrated of this ReportDto.  # noqa: E501
        :type: int
        """

        self._migrated = migrated

    @property
    def name(self):
        """Gets the name of this ReportDto.  # noqa: E501


        :return: The name of this ReportDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportDto.


        :param name: The name of this ReportDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def next_run(self):
        """Gets the next_run of this ReportDto.  # noqa: E501


        :return: The next_run of this ReportDto.  # noqa: E501
        :rtype: int
        """
        return self._next_run

    @next_run.setter
    def next_run(self, next_run):
        """Sets the next_run of this ReportDto.


        :param next_run: The next_run of this ReportDto.  # noqa: E501
        :type: int
        """

        self._next_run = next_run

    @property
    def number_of_columns(self):
        """Gets the number_of_columns of this ReportDto.  # noqa: E501


        :return: The number_of_columns of this ReportDto.  # noqa: E501
        :rtype: int
        """
        return self._number_of_columns

    @number_of_columns.setter
    def number_of_columns(self, number_of_columns):
        """Sets the number_of_columns of this ReportDto.


        :param number_of_columns: The number_of_columns of this ReportDto.  # noqa: E501
        :type: int
        """

        self._number_of_columns = number_of_columns

    @property
    def run_unit(self):
        """Gets the run_unit of this ReportDto.  # noqa: E501


        :return: The run_unit of this ReportDto.  # noqa: E501
        :rtype: str
        """
        return self._run_unit

    @run_unit.setter
    def run_unit(self, run_unit):
        """Sets the run_unit of this ReportDto.


        :param run_unit: The run_unit of this ReportDto.  # noqa: E501
        :type: str
        """

        self._run_unit = run_unit

    @property
    def run_value(self):
        """Gets the run_value of this ReportDto.  # noqa: E501


        :return: The run_value of this ReportDto.  # noqa: E501
        :rtype: int
        """
        return self._run_value

    @run_value.setter
    def run_value(self, run_value):
        """Sets the run_value of this ReportDto.


        :param run_value: The run_value of this ReportDto.  # noqa: E501
        :type: int
        """

        self._run_value = run_value

    @property
    def template_type(self):
        """Gets the template_type of this ReportDto.  # noqa: E501


        :return: The template_type of this ReportDto.  # noqa: E501
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this ReportDto.


        :param template_type: The template_type of this ReportDto.  # noqa: E501
        :type: str
        """

        self._template_type = template_type

    @property
    def timezone(self):
        """Gets the timezone of this ReportDto.  # noqa: E501


        :return: The timezone of this ReportDto.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this ReportDto.


        :param timezone: The timezone of this ReportDto.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def user_id(self):
        """Gets the user_id of this ReportDto.  # noqa: E501


        :return: The user_id of this ReportDto.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ReportDto.


        :param user_id: The user_id of this ReportDto.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def user_role_id(self):
        """Gets the user_role_id of this ReportDto.  # noqa: E501


        :return: The user_role_id of this ReportDto.  # noqa: E501
        :rtype: int
        """
        return self._user_role_id

    @user_role_id.setter
    def user_role_id(self, user_role_id):
        """Sets the user_role_id of this ReportDto.


        :param user_role_id: The user_role_id of this ReportDto.  # noqa: E501
        :type: int
        """

        self._user_role_id = user_role_id

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
        if issubclass(ReportDto, dict):
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
        if not isinstance(other, ReportDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
