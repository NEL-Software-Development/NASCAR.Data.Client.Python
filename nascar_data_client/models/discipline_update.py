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


class DisciplineUpdate(object):
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
        'inspection_type': 'str',
        'discipline': 'str',
        'vehicle_number': 'str',
        'chassis': 'str',
        'inspection_time': 'datetime'
    }

    attribute_map = {
        'inspection_type': 'inspection_type',
        'discipline': 'discipline',
        'vehicle_number': 'vehicle_number',
        'chassis': 'chassis',
        'inspection_time': 'inspection_time'
    }

    def __init__(self, inspection_type=None, discipline=None, vehicle_number=None, chassis=None, inspection_time=None):  # noqa: E501
        """DisciplineUpdate - a model defined in Swagger"""  # noqa: E501
        self._inspection_type = None
        self._discipline = None
        self._vehicle_number = None
        self._chassis = None
        self._inspection_time = None
        self.discriminator = None
        if inspection_type is not None:
            self.inspection_type = inspection_type
        if discipline is not None:
            self.discipline = discipline
        if vehicle_number is not None:
            self.vehicle_number = vehicle_number
        if chassis is not None:
            self.chassis = chassis
        if inspection_time is not None:
            self.inspection_time = inspection_time

    @property
    def inspection_type(self):
        """Gets the inspection_type of this DisciplineUpdate.  # noqa: E501

        The type of inspection  # noqa: E501

        :return: The inspection_type of this DisciplineUpdate.  # noqa: E501
        :rtype: str
        """
        return self._inspection_type

    @inspection_type.setter
    def inspection_type(self, inspection_type):
        """Sets the inspection_type of this DisciplineUpdate.

        The type of inspection  # noqa: E501

        :param inspection_type: The inspection_type of this DisciplineUpdate.  # noqa: E501
        :type: str
        """

        self._inspection_type = inspection_type

    @property
    def discipline(self):
        """Gets the discipline of this DisciplineUpdate.  # noqa: E501

        The inspection discipline  # noqa: E501

        :return: The discipline of this DisciplineUpdate.  # noqa: E501
        :rtype: str
        """
        return self._discipline

    @discipline.setter
    def discipline(self, discipline):
        """Sets the discipline of this DisciplineUpdate.

        The inspection discipline  # noqa: E501

        :param discipline: The discipline of this DisciplineUpdate.  # noqa: E501
        :type: str
        """

        self._discipline = discipline

    @property
    def vehicle_number(self):
        """Gets the vehicle_number of this DisciplineUpdate.  # noqa: E501

        The vehicle inspected  # noqa: E501

        :return: The vehicle_number of this DisciplineUpdate.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_number

    @vehicle_number.setter
    def vehicle_number(self, vehicle_number):
        """Sets the vehicle_number of this DisciplineUpdate.

        The vehicle inspected  # noqa: E501

        :param vehicle_number: The vehicle_number of this DisciplineUpdate.  # noqa: E501
        :type: str
        """

        self._vehicle_number = vehicle_number

    @property
    def chassis(self):
        """Gets the chassis of this DisciplineUpdate.  # noqa: E501

        The chassis inspected  # noqa: E501

        :return: The chassis of this DisciplineUpdate.  # noqa: E501
        :rtype: str
        """
        return self._chassis

    @chassis.setter
    def chassis(self, chassis):
        """Sets the chassis of this DisciplineUpdate.

        The chassis inspected  # noqa: E501

        :param chassis: The chassis of this DisciplineUpdate.  # noqa: E501
        :type: str
        """

        self._chassis = chassis

    @property
    def inspection_time(self):
        """Gets the inspection_time of this DisciplineUpdate.  # noqa: E501

        The time of the inspection  # noqa: E501

        :return: The inspection_time of this DisciplineUpdate.  # noqa: E501
        :rtype: datetime
        """
        return self._inspection_time

    @inspection_time.setter
    def inspection_time(self, inspection_time):
        """Sets the inspection_time of this DisciplineUpdate.

        The time of the inspection  # noqa: E501

        :param inspection_time: The inspection_time of this DisciplineUpdate.  # noqa: E501
        :type: datetime
        """

        self._inspection_time = inspection_time

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
        if issubclass(DisciplineUpdate, dict):
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
        if not isinstance(other, DisciplineUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
