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


class RaceRunResults(object):
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
        'run_name': 'str',
        'run_state': 'str',
        'flag_state': 'str',
        'results': 'list[RaceResult]'
    }

    attribute_map = {
        'run_name': 'run_name',
        'run_state': 'run_state',
        'flag_state': 'flag_state',
        'results': 'results'
    }

    def __init__(self, run_name=None, run_state=None, flag_state=None, results=None):  # noqa: E501
        """RaceRunResults - a model defined in Swagger"""  # noqa: E501
        self._run_name = None
        self._run_state = None
        self._flag_state = None
        self._results = None
        self.discriminator = None
        if run_name is not None:
            self.run_name = run_name
        if run_state is not None:
            self.run_state = run_state
        if flag_state is not None:
            self.flag_state = flag_state
        if results is not None:
            self.results = results

    @property
    def run_name(self):
        """Gets the run_name of this RaceRunResults.  # noqa: E501

        Run name  # noqa: E501

        :return: The run_name of this RaceRunResults.  # noqa: E501
        :rtype: str
        """
        return self._run_name

    @run_name.setter
    def run_name(self, run_name):
        """Sets the run_name of this RaceRunResults.

        Run name  # noqa: E501

        :param run_name: The run_name of this RaceRunResults.  # noqa: E501
        :type: str
        """

        self._run_name = run_name

    @property
    def run_state(self):
        """Gets the run_state of this RaceRunResults.  # noqa: E501

        Run state:  (Inactive, Active, Completed)  # noqa: E501

        :return: The run_state of this RaceRunResults.  # noqa: E501
        :rtype: str
        """
        return self._run_state

    @run_state.setter
    def run_state(self, run_state):
        """Sets the run_state of this RaceRunResults.

        Run state:  (Inactive, Active, Completed)  # noqa: E501

        :param run_state: The run_state of this RaceRunResults.  # noqa: E501
        :type: str
        """

        self._run_state = run_state

    @property
    def flag_state(self):
        """Gets the flag_state of this RaceRunResults.  # noqa: E501

        Flag state:  (NONE, WARMUP, GREEN, YELLOW, RED, WHITE, FINISH, EXTRA)  # noqa: E501

        :return: The flag_state of this RaceRunResults.  # noqa: E501
        :rtype: str
        """
        return self._flag_state

    @flag_state.setter
    def flag_state(self, flag_state):
        """Sets the flag_state of this RaceRunResults.

        Flag state:  (NONE, WARMUP, GREEN, YELLOW, RED, WHITE, FINISH, EXTRA)  # noqa: E501

        :param flag_state: The flag_state of this RaceRunResults.  # noqa: E501
        :type: str
        """

        self._flag_state = flag_state

    @property
    def results(self):
        """Gets the results of this RaceRunResults.  # noqa: E501

        Race results  # noqa: E501

        :return: The results of this RaceRunResults.  # noqa: E501
        :rtype: list[RaceResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this RaceRunResults.

        Race results  # noqa: E501

        :param results: The results of this RaceRunResults.  # noqa: E501
        :type: list[RaceResult]
        """

        self._results = results

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
        if issubclass(RaceRunResults, dict):
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
        if not isinstance(other, RaceRunResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
