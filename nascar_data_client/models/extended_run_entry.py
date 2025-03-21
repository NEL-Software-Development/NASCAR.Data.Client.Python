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


class ExtendedRunEntry(object):
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
        'vehicle_number': 'str',
        'adjusted_vehicle_number': 'str',
        'model_year': 'int',
        'model': 'str',
        'crew_chief_name': 'str',
        'driver_name': 'str',
        'driver_member_id': 'int',
        'driver_details': 'str',
        'owner_name': 'str',
        'vehicle_details': 'str',
        'pitbox': 'int',
        'sponsor': 'str',
        'season': 'int',
        'nascar_one_race_id': 'int',
        'nascar_one_driver_contact_id': 'int',
        'nascar_one_crew_chief_contact_id': 'int',
        'nascar_one_entry_coupon_id': 'int',
        'timing_event_id': 'int',
        'timing_competitor_id': 'int',
        'etl_crew_chief_id': 'int',
        'etl_driver_id': 'int',
        'etl_organization_id': 'int',
        'etl_owner_id': 'int',
        'etl_series_id': 'int',
        'etl_track_id': 'int',
        'etl_vehicle_id': 'int',
        'history_race_id': 'int',
        'history_race_entry_id': 'int',
        'history_driver_id': 'int',
        'history_track_id': 'int',
        'first_name': 'str',
        'last_name': 'str',
        'suffix': 'str',
        'member_id': 'int',
        'hometown_city': 'str',
        'hometown_state': 'str',
        'hometown_country': 'str'
    }

    attribute_map = {
        'publish_state': 'PublishState',
        'id': 'id',
        'tracking_id': 'tracking_id',
        'in_data_warehouse': 'InDataWarehouse',
        'manually_set': 'Manually_Set',
        'last_update': 'LastUpdate',
        'last_updated_by': 'LastUpdatedBy',
        'vehicle_number': 'VehicleNumber',
        'adjusted_vehicle_number': 'Adjusted_VehicleNumber',
        'model_year': 'ModelYear',
        'model': 'Model',
        'crew_chief_name': 'CrewChiefName',
        'driver_name': 'DriverName',
        'driver_member_id': 'DriverMemberId',
        'driver_details': 'DriverDetails',
        'owner_name': 'OwnerName',
        'vehicle_details': 'VehicleDetails',
        'pitbox': 'Pitbox',
        'sponsor': 'Sponsor',
        'season': 'Season',
        'nascar_one_race_id': 'NascarOne_RaceId',
        'nascar_one_driver_contact_id': 'NascarOne_DriverContactId',
        'nascar_one_crew_chief_contact_id': 'NascarOne_CrewChiefContactId',
        'nascar_one_entry_coupon_id': 'NascarOne_EntryCouponId',
        'timing_event_id': 'Timing_EventId',
        'timing_competitor_id': 'Timing_CompetitorId',
        'etl_crew_chief_id': 'ETL_CrewChiefId',
        'etl_driver_id': 'ETL_DriverId',
        'etl_organization_id': 'ETL_OrganizationId',
        'etl_owner_id': 'ETL_OwnerId',
        'etl_series_id': 'ETL_SeriesId',
        'etl_track_id': 'ETL_TrackId',
        'etl_vehicle_id': 'ETL_VehicleId',
        'history_race_id': 'History_RaceId',
        'history_race_entry_id': 'History_RaceEntryId',
        'history_driver_id': 'History_DriverId',
        'history_track_id': 'History_TrackId',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'suffix': 'Suffix',
        'member_id': 'MemberID',
        'hometown_city': 'HometownCity',
        'hometown_state': 'HometownState',
        'hometown_country': 'HometownCountry'
    }

    def __init__(self, publish_state=None, id=None, tracking_id=None, in_data_warehouse=None, manually_set=None, last_update=None, last_updated_by=None, vehicle_number=None, adjusted_vehicle_number=None, model_year=None, model=None, crew_chief_name=None, driver_name=None, driver_member_id=None, driver_details=None, owner_name=None, vehicle_details=None, pitbox=None, sponsor=None, season=None, nascar_one_race_id=None, nascar_one_driver_contact_id=None, nascar_one_crew_chief_contact_id=None, nascar_one_entry_coupon_id=None, timing_event_id=None, timing_competitor_id=None, etl_crew_chief_id=None, etl_driver_id=None, etl_organization_id=None, etl_owner_id=None, etl_series_id=None, etl_track_id=None, etl_vehicle_id=None, history_race_id=None, history_race_entry_id=None, history_driver_id=None, history_track_id=None, first_name=None, last_name=None, suffix=None, member_id=None, hometown_city=None, hometown_state=None, hometown_country=None):  # noqa: E501
        """ExtendedRunEntry - a model defined in Swagger"""  # noqa: E501
        self._publish_state = None
        self._id = None
        self._tracking_id = None
        self._in_data_warehouse = None
        self._manually_set = None
        self._last_update = None
        self._last_updated_by = None
        self._vehicle_number = None
        self._adjusted_vehicle_number = None
        self._model_year = None
        self._model = None
        self._crew_chief_name = None
        self._driver_name = None
        self._driver_member_id = None
        self._driver_details = None
        self._owner_name = None
        self._vehicle_details = None
        self._pitbox = None
        self._sponsor = None
        self._season = None
        self._nascar_one_race_id = None
        self._nascar_one_driver_contact_id = None
        self._nascar_one_crew_chief_contact_id = None
        self._nascar_one_entry_coupon_id = None
        self._timing_event_id = None
        self._timing_competitor_id = None
        self._etl_crew_chief_id = None
        self._etl_driver_id = None
        self._etl_organization_id = None
        self._etl_owner_id = None
        self._etl_series_id = None
        self._etl_track_id = None
        self._etl_vehicle_id = None
        self._history_race_id = None
        self._history_race_entry_id = None
        self._history_driver_id = None
        self._history_track_id = None
        self._first_name = None
        self._last_name = None
        self._suffix = None
        self._member_id = None
        self._hometown_city = None
        self._hometown_state = None
        self._hometown_country = None
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
        if vehicle_number is not None:
            self.vehicle_number = vehicle_number
        if adjusted_vehicle_number is not None:
            self.adjusted_vehicle_number = adjusted_vehicle_number
        if model_year is not None:
            self.model_year = model_year
        if model is not None:
            self.model = model
        if crew_chief_name is not None:
            self.crew_chief_name = crew_chief_name
        if driver_name is not None:
            self.driver_name = driver_name
        if driver_member_id is not None:
            self.driver_member_id = driver_member_id
        if driver_details is not None:
            self.driver_details = driver_details
        if owner_name is not None:
            self.owner_name = owner_name
        if vehicle_details is not None:
            self.vehicle_details = vehicle_details
        if pitbox is not None:
            self.pitbox = pitbox
        if sponsor is not None:
            self.sponsor = sponsor
        if season is not None:
            self.season = season
        if nascar_one_race_id is not None:
            self.nascar_one_race_id = nascar_one_race_id
        if nascar_one_driver_contact_id is not None:
            self.nascar_one_driver_contact_id = nascar_one_driver_contact_id
        if nascar_one_crew_chief_contact_id is not None:
            self.nascar_one_crew_chief_contact_id = nascar_one_crew_chief_contact_id
        if nascar_one_entry_coupon_id is not None:
            self.nascar_one_entry_coupon_id = nascar_one_entry_coupon_id
        if timing_event_id is not None:
            self.timing_event_id = timing_event_id
        if timing_competitor_id is not None:
            self.timing_competitor_id = timing_competitor_id
        if etl_crew_chief_id is not None:
            self.etl_crew_chief_id = etl_crew_chief_id
        if etl_driver_id is not None:
            self.etl_driver_id = etl_driver_id
        if etl_organization_id is not None:
            self.etl_organization_id = etl_organization_id
        if etl_owner_id is not None:
            self.etl_owner_id = etl_owner_id
        if etl_series_id is not None:
            self.etl_series_id = etl_series_id
        if etl_track_id is not None:
            self.etl_track_id = etl_track_id
        if etl_vehicle_id is not None:
            self.etl_vehicle_id = etl_vehicle_id
        if history_race_id is not None:
            self.history_race_id = history_race_id
        if history_race_entry_id is not None:
            self.history_race_entry_id = history_race_entry_id
        if history_driver_id is not None:
            self.history_driver_id = history_driver_id
        if history_track_id is not None:
            self.history_track_id = history_track_id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if suffix is not None:
            self.suffix = suffix
        if member_id is not None:
            self.member_id = member_id
        if hometown_city is not None:
            self.hometown_city = hometown_city
        if hometown_state is not None:
            self.hometown_state = hometown_state
        if hometown_country is not None:
            self.hometown_country = hometown_country

    @property
    def publish_state(self):
        """Gets the publish_state of this ExtendedRunEntry.  # noqa: E501


        :return: The publish_state of this ExtendedRunEntry.  # noqa: E501
        :rtype: PublishState
        """
        return self._publish_state

    @publish_state.setter
    def publish_state(self, publish_state):
        """Sets the publish_state of this ExtendedRunEntry.


        :param publish_state: The publish_state of this ExtendedRunEntry.  # noqa: E501
        :type: PublishState
        """

        self._publish_state = publish_state

    @property
    def id(self):
        """Gets the id of this ExtendedRunEntry.  # noqa: E501


        :return: The id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExtendedRunEntry.


        :param id: The id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def tracking_id(self):
        """Gets the tracking_id of this ExtendedRunEntry.  # noqa: E501


        :return: The tracking_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: str
        """
        return self._tracking_id

    @tracking_id.setter
    def tracking_id(self, tracking_id):
        """Sets the tracking_id of this ExtendedRunEntry.


        :param tracking_id: The tracking_id of this ExtendedRunEntry.  # noqa: E501
        :type: str
        """

        self._tracking_id = tracking_id

    @property
    def in_data_warehouse(self):
        """Gets the in_data_warehouse of this ExtendedRunEntry.  # noqa: E501


        :return: The in_data_warehouse of this ExtendedRunEntry.  # noqa: E501
        :rtype: bool
        """
        return self._in_data_warehouse

    @in_data_warehouse.setter
    def in_data_warehouse(self, in_data_warehouse):
        """Sets the in_data_warehouse of this ExtendedRunEntry.


        :param in_data_warehouse: The in_data_warehouse of this ExtendedRunEntry.  # noqa: E501
        :type: bool
        """

        self._in_data_warehouse = in_data_warehouse

    @property
    def manually_set(self):
        """Gets the manually_set of this ExtendedRunEntry.  # noqa: E501


        :return: The manually_set of this ExtendedRunEntry.  # noqa: E501
        :rtype: bool
        """
        return self._manually_set

    @manually_set.setter
    def manually_set(self, manually_set):
        """Sets the manually_set of this ExtendedRunEntry.


        :param manually_set: The manually_set of this ExtendedRunEntry.  # noqa: E501
        :type: bool
        """

        self._manually_set = manually_set

    @property
    def last_update(self):
        """Gets the last_update of this ExtendedRunEntry.  # noqa: E501


        :return: The last_update of this ExtendedRunEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this ExtendedRunEntry.


        :param last_update: The last_update of this ExtendedRunEntry.  # noqa: E501
        :type: datetime
        """

        self._last_update = last_update

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this ExtendedRunEntry.  # noqa: E501


        :return: The last_updated_by of this ExtendedRunEntry.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this ExtendedRunEntry.


        :param last_updated_by: The last_updated_by of this ExtendedRunEntry.  # noqa: E501
        :type: str
        """

        self._last_updated_by = last_updated_by

    @property
    def vehicle_number(self):
        """Gets the vehicle_number of this ExtendedRunEntry.  # noqa: E501


        :return: The vehicle_number of this ExtendedRunEntry.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_number

    @vehicle_number.setter
    def vehicle_number(self, vehicle_number):
        """Sets the vehicle_number of this ExtendedRunEntry.


        :param vehicle_number: The vehicle_number of this ExtendedRunEntry.  # noqa: E501
        :type: str
        """

        self._vehicle_number = vehicle_number

    @property
    def adjusted_vehicle_number(self):
        """Gets the adjusted_vehicle_number of this ExtendedRunEntry.  # noqa: E501


        :return: The adjusted_vehicle_number of this ExtendedRunEntry.  # noqa: E501
        :rtype: str
        """
        return self._adjusted_vehicle_number

    @adjusted_vehicle_number.setter
    def adjusted_vehicle_number(self, adjusted_vehicle_number):
        """Sets the adjusted_vehicle_number of this ExtendedRunEntry.


        :param adjusted_vehicle_number: The adjusted_vehicle_number of this ExtendedRunEntry.  # noqa: E501
        :type: str
        """

        self._adjusted_vehicle_number = adjusted_vehicle_number

    @property
    def model_year(self):
        """Gets the model_year of this ExtendedRunEntry.  # noqa: E501


        :return: The model_year of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._model_year

    @model_year.setter
    def model_year(self, model_year):
        """Sets the model_year of this ExtendedRunEntry.


        :param model_year: The model_year of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._model_year = model_year

    @property
    def model(self):
        """Gets the model of this ExtendedRunEntry.  # noqa: E501


        :return: The model of this ExtendedRunEntry.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ExtendedRunEntry.


        :param model: The model of this ExtendedRunEntry.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def crew_chief_name(self):
        """Gets the crew_chief_name of this ExtendedRunEntry.  # noqa: E501


        :return: The crew_chief_name of this ExtendedRunEntry.  # noqa: E501
        :rtype: str
        """
        return self._crew_chief_name

    @crew_chief_name.setter
    def crew_chief_name(self, crew_chief_name):
        """Sets the crew_chief_name of this ExtendedRunEntry.


        :param crew_chief_name: The crew_chief_name of this ExtendedRunEntry.  # noqa: E501
        :type: str
        """

        self._crew_chief_name = crew_chief_name

    @property
    def driver_name(self):
        """Gets the driver_name of this ExtendedRunEntry.  # noqa: E501


        :return: The driver_name of this ExtendedRunEntry.  # noqa: E501
        :rtype: str
        """
        return self._driver_name

    @driver_name.setter
    def driver_name(self, driver_name):
        """Sets the driver_name of this ExtendedRunEntry.


        :param driver_name: The driver_name of this ExtendedRunEntry.  # noqa: E501
        :type: str
        """

        self._driver_name = driver_name

    @property
    def driver_member_id(self):
        """Gets the driver_member_id of this ExtendedRunEntry.  # noqa: E501


        :return: The driver_member_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._driver_member_id

    @driver_member_id.setter
    def driver_member_id(self, driver_member_id):
        """Sets the driver_member_id of this ExtendedRunEntry.


        :param driver_member_id: The driver_member_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._driver_member_id = driver_member_id

    @property
    def driver_details(self):
        """Gets the driver_details of this ExtendedRunEntry.  # noqa: E501


        :return: The driver_details of this ExtendedRunEntry.  # noqa: E501
        :rtype: str
        """
        return self._driver_details

    @driver_details.setter
    def driver_details(self, driver_details):
        """Sets the driver_details of this ExtendedRunEntry.


        :param driver_details: The driver_details of this ExtendedRunEntry.  # noqa: E501
        :type: str
        """

        self._driver_details = driver_details

    @property
    def owner_name(self):
        """Gets the owner_name of this ExtendedRunEntry.  # noqa: E501


        :return: The owner_name of this ExtendedRunEntry.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this ExtendedRunEntry.


        :param owner_name: The owner_name of this ExtendedRunEntry.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def vehicle_details(self):
        """Gets the vehicle_details of this ExtendedRunEntry.  # noqa: E501


        :return: The vehicle_details of this ExtendedRunEntry.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_details

    @vehicle_details.setter
    def vehicle_details(self, vehicle_details):
        """Sets the vehicle_details of this ExtendedRunEntry.


        :param vehicle_details: The vehicle_details of this ExtendedRunEntry.  # noqa: E501
        :type: str
        """

        self._vehicle_details = vehicle_details

    @property
    def pitbox(self):
        """Gets the pitbox of this ExtendedRunEntry.  # noqa: E501


        :return: The pitbox of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._pitbox

    @pitbox.setter
    def pitbox(self, pitbox):
        """Sets the pitbox of this ExtendedRunEntry.


        :param pitbox: The pitbox of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._pitbox = pitbox

    @property
    def sponsor(self):
        """Gets the sponsor of this ExtendedRunEntry.  # noqa: E501


        :return: The sponsor of this ExtendedRunEntry.  # noqa: E501
        :rtype: str
        """
        return self._sponsor

    @sponsor.setter
    def sponsor(self, sponsor):
        """Sets the sponsor of this ExtendedRunEntry.


        :param sponsor: The sponsor of this ExtendedRunEntry.  # noqa: E501
        :type: str
        """

        self._sponsor = sponsor

    @property
    def season(self):
        """Gets the season of this ExtendedRunEntry.  # noqa: E501


        :return: The season of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this ExtendedRunEntry.


        :param season: The season of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def nascar_one_race_id(self):
        """Gets the nascar_one_race_id of this ExtendedRunEntry.  # noqa: E501


        :return: The nascar_one_race_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._nascar_one_race_id

    @nascar_one_race_id.setter
    def nascar_one_race_id(self, nascar_one_race_id):
        """Sets the nascar_one_race_id of this ExtendedRunEntry.


        :param nascar_one_race_id: The nascar_one_race_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._nascar_one_race_id = nascar_one_race_id

    @property
    def nascar_one_driver_contact_id(self):
        """Gets the nascar_one_driver_contact_id of this ExtendedRunEntry.  # noqa: E501


        :return: The nascar_one_driver_contact_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._nascar_one_driver_contact_id

    @nascar_one_driver_contact_id.setter
    def nascar_one_driver_contact_id(self, nascar_one_driver_contact_id):
        """Sets the nascar_one_driver_contact_id of this ExtendedRunEntry.


        :param nascar_one_driver_contact_id: The nascar_one_driver_contact_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._nascar_one_driver_contact_id = nascar_one_driver_contact_id

    @property
    def nascar_one_crew_chief_contact_id(self):
        """Gets the nascar_one_crew_chief_contact_id of this ExtendedRunEntry.  # noqa: E501


        :return: The nascar_one_crew_chief_contact_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._nascar_one_crew_chief_contact_id

    @nascar_one_crew_chief_contact_id.setter
    def nascar_one_crew_chief_contact_id(self, nascar_one_crew_chief_contact_id):
        """Sets the nascar_one_crew_chief_contact_id of this ExtendedRunEntry.


        :param nascar_one_crew_chief_contact_id: The nascar_one_crew_chief_contact_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._nascar_one_crew_chief_contact_id = nascar_one_crew_chief_contact_id

    @property
    def nascar_one_entry_coupon_id(self):
        """Gets the nascar_one_entry_coupon_id of this ExtendedRunEntry.  # noqa: E501


        :return: The nascar_one_entry_coupon_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._nascar_one_entry_coupon_id

    @nascar_one_entry_coupon_id.setter
    def nascar_one_entry_coupon_id(self, nascar_one_entry_coupon_id):
        """Sets the nascar_one_entry_coupon_id of this ExtendedRunEntry.


        :param nascar_one_entry_coupon_id: The nascar_one_entry_coupon_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._nascar_one_entry_coupon_id = nascar_one_entry_coupon_id

    @property
    def timing_event_id(self):
        """Gets the timing_event_id of this ExtendedRunEntry.  # noqa: E501


        :return: The timing_event_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._timing_event_id

    @timing_event_id.setter
    def timing_event_id(self, timing_event_id):
        """Sets the timing_event_id of this ExtendedRunEntry.


        :param timing_event_id: The timing_event_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._timing_event_id = timing_event_id

    @property
    def timing_competitor_id(self):
        """Gets the timing_competitor_id of this ExtendedRunEntry.  # noqa: E501


        :return: The timing_competitor_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._timing_competitor_id

    @timing_competitor_id.setter
    def timing_competitor_id(self, timing_competitor_id):
        """Sets the timing_competitor_id of this ExtendedRunEntry.


        :param timing_competitor_id: The timing_competitor_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._timing_competitor_id = timing_competitor_id

    @property
    def etl_crew_chief_id(self):
        """Gets the etl_crew_chief_id of this ExtendedRunEntry.  # noqa: E501


        :return: The etl_crew_chief_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._etl_crew_chief_id

    @etl_crew_chief_id.setter
    def etl_crew_chief_id(self, etl_crew_chief_id):
        """Sets the etl_crew_chief_id of this ExtendedRunEntry.


        :param etl_crew_chief_id: The etl_crew_chief_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._etl_crew_chief_id = etl_crew_chief_id

    @property
    def etl_driver_id(self):
        """Gets the etl_driver_id of this ExtendedRunEntry.  # noqa: E501


        :return: The etl_driver_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._etl_driver_id

    @etl_driver_id.setter
    def etl_driver_id(self, etl_driver_id):
        """Sets the etl_driver_id of this ExtendedRunEntry.


        :param etl_driver_id: The etl_driver_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._etl_driver_id = etl_driver_id

    @property
    def etl_organization_id(self):
        """Gets the etl_organization_id of this ExtendedRunEntry.  # noqa: E501


        :return: The etl_organization_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._etl_organization_id

    @etl_organization_id.setter
    def etl_organization_id(self, etl_organization_id):
        """Sets the etl_organization_id of this ExtendedRunEntry.


        :param etl_organization_id: The etl_organization_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._etl_organization_id = etl_organization_id

    @property
    def etl_owner_id(self):
        """Gets the etl_owner_id of this ExtendedRunEntry.  # noqa: E501


        :return: The etl_owner_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._etl_owner_id

    @etl_owner_id.setter
    def etl_owner_id(self, etl_owner_id):
        """Sets the etl_owner_id of this ExtendedRunEntry.


        :param etl_owner_id: The etl_owner_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._etl_owner_id = etl_owner_id

    @property
    def etl_series_id(self):
        """Gets the etl_series_id of this ExtendedRunEntry.  # noqa: E501


        :return: The etl_series_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._etl_series_id

    @etl_series_id.setter
    def etl_series_id(self, etl_series_id):
        """Sets the etl_series_id of this ExtendedRunEntry.


        :param etl_series_id: The etl_series_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._etl_series_id = etl_series_id

    @property
    def etl_track_id(self):
        """Gets the etl_track_id of this ExtendedRunEntry.  # noqa: E501


        :return: The etl_track_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._etl_track_id

    @etl_track_id.setter
    def etl_track_id(self, etl_track_id):
        """Sets the etl_track_id of this ExtendedRunEntry.


        :param etl_track_id: The etl_track_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._etl_track_id = etl_track_id

    @property
    def etl_vehicle_id(self):
        """Gets the etl_vehicle_id of this ExtendedRunEntry.  # noqa: E501


        :return: The etl_vehicle_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._etl_vehicle_id

    @etl_vehicle_id.setter
    def etl_vehicle_id(self, etl_vehicle_id):
        """Sets the etl_vehicle_id of this ExtendedRunEntry.


        :param etl_vehicle_id: The etl_vehicle_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._etl_vehicle_id = etl_vehicle_id

    @property
    def history_race_id(self):
        """Gets the history_race_id of this ExtendedRunEntry.  # noqa: E501


        :return: The history_race_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._history_race_id

    @history_race_id.setter
    def history_race_id(self, history_race_id):
        """Sets the history_race_id of this ExtendedRunEntry.


        :param history_race_id: The history_race_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._history_race_id = history_race_id

    @property
    def history_race_entry_id(self):
        """Gets the history_race_entry_id of this ExtendedRunEntry.  # noqa: E501


        :return: The history_race_entry_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._history_race_entry_id

    @history_race_entry_id.setter
    def history_race_entry_id(self, history_race_entry_id):
        """Sets the history_race_entry_id of this ExtendedRunEntry.


        :param history_race_entry_id: The history_race_entry_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._history_race_entry_id = history_race_entry_id

    @property
    def history_driver_id(self):
        """Gets the history_driver_id of this ExtendedRunEntry.  # noqa: E501


        :return: The history_driver_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._history_driver_id

    @history_driver_id.setter
    def history_driver_id(self, history_driver_id):
        """Sets the history_driver_id of this ExtendedRunEntry.


        :param history_driver_id: The history_driver_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._history_driver_id = history_driver_id

    @property
    def history_track_id(self):
        """Gets the history_track_id of this ExtendedRunEntry.  # noqa: E501


        :return: The history_track_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._history_track_id

    @history_track_id.setter
    def history_track_id(self, history_track_id):
        """Sets the history_track_id of this ExtendedRunEntry.


        :param history_track_id: The history_track_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._history_track_id = history_track_id

    @property
    def first_name(self):
        """Gets the first_name of this ExtendedRunEntry.  # noqa: E501

        First name  # noqa: E501

        :return: The first_name of this ExtendedRunEntry.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ExtendedRunEntry.

        First name  # noqa: E501

        :param first_name: The first_name of this ExtendedRunEntry.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this ExtendedRunEntry.  # noqa: E501

        Last name  # noqa: E501

        :return: The last_name of this ExtendedRunEntry.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ExtendedRunEntry.

        Last name  # noqa: E501

        :param last_name: The last_name of this ExtendedRunEntry.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def suffix(self):
        """Gets the suffix of this ExtendedRunEntry.  # noqa: E501

        Suffix  # noqa: E501

        :return: The suffix of this ExtendedRunEntry.  # noqa: E501
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this ExtendedRunEntry.

        Suffix  # noqa: E501

        :param suffix: The suffix of this ExtendedRunEntry.  # noqa: E501
        :type: str
        """

        self._suffix = suffix

    @property
    def member_id(self):
        """Gets the member_id of this ExtendedRunEntry.  # noqa: E501

        member id  # noqa: E501

        :return: The member_id of this ExtendedRunEntry.  # noqa: E501
        :rtype: int
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """Sets the member_id of this ExtendedRunEntry.

        member id  # noqa: E501

        :param member_id: The member_id of this ExtendedRunEntry.  # noqa: E501
        :type: int
        """

        self._member_id = member_id

    @property
    def hometown_city(self):
        """Gets the hometown_city of this ExtendedRunEntry.  # noqa: E501

        The driver's hometown  # noqa: E501

        :return: The hometown_city of this ExtendedRunEntry.  # noqa: E501
        :rtype: str
        """
        return self._hometown_city

    @hometown_city.setter
    def hometown_city(self, hometown_city):
        """Sets the hometown_city of this ExtendedRunEntry.

        The driver's hometown  # noqa: E501

        :param hometown_city: The hometown_city of this ExtendedRunEntry.  # noqa: E501
        :type: str
        """

        self._hometown_city = hometown_city

    @property
    def hometown_state(self):
        """Gets the hometown_state of this ExtendedRunEntry.  # noqa: E501

        The driver's home state  # noqa: E501

        :return: The hometown_state of this ExtendedRunEntry.  # noqa: E501
        :rtype: str
        """
        return self._hometown_state

    @hometown_state.setter
    def hometown_state(self, hometown_state):
        """Sets the hometown_state of this ExtendedRunEntry.

        The driver's home state  # noqa: E501

        :param hometown_state: The hometown_state of this ExtendedRunEntry.  # noqa: E501
        :type: str
        """

        self._hometown_state = hometown_state

    @property
    def hometown_country(self):
        """Gets the hometown_country of this ExtendedRunEntry.  # noqa: E501

        The driver's home country  # noqa: E501

        :return: The hometown_country of this ExtendedRunEntry.  # noqa: E501
        :rtype: str
        """
        return self._hometown_country

    @hometown_country.setter
    def hometown_country(self, hometown_country):
        """Sets the hometown_country of this ExtendedRunEntry.

        The driver's home country  # noqa: E501

        :param hometown_country: The hometown_country of this ExtendedRunEntry.  # noqa: E501
        :type: str
        """

        self._hometown_country = hometown_country

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
        if issubclass(ExtendedRunEntry, dict):
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
        if not isinstance(other, ExtendedRunEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
