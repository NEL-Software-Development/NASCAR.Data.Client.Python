# coding: utf-8

"""
    NASCAR.Data.API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class RosterMember(object):
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
        'name': 'str',
        'position': 'str'
    }

    attribute_map = {
        'name': 'name',
        'position': 'position'
    }

    def __init__(self, name=None, position=None):  # noqa: E501
        """RosterMember - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._position = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if position is not None:
            self.position = position

    @property
    def name(self):
        """Gets the name of this RosterMember.  # noqa: E501

        Team member name  # noqa: E501

        :return: The name of this RosterMember.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RosterMember.

        Team member name  # noqa: E501

        :param name: The name of this RosterMember.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def position(self):
        """Gets the position of this RosterMember.  # noqa: E501

        Position  # noqa: E501

        :return: The position of this RosterMember.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this RosterMember.

        Position  # noqa: E501

        :param position: The position of this RosterMember.  # noqa: E501
        :type: str
        """

        self._position = position

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
        if issubclass(RosterMember, dict):
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
        if not isinstance(other, RosterMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
