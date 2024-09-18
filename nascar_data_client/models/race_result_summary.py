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


class RaceResultSummary(object):
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
        '_date': 'datetime',
        'race_name': 'str',
        'vehicle_number': 'str',
        'finish_position': 'int',
        'best_time': 'int',
        'best_speed': 'float',
        'delta_next_time': 'int',
        'delta_next_laps': 'int',
        'delta_leader_time': 'int',
        'delta_leader_laps': 'int',
        'best_lap': 'int',
        'laps': 'int'
    }

    attribute_map = {
        '_date': 'date',
        'race_name': 'race_name',
        'vehicle_number': 'vehicle_number',
        'finish_position': 'finish_position',
        'best_time': 'best_time',
        'best_speed': 'best_speed',
        'delta_next_time': 'delta_next_time',
        'delta_next_laps': 'delta_next_laps',
        'delta_leader_time': 'delta_leader_time',
        'delta_leader_laps': 'delta_leader_laps',
        'best_lap': 'best_lap',
        'laps': 'laps'
    }

    def __init__(self, _date=None, race_name=None, vehicle_number=None, finish_position=None, best_time=None, best_speed=None, delta_next_time=None, delta_next_laps=None, delta_leader_time=None, delta_leader_laps=None, best_lap=None, laps=None):  # noqa: E501
        """RaceResultSummary - a model defined in Swagger"""  # noqa: E501
        self.__date = None
        self._race_name = None
        self._vehicle_number = None
        self._finish_position = None
        self._best_time = None
        self._best_speed = None
        self._delta_next_time = None
        self._delta_next_laps = None
        self._delta_leader_time = None
        self._delta_leader_laps = None
        self._best_lap = None
        self._laps = None
        self.discriminator = None
        if _date is not None:
            self._date = _date
        if race_name is not None:
            self.race_name = race_name
        if vehicle_number is not None:
            self.vehicle_number = vehicle_number
        if finish_position is not None:
            self.finish_position = finish_position
        if best_time is not None:
            self.best_time = best_time
        if best_speed is not None:
            self.best_speed = best_speed
        if delta_next_time is not None:
            self.delta_next_time = delta_next_time
        if delta_next_laps is not None:
            self.delta_next_laps = delta_next_laps
        if delta_leader_time is not None:
            self.delta_leader_time = delta_leader_time
        if delta_leader_laps is not None:
            self.delta_leader_laps = delta_leader_laps
        if best_lap is not None:
            self.best_lap = best_lap
        if laps is not None:
            self.laps = laps

    @property
    def _date(self):
        """Gets the _date of this RaceResultSummary.  # noqa: E501

        Race date  # noqa: E501

        :return: The _date of this RaceResultSummary.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this RaceResultSummary.

        Race date  # noqa: E501

        :param _date: The _date of this RaceResultSummary.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def race_name(self):
        """Gets the race_name of this RaceResultSummary.  # noqa: E501

        Race name  # noqa: E501

        :return: The race_name of this RaceResultSummary.  # noqa: E501
        :rtype: str
        """
        return self._race_name

    @race_name.setter
    def race_name(self, race_name):
        """Sets the race_name of this RaceResultSummary.

        Race name  # noqa: E501

        :param race_name: The race_name of this RaceResultSummary.  # noqa: E501
        :type: str
        """

        self._race_name = race_name

    @property
    def vehicle_number(self):
        """Gets the vehicle_number of this RaceResultSummary.  # noqa: E501

        Vehicle number  # noqa: E501

        :return: The vehicle_number of this RaceResultSummary.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_number

    @vehicle_number.setter
    def vehicle_number(self, vehicle_number):
        """Sets the vehicle_number of this RaceResultSummary.

        Vehicle number  # noqa: E501

        :param vehicle_number: The vehicle_number of this RaceResultSummary.  # noqa: E501
        :type: str
        """

        self._vehicle_number = vehicle_number

    @property
    def finish_position(self):
        """Gets the finish_position of this RaceResultSummary.  # noqa: E501

        Finish position  # noqa: E501

        :return: The finish_position of this RaceResultSummary.  # noqa: E501
        :rtype: int
        """
        return self._finish_position

    @finish_position.setter
    def finish_position(self, finish_position):
        """Sets the finish_position of this RaceResultSummary.

        Finish position  # noqa: E501

        :param finish_position: The finish_position of this RaceResultSummary.  # noqa: E501
        :type: int
        """

        self._finish_position = finish_position

    @property
    def best_time(self):
        """Gets the best_time of this RaceResultSummary.  # noqa: E501

        Best lap time  # noqa: E501

        :return: The best_time of this RaceResultSummary.  # noqa: E501
        :rtype: int
        """
        return self._best_time

    @best_time.setter
    def best_time(self, best_time):
        """Sets the best_time of this RaceResultSummary.

        Best lap time  # noqa: E501

        :param best_time: The best_time of this RaceResultSummary.  # noqa: E501
        :type: int
        """

        self._best_time = best_time

    @property
    def best_speed(self):
        """Gets the best_speed of this RaceResultSummary.  # noqa: E501

        Best speed  # noqa: E501

        :return: The best_speed of this RaceResultSummary.  # noqa: E501
        :rtype: float
        """
        return self._best_speed

    @best_speed.setter
    def best_speed(self, best_speed):
        """Sets the best_speed of this RaceResultSummary.

        Best speed  # noqa: E501

        :param best_speed: The best_speed of this RaceResultSummary.  # noqa: E501
        :type: float
        """

        self._best_speed = best_speed

    @property
    def delta_next_time(self):
        """Gets the delta_next_time of this RaceResultSummary.  # noqa: E501

        The number of milliseconds behind the next entry  # noqa: E501

        :return: The delta_next_time of this RaceResultSummary.  # noqa: E501
        :rtype: int
        """
        return self._delta_next_time

    @delta_next_time.setter
    def delta_next_time(self, delta_next_time):
        """Sets the delta_next_time of this RaceResultSummary.

        The number of milliseconds behind the next entry  # noqa: E501

        :param delta_next_time: The delta_next_time of this RaceResultSummary.  # noqa: E501
        :type: int
        """

        self._delta_next_time = delta_next_time

    @property
    def delta_next_laps(self):
        """Gets the delta_next_laps of this RaceResultSummary.  # noqa: E501

        The number of laps behind the next entry  # noqa: E501

        :return: The delta_next_laps of this RaceResultSummary.  # noqa: E501
        :rtype: int
        """
        return self._delta_next_laps

    @delta_next_laps.setter
    def delta_next_laps(self, delta_next_laps):
        """Sets the delta_next_laps of this RaceResultSummary.

        The number of laps behind the next entry  # noqa: E501

        :param delta_next_laps: The delta_next_laps of this RaceResultSummary.  # noqa: E501
        :type: int
        """

        self._delta_next_laps = delta_next_laps

    @property
    def delta_leader_time(self):
        """Gets the delta_leader_time of this RaceResultSummary.  # noqa: E501

        The number of milliseconds behind the leader  # noqa: E501

        :return: The delta_leader_time of this RaceResultSummary.  # noqa: E501
        :rtype: int
        """
        return self._delta_leader_time

    @delta_leader_time.setter
    def delta_leader_time(self, delta_leader_time):
        """Sets the delta_leader_time of this RaceResultSummary.

        The number of milliseconds behind the leader  # noqa: E501

        :param delta_leader_time: The delta_leader_time of this RaceResultSummary.  # noqa: E501
        :type: int
        """

        self._delta_leader_time = delta_leader_time

    @property
    def delta_leader_laps(self):
        """Gets the delta_leader_laps of this RaceResultSummary.  # noqa: E501

        The number of laps behind the leader  # noqa: E501

        :return: The delta_leader_laps of this RaceResultSummary.  # noqa: E501
        :rtype: int
        """
        return self._delta_leader_laps

    @delta_leader_laps.setter
    def delta_leader_laps(self, delta_leader_laps):
        """Sets the delta_leader_laps of this RaceResultSummary.

        The number of laps behind the leader  # noqa: E501

        :param delta_leader_laps: The delta_leader_laps of this RaceResultSummary.  # noqa: E501
        :type: int
        """

        self._delta_leader_laps = delta_leader_laps

    @property
    def best_lap(self):
        """Gets the best_lap of this RaceResultSummary.  # noqa: E501

        The best lap  # noqa: E501

        :return: The best_lap of this RaceResultSummary.  # noqa: E501
        :rtype: int
        """
        return self._best_lap

    @best_lap.setter
    def best_lap(self, best_lap):
        """Sets the best_lap of this RaceResultSummary.

        The best lap  # noqa: E501

        :param best_lap: The best_lap of this RaceResultSummary.  # noqa: E501
        :type: int
        """

        self._best_lap = best_lap

    @property
    def laps(self):
        """Gets the laps of this RaceResultSummary.  # noqa: E501

        The number of laps completed  # noqa: E501

        :return: The laps of this RaceResultSummary.  # noqa: E501
        :rtype: int
        """
        return self._laps

    @laps.setter
    def laps(self, laps):
        """Sets the laps of this RaceResultSummary.

        The number of laps completed  # noqa: E501

        :param laps: The laps of this RaceResultSummary.  # noqa: E501
        :type: int
        """

        self._laps = laps

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
        if issubclass(RaceResultSummary, dict):
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
        if not isinstance(other, RaceResultSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
