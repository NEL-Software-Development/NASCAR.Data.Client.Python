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


class Company(object):
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
        'abbreviation': 'str',
        'alias': 'str',
        'category_id': 'int',
        'category_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'abbreviation': 'abbreviation',
        'alias': 'alias',
        'category_id': 'category_id',
        'category_name': 'category_name'
    }

    def __init__(self, id=None, name=None, abbreviation=None, alias=None, category_id=None, category_name=None):  # noqa: E501
        """Company - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._abbreviation = None
        self._alias = None
        self._category_id = None
        self._category_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if abbreviation is not None:
            self.abbreviation = abbreviation
        if alias is not None:
            self.alias = alias
        if category_id is not None:
            self.category_id = category_id
        if category_name is not None:
            self.category_name = category_name

    @property
    def id(self):
        """Gets the id of this Company.  # noqa: E501

        Company Id  # noqa: E501

        :return: The id of this Company.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Company.

        Company Id  # noqa: E501

        :param id: The id of this Company.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Company.  # noqa: E501

        The name of the company  # noqa: E501

        :return: The name of this Company.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Company.

        The name of the company  # noqa: E501

        :param name: The name of this Company.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def abbreviation(self):
        """Gets the abbreviation of this Company.  # noqa: E501

        The company's abbreviation  # noqa: E501

        :return: The abbreviation of this Company.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this Company.

        The company's abbreviation  # noqa: E501

        :param abbreviation: The abbreviation of this Company.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

    @property
    def alias(self):
        """Gets the alias of this Company.  # noqa: E501

        The company's alias  # noqa: E501

        :return: The alias of this Company.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this Company.

        The company's alias  # noqa: E501

        :param alias: The alias of this Company.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def category_id(self):
        """Gets the category_id of this Company.  # noqa: E501

        Company category Id  # noqa: E501

        :return: The category_id of this Company.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this Company.

        Company category Id  # noqa: E501

        :param category_id: The category_id of this Company.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def category_name(self):
        """Gets the category_name of this Company.  # noqa: E501

        Category name  # noqa: E501

        :return: The category_name of this Company.  # noqa: E501
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this Company.

        Category name  # noqa: E501

        :param category_name: The category_name of this Company.  # noqa: E501
        :type: str
        """

        self._category_name = category_name

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
        if issubclass(Company, dict):
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
        if not isinstance(other, Company):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
