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


class FlagMapping(object):
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
        'race_event_key': 'int',
        'nascar_one_race_id': 'int',
        'history_race_id': 'int',
        'timing_run_id': 'int',
        'run_flag_id': 'int',
        'start_lap': 'int',
        'end_lap': 'int',
        'num_laps': 'int',
        'time': 'datetime',
        'elapsed_time': 'int',
        'duration': 'int',
        'flag_id': 'int',
        'comment': 'str',
        'flag_state': 'str',
        'is_valid_flag': 'bool',
        'etl_run_id': 'int'
    }

    attribute_map = {
        'publish_state': 'PublishState',
        'id': 'id',
        'tracking_id': 'tracking_id',
        'in_data_warehouse': 'InDataWarehouse',
        'manually_set': 'Manually_Set',
        'last_update': 'LastUpdate',
        'last_updated_by': 'LastUpdatedBy',
        'race_event_key': 'RaceEventKey',
        'nascar_one_race_id': 'NascarOneRaceID',
        'history_race_id': 'HistoryRaceID',
        'timing_run_id': 'TimingRunID',
        'run_flag_id': 'RunFlagID',
        'start_lap': 'StartLap',
        'end_lap': 'EndLap',
        'num_laps': 'NumLaps',
        'time': 'Time',
        'elapsed_time': 'ElapsedTime',
        'duration': 'Duration',
        'flag_id': 'FlagID',
        'comment': 'Comment',
        'flag_state': 'FlagState',
        'is_valid_flag': 'IsValidFlag',
        'etl_run_id': 'ETLRunID'
    }

    def __init__(self, publish_state=None, id=None, tracking_id=None, in_data_warehouse=None, manually_set=None, last_update=None, last_updated_by=None, race_event_key=None, nascar_one_race_id=None, history_race_id=None, timing_run_id=None, run_flag_id=None, start_lap=None, end_lap=None, num_laps=None, time=None, elapsed_time=None, duration=None, flag_id=None, comment=None, flag_state=None, is_valid_flag=None, etl_run_id=None):  # noqa: E501
        """FlagMapping - a model defined in Swagger"""  # noqa: E501
        self._publish_state = None
        self._id = None
        self._tracking_id = None
        self._in_data_warehouse = None
        self._manually_set = None
        self._last_update = None
        self._last_updated_by = None
        self._race_event_key = None
        self._nascar_one_race_id = None
        self._history_race_id = None
        self._timing_run_id = None
        self._run_flag_id = None
        self._start_lap = None
        self._end_lap = None
        self._num_laps = None
        self._time = None
        self._elapsed_time = None
        self._duration = None
        self._flag_id = None
        self._comment = None
        self._flag_state = None
        self._is_valid_flag = None
        self._etl_run_id = None
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
        if race_event_key is not None:
            self.race_event_key = race_event_key
        if nascar_one_race_id is not None:
            self.nascar_one_race_id = nascar_one_race_id
        if history_race_id is not None:
            self.history_race_id = history_race_id
        if timing_run_id is not None:
            self.timing_run_id = timing_run_id
        if run_flag_id is not None:
            self.run_flag_id = run_flag_id
        if start_lap is not None:
            self.start_lap = start_lap
        if end_lap is not None:
            self.end_lap = end_lap
        if num_laps is not None:
            self.num_laps = num_laps
        if time is not None:
            self.time = time
        if elapsed_time is not None:
            self.elapsed_time = elapsed_time
        if duration is not None:
            self.duration = duration
        if flag_id is not None:
            self.flag_id = flag_id
        if comment is not None:
            self.comment = comment
        if flag_state is not None:
            self.flag_state = flag_state
        if is_valid_flag is not None:
            self.is_valid_flag = is_valid_flag
        if etl_run_id is not None:
            self.etl_run_id = etl_run_id

    @property
    def publish_state(self):
        """Gets the publish_state of this FlagMapping.  # noqa: E501


        :return: The publish_state of this FlagMapping.  # noqa: E501
        :rtype: PublishState
        """
        return self._publish_state

    @publish_state.setter
    def publish_state(self, publish_state):
        """Sets the publish_state of this FlagMapping.


        :param publish_state: The publish_state of this FlagMapping.  # noqa: E501
        :type: PublishState
        """

        self._publish_state = publish_state

    @property
    def id(self):
        """Gets the id of this FlagMapping.  # noqa: E501


        :return: The id of this FlagMapping.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FlagMapping.


        :param id: The id of this FlagMapping.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def tracking_id(self):
        """Gets the tracking_id of this FlagMapping.  # noqa: E501


        :return: The tracking_id of this FlagMapping.  # noqa: E501
        :rtype: str
        """
        return self._tracking_id

    @tracking_id.setter
    def tracking_id(self, tracking_id):
        """Sets the tracking_id of this FlagMapping.


        :param tracking_id: The tracking_id of this FlagMapping.  # noqa: E501
        :type: str
        """

        self._tracking_id = tracking_id

    @property
    def in_data_warehouse(self):
        """Gets the in_data_warehouse of this FlagMapping.  # noqa: E501


        :return: The in_data_warehouse of this FlagMapping.  # noqa: E501
        :rtype: bool
        """
        return self._in_data_warehouse

    @in_data_warehouse.setter
    def in_data_warehouse(self, in_data_warehouse):
        """Sets the in_data_warehouse of this FlagMapping.


        :param in_data_warehouse: The in_data_warehouse of this FlagMapping.  # noqa: E501
        :type: bool
        """

        self._in_data_warehouse = in_data_warehouse

    @property
    def manually_set(self):
        """Gets the manually_set of this FlagMapping.  # noqa: E501


        :return: The manually_set of this FlagMapping.  # noqa: E501
        :rtype: bool
        """
        return self._manually_set

    @manually_set.setter
    def manually_set(self, manually_set):
        """Sets the manually_set of this FlagMapping.


        :param manually_set: The manually_set of this FlagMapping.  # noqa: E501
        :type: bool
        """

        self._manually_set = manually_set

    @property
    def last_update(self):
        """Gets the last_update of this FlagMapping.  # noqa: E501


        :return: The last_update of this FlagMapping.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this FlagMapping.


        :param last_update: The last_update of this FlagMapping.  # noqa: E501
        :type: datetime
        """

        self._last_update = last_update

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this FlagMapping.  # noqa: E501


        :return: The last_updated_by of this FlagMapping.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this FlagMapping.


        :param last_updated_by: The last_updated_by of this FlagMapping.  # noqa: E501
        :type: str
        """

        self._last_updated_by = last_updated_by

    @property
    def race_event_key(self):
        """Gets the race_event_key of this FlagMapping.  # noqa: E501


        :return: The race_event_key of this FlagMapping.  # noqa: E501
        :rtype: int
        """
        return self._race_event_key

    @race_event_key.setter
    def race_event_key(self, race_event_key):
        """Sets the race_event_key of this FlagMapping.


        :param race_event_key: The race_event_key of this FlagMapping.  # noqa: E501
        :type: int
        """

        self._race_event_key = race_event_key

    @property
    def nascar_one_race_id(self):
        """Gets the nascar_one_race_id of this FlagMapping.  # noqa: E501


        :return: The nascar_one_race_id of this FlagMapping.  # noqa: E501
        :rtype: int
        """
        return self._nascar_one_race_id

    @nascar_one_race_id.setter
    def nascar_one_race_id(self, nascar_one_race_id):
        """Sets the nascar_one_race_id of this FlagMapping.


        :param nascar_one_race_id: The nascar_one_race_id of this FlagMapping.  # noqa: E501
        :type: int
        """

        self._nascar_one_race_id = nascar_one_race_id

    @property
    def history_race_id(self):
        """Gets the history_race_id of this FlagMapping.  # noqa: E501


        :return: The history_race_id of this FlagMapping.  # noqa: E501
        :rtype: int
        """
        return self._history_race_id

    @history_race_id.setter
    def history_race_id(self, history_race_id):
        """Sets the history_race_id of this FlagMapping.


        :param history_race_id: The history_race_id of this FlagMapping.  # noqa: E501
        :type: int
        """

        self._history_race_id = history_race_id

    @property
    def timing_run_id(self):
        """Gets the timing_run_id of this FlagMapping.  # noqa: E501


        :return: The timing_run_id of this FlagMapping.  # noqa: E501
        :rtype: int
        """
        return self._timing_run_id

    @timing_run_id.setter
    def timing_run_id(self, timing_run_id):
        """Sets the timing_run_id of this FlagMapping.


        :param timing_run_id: The timing_run_id of this FlagMapping.  # noqa: E501
        :type: int
        """

        self._timing_run_id = timing_run_id

    @property
    def run_flag_id(self):
        """Gets the run_flag_id of this FlagMapping.  # noqa: E501


        :return: The run_flag_id of this FlagMapping.  # noqa: E501
        :rtype: int
        """
        return self._run_flag_id

    @run_flag_id.setter
    def run_flag_id(self, run_flag_id):
        """Sets the run_flag_id of this FlagMapping.


        :param run_flag_id: The run_flag_id of this FlagMapping.  # noqa: E501
        :type: int
        """

        self._run_flag_id = run_flag_id

    @property
    def start_lap(self):
        """Gets the start_lap of this FlagMapping.  # noqa: E501


        :return: The start_lap of this FlagMapping.  # noqa: E501
        :rtype: int
        """
        return self._start_lap

    @start_lap.setter
    def start_lap(self, start_lap):
        """Sets the start_lap of this FlagMapping.


        :param start_lap: The start_lap of this FlagMapping.  # noqa: E501
        :type: int
        """

        self._start_lap = start_lap

    @property
    def end_lap(self):
        """Gets the end_lap of this FlagMapping.  # noqa: E501


        :return: The end_lap of this FlagMapping.  # noqa: E501
        :rtype: int
        """
        return self._end_lap

    @end_lap.setter
    def end_lap(self, end_lap):
        """Sets the end_lap of this FlagMapping.


        :param end_lap: The end_lap of this FlagMapping.  # noqa: E501
        :type: int
        """

        self._end_lap = end_lap

    @property
    def num_laps(self):
        """Gets the num_laps of this FlagMapping.  # noqa: E501


        :return: The num_laps of this FlagMapping.  # noqa: E501
        :rtype: int
        """
        return self._num_laps

    @num_laps.setter
    def num_laps(self, num_laps):
        """Sets the num_laps of this FlagMapping.


        :param num_laps: The num_laps of this FlagMapping.  # noqa: E501
        :type: int
        """

        self._num_laps = num_laps

    @property
    def time(self):
        """Gets the time of this FlagMapping.  # noqa: E501


        :return: The time of this FlagMapping.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this FlagMapping.


        :param time: The time of this FlagMapping.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this FlagMapping.  # noqa: E501


        :return: The elapsed_time of this FlagMapping.  # noqa: E501
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this FlagMapping.


        :param elapsed_time: The elapsed_time of this FlagMapping.  # noqa: E501
        :type: int
        """

        self._elapsed_time = elapsed_time

    @property
    def duration(self):
        """Gets the duration of this FlagMapping.  # noqa: E501


        :return: The duration of this FlagMapping.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this FlagMapping.


        :param duration: The duration of this FlagMapping.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def flag_id(self):
        """Gets the flag_id of this FlagMapping.  # noqa: E501


        :return: The flag_id of this FlagMapping.  # noqa: E501
        :rtype: int
        """
        return self._flag_id

    @flag_id.setter
    def flag_id(self, flag_id):
        """Sets the flag_id of this FlagMapping.


        :param flag_id: The flag_id of this FlagMapping.  # noqa: E501
        :type: int
        """

        self._flag_id = flag_id

    @property
    def comment(self):
        """Gets the comment of this FlagMapping.  # noqa: E501


        :return: The comment of this FlagMapping.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this FlagMapping.


        :param comment: The comment of this FlagMapping.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def flag_state(self):
        """Gets the flag_state of this FlagMapping.  # noqa: E501


        :return: The flag_state of this FlagMapping.  # noqa: E501
        :rtype: str
        """
        return self._flag_state

    @flag_state.setter
    def flag_state(self, flag_state):
        """Sets the flag_state of this FlagMapping.


        :param flag_state: The flag_state of this FlagMapping.  # noqa: E501
        :type: str
        """

        self._flag_state = flag_state

    @property
    def is_valid_flag(self):
        """Gets the is_valid_flag of this FlagMapping.  # noqa: E501


        :return: The is_valid_flag of this FlagMapping.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid_flag

    @is_valid_flag.setter
    def is_valid_flag(self, is_valid_flag):
        """Sets the is_valid_flag of this FlagMapping.


        :param is_valid_flag: The is_valid_flag of this FlagMapping.  # noqa: E501
        :type: bool
        """

        self._is_valid_flag = is_valid_flag

    @property
    def etl_run_id(self):
        """Gets the etl_run_id of this FlagMapping.  # noqa: E501


        :return: The etl_run_id of this FlagMapping.  # noqa: E501
        :rtype: int
        """
        return self._etl_run_id

    @etl_run_id.setter
    def etl_run_id(self, etl_run_id):
        """Sets the etl_run_id of this FlagMapping.


        :param etl_run_id: The etl_run_id of this FlagMapping.  # noqa: E501
        :type: int
        """

        self._etl_run_id = etl_run_id

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
        if issubclass(FlagMapping, dict):
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
        if not isinstance(other, FlagMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
