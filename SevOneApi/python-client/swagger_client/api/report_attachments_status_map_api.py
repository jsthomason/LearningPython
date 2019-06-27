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


class ReportAttachmentsStatusMapApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_status_map_attachment(self, id, request_dto, **kwargs):  # noqa: E501
        """Create statusmap attachment  # noqa: E501

        Create a new statusmap attachment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_status_map_attachment(id, request_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the report where the report attachment will be created (required)
        :param StatusMapAttachmentRequestDtoV1 request_dto: StatusMap attachment object (required)
        :return: StatusMapAttachmentResponseDtoV1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_status_map_attachment_with_http_info(id, request_dto, **kwargs)  # noqa: E501
        else:
            (data) = self.create_status_map_attachment_with_http_info(id, request_dto, **kwargs)  # noqa: E501
            return data

    def create_status_map_attachment_with_http_info(self, id, request_dto, **kwargs):  # noqa: E501
        """Create statusmap attachment  # noqa: E501

        Create a new statusmap attachment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_status_map_attachment_with_http_info(id, request_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the report where the report attachment will be created (required)
        :param StatusMapAttachmentRequestDtoV1 request_dto: StatusMap attachment object (required)
        :return: StatusMapAttachmentResponseDtoV1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'request_dto']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_status_map_attachment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_status_map_attachment`")  # noqa: E501
        # verify the required parameter 'request_dto' is set
        if ('request_dto' not in params or
                params['request_dto'] is None):
            raise ValueError("Missing the required parameter `request_dto` when calling `create_status_map_attachment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request_dto' in params:
            body_params = params['request_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reports/{id}/attachments/statusmap', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusMapAttachmentResponseDtoV1',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_status_map_attachment1(self, id, request_dto, **kwargs):  # noqa: E501
        """Create statusmap attachment  # noqa: E501

        Create a new statusmap attachment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_status_map_attachment1(id, request_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the report where the report attachment will be created (required)
        :param StatusMapAttachmentRequestDto request_dto: StatusMap attachment object (required)
        :return: StatusMapAttachmentResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_status_map_attachment1_with_http_info(id, request_dto, **kwargs)  # noqa: E501
        else:
            (data) = self.create_status_map_attachment1_with_http_info(id, request_dto, **kwargs)  # noqa: E501
            return data

    def create_status_map_attachment1_with_http_info(self, id, request_dto, **kwargs):  # noqa: E501
        """Create statusmap attachment  # noqa: E501

        Create a new statusmap attachment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_status_map_attachment1_with_http_info(id, request_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the report where the report attachment will be created (required)
        :param StatusMapAttachmentRequestDto request_dto: StatusMap attachment object (required)
        :return: StatusMapAttachmentResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'request_dto']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_status_map_attachment1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `create_status_map_attachment1`")  # noqa: E501
        # verify the required parameter 'request_dto' is set
        if ('request_dto' not in params or
                params['request_dto'] is None):
            raise ValueError("Missing the required parameter `request_dto` when calling `create_status_map_attachment1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request_dto' in params:
            body_params = params['request_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/reports/{id}/attachments/statusmap', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusMapAttachmentResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_status_attachment(self, id, **kwargs):  # noqa: E501
        """Get status map attachment  # noqa: E501

        Get an existing status map attachment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status_attachment(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: StatusMap attachment id (required)
        :return: StatusMapAttachmentResponseDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_status_attachment_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_status_attachment_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_status_attachment_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get status map attachment  # noqa: E501

        Get an existing status map attachment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status_attachment_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: StatusMap attachment id (required)
        :return: StatusMapAttachmentResponseDto
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
                    " to method get_status_attachment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_status_attachment`")  # noqa: E501

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
            '/api/v2/reports/attachments/statusmap/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusMapAttachmentResponseDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_status_map_attachment_resources(self, id, **kwargs):  # noqa: E501
        """Get resources  # noqa: E501

        Get statusmap resources  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status_map_attachment_resources(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the report attachment (required)
        :return: StatusMapAttachmentResourceV1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_status_map_attachment_resources_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_status_map_attachment_resources_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_status_map_attachment_resources_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get resources  # noqa: E501

        Get statusmap resources  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status_map_attachment_resources_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the report attachment (required)
        :return: StatusMapAttachmentResourceV1
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
                    " to method get_status_map_attachment_resources" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_status_map_attachment_resources`")  # noqa: E501

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
            '/api/v1/reports/attachments/statusmap/{id}/resources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusMapAttachmentResourceV1',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_status_map_attachment_resources1(self, id, **kwargs):  # noqa: E501
        """Get resources  # noqa: E501

        Get statusmap resources  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status_map_attachment_resources1(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the report attachment (required)
        :return: StatusMapAttachmentResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_status_map_attachment_resources1_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_status_map_attachment_resources1_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_status_map_attachment_resources1_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get resources  # noqa: E501

        Get statusmap resources  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status_map_attachment_resources1_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the report attachment (required)
        :return: StatusMapAttachmentResource
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
                    " to method get_status_map_attachment_resources1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_status_map_attachment_resources1`")  # noqa: E501

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
            '/api/v2/reports/attachments/statusmap/{id}/resources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusMapAttachmentResource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_status_map_attachment_resources(self, id, resources, **kwargs):  # noqa: E501
        """Update resources  # noqa: E501

        Update statusmap resources  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_status_map_attachment_resources(id, resources, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the report attachment (required)
        :param StatusMapAttachmentResourceV1 resources: StatusMap attachment resources (required)
        :return: StatusMapAttachmentResourceV1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_status_map_attachment_resources_with_http_info(id, resources, **kwargs)  # noqa: E501
        else:
            (data) = self.update_status_map_attachment_resources_with_http_info(id, resources, **kwargs)  # noqa: E501
            return data

    def update_status_map_attachment_resources_with_http_info(self, id, resources, **kwargs):  # noqa: E501
        """Update resources  # noqa: E501

        Update statusmap resources  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_status_map_attachment_resources_with_http_info(id, resources, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the report attachment (required)
        :param StatusMapAttachmentResourceV1 resources: StatusMap attachment resources (required)
        :return: StatusMapAttachmentResourceV1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'resources']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_status_map_attachment_resources" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_status_map_attachment_resources`")  # noqa: E501
        # verify the required parameter 'resources' is set
        if ('resources' not in params or
                params['resources'] is None):
            raise ValueError("Missing the required parameter `resources` when calling `update_status_map_attachment_resources`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'resources' in params:
            body_params = params['resources']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/reports/attachments/statusmap/{id}/resources', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusMapAttachmentResourceV1',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_status_map_attachment_resources1(self, id, resources, **kwargs):  # noqa: E501
        """Update resources  # noqa: E501

        Update statusmap resources  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_status_map_attachment_resources1(id, resources, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the report attachment (required)
        :param StatusMapAttachmentResource resources: StatusMap attachment resources (required)
        :return: StatusMapAttachmentResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_status_map_attachment_resources1_with_http_info(id, resources, **kwargs)  # noqa: E501
        else:
            (data) = self.update_status_map_attachment_resources1_with_http_info(id, resources, **kwargs)  # noqa: E501
            return data

    def update_status_map_attachment_resources1_with_http_info(self, id, resources, **kwargs):  # noqa: E501
        """Update resources  # noqa: E501

        Update statusmap resources  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_status_map_attachment_resources1_with_http_info(id, resources, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the report attachment (required)
        :param StatusMapAttachmentResource resources: StatusMap attachment resources (required)
        :return: StatusMapAttachmentResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'resources']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_status_map_attachment_resources1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_status_map_attachment_resources1`")  # noqa: E501
        # verify the required parameter 'resources' is set
        if ('resources' not in params or
                params['resources'] is None):
            raise ValueError("Missing the required parameter `resources` when calling `update_status_map_attachment_resources1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'resources' in params:
            body_params = params['resources']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/reports/attachments/statusmap/{id}/resources', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusMapAttachmentResource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
