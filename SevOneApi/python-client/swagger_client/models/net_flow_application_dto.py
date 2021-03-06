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


class NetFlowApplicationDto(object):
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
        'ip': 'str',
        'name': 'str',
        'port': 'int',
        'protocol': 'int'
    }

    attribute_map = {
        'description': 'description',
        'ip': 'ip',
        'name': 'name',
        'port': 'port',
        'protocol': 'protocol'
    }

    def __init__(self, description=None, ip=None, name=None, port=None, protocol=None):  # noqa: E501
        """NetFlowApplicationDto - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._ip = None
        self._name = None
        self._port = None
        self._protocol = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if ip is not None:
            self.ip = ip
        if name is not None:
            self.name = name
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol

    @property
    def description(self):
        """Gets the description of this NetFlowApplicationDto.  # noqa: E501


        :return: The description of this NetFlowApplicationDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NetFlowApplicationDto.


        :param description: The description of this NetFlowApplicationDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ip(self):
        """Gets the ip of this NetFlowApplicationDto.  # noqa: E501


        :return: The ip of this NetFlowApplicationDto.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this NetFlowApplicationDto.


        :param ip: The ip of this NetFlowApplicationDto.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def name(self):
        """Gets the name of this NetFlowApplicationDto.  # noqa: E501


        :return: The name of this NetFlowApplicationDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetFlowApplicationDto.


        :param name: The name of this NetFlowApplicationDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def port(self):
        """Gets the port of this NetFlowApplicationDto.  # noqa: E501


        :return: The port of this NetFlowApplicationDto.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this NetFlowApplicationDto.


        :param port: The port of this NetFlowApplicationDto.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this NetFlowApplicationDto.  # noqa: E501


        :return: The protocol of this NetFlowApplicationDto.  # noqa: E501
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this NetFlowApplicationDto.


        :param protocol: The protocol of this NetFlowApplicationDto.  # noqa: E501
        :type: int
        """

        self._protocol = protocol

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
        if issubclass(NetFlowApplicationDto, dict):
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
        if not isinstance(other, NetFlowApplicationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
