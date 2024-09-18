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


class DriverSummaryByTrack(object):
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
        'average_start': 'float',
        'average_finish': 'float',
        'dnf': 'int',
        'driver_id': 'int',
        'laps_completed': 'int',
        'laps_led': 'int',
        'lead_lap_finish': 'int',
        'miles_completed': 'float',
        'poles': 'int',
        'running_at_finish': 'int',
        'series_id': 'int',
        'top5': 'int',
        'top10': 'int',
        'total_races': 'int',
        'wins': 'int',
        'season': 'int',
        'track_id': 'int',
        'track_name': 'str'
    }

    attribute_map = {
        'average_start': 'average_start',
        'average_finish': 'average_finish',
        'dnf': 'dnf',
        'driver_id': 'driver_id',
        'laps_completed': 'laps_completed',
        'laps_led': 'laps_led',
        'lead_lap_finish': 'lead_lap_finish',
        'miles_completed': 'miles_completed',
        'poles': 'poles',
        'running_at_finish': 'running_at_finish',
        'series_id': 'series_id',
        'top5': 'top5',
        'top10': 'top10',
        'total_races': 'total_races',
        'wins': 'wins',
        'season': 'season',
        'track_id': 'track_id',
        'track_name': 'track_name'
    }

    def __init__(self, average_start=None, average_finish=None, dnf=None, driver_id=None, laps_completed=None, laps_led=None, lead_lap_finish=None, miles_completed=None, poles=None, running_at_finish=None, series_id=None, top5=None, top10=None, total_races=None, wins=None, season=None, track_id=None, track_name=None):  # noqa: E501
        """DriverSummaryByTrack - a model defined in Swagger"""  # noqa: E501
        self._average_start = None
        self._average_finish = None
        self._dnf = None
        self._driver_id = None
        self._laps_completed = None
        self._laps_led = None
        self._lead_lap_finish = None
        self._miles_completed = None
        self._poles = None
        self._running_at_finish = None
        self._series_id = None
        self._top5 = None
        self._top10 = None
        self._total_races = None
        self._wins = None
        self._season = None
        self._track_id = None
        self._track_name = None
        self.discriminator = None
        if average_start is not None:
            self.average_start = average_start
        if average_finish is not None:
            self.average_finish = average_finish
        if dnf is not None:
            self.dnf = dnf
        if driver_id is not None:
            self.driver_id = driver_id
        if laps_completed is not None:
            self.laps_completed = laps_completed
        if laps_led is not None:
            self.laps_led = laps_led
        if lead_lap_finish is not None:
            self.lead_lap_finish = lead_lap_finish
        if miles_completed is not None:
            self.miles_completed = miles_completed
        if poles is not None:
            self.poles = poles
        if running_at_finish is not None:
            self.running_at_finish = running_at_finish
        if series_id is not None:
            self.series_id = series_id
        if top5 is not None:
            self.top5 = top5
        if top10 is not None:
            self.top10 = top10
        if total_races is not None:
            self.total_races = total_races
        if wins is not None:
            self.wins = wins
        if season is not None:
            self.season = season
        if track_id is not None:
            self.track_id = track_id
        if track_name is not None:
            self.track_name = track_name

    @property
    def average_start(self):
        """Gets the average_start of this DriverSummaryByTrack.  # noqa: E501

        Average start position  # noqa: E501

        :return: The average_start of this DriverSummaryByTrack.  # noqa: E501
        :rtype: float
        """
        return self._average_start

    @average_start.setter
    def average_start(self, average_start):
        """Sets the average_start of this DriverSummaryByTrack.

        Average start position  # noqa: E501

        :param average_start: The average_start of this DriverSummaryByTrack.  # noqa: E501
        :type: float
        """

        self._average_start = average_start

    @property
    def average_finish(self):
        """Gets the average_finish of this DriverSummaryByTrack.  # noqa: E501

        Average finish position  # noqa: E501

        :return: The average_finish of this DriverSummaryByTrack.  # noqa: E501
        :rtype: float
        """
        return self._average_finish

    @average_finish.setter
    def average_finish(self, average_finish):
        """Sets the average_finish of this DriverSummaryByTrack.

        Average finish position  # noqa: E501

        :param average_finish: The average_finish of this DriverSummaryByTrack.  # noqa: E501
        :type: float
        """

        self._average_finish = average_finish

    @property
    def dnf(self):
        """Gets the dnf of this DriverSummaryByTrack.  # noqa: E501

        The number of races where the driver did not finish  # noqa: E501

        :return: The dnf of this DriverSummaryByTrack.  # noqa: E501
        :rtype: int
        """
        return self._dnf

    @dnf.setter
    def dnf(self, dnf):
        """Sets the dnf of this DriverSummaryByTrack.

        The number of races where the driver did not finish  # noqa: E501

        :param dnf: The dnf of this DriverSummaryByTrack.  # noqa: E501
        :type: int
        """

        self._dnf = dnf

    @property
    def driver_id(self):
        """Gets the driver_id of this DriverSummaryByTrack.  # noqa: E501

        Driver Id  # noqa: E501

        :return: The driver_id of this DriverSummaryByTrack.  # noqa: E501
        :rtype: int
        """
        return self._driver_id

    @driver_id.setter
    def driver_id(self, driver_id):
        """Sets the driver_id of this DriverSummaryByTrack.

        Driver Id  # noqa: E501

        :param driver_id: The driver_id of this DriverSummaryByTrack.  # noqa: E501
        :type: int
        """

        self._driver_id = driver_id

    @property
    def laps_completed(self):
        """Gets the laps_completed of this DriverSummaryByTrack.  # noqa: E501

        The number of laps completed  # noqa: E501

        :return: The laps_completed of this DriverSummaryByTrack.  # noqa: E501
        :rtype: int
        """
        return self._laps_completed

    @laps_completed.setter
    def laps_completed(self, laps_completed):
        """Sets the laps_completed of this DriverSummaryByTrack.

        The number of laps completed  # noqa: E501

        :param laps_completed: The laps_completed of this DriverSummaryByTrack.  # noqa: E501
        :type: int
        """

        self._laps_completed = laps_completed

    @property
    def laps_led(self):
        """Gets the laps_led of this DriverSummaryByTrack.  # noqa: E501

        The number of laps led  # noqa: E501

        :return: The laps_led of this DriverSummaryByTrack.  # noqa: E501
        :rtype: int
        """
        return self._laps_led

    @laps_led.setter
    def laps_led(self, laps_led):
        """Sets the laps_led of this DriverSummaryByTrack.

        The number of laps led  # noqa: E501

        :param laps_led: The laps_led of this DriverSummaryByTrack.  # noqa: E501
        :type: int
        """

        self._laps_led = laps_led

    @property
    def lead_lap_finish(self):
        """Gets the lead_lap_finish of this DriverSummaryByTrack.  # noqa: E501

        The number of finishes where the driver was on the lead lap  # noqa: E501

        :return: The lead_lap_finish of this DriverSummaryByTrack.  # noqa: E501
        :rtype: int
        """
        return self._lead_lap_finish

    @lead_lap_finish.setter
    def lead_lap_finish(self, lead_lap_finish):
        """Sets the lead_lap_finish of this DriverSummaryByTrack.

        The number of finishes where the driver was on the lead lap  # noqa: E501

        :param lead_lap_finish: The lead_lap_finish of this DriverSummaryByTrack.  # noqa: E501
        :type: int
        """

        self._lead_lap_finish = lead_lap_finish

    @property
    def miles_completed(self):
        """Gets the miles_completed of this DriverSummaryByTrack.  # noqa: E501

        Total miles completed  # noqa: E501

        :return: The miles_completed of this DriverSummaryByTrack.  # noqa: E501
        :rtype: float
        """
        return self._miles_completed

    @miles_completed.setter
    def miles_completed(self, miles_completed):
        """Sets the miles_completed of this DriverSummaryByTrack.

        Total miles completed  # noqa: E501

        :param miles_completed: The miles_completed of this DriverSummaryByTrack.  # noqa: E501
        :type: float
        """

        self._miles_completed = miles_completed

    @property
    def poles(self):
        """Gets the poles of this DriverSummaryByTrack.  # noqa: E501

        The number of times the driver earned the pole position  # noqa: E501

        :return: The poles of this DriverSummaryByTrack.  # noqa: E501
        :rtype: int
        """
        return self._poles

    @poles.setter
    def poles(self, poles):
        """Sets the poles of this DriverSummaryByTrack.

        The number of times the driver earned the pole position  # noqa: E501

        :param poles: The poles of this DriverSummaryByTrack.  # noqa: E501
        :type: int
        """

        self._poles = poles

    @property
    def running_at_finish(self):
        """Gets the running_at_finish of this DriverSummaryByTrack.  # noqa: E501

        Running at finish  # noqa: E501

        :return: The running_at_finish of this DriverSummaryByTrack.  # noqa: E501
        :rtype: int
        """
        return self._running_at_finish

    @running_at_finish.setter
    def running_at_finish(self, running_at_finish):
        """Sets the running_at_finish of this DriverSummaryByTrack.

        Running at finish  # noqa: E501

        :param running_at_finish: The running_at_finish of this DriverSummaryByTrack.  # noqa: E501
        :type: int
        """

        self._running_at_finish = running_at_finish

    @property
    def series_id(self):
        """Gets the series_id of this DriverSummaryByTrack.  # noqa: E501

        Series ID  # noqa: E501

        :return: The series_id of this DriverSummaryByTrack.  # noqa: E501
        :rtype: int
        """
        return self._series_id

    @series_id.setter
    def series_id(self, series_id):
        """Sets the series_id of this DriverSummaryByTrack.

        Series ID  # noqa: E501

        :param series_id: The series_id of this DriverSummaryByTrack.  # noqa: E501
        :type: int
        """

        self._series_id = series_id

    @property
    def top5(self):
        """Gets the top5 of this DriverSummaryByTrack.  # noqa: E501

        The number of top 5 finishes  # noqa: E501

        :return: The top5 of this DriverSummaryByTrack.  # noqa: E501
        :rtype: int
        """
        return self._top5

    @top5.setter
    def top5(self, top5):
        """Sets the top5 of this DriverSummaryByTrack.

        The number of top 5 finishes  # noqa: E501

        :param top5: The top5 of this DriverSummaryByTrack.  # noqa: E501
        :type: int
        """

        self._top5 = top5

    @property
    def top10(self):
        """Gets the top10 of this DriverSummaryByTrack.  # noqa: E501

        The number of top 10 finishes  # noqa: E501

        :return: The top10 of this DriverSummaryByTrack.  # noqa: E501
        :rtype: int
        """
        return self._top10

    @top10.setter
    def top10(self, top10):
        """Sets the top10 of this DriverSummaryByTrack.

        The number of top 10 finishes  # noqa: E501

        :param top10: The top10 of this DriverSummaryByTrack.  # noqa: E501
        :type: int
        """

        self._top10 = top10

    @property
    def total_races(self):
        """Gets the total_races of this DriverSummaryByTrack.  # noqa: E501

        The total number of races  # noqa: E501

        :return: The total_races of this DriverSummaryByTrack.  # noqa: E501
        :rtype: int
        """
        return self._total_races

    @total_races.setter
    def total_races(self, total_races):
        """Sets the total_races of this DriverSummaryByTrack.

        The total number of races  # noqa: E501

        :param total_races: The total_races of this DriverSummaryByTrack.  # noqa: E501
        :type: int
        """

        self._total_races = total_races

    @property
    def wins(self):
        """Gets the wins of this DriverSummaryByTrack.  # noqa: E501

        Race wins  # noqa: E501

        :return: The wins of this DriverSummaryByTrack.  # noqa: E501
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this DriverSummaryByTrack.

        Race wins  # noqa: E501

        :param wins: The wins of this DriverSummaryByTrack.  # noqa: E501
        :type: int
        """

        self._wins = wins

    @property
    def season(self):
        """Gets the season of this DriverSummaryByTrack.  # noqa: E501

        Race season  # noqa: E501

        :return: The season of this DriverSummaryByTrack.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this DriverSummaryByTrack.

        Race season  # noqa: E501

        :param season: The season of this DriverSummaryByTrack.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def track_id(self):
        """Gets the track_id of this DriverSummaryByTrack.  # noqa: E501

        Track Id  # noqa: E501

        :return: The track_id of this DriverSummaryByTrack.  # noqa: E501
        :rtype: int
        """
        return self._track_id

    @track_id.setter
    def track_id(self, track_id):
        """Sets the track_id of this DriverSummaryByTrack.

        Track Id  # noqa: E501

        :param track_id: The track_id of this DriverSummaryByTrack.  # noqa: E501
        :type: int
        """

        self._track_id = track_id

    @property
    def track_name(self):
        """Gets the track_name of this DriverSummaryByTrack.  # noqa: E501

        Track name  # noqa: E501

        :return: The track_name of this DriverSummaryByTrack.  # noqa: E501
        :rtype: str
        """
        return self._track_name

    @track_name.setter
    def track_name(self, track_name):
        """Sets the track_name of this DriverSummaryByTrack.

        Track name  # noqa: E501

        :param track_name: The track_name of this DriverSummaryByTrack.  # noqa: E501
        :type: str
        """

        self._track_name = track_name

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
        if issubclass(DriverSummaryByTrack, dict):
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
        if not isinstance(other, DriverSummaryByTrack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
