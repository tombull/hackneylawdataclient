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


class DocumentState(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DocumentState - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'owner_id': 'str',
            'created_at': 'datetime',
            'present': 'bool',
            'case_record': 'CaseRecord',
            'document': 'RequiredDocument',
            'id': 'str',
            'v': 'float',
            'id': 'str'
        }

        self.attribute_map = {
            'owner_id': '_ownerId',
            'created_at': '_createdAt',
            'present': 'present',
            'case_record': 'caseRecord',
            'document': 'document',
            'id': '_id',
            'v': '__v',
            'id': 'id'
        }

        self._owner_id = None
        self._created_at = None
        self._present = None
        self._case_record = None
        self._document = None
        self._id = None
        self._v = None
        self._id = None

    @property
    def owner_id(self):
        """
        Gets the owner_id of this DocumentState.


        :return: The owner_id of this DocumentState.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """
        Sets the owner_id of this DocumentState.


        :param owner_id: The owner_id of this DocumentState.
        :type: str
        """
        self._owner_id = owner_id

    @property
    def created_at(self):
        """
        Gets the created_at of this DocumentState.


        :return: The created_at of this DocumentState.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this DocumentState.


        :param created_at: The created_at of this DocumentState.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def present(self):
        """
        Gets the present of this DocumentState.


        :return: The present of this DocumentState.
        :rtype: bool
        """
        return self._present

    @present.setter
    def present(self, present):
        """
        Sets the present of this DocumentState.


        :param present: The present of this DocumentState.
        :type: bool
        """
        self._present = present

    @property
    def case_record(self):
        """
        Gets the case_record of this DocumentState.


        :return: The case_record of this DocumentState.
        :rtype: CaseRecord
        """
        return self._case_record

    @case_record.setter
    def case_record(self, case_record):
        """
        Sets the case_record of this DocumentState.


        :param case_record: The case_record of this DocumentState.
        :type: CaseRecord
        """
        self._case_record = case_record

    @property
    def document(self):
        """
        Gets the document of this DocumentState.


        :return: The document of this DocumentState.
        :rtype: RequiredDocument
        """
        return self._document

    @document.setter
    def document(self, document):
        """
        Sets the document of this DocumentState.


        :param document: The document of this DocumentState.
        :type: RequiredDocument
        """
        self._document = document

    @property
    def id(self):
        """
        Gets the id of this DocumentState.


        :return: The id of this DocumentState.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DocumentState.


        :param id: The id of this DocumentState.
        :type: str
        """
        self._id = id

    @property
    def v(self):
        """
        Gets the v of this DocumentState.


        :return: The v of this DocumentState.
        :rtype: float
        """
        return self._v

    @v.setter
    def v(self, v):
        """
        Sets the v of this DocumentState.


        :param v: The v of this DocumentState.
        :type: float
        """
        self._v = v

    @property
    def id(self):
        """
        Gets the id of this DocumentState.


        :return: The id of this DocumentState.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DocumentState.


        :param id: The id of this DocumentState.
        :type: str
        """
        self._id = id

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

