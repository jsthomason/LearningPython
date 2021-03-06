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


class NetFlowInterfaceFilterDto(object):
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
        'allowed': 'bool',
        'description': 'str',
        'ids': 'list[int]',
        'interface_numbers': 'list[int]',
        'name': 'str',
        'netflow_device_ids': 'list[int]',
        'origin_ips': 'list[str]',
        'override_description': 'int',
        'override_name': 'int',
        'override_speed': 'int',
        'peers': 'list[int]',
        'reason': 'str',
        'search_text': 'str',
        'speed': 'int',
        'system_description': 'str',
        'system_name': 'str',
        'system_speed': 'int',
        'visible': 'int'
    }

    attribute_map = {
        'allowed': 'allowed',
        'description': 'description',
        'ids': 'ids',
        'interface_numbers': 'interfaceNumbers',
        'name': 'name',
        'netflow_device_ids': 'netflowDeviceIds',
        'origin_ips': 'originIps',
        'override_description': 'overrideDescription',
        'override_name': 'overrideName',
        'override_speed': 'overrideSpeed',
        'peers': 'peers',
        'reason': 'reason',
        'search_text': 'searchText',
        'speed': 'speed',
        'system_description': 'systemDescription',
        'system_name': 'systemName',
        'system_speed': 'systemSpeed',
        'visible': 'visible'
    }

    def __init__(self, allowed=None, description=None, ids=None, interface_numbers=None, name=None, netflow_device_ids=None, origin_ips=None, override_description=None, override_name=None, override_speed=None, peers=None, reason=None, search_text=None, speed=None, system_description=None, system_name=None, system_speed=None, visible=None):  # noqa: E501
        """NetFlowInterfaceFilterDto - a model defined in Swagger"""  # noqa: E501

        self._allowed = None
        self._description = None
        self._ids = None
        self._interface_numbers = None
        self._name = None
        self._netflow_device_ids = None
        self._origin_ips = None
        self._override_description = None
        self._override_name = None
        self._override_speed = None
        self._peers = None
        self._reason = None
        self._search_text = None
        self._speed = None
        self._system_description = None
        self._system_name = None
        self._system_speed = None
        self._visible = None
        self.discriminator = None

        if allowed is not None:
            self.allowed = allowed
        if description is not None:
            self.description = description
        if ids is not None:
            self.ids = ids
        if interface_numbers is not None:
            self.interface_numbers = interface_numbers
        if name is not None:
            self.name = name
        if netflow_device_ids is not None:
            self.netflow_device_ids = netflow_device_ids
        if origin_ips is not None:
            self.origin_ips = origin_ips
        if override_description is not None:
            self.override_description = override_description
        if override_name is not None:
            self.override_name = override_name
        if override_speed is not None:
            self.override_speed = override_speed
        if peers is not None:
            self.peers = peers
        if reason is not None:
            self.reason = reason
        if search_text is not None:
            self.search_text = search_text
        if speed is not None:
            self.speed = speed
        if system_description is not None:
            self.system_description = system_description
        if system_name is not None:
            self.system_name = system_name
        if system_speed is not None:
            self.system_speed = system_speed
        if visible is not None:
            self.visible = visible

    @property
    def allowed(self):
        """Gets the allowed of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The allowed of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: bool
        """
        return self._allowed

    @allowed.setter
    def allowed(self, allowed):
        """Sets the allowed of this NetFlowInterfaceFilterDto.


        :param allowed: The allowed of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: bool
        """

        self._allowed = allowed

    @property
    def description(self):
        """Gets the description of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The description of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NetFlowInterfaceFilterDto.


        :param description: The description of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ids(self):
        """Gets the ids of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The ids of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this NetFlowInterfaceFilterDto.


        :param ids: The ids of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: list[int]
        """

        self._ids = ids

    @property
    def interface_numbers(self):
        """Gets the interface_numbers of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The interface_numbers of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._interface_numbers

    @interface_numbers.setter
    def interface_numbers(self, interface_numbers):
        """Sets the interface_numbers of this NetFlowInterfaceFilterDto.


        :param interface_numbers: The interface_numbers of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: list[int]
        """

        self._interface_numbers = interface_numbers

    @property
    def name(self):
        """Gets the name of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The name of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetFlowInterfaceFilterDto.


        :param name: The name of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def netflow_device_ids(self):
        """Gets the netflow_device_ids of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The netflow_device_ids of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._netflow_device_ids

    @netflow_device_ids.setter
    def netflow_device_ids(self, netflow_device_ids):
        """Sets the netflow_device_ids of this NetFlowInterfaceFilterDto.


        :param netflow_device_ids: The netflow_device_ids of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: list[int]
        """

        self._netflow_device_ids = netflow_device_ids

    @property
    def origin_ips(self):
        """Gets the origin_ips of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The origin_ips of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._origin_ips

    @origin_ips.setter
    def origin_ips(self, origin_ips):
        """Sets the origin_ips of this NetFlowInterfaceFilterDto.


        :param origin_ips: The origin_ips of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: list[str]
        """

        self._origin_ips = origin_ips

    @property
    def override_description(self):
        """Gets the override_description of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The override_description of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._override_description

    @override_description.setter
    def override_description(self, override_description):
        """Sets the override_description of this NetFlowInterfaceFilterDto.


        :param override_description: The override_description of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: int
        """

        self._override_description = override_description

    @property
    def override_name(self):
        """Gets the override_name of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The override_name of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._override_name

    @override_name.setter
    def override_name(self, override_name):
        """Sets the override_name of this NetFlowInterfaceFilterDto.


        :param override_name: The override_name of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: int
        """

        self._override_name = override_name

    @property
    def override_speed(self):
        """Gets the override_speed of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The override_speed of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._override_speed

    @override_speed.setter
    def override_speed(self, override_speed):
        """Sets the override_speed of this NetFlowInterfaceFilterDto.


        :param override_speed: The override_speed of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: int
        """

        self._override_speed = override_speed

    @property
    def peers(self):
        """Gets the peers of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The peers of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._peers

    @peers.setter
    def peers(self, peers):
        """Sets the peers of this NetFlowInterfaceFilterDto.


        :param peers: The peers of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: list[int]
        """

        self._peers = peers

    @property
    def reason(self):
        """Gets the reason of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The reason of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this NetFlowInterfaceFilterDto.


        :param reason: The reason of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["normal", "exceeded_capacity"]  # noqa: E501
        if reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values)
            )

        self._reason = reason

    @property
    def search_text(self):
        """Gets the search_text of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The search_text of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._search_text

    @search_text.setter
    def search_text(self, search_text):
        """Sets the search_text of this NetFlowInterfaceFilterDto.


        :param search_text: The search_text of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: str
        """

        self._search_text = search_text

    @property
    def speed(self):
        """Gets the speed of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The speed of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this NetFlowInterfaceFilterDto.


        :param speed: The speed of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: int
        """

        self._speed = speed

    @property
    def system_description(self):
        """Gets the system_description of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The system_description of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._system_description

    @system_description.setter
    def system_description(self, system_description):
        """Sets the system_description of this NetFlowInterfaceFilterDto.


        :param system_description: The system_description of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: str
        """

        self._system_description = system_description

    @property
    def system_name(self):
        """Gets the system_name of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The system_name of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this NetFlowInterfaceFilterDto.


        :param system_name: The system_name of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: str
        """

        self._system_name = system_name

    @property
    def system_speed(self):
        """Gets the system_speed of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The system_speed of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._system_speed

    @system_speed.setter
    def system_speed(self, system_speed):
        """Sets the system_speed of this NetFlowInterfaceFilterDto.


        :param system_speed: The system_speed of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: int
        """

        self._system_speed = system_speed

    @property
    def visible(self):
        """Gets the visible of this NetFlowInterfaceFilterDto.  # noqa: E501


        :return: The visible of this NetFlowInterfaceFilterDto.  # noqa: E501
        :rtype: int
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this NetFlowInterfaceFilterDto.


        :param visible: The visible of this NetFlowInterfaceFilterDto.  # noqa: E501
        :type: int
        """

        self._visible = visible

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
        if issubclass(NetFlowInterfaceFilterDto, dict):
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
        if not isinstance(other, NetFlowInterfaceFilterDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
