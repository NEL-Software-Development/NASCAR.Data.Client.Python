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


class EditorNextGenDataPoint(object):
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
        'name': 'str',
        'description': 'str',
        'datapoint_id': 'str',
        'ecu': 'str',
        'can_id': 'int',
        'most_significant_bit': 'int',
        'length': 'int',
        'gain': 'int',
        'offset': 'int',
        'signed': 'bool',
        'range_min': 'int',
        'range_max': 'int',
        'mux_most_significant_bit': 'int',
        'mux_length': 'int',
        'mux_id': 'int'
    }

    attribute_map = {
        'publish_state': 'PublishState',
        'id': 'id',
        'tracking_id': 'tracking_id',
        'in_data_warehouse': 'InDataWarehouse',
        'manually_set': 'Manually_Set',
        'last_update': 'LastUpdate',
        'last_updated_by': 'LastUpdatedBy',
        'name': 'Name',
        'description': 'Description',
        'datapoint_id': 'DatapointId',
        'ecu': 'ECU',
        'can_id': 'CanId',
        'most_significant_bit': 'MostSignificantBit',
        'length': 'Length',
        'gain': 'Gain',
        'offset': 'Offset',
        'signed': 'Signed',
        'range_min': 'RangeMin',
        'range_max': 'RangeMax',
        'mux_most_significant_bit': 'MuxMostSignificantBit',
        'mux_length': 'MuxLength',
        'mux_id': 'MuxId'
    }

    def __init__(self, publish_state=None, id=None, tracking_id=None, in_data_warehouse=None, manually_set=None, last_update=None, last_updated_by=None, name=None, description=None, datapoint_id=None, ecu=None, can_id=None, most_significant_bit=None, length=None, gain=None, offset=None, signed=None, range_min=None, range_max=None, mux_most_significant_bit=None, mux_length=None, mux_id=None):  # noqa: E501
        """EditorNextGenDataPoint - a model defined in Swagger"""  # noqa: E501
        self._publish_state = None
        self._id = None
        self._tracking_id = None
        self._in_data_warehouse = None
        self._manually_set = None
        self._last_update = None
        self._last_updated_by = None
        self._name = None
        self._description = None
        self._datapoint_id = None
        self._ecu = None
        self._can_id = None
        self._most_significant_bit = None
        self._length = None
        self._gain = None
        self._offset = None
        self._signed = None
        self._range_min = None
        self._range_max = None
        self._mux_most_significant_bit = None
        self._mux_length = None
        self._mux_id = None
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
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if datapoint_id is not None:
            self.datapoint_id = datapoint_id
        if ecu is not None:
            self.ecu = ecu
        if can_id is not None:
            self.can_id = can_id
        if most_significant_bit is not None:
            self.most_significant_bit = most_significant_bit
        if length is not None:
            self.length = length
        if gain is not None:
            self.gain = gain
        if offset is not None:
            self.offset = offset
        if signed is not None:
            self.signed = signed
        if range_min is not None:
            self.range_min = range_min
        if range_max is not None:
            self.range_max = range_max
        if mux_most_significant_bit is not None:
            self.mux_most_significant_bit = mux_most_significant_bit
        if mux_length is not None:
            self.mux_length = mux_length
        if mux_id is not None:
            self.mux_id = mux_id

    @property
    def publish_state(self):
        """Gets the publish_state of this EditorNextGenDataPoint.  # noqa: E501


        :return: The publish_state of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: PublishState
        """
        return self._publish_state

    @publish_state.setter
    def publish_state(self, publish_state):
        """Sets the publish_state of this EditorNextGenDataPoint.


        :param publish_state: The publish_state of this EditorNextGenDataPoint.  # noqa: E501
        :type: PublishState
        """

        self._publish_state = publish_state

    @property
    def id(self):
        """Gets the id of this EditorNextGenDataPoint.  # noqa: E501


        :return: The id of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EditorNextGenDataPoint.


        :param id: The id of this EditorNextGenDataPoint.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def tracking_id(self):
        """Gets the tracking_id of this EditorNextGenDataPoint.  # noqa: E501


        :return: The tracking_id of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: str
        """
        return self._tracking_id

    @tracking_id.setter
    def tracking_id(self, tracking_id):
        """Sets the tracking_id of this EditorNextGenDataPoint.


        :param tracking_id: The tracking_id of this EditorNextGenDataPoint.  # noqa: E501
        :type: str
        """

        self._tracking_id = tracking_id

    @property
    def in_data_warehouse(self):
        """Gets the in_data_warehouse of this EditorNextGenDataPoint.  # noqa: E501


        :return: The in_data_warehouse of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: bool
        """
        return self._in_data_warehouse

    @in_data_warehouse.setter
    def in_data_warehouse(self, in_data_warehouse):
        """Sets the in_data_warehouse of this EditorNextGenDataPoint.


        :param in_data_warehouse: The in_data_warehouse of this EditorNextGenDataPoint.  # noqa: E501
        :type: bool
        """

        self._in_data_warehouse = in_data_warehouse

    @property
    def manually_set(self):
        """Gets the manually_set of this EditorNextGenDataPoint.  # noqa: E501


        :return: The manually_set of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: bool
        """
        return self._manually_set

    @manually_set.setter
    def manually_set(self, manually_set):
        """Sets the manually_set of this EditorNextGenDataPoint.


        :param manually_set: The manually_set of this EditorNextGenDataPoint.  # noqa: E501
        :type: bool
        """

        self._manually_set = manually_set

    @property
    def last_update(self):
        """Gets the last_update of this EditorNextGenDataPoint.  # noqa: E501


        :return: The last_update of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this EditorNextGenDataPoint.


        :param last_update: The last_update of this EditorNextGenDataPoint.  # noqa: E501
        :type: datetime
        """

        self._last_update = last_update

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this EditorNextGenDataPoint.  # noqa: E501


        :return: The last_updated_by of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this EditorNextGenDataPoint.


        :param last_updated_by: The last_updated_by of this EditorNextGenDataPoint.  # noqa: E501
        :type: str
        """

        self._last_updated_by = last_updated_by

    @property
    def name(self):
        """Gets the name of this EditorNextGenDataPoint.  # noqa: E501


        :return: The name of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EditorNextGenDataPoint.


        :param name: The name of this EditorNextGenDataPoint.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this EditorNextGenDataPoint.  # noqa: E501


        :return: The description of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EditorNextGenDataPoint.


        :param description: The description of this EditorNextGenDataPoint.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def datapoint_id(self):
        """Gets the datapoint_id of this EditorNextGenDataPoint.  # noqa: E501


        :return: The datapoint_id of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: str
        """
        return self._datapoint_id

    @datapoint_id.setter
    def datapoint_id(self, datapoint_id):
        """Sets the datapoint_id of this EditorNextGenDataPoint.


        :param datapoint_id: The datapoint_id of this EditorNextGenDataPoint.  # noqa: E501
        :type: str
        """

        self._datapoint_id = datapoint_id

    @property
    def ecu(self):
        """Gets the ecu of this EditorNextGenDataPoint.  # noqa: E501


        :return: The ecu of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: str
        """
        return self._ecu

    @ecu.setter
    def ecu(self, ecu):
        """Sets the ecu of this EditorNextGenDataPoint.


        :param ecu: The ecu of this EditorNextGenDataPoint.  # noqa: E501
        :type: str
        """

        self._ecu = ecu

    @property
    def can_id(self):
        """Gets the can_id of this EditorNextGenDataPoint.  # noqa: E501


        :return: The can_id of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._can_id

    @can_id.setter
    def can_id(self, can_id):
        """Sets the can_id of this EditorNextGenDataPoint.


        :param can_id: The can_id of this EditorNextGenDataPoint.  # noqa: E501
        :type: int
        """

        self._can_id = can_id

    @property
    def most_significant_bit(self):
        """Gets the most_significant_bit of this EditorNextGenDataPoint.  # noqa: E501


        :return: The most_significant_bit of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._most_significant_bit

    @most_significant_bit.setter
    def most_significant_bit(self, most_significant_bit):
        """Sets the most_significant_bit of this EditorNextGenDataPoint.


        :param most_significant_bit: The most_significant_bit of this EditorNextGenDataPoint.  # noqa: E501
        :type: int
        """

        self._most_significant_bit = most_significant_bit

    @property
    def length(self):
        """Gets the length of this EditorNextGenDataPoint.  # noqa: E501


        :return: The length of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this EditorNextGenDataPoint.


        :param length: The length of this EditorNextGenDataPoint.  # noqa: E501
        :type: int
        """

        self._length = length

    @property
    def gain(self):
        """Gets the gain of this EditorNextGenDataPoint.  # noqa: E501


        :return: The gain of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._gain

    @gain.setter
    def gain(self, gain):
        """Sets the gain of this EditorNextGenDataPoint.


        :param gain: The gain of this EditorNextGenDataPoint.  # noqa: E501
        :type: int
        """

        self._gain = gain

    @property
    def offset(self):
        """Gets the offset of this EditorNextGenDataPoint.  # noqa: E501


        :return: The offset of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this EditorNextGenDataPoint.


        :param offset: The offset of this EditorNextGenDataPoint.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def signed(self):
        """Gets the signed of this EditorNextGenDataPoint.  # noqa: E501


        :return: The signed of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: bool
        """
        return self._signed

    @signed.setter
    def signed(self, signed):
        """Sets the signed of this EditorNextGenDataPoint.


        :param signed: The signed of this EditorNextGenDataPoint.  # noqa: E501
        :type: bool
        """

        self._signed = signed

    @property
    def range_min(self):
        """Gets the range_min of this EditorNextGenDataPoint.  # noqa: E501


        :return: The range_min of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._range_min

    @range_min.setter
    def range_min(self, range_min):
        """Sets the range_min of this EditorNextGenDataPoint.


        :param range_min: The range_min of this EditorNextGenDataPoint.  # noqa: E501
        :type: int
        """

        self._range_min = range_min

    @property
    def range_max(self):
        """Gets the range_max of this EditorNextGenDataPoint.  # noqa: E501


        :return: The range_max of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._range_max

    @range_max.setter
    def range_max(self, range_max):
        """Sets the range_max of this EditorNextGenDataPoint.


        :param range_max: The range_max of this EditorNextGenDataPoint.  # noqa: E501
        :type: int
        """

        self._range_max = range_max

    @property
    def mux_most_significant_bit(self):
        """Gets the mux_most_significant_bit of this EditorNextGenDataPoint.  # noqa: E501


        :return: The mux_most_significant_bit of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._mux_most_significant_bit

    @mux_most_significant_bit.setter
    def mux_most_significant_bit(self, mux_most_significant_bit):
        """Sets the mux_most_significant_bit of this EditorNextGenDataPoint.


        :param mux_most_significant_bit: The mux_most_significant_bit of this EditorNextGenDataPoint.  # noqa: E501
        :type: int
        """

        self._mux_most_significant_bit = mux_most_significant_bit

    @property
    def mux_length(self):
        """Gets the mux_length of this EditorNextGenDataPoint.  # noqa: E501


        :return: The mux_length of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._mux_length

    @mux_length.setter
    def mux_length(self, mux_length):
        """Sets the mux_length of this EditorNextGenDataPoint.


        :param mux_length: The mux_length of this EditorNextGenDataPoint.  # noqa: E501
        :type: int
        """

        self._mux_length = mux_length

    @property
    def mux_id(self):
        """Gets the mux_id of this EditorNextGenDataPoint.  # noqa: E501


        :return: The mux_id of this EditorNextGenDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._mux_id

    @mux_id.setter
    def mux_id(self, mux_id):
        """Sets the mux_id of this EditorNextGenDataPoint.


        :param mux_id: The mux_id of this EditorNextGenDataPoint.  # noqa: E501
        :type: int
        """

        self._mux_id = mux_id

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
        if issubclass(EditorNextGenDataPoint, dict):
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
        if not isinstance(other, EditorNextGenDataPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
