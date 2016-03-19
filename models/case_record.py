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


class CaseRecord(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CaseRecord - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'owner_id': 'str',
            'created_at': 'datetime',
            'start_time': 'datetime',
            'case_state': 'str',
            'relation_to_user': 'str',
            'user': 'User',
            'case_type': 'Classification',
            'id': 'str',
            'v': 'float',
            'id': 'str',
            'location': 'GeoJsonPoint',
            'related_files': 'list[str]',
            'related_pictures': 'list[str]',
            'required_documents': 'list[str]',
            'contact_items': 'list[str]',
            'referral': 'list[str]'
        }

        self.attribute_map = {
            'owner_id': '_ownerId',
            'created_at': '_createdAt',
            'start_time': 'startTime',
            'case_state': 'caseState',
            'relation_to_user': 'relationToUser',
            'user': 'user',
            'case_type': 'caseType',
            'id': '_id',
            'v': '__v',
            
            'location': 'location',
            'related_files': 'relatedFiles',
            'related_pictures': 'relatedPictures',
            'required_documents': 'requiredDocuments',
            'contact_items': 'contactItems',
            'referral': 'referral'
        }

        self._owner_id = None
        self._created_at = None
        self._start_time = None
        self._case_state = None
        self._relation_to_user = None
        self._user = None
        self._case_type = None
        self._id = None
        self._v = None
        self._id = None
        self._location = None
        self._related_files = None
        self._related_pictures = None
        self._required_documents = None
        self._contact_items = None
        self._referral = None

    @property
    def owner_id(self):
        """
        Gets the owner_id of this CaseRecord.


        :return: The owner_id of this CaseRecord.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """
        Sets the owner_id of this CaseRecord.


        :param owner_id: The owner_id of this CaseRecord.
        :type: str
        """
        self._owner_id = owner_id

    @property
    def created_at(self):
        """
        Gets the created_at of this CaseRecord.


        :return: The created_at of this CaseRecord.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this CaseRecord.


        :param created_at: The created_at of this CaseRecord.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def start_time(self):
        """
        Gets the start_time of this CaseRecord.


        :return: The start_time of this CaseRecord.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this CaseRecord.


        :param start_time: The start_time of this CaseRecord.
        :type: datetime
        """
        self._start_time = start_time

    @property
    def case_state(self):
        """
        Gets the case_state of this CaseRecord.


        :return: The case_state of this CaseRecord.
        :rtype: str
        """
        return self._case_state

    @case_state.setter
    def case_state(self, case_state):
        """
        Sets the case_state of this CaseRecord.


        :param case_state: The case_state of this CaseRecord.
        :type: str
        """
        self._case_state = case_state

    @property
    def relation_to_user(self):
        """
        Gets the relation_to_user of this CaseRecord.


        :return: The relation_to_user of this CaseRecord.
        :rtype: str
        """
        return self._relation_to_user

    @relation_to_user.setter
    def relation_to_user(self, relation_to_user):
        """
        Sets the relation_to_user of this CaseRecord.


        :param relation_to_user: The relation_to_user of this CaseRecord.
        :type: str
        """
        self._relation_to_user = relation_to_user

    @property
    def user(self):
        """
        Gets the user of this CaseRecord.


        :return: The user of this CaseRecord.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this CaseRecord.


        :param user: The user of this CaseRecord.
        :type: User
        """
        self._user = user

    @property
    def case_type(self):
        """
        Gets the case_type of this CaseRecord.


        :return: The case_type of this CaseRecord.
        :rtype: Classification
        """
        return self._case_type

    @case_type.setter
    def case_type(self, case_type):
        """
        Sets the case_type of this CaseRecord.


        :param case_type: The case_type of this CaseRecord.
        :type: Classification
        """
        self._case_type = case_type

    @property
    def id(self):
        """
        Gets the id of this CaseRecord.


        :return: The id of this CaseRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CaseRecord.


        :param id: The id of this CaseRecord.
        :type: str
        """
        self._id = id

    @property
    def v(self):
        """
        Gets the v of this CaseRecord.


        :return: The v of this CaseRecord.
        :rtype: float
        """
        return self._v

    @v.setter
    def v(self, v):
        """
        Sets the v of this CaseRecord.


        :param v: The v of this CaseRecord.
        :type: float
        """
        self._v = v

    @property
    def id(self):
        """
        Gets the id of this CaseRecord.


        :return: The id of this CaseRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CaseRecord.


        :param id: The id of this CaseRecord.
        :type: str
        """
        self._id = id

    @property
    def location(self):
        """
        Gets the location of this CaseRecord.


        :return: The location of this CaseRecord.
        :rtype: GeoJsonPoint
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this CaseRecord.


        :param location: The location of this CaseRecord.
        :type: GeoJsonPoint
        """
        self._location = location

    @property
    def related_files(self):
        """
        Gets the related_files of this CaseRecord.


        :return: The related_files of this CaseRecord.
        :rtype: list[str]
        """
        return self._related_files

    @related_files.setter
    def related_files(self, related_files):
        """
        Sets the related_files of this CaseRecord.


        :param related_files: The related_files of this CaseRecord.
        :type: list[str]
        """
        self._related_files = related_files

    @property
    def related_pictures(self):
        """
        Gets the related_pictures of this CaseRecord.


        :return: The related_pictures of this CaseRecord.
        :rtype: list[str]
        """
        return self._related_pictures

    @related_pictures.setter
    def related_pictures(self, related_pictures):
        """
        Sets the related_pictures of this CaseRecord.


        :param related_pictures: The related_pictures of this CaseRecord.
        :type: list[str]
        """
        self._related_pictures = related_pictures

    @property
    def required_documents(self):
        """
        Gets the required_documents of this CaseRecord.


        :return: The required_documents of this CaseRecord.
        :rtype: list[str]
        """
        return self._required_documents

    @required_documents.setter
    def required_documents(self, required_documents):
        """
        Sets the required_documents of this CaseRecord.


        :param required_documents: The required_documents of this CaseRecord.
        :type: list[str]
        """
        self._required_documents = required_documents

    @property
    def contact_items(self):
        """
        Gets the contact_items of this CaseRecord.


        :return: The contact_items of this CaseRecord.
        :rtype: list[str]
        """
        return self._contact_items

    @contact_items.setter
    def contact_items(self, contact_items):
        """
        Sets the contact_items of this CaseRecord.


        :param contact_items: The contact_items of this CaseRecord.
        :type: list[str]
        """
        self._contact_items = contact_items

    @property
    def referral(self):
        """
        Gets the referral of this CaseRecord.


        :return: The referral of this CaseRecord.
        :rtype: list[str]
        """
        return self._referral

    @referral.setter
    def referral(self, referral):
        """
        Sets the referral of this CaseRecord.


        :param referral: The referral of this CaseRecord.
        :type: list[str]
        """
        self._referral = referral

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

