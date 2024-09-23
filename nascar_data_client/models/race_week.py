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


class RaceWeek(object):
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
        'id': 'int',
        'season': 'int',
        'venue': 'str',
        'running_series': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'is_live': 'bool',
        'details': 'str'
    }

    attribute_map = {
        'id': 'id',
        'season': 'season',
        'venue': 'venue',
        'running_series': 'running_series',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'is_live': 'is_live',
        'details': 'details'
    }

    def __init__(self, id=None, season=0, venue='', running_series='', start_date=None, end_date=None, is_live=None, details=None):  # noqa: E501
        """RaceWeek - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._season = None
        self._venue = None
        self._running_series = None
        self._start_date = None
        self._end_date = None
        self._is_live = None
        self._details = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.season = season
        self.venue = venue
        self.running_series = running_series
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if is_live is not None:
            self.is_live = is_live
        if details is not None:
            self.details = details

    @property
    def id(self):
        """Gets the id of this RaceWeek.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this RaceWeek.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RaceWeek.

        Id  # noqa: E501

        :param id: The id of this RaceWeek.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def season(self):
        """Gets the season of this RaceWeek.  # noqa: E501

        Race season  # noqa: E501

        :return: The season of this RaceWeek.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this RaceWeek.

        Race season  # noqa: E501

        :param season: The season of this RaceWeek.  # noqa: E501
        :type: int
        """
        if season is None:
            raise ValueError("Invalid value for `season`, must not be `None`")  # noqa: E501

        self._season = season

    @property
    def venue(self):
        """Gets the venue of this RaceWeek.  # noqa: E501

        Venue  # noqa: E501

        :return: The venue of this RaceWeek.  # noqa: E501
        :rtype: str
        """
        return self._venue

    @venue.setter
    def venue(self, venue):
        """Sets the venue of this RaceWeek.

        Venue  # noqa: E501

        :param venue: The venue of this RaceWeek.  # noqa: E501
        :type: str
        """
        if venue is None:
            raise ValueError("Invalid value for `venue`, must not be `None`")  # noqa: E501

        self._venue = venue

    @property
    def running_series(self):
        """Gets the running_series of this RaceWeek.  # noqa: E501

        List of series running at this event  # noqa: E501

        :return: The running_series of this RaceWeek.  # noqa: E501
        :rtype: str
        """
        return self._running_series

    @running_series.setter
    def running_series(self, running_series):
        """Sets the running_series of this RaceWeek.

        List of series running at this event  # noqa: E501

        :param running_series: The running_series of this RaceWeek.  # noqa: E501
        :type: str
        """
        if running_series is None:
            raise ValueError("Invalid value for `running_series`, must not be `None`")  # noqa: E501

        self._running_series = running_series

    @property
    def start_date(self):
        """Gets the start_date of this RaceWeek.  # noqa: E501

        Start of raceweek  # noqa: E501

        :return: The start_date of this RaceWeek.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this RaceWeek.

        Start of raceweek  # noqa: E501

        :param start_date: The start_date of this RaceWeek.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this RaceWeek.  # noqa: E501

        End of raceweek  # noqa: E501

        :return: The end_date of this RaceWeek.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this RaceWeek.

        End of raceweek  # noqa: E501

        :param end_date: The end_date of this RaceWeek.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def is_live(self):
        """Gets the is_live of this RaceWeek.  # noqa: E501

        Is this raceweek currently in progress  # noqa: E501

        :return: The is_live of this RaceWeek.  # noqa: E501
        :rtype: bool
        """
        return self._is_live

    @is_live.setter
    def is_live(self, is_live):
        """Sets the is_live of this RaceWeek.

        Is this raceweek currently in progress  # noqa: E501

        :param is_live: The is_live of this RaceWeek.  # noqa: E501
        :type: bool
        """

        self._is_live = is_live

    @property
    def details(self):
        """Gets the details of this RaceWeek.  # noqa: E501

        URL to raceweek details  # noqa: E501

        :return: The details of this RaceWeek.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this RaceWeek.

        URL to raceweek details  # noqa: E501

        :param details: The details of this RaceWeek.  # noqa: E501
        :type: str
        """

        self._details = details

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
        if issubclass(RaceWeek, dict):
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
        if not isinstance(other, RaceWeek):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
