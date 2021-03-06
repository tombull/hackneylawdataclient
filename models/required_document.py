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


class RequiredDocument(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RequiredDocument - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'owner_id': 'str',
            'created_at': 'datetime',
            'name': 'str',
            'description': 'str',
            'explanation': 'str',
            'classification': 'Classification',
            'related_answer': 'PotentialAnswer',
            'id': 'str',
            'v': 'float',
            'id': 'str',
            'uploaded_document': 'list[str]',
            'uploaded_picture': 'list[str]',
            'document_state': 'list[str]'
        }

        self.attribute_map = {
            'owner_id': '_ownerId',
            'created_at': '_createdAt',
            'name': 'name',
            'description': 'description',
            'explanation': 'explanation',
            'classification': 'classification',
            'related_answer': 'relatedAnswer',
            'id': '_id',
            'v': '__v',
            'uploaded_document': 'uploadedDocument',
            'uploaded_picture': 'uploadedPicture',
            'document_state': 'documentState'
        }

        self._owner_id = None
        self._created_at = None
        self._name = None
        self._description = None
        self._explanation = None
        self._classification = None
        self._related_answer = None
        self._id = None
        self._v = None
        self._id = None
        self._uploaded_document = None
        self._uploaded_picture = None
        self._document_state = None

    @property
    def owner_id(self):
        """
        Gets the owner_id of this RequiredDocument.


        :return: The owner_id of this RequiredDocument.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """
        Sets the owner_id of this RequiredDocument.


        :param owner_id: The owner_id of this RequiredDocument.
        :type: str
        """
        self._owner_id = owner_id

    @property
    def created_at(self):
        """
        Gets the created_at of this RequiredDocument.


        :return: The created_at of this RequiredDocument.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this RequiredDocument.


        :param created_at: The created_at of this RequiredDocument.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def name(self):
        """
        Gets the name of this RequiredDocument.


        :return: The name of this RequiredDocument.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RequiredDocument.


        :param name: The name of this RequiredDocument.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this RequiredDocument.


        :return: The description of this RequiredDocument.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RequiredDocument.


        :param description: The description of this RequiredDocument.
        :type: str
        """
        self._description = description

    @property
    def explanation(self):
        """
        Gets the explanation of this RequiredDocument.


        :return: The explanation of this RequiredDocument.
        :rtype: str
        """
        return self._explanation

    @explanation.setter
    def explanation(self, explanation):
        """
        Sets the explanation of this RequiredDocument.


        :param explanation: The explanation of this RequiredDocument.
        :type: str
        """
        self._explanation = explanation

    @property
    def classification(self):
        """
        Gets the classification of this RequiredDocument.


        :return: The classification of this RequiredDocument.
        :rtype: Classification
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """
        Sets the classification of this RequiredDocument.


        :param classification: The classification of this RequiredDocument.
        :type: Classification
        """
        self._classification = classification

    @property
    def related_answer(self):
        """
        Gets the related_answer of this RequiredDocument.


        :return: The related_answer of this RequiredDocument.
        :rtype: PotentialAnswer
        """
        return self._related_answer

    @related_answer.setter
    def related_answer(self, related_answer):
        """
        Sets the related_answer of this RequiredDocument.


        :param related_answer: The related_answer of this RequiredDocument.
        :type: PotentialAnswer
        """
        self._related_answer = related_answer

    @property
    def id(self):
        """
        Gets the id of this RequiredDocument.


        :return: The id of this RequiredDocument.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RequiredDocument.


        :param id: The id of this RequiredDocument.
        :type: str
        """
        self._id = id

    @property
    def v(self):
        """
        Gets the v of this RequiredDocument.


        :return: The v of this RequiredDocument.
        :rtype: float
        """
        return self._v

    @v.setter
    def v(self, v):
        """
        Sets the v of this RequiredDocument.


        :param v: The v of this RequiredDocument.
        :type: float
        """
        self._v = v

    @property
    def id(self):
        """
        Gets the id of this RequiredDocument.


        :return: The id of this RequiredDocument.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RequiredDocument.


        :param id: The id of this RequiredDocument.
        :type: str
        """
        self._id = id

    @property
    def uploaded_document(self):
        """
        Gets the uploaded_document of this RequiredDocument.


        :return: The uploaded_document of this RequiredDocument.
        :rtype: list[str]
        """
        return self._uploaded_document

    @uploaded_document.setter
    def uploaded_document(self, uploaded_document):
        """
        Sets the uploaded_document of this RequiredDocument.


        :param uploaded_document: The uploaded_document of this RequiredDocument.
        :type: list[str]
        """
        self._uploaded_document = uploaded_document

    @property
    def uploaded_picture(self):
        """
        Gets the uploaded_picture of this RequiredDocument.


        :return: The uploaded_picture of this RequiredDocument.
        :rtype: list[str]
        """
        return self._uploaded_picture

    @uploaded_picture.setter
    def uploaded_picture(self, uploaded_picture):
        """
        Sets the uploaded_picture of this RequiredDocument.


        :param uploaded_picture: The uploaded_picture of this RequiredDocument.
        :type: list[str]
        """
        self._uploaded_picture = uploaded_picture

    @property
    def document_state(self):
        """
        Gets the document_state of this RequiredDocument.


        :return: The document_state of this RequiredDocument.
        :rtype: list[str]
        """
        return self._document_state

    @document_state.setter
    def document_state(self, document_state):
        """
        Sets the document_state of this RequiredDocument.


        :param document_state: The document_state of this RequiredDocument.
        :type: list[str]
        """
        self._document_state = document_state

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

