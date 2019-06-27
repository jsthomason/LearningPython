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

from swagger_client.models.mapped_device_group_entity_dto import MappedDeviceGroupEntityDto  # noqa: F401,E501
from swagger_client.models.schedule_instance_dto import ScheduleInstanceDto  # noqa: F401,E501


class MaintenanceWindowDeviceGroupDto(object):
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
        'actions': 'list[str]',
        'id': 'str',
        'maintenance_type': 'str',
        'mapped_entities': 'list[MappedDeviceGroupEntityDto]',
        'name': 'str',
        'notes': 'str',
        'schedule_instance': 'ScheduleInstanceDto'
    }

    attribute_map = {
        'actions': 'actions',
        'id': 'id',
        'maintenance_type': 'maintenanceType',
        'mapped_entities': 'mappedEntities',
        'name': 'name',
        'notes': 'notes',
        'schedule_instance': 'scheduleInstance'
    }

    def __init__(self, actions=None, id=None, maintenance_type=None, mapped_entities=None, name=None, notes=None, schedule_instance=None):  # noqa: E501
        """MaintenanceWindowDeviceGroupDto - a model defined in Swagger"""  # noqa: E501

        self._actions = None
        self._id = None
        self._maintenance_type = None
        self._mapped_entities = None
        self._name = None
        self._notes = None
        self._schedule_instance = None
        self.discriminator = None

        if actions is not None:
            self.actions = actions
        if id is not None:
            self.id = id
        if maintenance_type is not None:
            self.maintenance_type = maintenance_type
        if mapped_entities is not None:
            self.mapped_entities = mapped_entities
        self.name = name
        if notes is not None:
            self.notes = notes
        self.schedule_instance = schedule_instance

    @property
    def actions(self):
        """Gets the actions of this MaintenanceWindowDeviceGroupDto.  # noqa: E501

        List of actions for this maintenance window -- SUPPRESS_ALERT_NOTIFICATIONS (SevOne will not send notification emails or traps for alerts occurring during this maintenance window), CATEGORIZE_ALERTS (Prepend 'Maintenance Window' to alerts overlapping this maintenance window and downgrade severity levels higher than Info), EXCLUDE_DATA_FROM_BASELINES (Exclude data during the maintenance window from baseline calculations), EXCLUDE_DATA_FROM_AGGREGATION (Exclude data during the maintenance window from aggregation calculations)  # noqa: E501

        :return: The actions of this MaintenanceWindowDeviceGroupDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this MaintenanceWindowDeviceGroupDto.

        List of actions for this maintenance window -- SUPPRESS_ALERT_NOTIFICATIONS (SevOne will not send notification emails or traps for alerts occurring during this maintenance window), CATEGORIZE_ALERTS (Prepend 'Maintenance Window' to alerts overlapping this maintenance window and downgrade severity levels higher than Info), EXCLUDE_DATA_FROM_BASELINES (Exclude data during the maintenance window from baseline calculations), EXCLUDE_DATA_FROM_AGGREGATION (Exclude data during the maintenance window from aggregation calculations)  # noqa: E501

        :param actions: The actions of this MaintenanceWindowDeviceGroupDto.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["SUPPRESS_ALERT_NOTIFICATIONS", "CATEGORIZE_ALERTS", "EXCLUDE_DATA_FROM_BASELINES", "EXCLUDE_DATA_FROM_AGGREGATION"]  # noqa: E501
        if not set(actions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `actions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(actions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._actions = actions

    @property
    def id(self):
        """Gets the id of this MaintenanceWindowDeviceGroupDto.  # noqa: E501

        Maintenance window UUID -- omit to auto-generate for POST or leave unchanged for PUT  # noqa: E501

        :return: The id of this MaintenanceWindowDeviceGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MaintenanceWindowDeviceGroupDto.

        Maintenance window UUID -- omit to auto-generate for POST or leave unchanged for PUT  # noqa: E501

        :param id: The id of this MaintenanceWindowDeviceGroupDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def maintenance_type(self):
        """Gets the maintenance_type of this MaintenanceWindowDeviceGroupDto.  # noqa: E501

        Type of maintenance window  # noqa: E501

        :return: The maintenance_type of this MaintenanceWindowDeviceGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_type

    @maintenance_type.setter
    def maintenance_type(self, maintenance_type):
        """Sets the maintenance_type of this MaintenanceWindowDeviceGroupDto.

        Type of maintenance window  # noqa: E501

        :param maintenance_type: The maintenance_type of this MaintenanceWindowDeviceGroupDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["PLANNED"]  # noqa: E501
        if maintenance_type not in allowed_values:
            raise ValueError(
                "Invalid value for `maintenance_type` ({0}), must be one of {1}"  # noqa: E501
                .format(maintenance_type, allowed_values)
            )

        self._maintenance_type = maintenance_type

    @property
    def mapped_entities(self):
        """Gets the mapped_entities of this MaintenanceWindowDeviceGroupDto.  # noqa: E501


        :return: The mapped_entities of this MaintenanceWindowDeviceGroupDto.  # noqa: E501
        :rtype: list[MappedDeviceGroupEntityDto]
        """
        return self._mapped_entities

    @mapped_entities.setter
    def mapped_entities(self, mapped_entities):
        """Sets the mapped_entities of this MaintenanceWindowDeviceGroupDto.


        :param mapped_entities: The mapped_entities of this MaintenanceWindowDeviceGroupDto.  # noqa: E501
        :type: list[MappedDeviceGroupEntityDto]
        """

        self._mapped_entities = mapped_entities

    @property
    def name(self):
        """Gets the name of this MaintenanceWindowDeviceGroupDto.  # noqa: E501

        Name of maintenance window -- must be unique  # noqa: E501

        :return: The name of this MaintenanceWindowDeviceGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MaintenanceWindowDeviceGroupDto.

        Name of maintenance window -- must be unique  # noqa: E501

        :param name: The name of this MaintenanceWindowDeviceGroupDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this MaintenanceWindowDeviceGroupDto.  # noqa: E501

        Free form notes  # noqa: E501

        :return: The notes of this MaintenanceWindowDeviceGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this MaintenanceWindowDeviceGroupDto.

        Free form notes  # noqa: E501

        :param notes: The notes of this MaintenanceWindowDeviceGroupDto.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def schedule_instance(self):
        """Gets the schedule_instance of this MaintenanceWindowDeviceGroupDto.  # noqa: E501

        Maintenance window must be scheduled in the future and have a duration of at least 3 minutes  # noqa: E501

        :return: The schedule_instance of this MaintenanceWindowDeviceGroupDto.  # noqa: E501
        :rtype: ScheduleInstanceDto
        """
        return self._schedule_instance

    @schedule_instance.setter
    def schedule_instance(self, schedule_instance):
        """Sets the schedule_instance of this MaintenanceWindowDeviceGroupDto.

        Maintenance window must be scheduled in the future and have a duration of at least 3 minutes  # noqa: E501

        :param schedule_instance: The schedule_instance of this MaintenanceWindowDeviceGroupDto.  # noqa: E501
        :type: ScheduleInstanceDto
        """
        if schedule_instance is None:
            raise ValueError("Invalid value for `schedule_instance`, must not be `None`")  # noqa: E501

        self._schedule_instance = schedule_instance

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
        if issubclass(MaintenanceWindowDeviceGroupDto, dict):
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
        if not isinstance(other, MaintenanceWindowDeviceGroupDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
