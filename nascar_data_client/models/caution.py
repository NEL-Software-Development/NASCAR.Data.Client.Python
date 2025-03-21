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


class Caution(object):
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
        'lap_start': 'int',
        'lap_end': 'int',
        'beneficiary': 'str',
        'comment': 'str',
        'reason': 'str',
        'flag_time': 'datetime'
    }

    attribute_map = {
        'lap_start': 'lap_start',
        'lap_end': 'lap_end',
        'beneficiary': 'beneficiary',
        'comment': 'comment',
        'reason': 'reason',
        'flag_time': 'flag_time'
    }

    def __init__(self, lap_start=None, lap_end=None, beneficiary=None, comment=None, reason=None, flag_time=None):  # noqa: E501
        """Caution - a model defined in Swagger"""  # noqa: E501
        self._lap_start = None
        self._lap_end = None
        self._beneficiary = None
        self._comment = None
        self._reason = None
        self._flag_time = None
        self.discriminator = None
        if lap_start is not None:
            self.lap_start = lap_start
        if lap_end is not None:
            self.lap_end = lap_end
        if beneficiary is not None:
            self.beneficiary = beneficiary
        if comment is not None:
            self.comment = comment
        if reason is not None:
            self.reason = reason
        if flag_time is not None:
            self.flag_time = flag_time

    @property
    def lap_start(self):
        """Gets the lap_start of this Caution.  # noqa: E501

        The first lap of the caution  # noqa: E501

        :return: The lap_start of this Caution.  # noqa: E501
        :rtype: int
        """
        return self._lap_start

    @lap_start.setter
    def lap_start(self, lap_start):
        """Sets the lap_start of this Caution.

        The first lap of the caution  # noqa: E501

        :param lap_start: The lap_start of this Caution.  # noqa: E501
        :type: int
        """

        self._lap_start = lap_start

    @property
    def lap_end(self):
        """Gets the lap_end of this Caution.  # noqa: E501

        The last lap of the caution  # noqa: E501

        :return: The lap_end of this Caution.  # noqa: E501
        :rtype: int
        """
        return self._lap_end

    @lap_end.setter
    def lap_end(self, lap_end):
        """Sets the lap_end of this Caution.

        The last lap of the caution  # noqa: E501

        :param lap_end: The lap_end of this Caution.  # noqa: E501
        :type: int
        """

        self._lap_end = lap_end

    @property
    def beneficiary(self):
        """Gets the beneficiary of this Caution.  # noqa: E501

        The lap down vehicle put back on the lead lap  # noqa: E501

        :return: The beneficiary of this Caution.  # noqa: E501
        :rtype: str
        """
        return self._beneficiary

    @beneficiary.setter
    def beneficiary(self, beneficiary):
        """Sets the beneficiary of this Caution.

        The lap down vehicle put back on the lead lap  # noqa: E501

        :param beneficiary: The beneficiary of this Caution.  # noqa: E501
        :type: str
        """

        self._beneficiary = beneficiary

    @property
    def comment(self):
        """Gets the comment of this Caution.  # noqa: E501

        Comments about the caution  # noqa: E501

        :return: The comment of this Caution.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Caution.

        Comments about the caution  # noqa: E501

        :param comment: The comment of this Caution.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def reason(self):
        """Gets the reason of this Caution.  # noqa: E501

        The reason the caution was thrown  # noqa: E501

        :return: The reason of this Caution.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this Caution.

        The reason the caution was thrown  # noqa: E501

        :param reason: The reason of this Caution.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def flag_time(self):
        """Gets the flag_time of this Caution.  # noqa: E501

        The time the caution was thrown  # noqa: E501

        :return: The flag_time of this Caution.  # noqa: E501
        :rtype: datetime
        """
        return self._flag_time

    @flag_time.setter
    def flag_time(self, flag_time):
        """Sets the flag_time of this Caution.

        The time the caution was thrown  # noqa: E501

        :param flag_time: The flag_time of this Caution.  # noqa: E501
        :type: datetime
        """

        self._flag_time = flag_time

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
        if issubclass(Caution, dict):
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
        if not isinstance(other, Caution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
