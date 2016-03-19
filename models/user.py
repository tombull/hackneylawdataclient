# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class User(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        User - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'owner_id': 'str',
            'created_at': 'datetime',
            'identifier': 'str',
            'identifier_type': 'str',
            'default_language': 'str',
            'optional_identifier': 'str',
            'id': 'str',
            'v': 'float',
            'id': 'str',
            'case_records': 'list[str]'
        }

        self.attribute_map = {
            'owner_id': '_ownerId',
            'created_at': '_createdAt',
            'identifier': 'identifier',
            'identifier_type': 'identifierType',
            'default_language': 'defaultLanguage',
            'optional_identifier': 'optionalIdentifier',
            'id': '_id',
            'v': '__v',
            'id': 'id',
            'case_records': 'caseRecords'
        }

        self._owner_id = None
        self._created_at = None
        self._identifier = None
        self._identifier_type = None
        self._default_language = None
        self._optional_identifier = None
        self._id = None
        self._v = None
        self._id = None
        self._case_records = None

    @property
    def owner_id(self):
        """
        Gets the owner_id of this User.


        :return: The owner_id of this User.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """
        Sets the owner_id of this User.


        :param owner_id: The owner_id of this User.
        :type: str
        """
        self._owner_id = owner_id

    @property
    def created_at(self):
        """
        Gets the created_at of this User.


        :return: The created_at of this User.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this User.


        :param created_at: The created_at of this User.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def identifier(self):
        """
        Gets the identifier of this User.


        :return: The identifier of this User.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this User.


        :param identifier: The identifier of this User.
        :type: str
        """
        self._identifier = identifier

    @property
    def identifier_type(self):
        """
        Gets the identifier_type of this User.


        :return: The identifier_type of this User.
        :rtype: str
        """
        return self._identifier_type

    @identifier_type.setter
    def identifier_type(self, identifier_type):
        """
        Sets the identifier_type of this User.


        :param identifier_type: The identifier_type of this User.
        :type: str
        """
        self._identifier_type = identifier_type

    @property
    def default_language(self):
        """
        Gets the default_language of this User.


        :return: The default_language of this User.
        :rtype: str
        """
        return self._default_language

    @default_language.setter
    def default_language(self, default_language):
        """
        Sets the default_language of this User.


        :param default_language: The default_language of this User.
        :type: str
        """
        self._default_language = default_language

    @property
    def optional_identifier(self):
        """
        Gets the optional_identifier of this User.


        :return: The optional_identifier of this User.
        :rtype: str
        """
        return self._optional_identifier

    @optional_identifier.setter
    def optional_identifier(self, optional_identifier):
        """
        Sets the optional_identifier of this User.


        :param optional_identifier: The optional_identifier of this User.
        :type: str
        """
        self._optional_identifier = optional_identifier

    @property
    def id(self):
        """
        Gets the id of this User.


        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.


        :param id: The id of this User.
        :type: str
        """
        self._id = id

    @property
    def v(self):
        """
        Gets the v of this User.


        :return: The v of this User.
        :rtype: float
        """
        return self._v

    @v.setter
    def v(self, v):
        """
        Sets the v of this User.


        :param v: The v of this User.
        :type: float
        """
        self._v = v

    @property
    def id(self):
        """
        Gets the id of this User.


        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.


        :param id: The id of this User.
        :type: str
        """
        self._id = id

    @property
    def case_records(self):
        """
        Gets the case_records of this User.


        :return: The case_records of this User.
        :rtype: list[str]
        """
        return self._case_records

    @case_records.setter
    def case_records(self, case_records):
        """
        Sets the case_records of this User.


        :param case_records: The case_records of this User.
        :type: list[str]
        """
        self._case_records = case_records

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

