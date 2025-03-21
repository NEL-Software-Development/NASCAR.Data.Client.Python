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


class EditorVehicleWeight(object):
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
        'inspection_type': 'str',
        'vehicle_number': 'str',
        'driver_name': 'str',
        'added_weight_total': 'int',
        'added_weight_left': 'int',
        'added_weight_right': 'int',
        'cross_weight': 'int',
        'cross_weight_min': 'int',
        'cross_weight_max': 'int',
        'failed_reason': 'str',
        'go_around_reason': 'str',
        'is_evc': 'bool',
        'is_flange_body': 'bool',
        'is_go_around': 'bool',
        'is_passed': 'bool',
        'left_front': 'int',
        'left_rear': 'int',
        'left_side_weight': 'int',
        'left_side_weight_max': 'int',
        'nose_weight': 'int',
        'pre_qualifying_weight': 'int',
        'qualifying_weight_allowance': 'int',
        'qualifying_weight_difference': 'int',
        'rear_weight': 'int',
        'rear_weight_max': 'int',
        'right_front': 'int',
        'right_rear': 'int',
        'right_side_weight': 'int',
        'total_weight': 'int',
        'total_weight_min': 'int',
        'weight_adjustment': 'int',
        'pk_vehicle_weight_id': 'int',
        'nascar_one_race_id': 'int'
    }

    attribute_map = {
        'publish_state': 'PublishState',
        'id': 'id',
        'tracking_id': 'tracking_id',
        'in_data_warehouse': 'InDataWarehouse',
        'manually_set': 'Manually_Set',
        'last_update': 'LastUpdate',
        'last_updated_by': 'LastUpdatedBy',
        'inspection_type': 'InspectionType',
        'vehicle_number': 'VehicleNumber',
        'driver_name': 'DriverName',
        'added_weight_total': 'AddedWeightTotal',
        'added_weight_left': 'AddedWeightLeft',
        'added_weight_right': 'AddedWeightRight',
        'cross_weight': 'CrossWeight',
        'cross_weight_min': 'CrossWeightMin',
        'cross_weight_max': 'CrossWeightMax',
        'failed_reason': 'FailedReason',
        'go_around_reason': 'GoAroundReason',
        'is_evc': 'IsEVC',
        'is_flange_body': 'IsFlangeBody',
        'is_go_around': 'IsGoAround',
        'is_passed': 'IsPassed',
        'left_front': 'LeftFront',
        'left_rear': 'LeftRear',
        'left_side_weight': 'LeftSideWeight',
        'left_side_weight_max': 'LeftSideWeightMax',
        'nose_weight': 'NoseWeight',
        'pre_qualifying_weight': 'PreQualifyingWeight',
        'qualifying_weight_allowance': 'QualifyingWeightAllowance',
        'qualifying_weight_difference': 'QualifyingWeightDifference',
        'rear_weight': 'RearWeight',
        'rear_weight_max': 'RearWeightMax',
        'right_front': 'RightFront',
        'right_rear': 'RightRear',
        'right_side_weight': 'RightSideWeight',
        'total_weight': 'TotalWeight',
        'total_weight_min': 'TotalWeightMin',
        'weight_adjustment': 'WeightAdjustment',
        'pk_vehicle_weight_id': 'pkVehicleWeightID',
        'nascar_one_race_id': 'NascarOne_RaceId'
    }

    def __init__(self, publish_state=None, id=None, tracking_id=None, in_data_warehouse=None, manually_set=None, last_update=None, last_updated_by=None, inspection_type=None, vehicle_number=None, driver_name=None, added_weight_total=None, added_weight_left=None, added_weight_right=None, cross_weight=None, cross_weight_min=None, cross_weight_max=None, failed_reason=None, go_around_reason=None, is_evc=None, is_flange_body=None, is_go_around=None, is_passed=None, left_front=None, left_rear=None, left_side_weight=None, left_side_weight_max=None, nose_weight=None, pre_qualifying_weight=None, qualifying_weight_allowance=None, qualifying_weight_difference=None, rear_weight=None, rear_weight_max=None, right_front=None, right_rear=None, right_side_weight=None, total_weight=None, total_weight_min=None, weight_adjustment=None, pk_vehicle_weight_id=None, nascar_one_race_id=None):  # noqa: E501
        """EditorVehicleWeight - a model defined in Swagger"""  # noqa: E501
        self._publish_state = None
        self._id = None
        self._tracking_id = None
        self._in_data_warehouse = None
        self._manually_set = None
        self._last_update = None
        self._last_updated_by = None
        self._inspection_type = None
        self._vehicle_number = None
        self._driver_name = None
        self._added_weight_total = None
        self._added_weight_left = None
        self._added_weight_right = None
        self._cross_weight = None
        self._cross_weight_min = None
        self._cross_weight_max = None
        self._failed_reason = None
        self._go_around_reason = None
        self._is_evc = None
        self._is_flange_body = None
        self._is_go_around = None
        self._is_passed = None
        self._left_front = None
        self._left_rear = None
        self._left_side_weight = None
        self._left_side_weight_max = None
        self._nose_weight = None
        self._pre_qualifying_weight = None
        self._qualifying_weight_allowance = None
        self._qualifying_weight_difference = None
        self._rear_weight = None
        self._rear_weight_max = None
        self._right_front = None
        self._right_rear = None
        self._right_side_weight = None
        self._total_weight = None
        self._total_weight_min = None
        self._weight_adjustment = None
        self._pk_vehicle_weight_id = None
        self._nascar_one_race_id = None
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
        if inspection_type is not None:
            self.inspection_type = inspection_type
        if vehicle_number is not None:
            self.vehicle_number = vehicle_number
        if driver_name is not None:
            self.driver_name = driver_name
        if added_weight_total is not None:
            self.added_weight_total = added_weight_total
        if added_weight_left is not None:
            self.added_weight_left = added_weight_left
        if added_weight_right is not None:
            self.added_weight_right = added_weight_right
        if cross_weight is not None:
            self.cross_weight = cross_weight
        if cross_weight_min is not None:
            self.cross_weight_min = cross_weight_min
        if cross_weight_max is not None:
            self.cross_weight_max = cross_weight_max
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if go_around_reason is not None:
            self.go_around_reason = go_around_reason
        if is_evc is not None:
            self.is_evc = is_evc
        if is_flange_body is not None:
            self.is_flange_body = is_flange_body
        if is_go_around is not None:
            self.is_go_around = is_go_around
        if is_passed is not None:
            self.is_passed = is_passed
        if left_front is not None:
            self.left_front = left_front
        if left_rear is not None:
            self.left_rear = left_rear
        if left_side_weight is not None:
            self.left_side_weight = left_side_weight
        if left_side_weight_max is not None:
            self.left_side_weight_max = left_side_weight_max
        if nose_weight is not None:
            self.nose_weight = nose_weight
        if pre_qualifying_weight is not None:
            self.pre_qualifying_weight = pre_qualifying_weight
        if qualifying_weight_allowance is not None:
            self.qualifying_weight_allowance = qualifying_weight_allowance
        if qualifying_weight_difference is not None:
            self.qualifying_weight_difference = qualifying_weight_difference
        if rear_weight is not None:
            self.rear_weight = rear_weight
        if rear_weight_max is not None:
            self.rear_weight_max = rear_weight_max
        if right_front is not None:
            self.right_front = right_front
        if right_rear is not None:
            self.right_rear = right_rear
        if right_side_weight is not None:
            self.right_side_weight = right_side_weight
        if total_weight is not None:
            self.total_weight = total_weight
        if total_weight_min is not None:
            self.total_weight_min = total_weight_min
        if weight_adjustment is not None:
            self.weight_adjustment = weight_adjustment
        if pk_vehicle_weight_id is not None:
            self.pk_vehicle_weight_id = pk_vehicle_weight_id
        if nascar_one_race_id is not None:
            self.nascar_one_race_id = nascar_one_race_id

    @property
    def publish_state(self):
        """Gets the publish_state of this EditorVehicleWeight.  # noqa: E501


        :return: The publish_state of this EditorVehicleWeight.  # noqa: E501
        :rtype: PublishState
        """
        return self._publish_state

    @publish_state.setter
    def publish_state(self, publish_state):
        """Sets the publish_state of this EditorVehicleWeight.


        :param publish_state: The publish_state of this EditorVehicleWeight.  # noqa: E501
        :type: PublishState
        """

        self._publish_state = publish_state

    @property
    def id(self):
        """Gets the id of this EditorVehicleWeight.  # noqa: E501


        :return: The id of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EditorVehicleWeight.


        :param id: The id of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def tracking_id(self):
        """Gets the tracking_id of this EditorVehicleWeight.  # noqa: E501


        :return: The tracking_id of this EditorVehicleWeight.  # noqa: E501
        :rtype: str
        """
        return self._tracking_id

    @tracking_id.setter
    def tracking_id(self, tracking_id):
        """Sets the tracking_id of this EditorVehicleWeight.


        :param tracking_id: The tracking_id of this EditorVehicleWeight.  # noqa: E501
        :type: str
        """

        self._tracking_id = tracking_id

    @property
    def in_data_warehouse(self):
        """Gets the in_data_warehouse of this EditorVehicleWeight.  # noqa: E501


        :return: The in_data_warehouse of this EditorVehicleWeight.  # noqa: E501
        :rtype: bool
        """
        return self._in_data_warehouse

    @in_data_warehouse.setter
    def in_data_warehouse(self, in_data_warehouse):
        """Sets the in_data_warehouse of this EditorVehicleWeight.


        :param in_data_warehouse: The in_data_warehouse of this EditorVehicleWeight.  # noqa: E501
        :type: bool
        """

        self._in_data_warehouse = in_data_warehouse

    @property
    def manually_set(self):
        """Gets the manually_set of this EditorVehicleWeight.  # noqa: E501


        :return: The manually_set of this EditorVehicleWeight.  # noqa: E501
        :rtype: bool
        """
        return self._manually_set

    @manually_set.setter
    def manually_set(self, manually_set):
        """Sets the manually_set of this EditorVehicleWeight.


        :param manually_set: The manually_set of this EditorVehicleWeight.  # noqa: E501
        :type: bool
        """

        self._manually_set = manually_set

    @property
    def last_update(self):
        """Gets the last_update of this EditorVehicleWeight.  # noqa: E501


        :return: The last_update of this EditorVehicleWeight.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this EditorVehicleWeight.


        :param last_update: The last_update of this EditorVehicleWeight.  # noqa: E501
        :type: datetime
        """

        self._last_update = last_update

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this EditorVehicleWeight.  # noqa: E501


        :return: The last_updated_by of this EditorVehicleWeight.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this EditorVehicleWeight.


        :param last_updated_by: The last_updated_by of this EditorVehicleWeight.  # noqa: E501
        :type: str
        """

        self._last_updated_by = last_updated_by

    @property
    def inspection_type(self):
        """Gets the inspection_type of this EditorVehicleWeight.  # noqa: E501


        :return: The inspection_type of this EditorVehicleWeight.  # noqa: E501
        :rtype: str
        """
        return self._inspection_type

    @inspection_type.setter
    def inspection_type(self, inspection_type):
        """Sets the inspection_type of this EditorVehicleWeight.


        :param inspection_type: The inspection_type of this EditorVehicleWeight.  # noqa: E501
        :type: str
        """

        self._inspection_type = inspection_type

    @property
    def vehicle_number(self):
        """Gets the vehicle_number of this EditorVehicleWeight.  # noqa: E501


        :return: The vehicle_number of this EditorVehicleWeight.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_number

    @vehicle_number.setter
    def vehicle_number(self, vehicle_number):
        """Sets the vehicle_number of this EditorVehicleWeight.


        :param vehicle_number: The vehicle_number of this EditorVehicleWeight.  # noqa: E501
        :type: str
        """

        self._vehicle_number = vehicle_number

    @property
    def driver_name(self):
        """Gets the driver_name of this EditorVehicleWeight.  # noqa: E501


        :return: The driver_name of this EditorVehicleWeight.  # noqa: E501
        :rtype: str
        """
        return self._driver_name

    @driver_name.setter
    def driver_name(self, driver_name):
        """Sets the driver_name of this EditorVehicleWeight.


        :param driver_name: The driver_name of this EditorVehicleWeight.  # noqa: E501
        :type: str
        """

        self._driver_name = driver_name

    @property
    def added_weight_total(self):
        """Gets the added_weight_total of this EditorVehicleWeight.  # noqa: E501


        :return: The added_weight_total of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._added_weight_total

    @added_weight_total.setter
    def added_weight_total(self, added_weight_total):
        """Sets the added_weight_total of this EditorVehicleWeight.


        :param added_weight_total: The added_weight_total of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._added_weight_total = added_weight_total

    @property
    def added_weight_left(self):
        """Gets the added_weight_left of this EditorVehicleWeight.  # noqa: E501


        :return: The added_weight_left of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._added_weight_left

    @added_weight_left.setter
    def added_weight_left(self, added_weight_left):
        """Sets the added_weight_left of this EditorVehicleWeight.


        :param added_weight_left: The added_weight_left of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._added_weight_left = added_weight_left

    @property
    def added_weight_right(self):
        """Gets the added_weight_right of this EditorVehicleWeight.  # noqa: E501


        :return: The added_weight_right of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._added_weight_right

    @added_weight_right.setter
    def added_weight_right(self, added_weight_right):
        """Sets the added_weight_right of this EditorVehicleWeight.


        :param added_weight_right: The added_weight_right of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._added_weight_right = added_weight_right

    @property
    def cross_weight(self):
        """Gets the cross_weight of this EditorVehicleWeight.  # noqa: E501


        :return: The cross_weight of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._cross_weight

    @cross_weight.setter
    def cross_weight(self, cross_weight):
        """Sets the cross_weight of this EditorVehicleWeight.


        :param cross_weight: The cross_weight of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._cross_weight = cross_weight

    @property
    def cross_weight_min(self):
        """Gets the cross_weight_min of this EditorVehicleWeight.  # noqa: E501


        :return: The cross_weight_min of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._cross_weight_min

    @cross_weight_min.setter
    def cross_weight_min(self, cross_weight_min):
        """Sets the cross_weight_min of this EditorVehicleWeight.


        :param cross_weight_min: The cross_weight_min of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._cross_weight_min = cross_weight_min

    @property
    def cross_weight_max(self):
        """Gets the cross_weight_max of this EditorVehicleWeight.  # noqa: E501


        :return: The cross_weight_max of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._cross_weight_max

    @cross_weight_max.setter
    def cross_weight_max(self, cross_weight_max):
        """Sets the cross_weight_max of this EditorVehicleWeight.


        :param cross_weight_max: The cross_weight_max of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._cross_weight_max = cross_weight_max

    @property
    def failed_reason(self):
        """Gets the failed_reason of this EditorVehicleWeight.  # noqa: E501


        :return: The failed_reason of this EditorVehicleWeight.  # noqa: E501
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this EditorVehicleWeight.


        :param failed_reason: The failed_reason of this EditorVehicleWeight.  # noqa: E501
        :type: str
        """

        self._failed_reason = failed_reason

    @property
    def go_around_reason(self):
        """Gets the go_around_reason of this EditorVehicleWeight.  # noqa: E501


        :return: The go_around_reason of this EditorVehicleWeight.  # noqa: E501
        :rtype: str
        """
        return self._go_around_reason

    @go_around_reason.setter
    def go_around_reason(self, go_around_reason):
        """Sets the go_around_reason of this EditorVehicleWeight.


        :param go_around_reason: The go_around_reason of this EditorVehicleWeight.  # noqa: E501
        :type: str
        """

        self._go_around_reason = go_around_reason

    @property
    def is_evc(self):
        """Gets the is_evc of this EditorVehicleWeight.  # noqa: E501


        :return: The is_evc of this EditorVehicleWeight.  # noqa: E501
        :rtype: bool
        """
        return self._is_evc

    @is_evc.setter
    def is_evc(self, is_evc):
        """Sets the is_evc of this EditorVehicleWeight.


        :param is_evc: The is_evc of this EditorVehicleWeight.  # noqa: E501
        :type: bool
        """

        self._is_evc = is_evc

    @property
    def is_flange_body(self):
        """Gets the is_flange_body of this EditorVehicleWeight.  # noqa: E501


        :return: The is_flange_body of this EditorVehicleWeight.  # noqa: E501
        :rtype: bool
        """
        return self._is_flange_body

    @is_flange_body.setter
    def is_flange_body(self, is_flange_body):
        """Sets the is_flange_body of this EditorVehicleWeight.


        :param is_flange_body: The is_flange_body of this EditorVehicleWeight.  # noqa: E501
        :type: bool
        """

        self._is_flange_body = is_flange_body

    @property
    def is_go_around(self):
        """Gets the is_go_around of this EditorVehicleWeight.  # noqa: E501


        :return: The is_go_around of this EditorVehicleWeight.  # noqa: E501
        :rtype: bool
        """
        return self._is_go_around

    @is_go_around.setter
    def is_go_around(self, is_go_around):
        """Sets the is_go_around of this EditorVehicleWeight.


        :param is_go_around: The is_go_around of this EditorVehicleWeight.  # noqa: E501
        :type: bool
        """

        self._is_go_around = is_go_around

    @property
    def is_passed(self):
        """Gets the is_passed of this EditorVehicleWeight.  # noqa: E501


        :return: The is_passed of this EditorVehicleWeight.  # noqa: E501
        :rtype: bool
        """
        return self._is_passed

    @is_passed.setter
    def is_passed(self, is_passed):
        """Sets the is_passed of this EditorVehicleWeight.


        :param is_passed: The is_passed of this EditorVehicleWeight.  # noqa: E501
        :type: bool
        """

        self._is_passed = is_passed

    @property
    def left_front(self):
        """Gets the left_front of this EditorVehicleWeight.  # noqa: E501


        :return: The left_front of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._left_front

    @left_front.setter
    def left_front(self, left_front):
        """Sets the left_front of this EditorVehicleWeight.


        :param left_front: The left_front of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._left_front = left_front

    @property
    def left_rear(self):
        """Gets the left_rear of this EditorVehicleWeight.  # noqa: E501


        :return: The left_rear of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._left_rear

    @left_rear.setter
    def left_rear(self, left_rear):
        """Sets the left_rear of this EditorVehicleWeight.


        :param left_rear: The left_rear of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._left_rear = left_rear

    @property
    def left_side_weight(self):
        """Gets the left_side_weight of this EditorVehicleWeight.  # noqa: E501


        :return: The left_side_weight of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._left_side_weight

    @left_side_weight.setter
    def left_side_weight(self, left_side_weight):
        """Sets the left_side_weight of this EditorVehicleWeight.


        :param left_side_weight: The left_side_weight of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._left_side_weight = left_side_weight

    @property
    def left_side_weight_max(self):
        """Gets the left_side_weight_max of this EditorVehicleWeight.  # noqa: E501


        :return: The left_side_weight_max of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._left_side_weight_max

    @left_side_weight_max.setter
    def left_side_weight_max(self, left_side_weight_max):
        """Sets the left_side_weight_max of this EditorVehicleWeight.


        :param left_side_weight_max: The left_side_weight_max of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._left_side_weight_max = left_side_weight_max

    @property
    def nose_weight(self):
        """Gets the nose_weight of this EditorVehicleWeight.  # noqa: E501


        :return: The nose_weight of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._nose_weight

    @nose_weight.setter
    def nose_weight(self, nose_weight):
        """Sets the nose_weight of this EditorVehicleWeight.


        :param nose_weight: The nose_weight of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._nose_weight = nose_weight

    @property
    def pre_qualifying_weight(self):
        """Gets the pre_qualifying_weight of this EditorVehicleWeight.  # noqa: E501


        :return: The pre_qualifying_weight of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._pre_qualifying_weight

    @pre_qualifying_weight.setter
    def pre_qualifying_weight(self, pre_qualifying_weight):
        """Sets the pre_qualifying_weight of this EditorVehicleWeight.


        :param pre_qualifying_weight: The pre_qualifying_weight of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._pre_qualifying_weight = pre_qualifying_weight

    @property
    def qualifying_weight_allowance(self):
        """Gets the qualifying_weight_allowance of this EditorVehicleWeight.  # noqa: E501


        :return: The qualifying_weight_allowance of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._qualifying_weight_allowance

    @qualifying_weight_allowance.setter
    def qualifying_weight_allowance(self, qualifying_weight_allowance):
        """Sets the qualifying_weight_allowance of this EditorVehicleWeight.


        :param qualifying_weight_allowance: The qualifying_weight_allowance of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._qualifying_weight_allowance = qualifying_weight_allowance

    @property
    def qualifying_weight_difference(self):
        """Gets the qualifying_weight_difference of this EditorVehicleWeight.  # noqa: E501


        :return: The qualifying_weight_difference of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._qualifying_weight_difference

    @qualifying_weight_difference.setter
    def qualifying_weight_difference(self, qualifying_weight_difference):
        """Sets the qualifying_weight_difference of this EditorVehicleWeight.


        :param qualifying_weight_difference: The qualifying_weight_difference of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._qualifying_weight_difference = qualifying_weight_difference

    @property
    def rear_weight(self):
        """Gets the rear_weight of this EditorVehicleWeight.  # noqa: E501


        :return: The rear_weight of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._rear_weight

    @rear_weight.setter
    def rear_weight(self, rear_weight):
        """Sets the rear_weight of this EditorVehicleWeight.


        :param rear_weight: The rear_weight of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._rear_weight = rear_weight

    @property
    def rear_weight_max(self):
        """Gets the rear_weight_max of this EditorVehicleWeight.  # noqa: E501


        :return: The rear_weight_max of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._rear_weight_max

    @rear_weight_max.setter
    def rear_weight_max(self, rear_weight_max):
        """Sets the rear_weight_max of this EditorVehicleWeight.


        :param rear_weight_max: The rear_weight_max of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._rear_weight_max = rear_weight_max

    @property
    def right_front(self):
        """Gets the right_front of this EditorVehicleWeight.  # noqa: E501


        :return: The right_front of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._right_front

    @right_front.setter
    def right_front(self, right_front):
        """Sets the right_front of this EditorVehicleWeight.


        :param right_front: The right_front of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._right_front = right_front

    @property
    def right_rear(self):
        """Gets the right_rear of this EditorVehicleWeight.  # noqa: E501


        :return: The right_rear of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._right_rear

    @right_rear.setter
    def right_rear(self, right_rear):
        """Sets the right_rear of this EditorVehicleWeight.


        :param right_rear: The right_rear of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._right_rear = right_rear

    @property
    def right_side_weight(self):
        """Gets the right_side_weight of this EditorVehicleWeight.  # noqa: E501


        :return: The right_side_weight of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._right_side_weight

    @right_side_weight.setter
    def right_side_weight(self, right_side_weight):
        """Sets the right_side_weight of this EditorVehicleWeight.


        :param right_side_weight: The right_side_weight of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._right_side_weight = right_side_weight

    @property
    def total_weight(self):
        """Gets the total_weight of this EditorVehicleWeight.  # noqa: E501


        :return: The total_weight of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._total_weight

    @total_weight.setter
    def total_weight(self, total_weight):
        """Sets the total_weight of this EditorVehicleWeight.


        :param total_weight: The total_weight of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._total_weight = total_weight

    @property
    def total_weight_min(self):
        """Gets the total_weight_min of this EditorVehicleWeight.  # noqa: E501


        :return: The total_weight_min of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._total_weight_min

    @total_weight_min.setter
    def total_weight_min(self, total_weight_min):
        """Sets the total_weight_min of this EditorVehicleWeight.


        :param total_weight_min: The total_weight_min of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._total_weight_min = total_weight_min

    @property
    def weight_adjustment(self):
        """Gets the weight_adjustment of this EditorVehicleWeight.  # noqa: E501


        :return: The weight_adjustment of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._weight_adjustment

    @weight_adjustment.setter
    def weight_adjustment(self, weight_adjustment):
        """Sets the weight_adjustment of this EditorVehicleWeight.


        :param weight_adjustment: The weight_adjustment of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._weight_adjustment = weight_adjustment

    @property
    def pk_vehicle_weight_id(self):
        """Gets the pk_vehicle_weight_id of this EditorVehicleWeight.  # noqa: E501


        :return: The pk_vehicle_weight_id of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._pk_vehicle_weight_id

    @pk_vehicle_weight_id.setter
    def pk_vehicle_weight_id(self, pk_vehicle_weight_id):
        """Sets the pk_vehicle_weight_id of this EditorVehicleWeight.


        :param pk_vehicle_weight_id: The pk_vehicle_weight_id of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._pk_vehicle_weight_id = pk_vehicle_weight_id

    @property
    def nascar_one_race_id(self):
        """Gets the nascar_one_race_id of this EditorVehicleWeight.  # noqa: E501


        :return: The nascar_one_race_id of this EditorVehicleWeight.  # noqa: E501
        :rtype: int
        """
        return self._nascar_one_race_id

    @nascar_one_race_id.setter
    def nascar_one_race_id(self, nascar_one_race_id):
        """Sets the nascar_one_race_id of this EditorVehicleWeight.


        :param nascar_one_race_id: The nascar_one_race_id of this EditorVehicleWeight.  # noqa: E501
        :type: int
        """

        self._nascar_one_race_id = nascar_one_race_id

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
        if issubclass(EditorVehicleWeight, dict):
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
        if not isinstance(other, EditorVehicleWeight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
