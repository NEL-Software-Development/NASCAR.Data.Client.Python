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


class OpticalTrackingUTMOffset(object):
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
        'track_id': 'int',
        'track_name': 'str',
        'zone': 'str',
        'x': 'float',
        'y': 'float',
        'z': 'float'
    }

    attribute_map = {
        'track_id': 'track_id',
        'track_name': 'track_name',
        'zone': 'zone',
        'x': 'x',
        'y': 'y',
        'z': 'z'
    }

    def __init__(self, track_id=None, track_name=None, zone=None, x=None, y=None, z=None):  # noqa: E501
        """OpticalTrackingUTMOffset - a model defined in Swagger"""  # noqa: E501
        self._track_id = None
        self._track_name = None
        self._zone = None
        self._x = None
        self._y = None
        self._z = None
        self.discriminator = None
        if track_id is not None:
            self.track_id = track_id
        if track_name is not None:
            self.track_name = track_name
        if zone is not None:
            self.zone = zone
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z

    @property
    def track_id(self):
        """Gets the track_id of this OpticalTrackingUTMOffset.  # noqa: E501

        Track Id  # noqa: E501

        :return: The track_id of this OpticalTrackingUTMOffset.  # noqa: E501
        :rtype: int
        """
        return self._track_id

    @track_id.setter
    def track_id(self, track_id):
        """Sets the track_id of this OpticalTrackingUTMOffset.

        Track Id  # noqa: E501

        :param track_id: The track_id of this OpticalTrackingUTMOffset.  # noqa: E501
        :type: int
        """

        self._track_id = track_id

    @property
    def track_name(self):
        """Gets the track_name of this OpticalTrackingUTMOffset.  # noqa: E501

        Track Name  # noqa: E501

        :return: The track_name of this OpticalTrackingUTMOffset.  # noqa: E501
        :rtype: str
        """
        return self._track_name

    @track_name.setter
    def track_name(self, track_name):
        """Sets the track_name of this OpticalTrackingUTMOffset.

        Track Name  # noqa: E501

        :param track_name: The track_name of this OpticalTrackingUTMOffset.  # noqa: E501
        :type: str
        """

        self._track_name = track_name

    @property
    def zone(self):
        """Gets the zone of this OpticalTrackingUTMOffset.  # noqa: E501

        Zone  # noqa: E501

        :return: The zone of this OpticalTrackingUTMOffset.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this OpticalTrackingUTMOffset.

        Zone  # noqa: E501

        :param zone: The zone of this OpticalTrackingUTMOffset.  # noqa: E501
        :type: str
        """

        self._zone = zone

    @property
    def x(self):
        """Gets the x of this OpticalTrackingUTMOffset.  # noqa: E501

        X Coordinate  # noqa: E501

        :return: The x of this OpticalTrackingUTMOffset.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this OpticalTrackingUTMOffset.

        X Coordinate  # noqa: E501

        :param x: The x of this OpticalTrackingUTMOffset.  # noqa: E501
        :type: float
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this OpticalTrackingUTMOffset.  # noqa: E501

        Y coordinate  # noqa: E501

        :return: The y of this OpticalTrackingUTMOffset.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this OpticalTrackingUTMOffset.

        Y coordinate  # noqa: E501

        :param y: The y of this OpticalTrackingUTMOffset.  # noqa: E501
        :type: float
        """

        self._y = y

    @property
    def z(self):
        """Gets the z of this OpticalTrackingUTMOffset.  # noqa: E501

        Z coordinate  # noqa: E501

        :return: The z of this OpticalTrackingUTMOffset.  # noqa: E501
        :rtype: float
        """
        return self._z

    @z.setter
    def z(self, z):
        """Sets the z of this OpticalTrackingUTMOffset.

        Z coordinate  # noqa: E501

        :param z: The z of this OpticalTrackingUTMOffset.  # noqa: E501
        :type: float
        """

        self._z = z

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
        if issubclass(OpticalTrackingUTMOffset, dict):
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
        if not isinstance(other, OpticalTrackingUTMOffset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
