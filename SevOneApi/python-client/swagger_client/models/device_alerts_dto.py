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

from swagger_client.models.alert_dto import AlertDto  # noqa: F401,E501
from swagger_client.models.device_object_dto import DeviceObjectDto  # noqa: F401,E501
from swagger_client.models.plugin_info import PluginInfo  # noqa: F401,E501


class DeviceAlertsDto(object):
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
        'alerts': 'list[AlertDto]',
        'allow_delete': 'bool',
        'alternate_name': 'str',
        'date_added': 'int',
        'description': 'str',
        'disable_concurrent_polling': 'bool',
        'disable_polling': 'bool',
        'disable_thresholding': 'bool',
        'id': 'int',
        'ip_address': 'str',
        'is_deleted': 'bool',
        'is_new': 'bool',
        'last_discovery': 'int',
        'manual_ip': 'bool',
        'name': 'str',
        'num_elements': 'int',
        'objects': 'list[DeviceObjectDto]',
        'peer_id': 'int',
        'plugin_info': 'dict(str, PluginInfo)',
        'plugin_manager_id': 'int',
        'poll_frequency': 'int',
        'timezone': 'str',
        'workhours_group_id': 'int'
    }

    attribute_map = {
        'alerts': 'alerts',
        'allow_delete': 'allowDelete',
        'alternate_name': 'alternateName',
        'date_added': 'dateAdded',
        'description': 'description',
        'disable_concurrent_polling': 'disableConcurrentPolling',
        'disable_polling': 'disablePolling',
        'disable_thresholding': 'disableThresholding',
        'id': 'id',
        'ip_address': 'ipAddress',
        'is_deleted': 'isDeleted',
        'is_new': 'isNew',
        'last_discovery': 'lastDiscovery',
        'manual_ip': 'manualIP',
        'name': 'name',
        'num_elements': 'numElements',
        'objects': 'objects',
        'peer_id': 'peerId',
        'plugin_info': 'pluginInfo',
        'plugin_manager_id': 'pluginManagerId',
        'poll_frequency': 'pollFrequency',
        'timezone': 'timezone',
        'workhours_group_id': 'workhoursGroupId'
    }

    def __init__(self, alerts=None, allow_delete=None, alternate_name=None, date_added=None, description=None, disable_concurrent_polling=None, disable_polling=None, disable_thresholding=None, id=None, ip_address=None, is_deleted=None, is_new=None, last_discovery=None, manual_ip=None, name=None, num_elements=None, objects=None, peer_id=None, plugin_info=None, plugin_manager_id=None, poll_frequency=None, timezone=None, workhours_group_id=None):  # noqa: E501
        """DeviceAlertsDto - a model defined in Swagger"""  # noqa: E501

        self._alerts = None
        self._allow_delete = None
        self._alternate_name = None
        self._date_added = None
        self._description = None
        self._disable_concurrent_polling = None
        self._disable_polling = None
        self._disable_thresholding = None
        self._id = None
        self._ip_address = None
        self._is_deleted = None
        self._is_new = None
        self._last_discovery = None
        self._manual_ip = None
        self._name = None
        self._num_elements = None
        self._objects = None
        self._peer_id = None
        self._plugin_info = None
        self._plugin_manager_id = None
        self._poll_frequency = None
        self._timezone = None
        self._workhours_group_id = None
        self.discriminator = None

        if alerts is not None:
            self.alerts = alerts
        if allow_delete is not None:
            self.allow_delete = allow_delete
        if alternate_name is not None:
            self.alternate_name = alternate_name
        if date_added is not None:
            self.date_added = date_added
        if description is not None:
            self.description = description
        if disable_concurrent_polling is not None:
            self.disable_concurrent_polling = disable_concurrent_polling
        if disable_polling is not None:
            self.disable_polling = disable_polling
        if disable_thresholding is not None:
            self.disable_thresholding = disable_thresholding
        if id is not None:
            self.id = id
        if ip_address is not None:
            self.ip_address = ip_address
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if is_new is not None:
            self.is_new = is_new
        if last_discovery is not None:
            self.last_discovery = last_discovery
        if manual_ip is not None:
            self.manual_ip = manual_ip
        if name is not None:
            self.name = name
        if num_elements is not None:
            self.num_elements = num_elements
        if objects is not None:
            self.objects = objects
        if peer_id is not None:
            self.peer_id = peer_id
        if plugin_info is not None:
            self.plugin_info = plugin_info
        if plugin_manager_id is not None:
            self.plugin_manager_id = plugin_manager_id
        if poll_frequency is not None:
            self.poll_frequency = poll_frequency
        if timezone is not None:
            self.timezone = timezone
        if workhours_group_id is not None:
            self.workhours_group_id = workhours_group_id

    @property
    def alerts(self):
        """Gets the alerts of this DeviceAlertsDto.  # noqa: E501


        :return: The alerts of this DeviceAlertsDto.  # noqa: E501
        :rtype: list[AlertDto]
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this DeviceAlertsDto.


        :param alerts: The alerts of this DeviceAlertsDto.  # noqa: E501
        :type: list[AlertDto]
        """

        self._alerts = alerts

    @property
    def allow_delete(self):
        """Gets the allow_delete of this DeviceAlertsDto.  # noqa: E501


        :return: The allow_delete of this DeviceAlertsDto.  # noqa: E501
        :rtype: bool
        """
        return self._allow_delete

    @allow_delete.setter
    def allow_delete(self, allow_delete):
        """Sets the allow_delete of this DeviceAlertsDto.


        :param allow_delete: The allow_delete of this DeviceAlertsDto.  # noqa: E501
        :type: bool
        """

        self._allow_delete = allow_delete

    @property
    def alternate_name(self):
        """Gets the alternate_name of this DeviceAlertsDto.  # noqa: E501


        :return: The alternate_name of this DeviceAlertsDto.  # noqa: E501
        :rtype: str
        """
        return self._alternate_name

    @alternate_name.setter
    def alternate_name(self, alternate_name):
        """Sets the alternate_name of this DeviceAlertsDto.


        :param alternate_name: The alternate_name of this DeviceAlertsDto.  # noqa: E501
        :type: str
        """

        self._alternate_name = alternate_name

    @property
    def date_added(self):
        """Gets the date_added of this DeviceAlertsDto.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The date_added of this DeviceAlertsDto.  # noqa: E501
        :rtype: int
        """
        return self._date_added

    @date_added.setter
    def date_added(self, date_added):
        """Sets the date_added of this DeviceAlertsDto.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param date_added: The date_added of this DeviceAlertsDto.  # noqa: E501
        :type: int
        """

        self._date_added = date_added

    @property
    def description(self):
        """Gets the description of this DeviceAlertsDto.  # noqa: E501


        :return: The description of this DeviceAlertsDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceAlertsDto.


        :param description: The description of this DeviceAlertsDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def disable_concurrent_polling(self):
        """Gets the disable_concurrent_polling of this DeviceAlertsDto.  # noqa: E501


        :return: The disable_concurrent_polling of this DeviceAlertsDto.  # noqa: E501
        :rtype: bool
        """
        return self._disable_concurrent_polling

    @disable_concurrent_polling.setter
    def disable_concurrent_polling(self, disable_concurrent_polling):
        """Sets the disable_concurrent_polling of this DeviceAlertsDto.


        :param disable_concurrent_polling: The disable_concurrent_polling of this DeviceAlertsDto.  # noqa: E501
        :type: bool
        """

        self._disable_concurrent_polling = disable_concurrent_polling

    @property
    def disable_polling(self):
        """Gets the disable_polling of this DeviceAlertsDto.  # noqa: E501


        :return: The disable_polling of this DeviceAlertsDto.  # noqa: E501
        :rtype: bool
        """
        return self._disable_polling

    @disable_polling.setter
    def disable_polling(self, disable_polling):
        """Sets the disable_polling of this DeviceAlertsDto.


        :param disable_polling: The disable_polling of this DeviceAlertsDto.  # noqa: E501
        :type: bool
        """

        self._disable_polling = disable_polling

    @property
    def disable_thresholding(self):
        """Gets the disable_thresholding of this DeviceAlertsDto.  # noqa: E501


        :return: The disable_thresholding of this DeviceAlertsDto.  # noqa: E501
        :rtype: bool
        """
        return self._disable_thresholding

    @disable_thresholding.setter
    def disable_thresholding(self, disable_thresholding):
        """Sets the disable_thresholding of this DeviceAlertsDto.


        :param disable_thresholding: The disable_thresholding of this DeviceAlertsDto.  # noqa: E501
        :type: bool
        """

        self._disable_thresholding = disable_thresholding

    @property
    def id(self):
        """Gets the id of this DeviceAlertsDto.  # noqa: E501


        :return: The id of this DeviceAlertsDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceAlertsDto.


        :param id: The id of this DeviceAlertsDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def ip_address(self):
        """Gets the ip_address of this DeviceAlertsDto.  # noqa: E501


        :return: The ip_address of this DeviceAlertsDto.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DeviceAlertsDto.


        :param ip_address: The ip_address of this DeviceAlertsDto.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def is_deleted(self):
        """Gets the is_deleted of this DeviceAlertsDto.  # noqa: E501


        :return: The is_deleted of this DeviceAlertsDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this DeviceAlertsDto.


        :param is_deleted: The is_deleted of this DeviceAlertsDto.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def is_new(self):
        """Gets the is_new of this DeviceAlertsDto.  # noqa: E501


        :return: The is_new of this DeviceAlertsDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_new

    @is_new.setter
    def is_new(self, is_new):
        """Sets the is_new of this DeviceAlertsDto.


        :param is_new: The is_new of this DeviceAlertsDto.  # noqa: E501
        :type: bool
        """

        self._is_new = is_new

    @property
    def last_discovery(self):
        """Gets the last_discovery of this DeviceAlertsDto.  # noqa: E501

        Unix timestamp with milliseconds proximity  # noqa: E501

        :return: The last_discovery of this DeviceAlertsDto.  # noqa: E501
        :rtype: int
        """
        return self._last_discovery

    @last_discovery.setter
    def last_discovery(self, last_discovery):
        """Sets the last_discovery of this DeviceAlertsDto.

        Unix timestamp with milliseconds proximity  # noqa: E501

        :param last_discovery: The last_discovery of this DeviceAlertsDto.  # noqa: E501
        :type: int
        """

        self._last_discovery = last_discovery

    @property
    def manual_ip(self):
        """Gets the manual_ip of this DeviceAlertsDto.  # noqa: E501


        :return: The manual_ip of this DeviceAlertsDto.  # noqa: E501
        :rtype: bool
        """
        return self._manual_ip

    @manual_ip.setter
    def manual_ip(self, manual_ip):
        """Sets the manual_ip of this DeviceAlertsDto.


        :param manual_ip: The manual_ip of this DeviceAlertsDto.  # noqa: E501
        :type: bool
        """

        self._manual_ip = manual_ip

    @property
    def name(self):
        """Gets the name of this DeviceAlertsDto.  # noqa: E501


        :return: The name of this DeviceAlertsDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceAlertsDto.


        :param name: The name of this DeviceAlertsDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def num_elements(self):
        """Gets the num_elements of this DeviceAlertsDto.  # noqa: E501


        :return: The num_elements of this DeviceAlertsDto.  # noqa: E501
        :rtype: int
        """
        return self._num_elements

    @num_elements.setter
    def num_elements(self, num_elements):
        """Sets the num_elements of this DeviceAlertsDto.


        :param num_elements: The num_elements of this DeviceAlertsDto.  # noqa: E501
        :type: int
        """

        self._num_elements = num_elements

    @property
    def objects(self):
        """Gets the objects of this DeviceAlertsDto.  # noqa: E501


        :return: The objects of this DeviceAlertsDto.  # noqa: E501
        :rtype: list[DeviceObjectDto]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """Sets the objects of this DeviceAlertsDto.


        :param objects: The objects of this DeviceAlertsDto.  # noqa: E501
        :type: list[DeviceObjectDto]
        """

        self._objects = objects

    @property
    def peer_id(self):
        """Gets the peer_id of this DeviceAlertsDto.  # noqa: E501


        :return: The peer_id of this DeviceAlertsDto.  # noqa: E501
        :rtype: int
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """Sets the peer_id of this DeviceAlertsDto.


        :param peer_id: The peer_id of this DeviceAlertsDto.  # noqa: E501
        :type: int
        """

        self._peer_id = peer_id

    @property
    def plugin_info(self):
        """Gets the plugin_info of this DeviceAlertsDto.  # noqa: E501


        :return: The plugin_info of this DeviceAlertsDto.  # noqa: E501
        :rtype: dict(str, PluginInfo)
        """
        return self._plugin_info

    @plugin_info.setter
    def plugin_info(self, plugin_info):
        """Sets the plugin_info of this DeviceAlertsDto.


        :param plugin_info: The plugin_info of this DeviceAlertsDto.  # noqa: E501
        :type: dict(str, PluginInfo)
        """

        self._plugin_info = plugin_info

    @property
    def plugin_manager_id(self):
        """Gets the plugin_manager_id of this DeviceAlertsDto.  # noqa: E501


        :return: The plugin_manager_id of this DeviceAlertsDto.  # noqa: E501
        :rtype: int
        """
        return self._plugin_manager_id

    @plugin_manager_id.setter
    def plugin_manager_id(self, plugin_manager_id):
        """Sets the plugin_manager_id of this DeviceAlertsDto.


        :param plugin_manager_id: The plugin_manager_id of this DeviceAlertsDto.  # noqa: E501
        :type: int
        """

        self._plugin_manager_id = plugin_manager_id

    @property
    def poll_frequency(self):
        """Gets the poll_frequency of this DeviceAlertsDto.  # noqa: E501


        :return: The poll_frequency of this DeviceAlertsDto.  # noqa: E501
        :rtype: int
        """
        return self._poll_frequency

    @poll_frequency.setter
    def poll_frequency(self, poll_frequency):
        """Sets the poll_frequency of this DeviceAlertsDto.


        :param poll_frequency: The poll_frequency of this DeviceAlertsDto.  # noqa: E501
        :type: int
        """

        self._poll_frequency = poll_frequency

    @property
    def timezone(self):
        """Gets the timezone of this DeviceAlertsDto.  # noqa: E501


        :return: The timezone of this DeviceAlertsDto.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this DeviceAlertsDto.


        :param timezone: The timezone of this DeviceAlertsDto.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def workhours_group_id(self):
        """Gets the workhours_group_id of this DeviceAlertsDto.  # noqa: E501


        :return: The workhours_group_id of this DeviceAlertsDto.  # noqa: E501
        :rtype: int
        """
        return self._workhours_group_id

    @workhours_group_id.setter
    def workhours_group_id(self, workhours_group_id):
        """Sets the workhours_group_id of this DeviceAlertsDto.


        :param workhours_group_id: The workhours_group_id of this DeviceAlertsDto.  # noqa: E501
        :type: int
        """

        self._workhours_group_id = workhours_group_id

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
        if issubclass(DeviceAlertsDto, dict):
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
        if not isinstance(other, DeviceAlertsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other