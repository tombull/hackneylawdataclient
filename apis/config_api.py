# coding: utf-8

"""
ConfigApi.py
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
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ConfigApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_config(self, document, **kwargs):
        """
        Create some admin-config
        Create one or more admin-config.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_config(document, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Config document: Create a document by sending the paths to be added in the request body. (required)
        :param str select: Select which paths will be returned by the query. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#select)
        :param str populate: Specify which paths to populate. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#populate)
        :param str sort: Set the fields by which to sort. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#sort)
        :return: Config
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document', 'select', 'populate', 'sort']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_config" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'document' is set
        if ('document' not in params) or (params['document'] is None):
            raise ValueError("Missing the required parameter `document` when calling `create_config`")

        resource_path = '/admin-config'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'select' in params:
            query_params['select'] = params['select']
        if 'populate' in params:
            query_params['populate'] = params['populate']
        if 'sort' in params:
            query_params['sort'] = params['sort']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'document' in params:
            body_params = params['document']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/html'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apikey', 'basic']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Config',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_config_by_id(self, id, **kwargs):
        """
        Delete a _config by its unique ID
        Deletes an existing _config by its ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_config_by_id(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The identifier of the resource. (required)
        :param str select: Select which paths will be returned by the query. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#select)
        :param str populate: Specify which paths to populate. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#populate)
        :return: Config
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'select', 'populate']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_config_by_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_config_by_id`")

        resource_path = '/admin-config/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'select' in params:
            query_params['select'] = params['select']
        if 'populate' in params:
            query_params['populate'] = params['populate']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/html'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apikey', 'basic']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Config',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_config_by_query(self, **kwargs):
        """
        Delete some admin-config by query
        Delete all admin-config matching the specified query.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_config_by_query(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str select: Select which paths will be returned by the query. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#select)
        :param str populate: Specify which paths to populate. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#populate)
        :param str sort: Set the fields by which to sort. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#sort)
        :param int skip: How many documents to skip. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#skip)
        :param int limit: The maximum number of documents to send. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#limit)
        :param str conditions: Set the conditions used to find or remove the document(s). [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#conditions)
        :param str distinct: Set to a path name to retrieve an array of distinct values. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#distinct)
        :param str hint: Add an index hint to the query (must be enabled per controller). [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#hint)
        :param str comment: Add a comment to a query (must be enabled per controller). [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#comment)
        :return: list[Config]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['select', 'populate', 'sort', 'skip', 'limit', 'conditions', 'distinct', 'hint', 'comment']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_config_by_query" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/admin-config'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'select' in params:
            query_params['select'] = params['select']
        if 'populate' in params:
            query_params['populate'] = params['populate']
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'skip' in params:
            query_params['skip'] = params['skip']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'conditions' in params:
            query_params['conditions'] = params['conditions']
        if 'distinct' in params:
            query_params['distinct'] = params['distinct']
        if 'hint' in params:
            query_params['hint'] = params['hint']
        if 'comment' in params:
            query_params['comment'] = params['comment']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/html'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apikey', 'basic']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Config]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_config_by_id(self, id, **kwargs):
        """
        Get a _config by its unique ID
        Retrieve a _config by its ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_config_by_id(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The identifier of the resource. (required)
        :param str select: Select which paths will be returned by the query. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#select)
        :param str populate: Specify which paths to populate. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#populate)
        :return: Config
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'select', 'populate']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_config_by_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_config_by_id`")

        resource_path = '/admin-config/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'select' in params:
            query_params['select'] = params['select']
        if 'populate' in params:
            query_params['populate'] = params['populate']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/html'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apikey', 'basic']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Config',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def query_config(self, **kwargs):
        """
        Query some admin-config
        Query over admin-config.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.query_config(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str select: Select which paths will be returned by the query. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#select)
        :param str populate: Specify which paths to populate. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#populate)
        :param str sort: Set the fields by which to sort. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#sort)
        :param bool count: Set to true to return count instead of documents. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#count)
        :param int skip: How many documents to skip. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#skip)
        :param int limit: The maximum number of documents to send. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#limit)
        :param str conditions: Set the conditions used to find or remove the document(s). [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#conditions)
        :param str distinct: Set to a path name to retrieve an array of distinct values. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#distinct)
        :param str hint: Add an index hint to the query (must be enabled per controller). [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#hint)
        :param str comment: Add a comment to a query (must be enabled per controller). [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#comment)
        :return: list[Config]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['select', 'populate', 'sort', 'count', 'skip', 'limit', 'conditions', 'distinct', 'hint', 'comment']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_config" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/admin-config'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'select' in params:
            query_params['select'] = params['select']
        if 'populate' in params:
            query_params['populate'] = params['populate']
        if 'sort' in params:
            query_params['sort'] = params['sort']
        if 'count' in params:
            query_params['count'] = params['count']
        if 'skip' in params:
            query_params['skip'] = params['skip']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'conditions' in params:
            query_params['conditions'] = params['conditions']
        if 'distinct' in params:
            query_params['distinct'] = params['distinct']
        if 'hint' in params:
            query_params['hint'] = params['hint']
        if 'comment' in params:
            query_params['comment'] = params['comment']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/html'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apikey', 'basic']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Config]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_config(self, id, document, **kwargs):
        """
        Modify a _config by its unique ID
        Update an existing _config by its ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_config(id, document, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The identifier of the resource. (required)
        :param Config document: Update a document by sending the paths to be updated in the request body. (required)
        :param str select: Select which paths will be returned by the query. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#select)
        :param str populate: Specify which paths to populate. [doc](https://github.com/wprl/baucis/wiki/Query-String-Parameters#populate)
        :param str x_baucis_update_operator: **BYPASSES VALIDATION** May be used with PUT to update the document using $push, $pull, or $set. [doc](https://github.com/wprl/baucis/wiki/HTTP-Headers)
        :return: Config
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'document', 'select', 'populate', 'x_baucis_update_operator']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_config" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_config`")
        # verify the required parameter 'document' is set
        if ('document' not in params) or (params['document'] is None):
            raise ValueError("Missing the required parameter `document` when calling `update_config`")

        resource_path = '/admin-config/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'select' in params:
            query_params['select'] = params['select']
        if 'populate' in params:
            query_params['populate'] = params['populate']

        header_params = {}
        if 'x_baucis_update_operator' in params:
            header_params['X-Baucis-Update-Operator'] = params['x_baucis_update_operator']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'document' in params:
            body_params = params['document']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/html'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apikey', 'basic']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Config',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
