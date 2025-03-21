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


class Tire(object):
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
        'epc': 'str',
        'd_number': 'str',
        'sequence': 'str',
        'tire_type': 'str',
        'side_code': 'str',
        'car_number': 'str'
    }

    attribute_map = {
        'epc': 'epc',
        'd_number': 'd_number',
        'sequence': 'sequence',
        'tire_type': 'tire_type',
        'side_code': 'side_code',
        'car_number': 'car_number'
    }

    def __init__(self, epc=None, d_number=None, sequence=None, tire_type=None, side_code=None, car_number=None):  # noqa: E501
        """Tire - a model defined in Swagger"""  # noqa: E501
        self._epc = None
        self._d_number = None
        self._sequence = None
        self._tire_type = None
        self._side_code = None
        self._car_number = None
        self.discriminator = None
        if epc is not None:
            self.epc = epc
        if d_number is not None:
            self.d_number = d_number
        if sequence is not None:
            self.sequence = sequence
        if tire_type is not None:
            self.tire_type = tire_type
        if side_code is not None:
            self.side_code = side_code
        if car_number is not None:
            self.car_number = car_number

    @property
    def epc(self):
        """Gets the epc of this Tire.  # noqa: E501


        :return: The epc of this Tire.  # noqa: E501
        :rtype: str
        """
        return self._epc

    @epc.setter
    def epc(self, epc):
        """Sets the epc of this Tire.


        :param epc: The epc of this Tire.  # noqa: E501
        :type: str
        """

        self._epc = epc

    @property
    def d_number(self):
        """Gets the d_number of this Tire.  # noqa: E501


        :return: The d_number of this Tire.  # noqa: E501
        :rtype: str
        """
        return self._d_number

    @d_number.setter
    def d_number(self, d_number):
        """Sets the d_number of this Tire.


        :param d_number: The d_number of this Tire.  # noqa: E501
        :type: str
        """

        self._d_number = d_number

    @property
    def sequence(self):
        """Gets the sequence of this Tire.  # noqa: E501


        :return: The sequence of this Tire.  # noqa: E501
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this Tire.


        :param sequence: The sequence of this Tire.  # noqa: E501
        :type: str
        """

        self._sequence = sequence

    @property
    def tire_type(self):
        """Gets the tire_type of this Tire.  # noqa: E501


        :return: The tire_type of this Tire.  # noqa: E501
        :rtype: str
        """
        return self._tire_type

    @tire_type.setter
    def tire_type(self, tire_type):
        """Sets the tire_type of this Tire.


        :param tire_type: The tire_type of this Tire.  # noqa: E501
        :type: str
        """

        self._tire_type = tire_type

    @property
    def side_code(self):
        """Gets the side_code of this Tire.  # noqa: E501


        :return: The side_code of this Tire.  # noqa: E501
        :rtype: str
        """
        return self._side_code

    @side_code.setter
    def side_code(self, side_code):
        """Sets the side_code of this Tire.


        :param side_code: The side_code of this Tire.  # noqa: E501
        :type: str
        """

        self._side_code = side_code

    @property
    def car_number(self):
        """Gets the car_number of this Tire.  # noqa: E501


        :return: The car_number of this Tire.  # noqa: E501
        :rtype: str
        """
        return self._car_number

    @car_number.setter
    def car_number(self, car_number):
        """Sets the car_number of this Tire.


        :param car_number: The car_number of this Tire.  # noqa: E501
        :type: str
        """

        self._car_number = car_number

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
        if issubclass(Tire, dict):
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
        if not isinstance(other, Tire):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
