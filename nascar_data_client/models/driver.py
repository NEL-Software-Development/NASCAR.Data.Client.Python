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


class Driver(object):
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
        'name': 'str',
        'date_of_birth': 'datetime',
        'date_of_death': 'datetime',
        'hometown_city': 'str',
        'hometown_state': 'str',
        'hometown_country': 'str',
        'resides_city': 'str',
        'resides_state': 'str',
        'resides_country': 'str',
        'series_1_rookie_year': 'int',
        'series_2_rookie_year': 'int',
        'series_3_rookie_year': 'int',
        'hobbies': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'date_of_birth': 'date_of_birth',
        'date_of_death': 'date_of_death',
        'hometown_city': 'hometown_city',
        'hometown_state': 'hometown_state',
        'hometown_country': 'hometown_country',
        'resides_city': 'resides_city',
        'resides_state': 'resides_state',
        'resides_country': 'resides_country',
        'series_1_rookie_year': 'series_1_rookie_year',
        'series_2_rookie_year': 'series_2_rookie_year',
        'series_3_rookie_year': 'series_3_rookie_year',
        'hobbies': 'hobbies'
    }

    def __init__(self, id=None, name=None, date_of_birth=None, date_of_death=None, hometown_city=None, hometown_state=None, hometown_country=None, resides_city=None, resides_state=None, resides_country=None, series_1_rookie_year=None, series_2_rookie_year=None, series_3_rookie_year=None, hobbies=None):  # noqa: E501
        """Driver - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._date_of_birth = None
        self._date_of_death = None
        self._hometown_city = None
        self._hometown_state = None
        self._hometown_country = None
        self._resides_city = None
        self._resides_state = None
        self._resides_country = None
        self._series_1_rookie_year = None
        self._series_2_rookie_year = None
        self._series_3_rookie_year = None
        self._hobbies = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if date_of_death is not None:
            self.date_of_death = date_of_death
        if hometown_city is not None:
            self.hometown_city = hometown_city
        if hometown_state is not None:
            self.hometown_state = hometown_state
        if hometown_country is not None:
            self.hometown_country = hometown_country
        if resides_city is not None:
            self.resides_city = resides_city
        if resides_state is not None:
            self.resides_state = resides_state
        if resides_country is not None:
            self.resides_country = resides_country
        if series_1_rookie_year is not None:
            self.series_1_rookie_year = series_1_rookie_year
        if series_2_rookie_year is not None:
            self.series_2_rookie_year = series_2_rookie_year
        if series_3_rookie_year is not None:
            self.series_3_rookie_year = series_3_rookie_year
        if hobbies is not None:
            self.hobbies = hobbies

    @property
    def id(self):
        """Gets the id of this Driver.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this Driver.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Driver.

        Id  # noqa: E501

        :param id: The id of this Driver.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Driver.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Driver.

        Name  # noqa: E501

        :param name: The name of this Driver.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this Driver.  # noqa: E501

        Date of birth  # noqa: E501

        :return: The date_of_birth of this Driver.  # noqa: E501
        :rtype: datetime
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this Driver.

        Date of birth  # noqa: E501

        :param date_of_birth: The date_of_birth of this Driver.  # noqa: E501
        :type: datetime
        """

        self._date_of_birth = date_of_birth

    @property
    def date_of_death(self):
        """Gets the date_of_death of this Driver.  # noqa: E501

        Date of death  # noqa: E501

        :return: The date_of_death of this Driver.  # noqa: E501
        :rtype: datetime
        """
        return self._date_of_death

    @date_of_death.setter
    def date_of_death(self, date_of_death):
        """Sets the date_of_death of this Driver.

        Date of death  # noqa: E501

        :param date_of_death: The date_of_death of this Driver.  # noqa: E501
        :type: datetime
        """

        self._date_of_death = date_of_death

    @property
    def hometown_city(self):
        """Gets the hometown_city of this Driver.  # noqa: E501

        The driver's hometown  # noqa: E501

        :return: The hometown_city of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._hometown_city

    @hometown_city.setter
    def hometown_city(self, hometown_city):
        """Sets the hometown_city of this Driver.

        The driver's hometown  # noqa: E501

        :param hometown_city: The hometown_city of this Driver.  # noqa: E501
        :type: str
        """

        self._hometown_city = hometown_city

    @property
    def hometown_state(self):
        """Gets the hometown_state of this Driver.  # noqa: E501

        The driver's home state  # noqa: E501

        :return: The hometown_state of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._hometown_state

    @hometown_state.setter
    def hometown_state(self, hometown_state):
        """Sets the hometown_state of this Driver.

        The driver's home state  # noqa: E501

        :param hometown_state: The hometown_state of this Driver.  # noqa: E501
        :type: str
        """

        self._hometown_state = hometown_state

    @property
    def hometown_country(self):
        """Gets the hometown_country of this Driver.  # noqa: E501

        The driver's home country  # noqa: E501

        :return: The hometown_country of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._hometown_country

    @hometown_country.setter
    def hometown_country(self, hometown_country):
        """Sets the hometown_country of this Driver.

        The driver's home country  # noqa: E501

        :param hometown_country: The hometown_country of this Driver.  # noqa: E501
        :type: str
        """

        self._hometown_country = hometown_country

    @property
    def resides_city(self):
        """Gets the resides_city of this Driver.  # noqa: E501

        The city where the driver resides  # noqa: E501

        :return: The resides_city of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._resides_city

    @resides_city.setter
    def resides_city(self, resides_city):
        """Sets the resides_city of this Driver.

        The city where the driver resides  # noqa: E501

        :param resides_city: The resides_city of this Driver.  # noqa: E501
        :type: str
        """

        self._resides_city = resides_city

    @property
    def resides_state(self):
        """Gets the resides_state of this Driver.  # noqa: E501

        The state where the driver resides  # noqa: E501

        :return: The resides_state of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._resides_state

    @resides_state.setter
    def resides_state(self, resides_state):
        """Sets the resides_state of this Driver.

        The state where the driver resides  # noqa: E501

        :param resides_state: The resides_state of this Driver.  # noqa: E501
        :type: str
        """

        self._resides_state = resides_state

    @property
    def resides_country(self):
        """Gets the resides_country of this Driver.  # noqa: E501

        The country where the driver resides  # noqa: E501

        :return: The resides_country of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._resides_country

    @resides_country.setter
    def resides_country(self, resides_country):
        """Sets the resides_country of this Driver.

        The country where the driver resides  # noqa: E501

        :param resides_country: The resides_country of this Driver.  # noqa: E501
        :type: str
        """

        self._resides_country = resides_country

    @property
    def series_1_rookie_year(self):
        """Gets the series_1_rookie_year of this Driver.  # noqa: E501

        The driver's rookie year in series 1  # noqa: E501

        :return: The series_1_rookie_year of this Driver.  # noqa: E501
        :rtype: int
        """
        return self._series_1_rookie_year

    @series_1_rookie_year.setter
    def series_1_rookie_year(self, series_1_rookie_year):
        """Sets the series_1_rookie_year of this Driver.

        The driver's rookie year in series 1  # noqa: E501

        :param series_1_rookie_year: The series_1_rookie_year of this Driver.  # noqa: E501
        :type: int
        """

        self._series_1_rookie_year = series_1_rookie_year

    @property
    def series_2_rookie_year(self):
        """Gets the series_2_rookie_year of this Driver.  # noqa: E501

        The driver's rookie year in series 2  # noqa: E501

        :return: The series_2_rookie_year of this Driver.  # noqa: E501
        :rtype: int
        """
        return self._series_2_rookie_year

    @series_2_rookie_year.setter
    def series_2_rookie_year(self, series_2_rookie_year):
        """Sets the series_2_rookie_year of this Driver.

        The driver's rookie year in series 2  # noqa: E501

        :param series_2_rookie_year: The series_2_rookie_year of this Driver.  # noqa: E501
        :type: int
        """

        self._series_2_rookie_year = series_2_rookie_year

    @property
    def series_3_rookie_year(self):
        """Gets the series_3_rookie_year of this Driver.  # noqa: E501

        The driver's rookie year in series 3  # noqa: E501

        :return: The series_3_rookie_year of this Driver.  # noqa: E501
        :rtype: int
        """
        return self._series_3_rookie_year

    @series_3_rookie_year.setter
    def series_3_rookie_year(self, series_3_rookie_year):
        """Sets the series_3_rookie_year of this Driver.

        The driver's rookie year in series 3  # noqa: E501

        :param series_3_rookie_year: The series_3_rookie_year of this Driver.  # noqa: E501
        :type: int
        """

        self._series_3_rookie_year = series_3_rookie_year

    @property
    def hobbies(self):
        """Gets the hobbies of this Driver.  # noqa: E501

        The driver's hobbies  # noqa: E501

        :return: The hobbies of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._hobbies

    @hobbies.setter
    def hobbies(self, hobbies):
        """Sets the hobbies of this Driver.

        The driver's hobbies  # noqa: E501

        :param hobbies: The hobbies of this Driver.  # noqa: E501
        :type: str
        """

        self._hobbies = hobbies

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
        if issubclass(Driver, dict):
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
        if not isinstance(other, Driver):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
