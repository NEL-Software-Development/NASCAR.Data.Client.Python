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


class RaceDetails(object):
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
        'history_race_id': 'int',
        'series_id': 'int',
        'name': 'str',
        'promoter': 'str',
        'laps': 'int',
        'distance': 'float',
        'practice_results': 'str',
        'qualifying_results': 'str',
        'race_results': 'str',
        'cautions': 'str',
        'infractions': 'str',
        'lap_leaders': 'str',
        'pitstops': 'str',
        '_date': 'datetime',
        'comments': 'str',
        'track_name': 'str',
        'track_id': 'int',
        'inspection_complete': 'bool',
        'entries': 'list[RunEntry]',
        'runs': 'list[RunDetails]',
        'schedule': 'list[WeekendSchedule]'
    }

    attribute_map = {
        'id': 'id',
        'history_race_id': 'history_race_id',
        'series_id': 'series_id',
        'name': 'name',
        'promoter': 'promoter',
        'laps': 'laps',
        'distance': 'distance',
        'practice_results': 'practice_results',
        'qualifying_results': 'qualifying_results',
        'race_results': 'race_results',
        'cautions': 'cautions',
        'infractions': 'infractions',
        'lap_leaders': 'lap_leaders',
        'pitstops': 'pitstops',
        '_date': 'date',
        'comments': 'comments',
        'track_name': 'track_name',
        'track_id': 'track_id',
        'inspection_complete': 'inspection_complete',
        'entries': 'entries',
        'runs': 'runs',
        'schedule': 'schedule'
    }

    def __init__(self, id=None, history_race_id=-1, series_id=None, name=None, promoter=None, laps=None, distance=None, practice_results=None, qualifying_results=None, race_results=None, cautions=None, infractions=None, lap_leaders=None, pitstops=None, _date=None, comments=None, track_name=None, track_id=None, inspection_complete=None, entries=None, runs=None, schedule=None):  # noqa: E501
        """RaceDetails - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._history_race_id = None
        self._series_id = None
        self._name = None
        self._promoter = None
        self._laps = None
        self._distance = None
        self._practice_results = None
        self._qualifying_results = None
        self._race_results = None
        self._cautions = None
        self._infractions = None
        self._lap_leaders = None
        self._pitstops = None
        self.__date = None
        self._comments = None
        self._track_name = None
        self._track_id = None
        self._inspection_complete = None
        self._entries = None
        self._runs = None
        self._schedule = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if history_race_id is not None:
            self.history_race_id = history_race_id
        if series_id is not None:
            self.series_id = series_id
        if name is not None:
            self.name = name
        if promoter is not None:
            self.promoter = promoter
        if laps is not None:
            self.laps = laps
        if distance is not None:
            self.distance = distance
        if practice_results is not None:
            self.practice_results = practice_results
        if qualifying_results is not None:
            self.qualifying_results = qualifying_results
        if race_results is not None:
            self.race_results = race_results
        if cautions is not None:
            self.cautions = cautions
        if infractions is not None:
            self.infractions = infractions
        if lap_leaders is not None:
            self.lap_leaders = lap_leaders
        if pitstops is not None:
            self.pitstops = pitstops
        if _date is not None:
            self._date = _date
        if comments is not None:
            self.comments = comments
        if track_name is not None:
            self.track_name = track_name
        if track_id is not None:
            self.track_id = track_id
        if inspection_complete is not None:
            self.inspection_complete = inspection_complete
        if entries is not None:
            self.entries = entries
        if runs is not None:
            self.runs = runs
        if schedule is not None:
            self.schedule = schedule

    @property
    def id(self):
        """Gets the id of this RaceDetails.  # noqa: E501

        The id of the race  # noqa: E501

        :return: The id of this RaceDetails.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RaceDetails.

        The id of the race  # noqa: E501

        :param id: The id of this RaceDetails.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def history_race_id(self):
        """Gets the history_race_id of this RaceDetails.  # noqa: E501

        The race id from the history database  # noqa: E501

        :return: The history_race_id of this RaceDetails.  # noqa: E501
        :rtype: int
        """
        return self._history_race_id

    @history_race_id.setter
    def history_race_id(self, history_race_id):
        """Sets the history_race_id of this RaceDetails.

        The race id from the history database  # noqa: E501

        :param history_race_id: The history_race_id of this RaceDetails.  # noqa: E501
        :type: int
        """

        self._history_race_id = history_race_id

    @property
    def series_id(self):
        """Gets the series_id of this RaceDetails.  # noqa: E501

        The series id of the race  # noqa: E501

        :return: The series_id of this RaceDetails.  # noqa: E501
        :rtype: int
        """
        return self._series_id

    @series_id.setter
    def series_id(self, series_id):
        """Sets the series_id of this RaceDetails.

        The series id of the race  # noqa: E501

        :param series_id: The series_id of this RaceDetails.  # noqa: E501
        :type: int
        """

        self._series_id = series_id

    @property
    def name(self):
        """Gets the name of this RaceDetails.  # noqa: E501

        The race name  # noqa: E501

        :return: The name of this RaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RaceDetails.

        The race name  # noqa: E501

        :param name: The name of this RaceDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def promoter(self):
        """Gets the promoter of this RaceDetails.  # noqa: E501

        The promoter of the race  # noqa: E501

        :return: The promoter of this RaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._promoter

    @promoter.setter
    def promoter(self, promoter):
        """Sets the promoter of this RaceDetails.

        The promoter of the race  # noqa: E501

        :param promoter: The promoter of this RaceDetails.  # noqa: E501
        :type: str
        """

        self._promoter = promoter

    @property
    def laps(self):
        """Gets the laps of this RaceDetails.  # noqa: E501

        Laps  # noqa: E501

        :return: The laps of this RaceDetails.  # noqa: E501
        :rtype: int
        """
        return self._laps

    @laps.setter
    def laps(self, laps):
        """Sets the laps of this RaceDetails.

        Laps  # noqa: E501

        :param laps: The laps of this RaceDetails.  # noqa: E501
        :type: int
        """

        self._laps = laps

    @property
    def distance(self):
        """Gets the distance of this RaceDetails.  # noqa: E501

        Race distance  # noqa: E501

        :return: The distance of this RaceDetails.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this RaceDetails.

        Race distance  # noqa: E501

        :param distance: The distance of this RaceDetails.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def practice_results(self):
        """Gets the practice_results of this RaceDetails.  # noqa: E501

        URL to Practice results  # noqa: E501

        :return: The practice_results of this RaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._practice_results

    @practice_results.setter
    def practice_results(self, practice_results):
        """Sets the practice_results of this RaceDetails.

        URL to Practice results  # noqa: E501

        :param practice_results: The practice_results of this RaceDetails.  # noqa: E501
        :type: str
        """

        self._practice_results = practice_results

    @property
    def qualifying_results(self):
        """Gets the qualifying_results of this RaceDetails.  # noqa: E501

        URL to Qualifying results  # noqa: E501

        :return: The qualifying_results of this RaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._qualifying_results

    @qualifying_results.setter
    def qualifying_results(self, qualifying_results):
        """Sets the qualifying_results of this RaceDetails.

        URL to Qualifying results  # noqa: E501

        :param qualifying_results: The qualifying_results of this RaceDetails.  # noqa: E501
        :type: str
        """

        self._qualifying_results = qualifying_results

    @property
    def race_results(self):
        """Gets the race_results of this RaceDetails.  # noqa: E501

        URL to race results  # noqa: E501

        :return: The race_results of this RaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._race_results

    @race_results.setter
    def race_results(self, race_results):
        """Sets the race_results of this RaceDetails.

        URL to race results  # noqa: E501

        :param race_results: The race_results of this RaceDetails.  # noqa: E501
        :type: str
        """

        self._race_results = race_results

    @property
    def cautions(self):
        """Gets the cautions of this RaceDetails.  # noqa: E501

        URL to race cautions  # noqa: E501

        :return: The cautions of this RaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._cautions

    @cautions.setter
    def cautions(self, cautions):
        """Sets the cautions of this RaceDetails.

        URL to race cautions  # noqa: E501

        :param cautions: The cautions of this RaceDetails.  # noqa: E501
        :type: str
        """

        self._cautions = cautions

    @property
    def infractions(self):
        """Gets the infractions of this RaceDetails.  # noqa: E501

        URL to race infractions  # noqa: E501

        :return: The infractions of this RaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._infractions

    @infractions.setter
    def infractions(self, infractions):
        """Sets the infractions of this RaceDetails.

        URL to race infractions  # noqa: E501

        :param infractions: The infractions of this RaceDetails.  # noqa: E501
        :type: str
        """

        self._infractions = infractions

    @property
    def lap_leaders(self):
        """Gets the lap_leaders of this RaceDetails.  # noqa: E501

        URL to race lap leaders  # noqa: E501

        :return: The lap_leaders of this RaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._lap_leaders

    @lap_leaders.setter
    def lap_leaders(self, lap_leaders):
        """Sets the lap_leaders of this RaceDetails.

        URL to race lap leaders  # noqa: E501

        :param lap_leaders: The lap_leaders of this RaceDetails.  # noqa: E501
        :type: str
        """

        self._lap_leaders = lap_leaders

    @property
    def pitstops(self):
        """Gets the pitstops of this RaceDetails.  # noqa: E501

        URL to race pitstops  # noqa: E501

        :return: The pitstops of this RaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._pitstops

    @pitstops.setter
    def pitstops(self, pitstops):
        """Sets the pitstops of this RaceDetails.

        URL to race pitstops  # noqa: E501

        :param pitstops: The pitstops of this RaceDetails.  # noqa: E501
        :type: str
        """

        self._pitstops = pitstops

    @property
    def _date(self):
        """Gets the _date of this RaceDetails.  # noqa: E501

        Race date  # noqa: E501

        :return: The _date of this RaceDetails.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this RaceDetails.

        Race date  # noqa: E501

        :param _date: The _date of this RaceDetails.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def comments(self):
        """Gets the comments of this RaceDetails.  # noqa: E501

        Race Comments  # noqa: E501

        :return: The comments of this RaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this RaceDetails.

        Race Comments  # noqa: E501

        :param comments: The comments of this RaceDetails.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def track_name(self):
        """Gets the track_name of this RaceDetails.  # noqa: E501

        Track Name  # noqa: E501

        :return: The track_name of this RaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._track_name

    @track_name.setter
    def track_name(self, track_name):
        """Sets the track_name of this RaceDetails.

        Track Name  # noqa: E501

        :param track_name: The track_name of this RaceDetails.  # noqa: E501
        :type: str
        """

        self._track_name = track_name

    @property
    def track_id(self):
        """Gets the track_id of this RaceDetails.  # noqa: E501

        Track Id  # noqa: E501

        :return: The track_id of this RaceDetails.  # noqa: E501
        :rtype: int
        """
        return self._track_id

    @track_id.setter
    def track_id(self, track_id):
        """Sets the track_id of this RaceDetails.

        Track Id  # noqa: E501

        :param track_id: The track_id of this RaceDetails.  # noqa: E501
        :type: int
        """

        self._track_id = track_id

    @property
    def inspection_complete(self):
        """Gets the inspection_complete of this RaceDetails.  # noqa: E501

        Has inspection been completed  # noqa: E501

        :return: The inspection_complete of this RaceDetails.  # noqa: E501
        :rtype: bool
        """
        return self._inspection_complete

    @inspection_complete.setter
    def inspection_complete(self, inspection_complete):
        """Sets the inspection_complete of this RaceDetails.

        Has inspection been completed  # noqa: E501

        :param inspection_complete: The inspection_complete of this RaceDetails.  # noqa: E501
        :type: bool
        """

        self._inspection_complete = inspection_complete

    @property
    def entries(self):
        """Gets the entries of this RaceDetails.  # noqa: E501

        Race entries  # noqa: E501

        :return: The entries of this RaceDetails.  # noqa: E501
        :rtype: list[RunEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this RaceDetails.

        Race entries  # noqa: E501

        :param entries: The entries of this RaceDetails.  # noqa: E501
        :type: list[RunEntry]
        """

        self._entries = entries

    @property
    def runs(self):
        """Gets the runs of this RaceDetails.  # noqa: E501

        Runs  # noqa: E501

        :return: The runs of this RaceDetails.  # noqa: E501
        :rtype: list[RunDetails]
        """
        return self._runs

    @runs.setter
    def runs(self, runs):
        """Sets the runs of this RaceDetails.

        Runs  # noqa: E501

        :param runs: The runs of this RaceDetails.  # noqa: E501
        :type: list[RunDetails]
        """

        self._runs = runs

    @property
    def schedule(self):
        """Gets the schedule of this RaceDetails.  # noqa: E501

        Weekend Schedule  # noqa: E501

        :return: The schedule of this RaceDetails.  # noqa: E501
        :rtype: list[WeekendSchedule]
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this RaceDetails.

        Weekend Schedule  # noqa: E501

        :param schedule: The schedule of this RaceDetails.  # noqa: E501
        :type: list[WeekendSchedule]
        """

        self._schedule = schedule

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
        if issubclass(RaceDetails, dict):
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
        if not isinstance(other, RaceDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
