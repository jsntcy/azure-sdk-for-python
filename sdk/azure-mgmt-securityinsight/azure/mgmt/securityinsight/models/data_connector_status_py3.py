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


class DataConnectorStatus(Model):
    """alert rule template data connector status.

    :param connector_id: the connector id
    :type connector_id: str
    :param data_types: The data types availability map
    :type data_types: dict[str, str or
     ~azure.mgmt.securityinsight.models.DataTypeStatus]
    """

    _attribute_map = {
        'connector_id': {'key': 'connectorId', 'type': 'str'},
        'data_types': {'key': 'dataTypes', 'type': '{str}'},
    }

    def __init__(self, *, connector_id: str=None, data_types=None, **kwargs) -> None:
        super(DataConnectorStatus, self).__init__(**kwargs)
        self.connector_id = connector_id
        self.data_types = data_types
