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


class Race(object):
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
        'principal_race_id': 'int',
        'raceweek_id': 'int',
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
        'comments': 'str'
    }

    attribute_map = {
        'id': 'id',
        'principal_race_id': 'principal_race_id',
        'raceweek_id': 'raceweek_id',
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
        'comments': 'comments'
    }

    def __init__(self, id=None, principal_race_id=None, raceweek_id=None, series_id=None, name=None, promoter=None, laps=None, distance=None, practice_results=None, qualifying_results=None, race_results=None, cautions=None, infractions=None, lap_leaders=None, pitstops=None, _date=None, comments=None):  # noqa: E501
        """Race - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._principal_race_id = None
        self._raceweek_id = None
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
        self.discriminator = None
        if id is not None:
            self.id = id
        if principal_race_id is not None:
            self.principal_race_id = principal_race_id
        if raceweek_id is not None:
            self.raceweek_id = raceweek_id
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

    @property
    def id(self):
        """Gets the id of this Race.  # noqa: E501

        The id of the race  # noqa: E501

        :return: The id of this Race.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Race.

        The id of the race  # noqa: E501

        :param id: The id of this Race.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def principal_race_id(self):
        """Gets the principal_race_id of this Race.  # noqa: E501

        The principal race id of the race  # noqa: E501

        :return: The principal_race_id of this Race.  # noqa: E501
        :rtype: int
        """
        return self._principal_race_id

    @principal_race_id.setter
    def principal_race_id(self, principal_race_id):
        """Sets the principal_race_id of this Race.

        The principal race id of the race  # noqa: E501

        :param principal_race_id: The principal_race_id of this Race.  # noqa: E501
        :type: int
        """

        self._principal_race_id = principal_race_id

    @property
    def raceweek_id(self):
        """Gets the raceweek_id of this Race.  # noqa: E501

        The race  # noqa: E501

        :return: The raceweek_id of this Race.  # noqa: E501
        :rtype: int
        """
        return self._raceweek_id

    @raceweek_id.setter
    def raceweek_id(self, raceweek_id):
        """Sets the raceweek_id of this Race.

        The race  # noqa: E501

        :param raceweek_id: The raceweek_id of this Race.  # noqa: E501
        :type: int
        """

        self._raceweek_id = raceweek_id

    @property
    def series_id(self):
        """Gets the series_id of this Race.  # noqa: E501

        The series id of the race  # noqa: E501

        :return: The series_id of this Race.  # noqa: E501
        :rtype: int
        """
        return self._series_id

    @series_id.setter
    def series_id(self, series_id):
        """Sets the series_id of this Race.

        The series id of the race  # noqa: E501

        :param series_id: The series_id of this Race.  # noqa: E501
        :type: int
        """

        self._series_id = series_id

    @property
    def name(self):
        """Gets the name of this Race.  # noqa: E501

        The race name  # noqa: E501

        :return: The name of this Race.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Race.

        The race name  # noqa: E501

        :param name: The name of this Race.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def promoter(self):
        """Gets the promoter of this Race.  # noqa: E501

        The promoter of the race  # noqa: E501

        :return: The promoter of this Race.  # noqa: E501
        :rtype: str
        """
        return self._promoter

    @promoter.setter
    def promoter(self, promoter):
        """Sets the promoter of this Race.

        The promoter of the race  # noqa: E501

        :param promoter: The promoter of this Race.  # noqa: E501
        :type: str
        """

        self._promoter = promoter

    @property
    def laps(self):
        """Gets the laps of this Race.  # noqa: E501

        Laps  # noqa: E501

        :return: The laps of this Race.  # noqa: E501
        :rtype: int
        """
        return self._laps

    @laps.setter
    def laps(self, laps):
        """Sets the laps of this Race.

        Laps  # noqa: E501

        :param laps: The laps of this Race.  # noqa: E501
        :type: int
        """

        self._laps = laps

    @property
    def distance(self):
        """Gets the distance of this Race.  # noqa: E501

        Race distance  # noqa: E501

        :return: The distance of this Race.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this Race.

        Race distance  # noqa: E501

        :param distance: The distance of this Race.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def practice_results(self):
        """Gets the practice_results of this Race.  # noqa: E501

        URL to practice results  # noqa: E501

        :return: The practice_results of this Race.  # noqa: E501
        :rtype: str
        """
        return self._practice_results

    @practice_results.setter
    def practice_results(self, practice_results):
        """Sets the practice_results of this Race.

        URL to practice results  # noqa: E501

        :param practice_results: The practice_results of this Race.  # noqa: E501
        :type: str
        """

        self._practice_results = practice_results

    @property
    def qualifying_results(self):
        """Gets the qualifying_results of this Race.  # noqa: E501

        URL to Qualifying results  # noqa: E501

        :return: The qualifying_results of this Race.  # noqa: E501
        :rtype: str
        """
        return self._qualifying_results

    @qualifying_results.setter
    def qualifying_results(self, qualifying_results):
        """Sets the qualifying_results of this Race.

        URL to Qualifying results  # noqa: E501

        :param qualifying_results: The qualifying_results of this Race.  # noqa: E501
        :type: str
        """

        self._qualifying_results = qualifying_results

    @property
    def race_results(self):
        """Gets the race_results of this Race.  # noqa: E501

        URL to race results  # noqa: E501

        :return: The race_results of this Race.  # noqa: E501
        :rtype: str
        """
        return self._race_results

    @race_results.setter
    def race_results(self, race_results):
        """Sets the race_results of this Race.

        URL to race results  # noqa: E501

        :param race_results: The race_results of this Race.  # noqa: E501
        :type: str
        """

        self._race_results = race_results

    @property
    def cautions(self):
        """Gets the cautions of this Race.  # noqa: E501

        URL to race cautions  # noqa: E501

        :return: The cautions of this Race.  # noqa: E501
        :rtype: str
        """
        return self._cautions

    @cautions.setter
    def cautions(self, cautions):
        """Sets the cautions of this Race.

        URL to race cautions  # noqa: E501

        :param cautions: The cautions of this Race.  # noqa: E501
        :type: str
        """

        self._cautions = cautions

    @property
    def infractions(self):
        """Gets the infractions of this Race.  # noqa: E501

        URL to race infractions  # noqa: E501

        :return: The infractions of this Race.  # noqa: E501
        :rtype: str
        """
        return self._infractions

    @infractions.setter
    def infractions(self, infractions):
        """Sets the infractions of this Race.

        URL to race infractions  # noqa: E501

        :param infractions: The infractions of this Race.  # noqa: E501
        :type: str
        """

        self._infractions = infractions

    @property
    def lap_leaders(self):
        """Gets the lap_leaders of this Race.  # noqa: E501

        URL to race lap leaders  # noqa: E501

        :return: The lap_leaders of this Race.  # noqa: E501
        :rtype: str
        """
        return self._lap_leaders

    @lap_leaders.setter
    def lap_leaders(self, lap_leaders):
        """Sets the lap_leaders of this Race.

        URL to race lap leaders  # noqa: E501

        :param lap_leaders: The lap_leaders of this Race.  # noqa: E501
        :type: str
        """

        self._lap_leaders = lap_leaders

    @property
    def pitstops(self):
        """Gets the pitstops of this Race.  # noqa: E501

        URL to race pitstops  # noqa: E501

        :return: The pitstops of this Race.  # noqa: E501
        :rtype: str
        """
        return self._pitstops

    @pitstops.setter
    def pitstops(self, pitstops):
        """Sets the pitstops of this Race.

        URL to race pitstops  # noqa: E501

        :param pitstops: The pitstops of this Race.  # noqa: E501
        :type: str
        """

        self._pitstops = pitstops

    @property
    def _date(self):
        """Gets the _date of this Race.  # noqa: E501

        Race date  # noqa: E501

        :return: The _date of this Race.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Race.

        Race date  # noqa: E501

        :param _date: The _date of this Race.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def comments(self):
        """Gets the comments of this Race.  # noqa: E501

        Race comments  # noqa: E501

        :return: The comments of this Race.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this Race.

        Race comments  # noqa: E501

        :param comments: The comments of this Race.  # noqa: E501
        :type: str
        """

        self._comments = comments

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
        if issubclass(Race, dict):
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
        if not isinstance(other, Race):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
