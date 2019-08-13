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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import ServiceBusManagementClientConfiguration
from .operations import Operations
from .operations import NamespacesOperations
from .operations import DisasterRecoveryConfigsOperations
from .operations import MigrationConfigsOperations
from .operations import QueuesOperations
from .operations import TopicsOperations
from .operations import SubscriptionsOperations
from .operations import RulesOperations
from .operations import RegionsOperations
from .operations import PremiumMessagingRegionsOperations
from .operations import EventHubsOperations
from . import models


class ServiceBusManagementClient(SDKClient):
    """Azure Service Bus client

    :ivar config: Configuration for client.
    :vartype config: ServiceBusManagementClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.servicebus.operations.Operations
    :ivar namespaces: Namespaces operations
    :vartype namespaces: azure.mgmt.servicebus.operations.NamespacesOperations
    :ivar disaster_recovery_configs: DisasterRecoveryConfigs operations
    :vartype disaster_recovery_configs: azure.mgmt.servicebus.operations.DisasterRecoveryConfigsOperations
    :ivar migration_configs: MigrationConfigs operations
    :vartype migration_configs: azure.mgmt.servicebus.operations.MigrationConfigsOperations
    :ivar queues: Queues operations
    :vartype queues: azure.mgmt.servicebus.operations.QueuesOperations
    :ivar topics: Topics operations
    :vartype topics: azure.mgmt.servicebus.operations.TopicsOperations
    :ivar subscriptions: Subscriptions operations
    :vartype subscriptions: azure.mgmt.servicebus.operations.SubscriptionsOperations
    :ivar rules: Rules operations
    :vartype rules: azure.mgmt.servicebus.operations.RulesOperations
    :ivar regions: Regions operations
    :vartype regions: azure.mgmt.servicebus.operations.RegionsOperations
    :ivar premium_messaging_regions: PremiumMessagingRegions operations
    :vartype premium_messaging_regions: azure.mgmt.servicebus.operations.PremiumMessagingRegionsOperations
    :ivar event_hubs: EventHubs operations
    :vartype event_hubs: azure.mgmt.servicebus.operations.EventHubsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials that uniquely identify a
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = ServiceBusManagementClientConfiguration(credentials, subscription_id, base_url)
        super(ServiceBusManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2017-04-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.namespaces = NamespacesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.disaster_recovery_configs = DisasterRecoveryConfigsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.migration_configs = MigrationConfigsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.queues = QueuesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.topics = TopicsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.subscriptions = SubscriptionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.rules = RulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.regions = RegionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.premium_messaging_regions = PremiumMessagingRegionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.event_hubs = EventHubsOperations(
            self._client, self.config, self._serialize, self._deserialize)