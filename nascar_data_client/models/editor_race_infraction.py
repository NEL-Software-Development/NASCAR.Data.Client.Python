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


class EditorRaceInfraction(object):
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
        'publish_state': 'PublishState',
        'id': 'int',
        'tracking_id': 'str',
        'in_data_warehouse': 'bool',
        'manually_set': 'bool',
        'last_update': 'datetime',
        'last_updated_by': 'str',
        'nascar_one_race_id': 'int',
        'timing_run_id': 'int',
        'racing_infraction_id': 'int',
        'vehicle': 'str',
        'infraction': 'str',
        'lap': 'int',
        'lap_assessed': 'int',
        'time_of_race': 'datetime',
        'flag_state': 'str',
        'penalty': 'str',
        'notes': 'str'
    }

    attribute_map = {
        'publish_state': 'PublishState',
        'id': 'id',
        'tracking_id': 'tracking_id',
        'in_data_warehouse': 'InDataWarehouse',
        'manually_set': 'Manually_Set',
        'last_update': 'LastUpdate',
        'last_updated_by': 'LastUpdatedBy',
        'nascar_one_race_id': 'NascarOne_RaceId',
        'timing_run_id': 'Timing_RunId',
        'racing_infraction_id': 'Racing_InfractionId',
        'vehicle': 'Vehicle',
        'infraction': 'Infraction',
        'lap': 'Lap',
        'lap_assessed': 'LapAssessed',
        'time_of_race': 'Time_Of_Race',
        'flag_state': 'FlagState',
        'penalty': 'Penalty',
        'notes': 'Notes'
    }

    def __init__(self, publish_state=None, id=None, tracking_id=None, in_data_warehouse=None, manually_set=None, last_update=None, last_updated_by=None, nascar_one_race_id=None, timing_run_id=None, racing_infraction_id=None, vehicle=None, infraction=None, lap=None, lap_assessed=None, time_of_race=None, flag_state=None, penalty=None, notes=None):  # noqa: E501
        """EditorRaceInfraction - a model defined in Swagger"""  # noqa: E501
        self._publish_state = None
        self._id = None
        self._tracking_id = None
        self._in_data_warehouse = None
        self._manually_set = None
        self._last_update = None
        self._last_updated_by = None
        self._nascar_one_race_id = None
        self._timing_run_id = None
        self._racing_infraction_id = None
        self._vehicle = None
        self._infraction = None
        self._lap = None
        self._lap_assessed = None
        self._time_of_race = None
        self._flag_state = None
        self._penalty = None
        self._notes = None
        self.discriminator = None
        if publish_state is not None:
            self.publish_state = publish_state
        if id is not None:
            self.id = id
        if tracking_id is not None:
            self.tracking_id = tracking_id
        if in_data_warehouse is not None:
            self.in_data_warehouse = in_data_warehouse
        if manually_set is not None:
            self.manually_set = manually_set
        if last_update is not None:
            self.last_update = last_update
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        if nascar_one_race_id is not None:
            self.nascar_one_race_id = nascar_one_race_id
        if timing_run_id is not None:
            self.timing_run_id = timing_run_id
        if racing_infraction_id is not None:
            self.racing_infraction_id = racing_infraction_id
        if vehicle is not None:
            self.vehicle = vehicle
        if infraction is not None:
            self.infraction = infraction
        if lap is not None:
            self.lap = lap
        if lap_assessed is not None:
            self.lap_assessed = lap_assessed
        if time_of_race is not None:
            self.time_of_race = time_of_race
        if flag_state is not None:
            self.flag_state = flag_state
        if penalty is not None:
            self.penalty = penalty
        if notes is not None:
            self.notes = notes

    @property
    def publish_state(self):
        """Gets the publish_state of this EditorRaceInfraction.  # noqa: E501


        :return: The publish_state of this EditorRaceInfraction.  # noqa: E501
        :rtype: PublishState
        """
        return self._publish_state

    @publish_state.setter
    def publish_state(self, publish_state):
        """Sets the publish_state of this EditorRaceInfraction.


        :param publish_state: The publish_state of this EditorRaceInfraction.  # noqa: E501
        :type: PublishState
        """

        self._publish_state = publish_state

    @property
    def id(self):
        """Gets the id of this EditorRaceInfraction.  # noqa: E501


        :return: The id of this EditorRaceInfraction.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EditorRaceInfraction.


        :param id: The id of this EditorRaceInfraction.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def tracking_id(self):
        """Gets the tracking_id of this EditorRaceInfraction.  # noqa: E501


        :return: The tracking_id of this EditorRaceInfraction.  # noqa: E501
        :rtype: str
        """
        return self._tracking_id

    @tracking_id.setter
    def tracking_id(self, tracking_id):
        """Sets the tracking_id of this EditorRaceInfraction.


        :param tracking_id: The tracking_id of this EditorRaceInfraction.  # noqa: E501
        :type: str
        """

        self._tracking_id = tracking_id

    @property
    def in_data_warehouse(self):
        """Gets the in_data_warehouse of this EditorRaceInfraction.  # noqa: E501


        :return: The in_data_warehouse of this EditorRaceInfraction.  # noqa: E501
        :rtype: bool
        """
        return self._in_data_warehouse

    @in_data_warehouse.setter
    def in_data_warehouse(self, in_data_warehouse):
        """Sets the in_data_warehouse of this EditorRaceInfraction.


        :param in_data_warehouse: The in_data_warehouse of this EditorRaceInfraction.  # noqa: E501
        :type: bool
        """

        self._in_data_warehouse = in_data_warehouse

    @property
    def manually_set(self):
        """Gets the manually_set of this EditorRaceInfraction.  # noqa: E501


        :return: The manually_set of this EditorRaceInfraction.  # noqa: E501
        :rtype: bool
        """
        return self._manually_set

    @manually_set.setter
    def manually_set(self, manually_set):
        """Sets the manually_set of this EditorRaceInfraction.


        :param manually_set: The manually_set of this EditorRaceInfraction.  # noqa: E501
        :type: bool
        """

        self._manually_set = manually_set

    @property
    def last_update(self):
        """Gets the last_update of this EditorRaceInfraction.  # noqa: E501


        :return: The last_update of this EditorRaceInfraction.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this EditorRaceInfraction.


        :param last_update: The last_update of this EditorRaceInfraction.  # noqa: E501
        :type: datetime
        """

        self._last_update = last_update

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this EditorRaceInfraction.  # noqa: E501


        :return: The last_updated_by of this EditorRaceInfraction.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this EditorRaceInfraction.


        :param last_updated_by: The last_updated_by of this EditorRaceInfraction.  # noqa: E501
        :type: str
        """

        self._last_updated_by = last_updated_by

    @property
    def nascar_one_race_id(self):
        """Gets the nascar_one_race_id of this EditorRaceInfraction.  # noqa: E501


        :return: The nascar_one_race_id of this EditorRaceInfraction.  # noqa: E501
        :rtype: int
        """
        return self._nascar_one_race_id

    @nascar_one_race_id.setter
    def nascar_one_race_id(self, nascar_one_race_id):
        """Sets the nascar_one_race_id of this EditorRaceInfraction.


        :param nascar_one_race_id: The nascar_one_race_id of this EditorRaceInfraction.  # noqa: E501
        :type: int
        """

        self._nascar_one_race_id = nascar_one_race_id

    @property
    def timing_run_id(self):
        """Gets the timing_run_id of this EditorRaceInfraction.  # noqa: E501


        :return: The timing_run_id of this EditorRaceInfraction.  # noqa: E501
        :rtype: int
        """
        return self._timing_run_id

    @timing_run_id.setter
    def timing_run_id(self, timing_run_id):
        """Sets the timing_run_id of this EditorRaceInfraction.


        :param timing_run_id: The timing_run_id of this EditorRaceInfraction.  # noqa: E501
        :type: int
        """

        self._timing_run_id = timing_run_id

    @property
    def racing_infraction_id(self):
        """Gets the racing_infraction_id of this EditorRaceInfraction.  # noqa: E501


        :return: The racing_infraction_id of this EditorRaceInfraction.  # noqa: E501
        :rtype: int
        """
        return self._racing_infraction_id

    @racing_infraction_id.setter
    def racing_infraction_id(self, racing_infraction_id):
        """Sets the racing_infraction_id of this EditorRaceInfraction.


        :param racing_infraction_id: The racing_infraction_id of this EditorRaceInfraction.  # noqa: E501
        :type: int
        """

        self._racing_infraction_id = racing_infraction_id

    @property
    def vehicle(self):
        """Gets the vehicle of this EditorRaceInfraction.  # noqa: E501


        :return: The vehicle of this EditorRaceInfraction.  # noqa: E501
        :rtype: str
        """
        return self._vehicle

    @vehicle.setter
    def vehicle(self, vehicle):
        """Sets the vehicle of this EditorRaceInfraction.


        :param vehicle: The vehicle of this EditorRaceInfraction.  # noqa: E501
        :type: str
        """

        self._vehicle = vehicle

    @property
    def infraction(self):
        """Gets the infraction of this EditorRaceInfraction.  # noqa: E501


        :return: The infraction of this EditorRaceInfraction.  # noqa: E501
        :rtype: str
        """
        return self._infraction

    @infraction.setter
    def infraction(self, infraction):
        """Sets the infraction of this EditorRaceInfraction.


        :param infraction: The infraction of this EditorRaceInfraction.  # noqa: E501
        :type: str
        """

        self._infraction = infraction

    @property
    def lap(self):
        """Gets the lap of this EditorRaceInfraction.  # noqa: E501


        :return: The lap of this EditorRaceInfraction.  # noqa: E501
        :rtype: int
        """
        return self._lap

    @lap.setter
    def lap(self, lap):
        """Sets the lap of this EditorRaceInfraction.


        :param lap: The lap of this EditorRaceInfraction.  # noqa: E501
        :type: int
        """

        self._lap = lap

    @property
    def lap_assessed(self):
        """Gets the lap_assessed of this EditorRaceInfraction.  # noqa: E501


        :return: The lap_assessed of this EditorRaceInfraction.  # noqa: E501
        :rtype: int
        """
        return self._lap_assessed

    @lap_assessed.setter
    def lap_assessed(self, lap_assessed):
        """Sets the lap_assessed of this EditorRaceInfraction.


        :param lap_assessed: The lap_assessed of this EditorRaceInfraction.  # noqa: E501
        :type: int
        """

        self._lap_assessed = lap_assessed

    @property
    def time_of_race(self):
        """Gets the time_of_race of this EditorRaceInfraction.  # noqa: E501


        :return: The time_of_race of this EditorRaceInfraction.  # noqa: E501
        :rtype: datetime
        """
        return self._time_of_race

    @time_of_race.setter
    def time_of_race(self, time_of_race):
        """Sets the time_of_race of this EditorRaceInfraction.


        :param time_of_race: The time_of_race of this EditorRaceInfraction.  # noqa: E501
        :type: datetime
        """

        self._time_of_race = time_of_race

    @property
    def flag_state(self):
        """Gets the flag_state of this EditorRaceInfraction.  # noqa: E501


        :return: The flag_state of this EditorRaceInfraction.  # noqa: E501
        :rtype: str
        """
        return self._flag_state

    @flag_state.setter
    def flag_state(self, flag_state):
        """Sets the flag_state of this EditorRaceInfraction.


        :param flag_state: The flag_state of this EditorRaceInfraction.  # noqa: E501
        :type: str
        """

        self._flag_state = flag_state

    @property
    def penalty(self):
        """Gets the penalty of this EditorRaceInfraction.  # noqa: E501


        :return: The penalty of this EditorRaceInfraction.  # noqa: E501
        :rtype: str
        """
        return self._penalty

    @penalty.setter
    def penalty(self, penalty):
        """Sets the penalty of this EditorRaceInfraction.


        :param penalty: The penalty of this EditorRaceInfraction.  # noqa: E501
        :type: str
        """

        self._penalty = penalty

    @property
    def notes(self):
        """Gets the notes of this EditorRaceInfraction.  # noqa: E501


        :return: The notes of this EditorRaceInfraction.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this EditorRaceInfraction.


        :param notes: The notes of this EditorRaceInfraction.  # noqa: E501
        :type: str
        """

        self._notes = notes

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
        if issubclass(EditorRaceInfraction, dict):
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
        if not isinstance(other, EditorRaceInfraction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
