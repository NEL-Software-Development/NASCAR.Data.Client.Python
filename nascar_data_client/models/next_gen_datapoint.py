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


class NextGenDatapoint(object):
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
        'datapoint_id': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'datapoint_id': 'datapoint_id',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, datapoint_id=None, name=None, description=None):  # noqa: E501
        """NextGenDatapoint - a model defined in Swagger"""  # noqa: E501
        self._datapoint_id = None
        self._name = None
        self._description = None
        self.discriminator = None
        if datapoint_id is not None:
            self.datapoint_id = datapoint_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description

    @property
    def datapoint_id(self):
        """Gets the datapoint_id of this NextGenDatapoint.  # noqa: E501


        :return: The datapoint_id of this NextGenDatapoint.  # noqa: E501
        :rtype: str
        """
        return self._datapoint_id

    @datapoint_id.setter
    def datapoint_id(self, datapoint_id):
        """Sets the datapoint_id of this NextGenDatapoint.


        :param datapoint_id: The datapoint_id of this NextGenDatapoint.  # noqa: E501
        :type: str
        """

        self._datapoint_id = datapoint_id

    @property
    def name(self):
        """Gets the name of this NextGenDatapoint.  # noqa: E501


        :return: The name of this NextGenDatapoint.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NextGenDatapoint.


        :param name: The name of this NextGenDatapoint.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this NextGenDatapoint.  # noqa: E501


        :return: The description of this NextGenDatapoint.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NextGenDatapoint.


        :param description: The description of this NextGenDatapoint.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(NextGenDatapoint, dict):
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
        if not isinstance(other, NextGenDatapoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
