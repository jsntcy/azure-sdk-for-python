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

from msrest.serialization import Model


class AvailableClustersList(Model):
    """The response of the List Available Clusters operation.

    :param value: The count of readily available and pre-provisioned Event
     Hubs Clusters per region.
    :type value:
     list[~azure.mgmt.eventhub.v2018_01_01_preview.models.AvailableCluster]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[AvailableCluster]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(AvailableClustersList, self).__init__(**kwargs)
        self.value = value
