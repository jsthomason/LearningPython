# coding: utf-8

"""
    SevOne API Documentation

    Supported endpoints by the new RESTful API  # noqa: E501

    OpenAPI spec version: 2.1.18, Hash: db562e6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class WorkHoursApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_work_hours(self, work_hours_group, **kwargs):  # noqa: E501
        """Create WorkHours  # noqa: E501

        Creates a new WorkHours  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_work_hours(work_hours_group, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WorkHoursGroupDto work_hours_group: WorkHour object that will be added to the database (required)
        :return: WorkHoursGroupDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_work_hours_with_http_info(work_hours_group, **kwargs)  # noqa: E501
        else:
            (data) = self.create_work_hours_with_http_info(work_hours_group, **kwargs)  # noqa: E501
            return data

    def create_work_hours_with_http_info(self, work_hours_group, **kwargs):  # noqa: E501
        """Create WorkHours  # noqa: E501

        Creates a new WorkHours  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_work_hours_with_http_info(work_hours_group, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WorkHoursGroupDto work_hours_group: WorkHour object that will be added to the database (required)
        :return: WorkHoursGroupDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['work_hours_group']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_work_hours" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'work_hours_group' is set
        if ('work_hours_group' not in params or
                params['work_hours_group'] is None):
            raise ValueError("Missing the required parameter `work_hours_group` when calling `create_work_hours`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'work_hours_group' in params:
            body_params = params['work_hours_group']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/workhours', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkHoursGroupDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_work_hours_group_by_id(self, id, **kwargs):  # noqa: E501
        """Delete WorkHour group  # noqa: E501

        Deletes an existing WorkHour group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_work_hours_group_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the WorkHour group to be deleted (required)
        :return: ResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_work_hours_group_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_work_hours_group_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_work_hours_group_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete WorkHour group  # noqa: E501

        Deletes an existing WorkHour group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_work_hours_group_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the WorkHour group to be deleted (required)
        :return: ResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_work_hours_group_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_work_hours_group_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/workhours/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_work_hours(self, **kwargs):  # noqa: E501
        """Get all WorkHours  # noqa: E501

        Endpoint for retrieving all WorkHours that supports pagination  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_work_hours(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The number of the requested page, defaults to 0
        :param int size: The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default)
        :param bool include_count: Whether to query for total elements count; defaults to true, set to false for performance boost
        :param str sort_by: String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort
        :param str fields: String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned 
        :param str name: Filter by WorkHours group name
        :return: PagerWorkHoursGroupDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_work_hours_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_work_hours_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_work_hours_with_http_info(self, **kwargs):  # noqa: E501
        """Get all WorkHours  # noqa: E501

        Endpoint for retrieving all WorkHours that supports pagination  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_work_hours_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The number of the requested page, defaults to 0
        :param int size: The size of the requested page, defaults to 20; limited to a configurable maximum (10000 by default)
        :param bool include_count: Whether to query for total elements count; defaults to true, set to false for performance boost
        :param str sort_by: String array of format \"parameter, -parameter, natural\\*parameter, -natural\\*parameter\", where minus is for descending, natural* is for natural sort
        :param str fields: String array of format \"id,name,objects(id,pluginId)\"; Defines which fields are returned 
        :param str name: Filter by WorkHours group name
        :return: PagerWorkHoursGroupDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'size', 'include_count', 'sort_by', 'fields', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_work_hours" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'include_count' in params:
            query_params.append(('includeCount', params['include_count']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sortBy', params['sort_by']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/workhours', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagerWorkHoursGroupDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_work_hours_by_group(self, id, **kwargs):  # noqa: E501
        """Get WorkHour by group  # noqa: E501

        Endpoint for retrieving WorkHours info by group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_work_hours_by_group(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: WorkHour group Id (required)
        :return: WorkHoursGroupDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_work_hours_by_group_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_work_hours_by_group_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_work_hours_by_group_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get WorkHour by group  # noqa: E501

        Endpoint for retrieving WorkHours info by group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_work_hours_by_group_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: WorkHour group Id (required)
        :return: WorkHoursGroupDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_work_hours_by_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_work_hours_by_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/workhours/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkHoursGroupDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_work_hours_by_group_id(self, id, work_hours_group, **kwargs):  # noqa: E501
        """Update WorkHours  # noqa: E501

        Updates an existing WorkHours  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_work_hours_by_group_id(id, work_hours_group, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the WorkHours to be updated (required)
        :param WorkHoursGroupDto work_hours_group: WorkHours to be updated (required)
        :return: WorkHoursGroupDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_work_hours_by_group_id_with_http_info(id, work_hours_group, **kwargs)  # noqa: E501
        else:
            (data) = self.update_work_hours_by_group_id_with_http_info(id, work_hours_group, **kwargs)  # noqa: E501
            return data

    def update_work_hours_by_group_id_with_http_info(self, id, work_hours_group, **kwargs):  # noqa: E501
        """Update WorkHours  # noqa: E501

        Updates an existing WorkHours  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_work_hours_by_group_id_with_http_info(id, work_hours_group, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the WorkHours to be updated (required)
        :param WorkHoursGroupDto work_hours_group: WorkHours to be updated (required)
        :return: WorkHoursGroupDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'work_hours_group']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_work_hours_by_group_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_work_hours_by_group_id`")  # noqa: E501
        # verify the required parameter 'work_hours_group' is set
        if ('work_hours_group' not in params or
                params['work_hours_group'] is None):
            raise ValueError("Missing the required parameter `work_hours_group` when calling `update_work_hours_by_group_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'work_hours_group' in params:
            body_params = params['work_hours_group']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/workhours/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkHoursGroupDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
