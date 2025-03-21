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


class NextGenSource(object):
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
        'source_id': 'str',
        'name': 'str',
        'description': 'str',
        'vehicle_number': 'str'
    }

    attribute_map = {
        'source_id': 'source_id',
        'name': 'name',
        'description': 'description',
        'vehicle_number': 'vehicle_number'
    }

    def __init__(self, source_id=None, name=None, description=None, vehicle_number=None):  # noqa: E501
        """NextGenSource - a model defined in Swagger"""  # noqa: E501
        self._source_id = None
        self._name = None
        self._description = None
        self._vehicle_number = None
        self.discriminator = None
        if source_id is not None:
            self.source_id = source_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if vehicle_number is not None:
            self.vehicle_number = vehicle_number

    @property
    def source_id(self):
        """Gets the source_id of this NextGenSource.  # noqa: E501


        :return: The source_id of this NextGenSource.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this NextGenSource.


        :param source_id: The source_id of this NextGenSource.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

    @property
    def name(self):
        """Gets the name of this NextGenSource.  # noqa: E501

        Source name  # noqa: E501

        :return: The name of this NextGenSource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NextGenSource.

        Source name  # noqa: E501

        :param name: The name of this NextGenSource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this NextGenSource.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this NextGenSource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NextGenSource.

        Description  # noqa: E501

        :param description: The description of this NextGenSource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def vehicle_number(self):
        """Gets the vehicle_number of this NextGenSource.  # noqa: E501

        Vehicle Number  # noqa: E501

        :return: The vehicle_number of this NextGenSource.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_number

    @vehicle_number.setter
    def vehicle_number(self, vehicle_number):
        """Sets the vehicle_number of this NextGenSource.

        Vehicle Number  # noqa: E501

        :param vehicle_number: The vehicle_number of this NextGenSource.  # noqa: E501
        :type: str
        """

        self._vehicle_number = vehicle_number

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
        if issubclass(NextGenSource, dict):
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
        if not isinstance(other, NextGenSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
