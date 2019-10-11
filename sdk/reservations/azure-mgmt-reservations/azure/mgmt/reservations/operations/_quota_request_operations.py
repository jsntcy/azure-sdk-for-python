# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling

from .. import models


class QuotaRequestOperations(object):
    """QuotaRequestOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Api version. Constant value: "2019-07-19-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2019-07-19-preview"

        self.config = config


    def _create_initial(
            self, subscription_id, provider_id, location, create_quota_request, if_match, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
            'providerId': self._serialize.url("provider_id", provider_id, 'str'),
            'location': self._serialize.url("location", location, 'str'),
            'resourceName': self._serialize.url("self.config.resource_name", self.config.resource_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(create_quota_request, 'CurrentQuotaLimitBase')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise models.ExceptionResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('QuotaRequestOneResourceSubmitResponse', response)
        if response.status_code == 201:
            deserialized = self._deserialize('QuotaRequestSubmitResponse201', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create(
            self, subscription_id, provider_id, location, create_quota_request, if_match, custom_headers=None, raw=False, polling=True, **operation_config):
        """Submits a Quota Request for a resource provider at the specified
        location for the specific resource in the parameter.

        Submits Quota change request for a resource provider for the specified
        location for the specific resource in the parameter. To use, first make
        a Get request to get quota information. This information consists of a
        list of resources and information regarding those resources. For all
        the resources in that list which require an update to their quotas,
        update their limit fields in the response from the Get request to their
        new values. Then, submit this updated JSON object to this quota request
        API. This will update the quotas to the values specified. The location
        header in the response will be used to track the status of the quota
        request.

        :param subscription_id: Azure subscription id.
        :type subscription_id: str
        :param provider_id: Azure resource Provider id.
        :type provider_id: str
        :param location: Azure region.
        :type location: str
        :param create_quota_request: Quota requests payload.
        :type create_quota_request:
         ~azure.mgmt.reservations.models.CurrentQuotaLimitBase
        :param if_match: ETag of the Entity. ETag should match the current
         entity state from the header response of the GET request or it should
         be * for unconditional update.
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns object or
         ClientRawResponse<object> if raw==True
        :rtype: ~msrestazure.azure_operation.AzureOperationPoller[object] or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[object]]
        :raises:
         :class:`ExceptionResponseException<azure.mgmt.reservations.models.ExceptionResponseException>`
        """
        raw_result = self._create_initial(
            subscription_id=subscription_id,
            provider_id=provider_id,
            location=location,
            create_quota_request=create_quota_request,
            if_match=if_match,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('object', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    create.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Capacity/providers/{providerId}/locations/{location}/serviceLimits/{resourceName}'}


    def _patch_method_initial(
            self, subscription_id, provider_id, location, create_quota_request, if_match, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.patch_method.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
            'providerId': self._serialize.url("provider_id", provider_id, 'str'),
            'location': self._serialize.url("location", location, 'str'),
            'resourceName': self._serialize.url("self.config.resource_name", self.config.resource_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(create_quota_request, 'CurrentQuotaLimitBase')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise models.ExceptionResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('QuotaRequestOneResourceSubmitResponse', response)
        if response.status_code == 201:
            deserialized = self._deserialize('QuotaRequestSubmitResponse201', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def patch_method(
            self, subscription_id, provider_id, location, create_quota_request, if_match, custom_headers=None, raw=False, polling=True, **operation_config):
        """Submits a Quota Request for a resource provider at the specified
        location for the specific resource in the parameter.

        Submits Quota change request for a resource provider for the specified
        location for the specific resource in the parameter. To use, first make
        a Get request to get quota information. This information consists of a
        list of resources and information regarding those resources. For all
        the resources in that list which require an update to their quotas,
        update their limit fields in the response from the Get request to their
        new values. Then, submit this updated JSON object to this quota request
        API. This will update the quotas to the values specified. The location
        header in the response will be used to track the status of the quota
        request.

        :param subscription_id: Azure subscription id.
        :type subscription_id: str
        :param provider_id: Azure resource Provider id.
        :type provider_id: str
        :param location: Azure region.
        :type location: str
        :param create_quota_request: Quota requests payload.
        :type create_quota_request:
         ~azure.mgmt.reservations.models.CurrentQuotaLimitBase
        :param if_match: ETag of the Entity. ETag should match the current
         entity state from the header response of the GET request or it should
         be * for unconditional update.
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns object or
         ClientRawResponse<object> if raw==True
        :rtype: ~msrestazure.azure_operation.AzureOperationPoller[object] or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[object]]
        :raises:
         :class:`ExceptionResponseException<azure.mgmt.reservations.models.ExceptionResponseException>`
        """
        raw_result = self._patch_method_initial(
            subscription_id=subscription_id,
            provider_id=provider_id,
            location=location,
            create_quota_request=create_quota_request,
            if_match=if_match,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('object', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    patch_method.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Capacity/providers/{providerId}/locations/{location}/serviceLimits/{resourceName}'}
