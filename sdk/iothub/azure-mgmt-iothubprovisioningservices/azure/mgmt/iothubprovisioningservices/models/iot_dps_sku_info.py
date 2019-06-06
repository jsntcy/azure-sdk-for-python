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


class IotDpsSkuInfo(Model):
    """List of possible provisioning service SKUs.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: Sku name. Possible values include: 'S1'
    :type name: str or ~azure.mgmt.iothubprovisioningservices.models.IotDpsSku
    :ivar tier: Pricing tier name of the provisioning service.
    :vartype tier: str
    :param capacity: The number of units to provision
    :type capacity: long
    """

    _validation = {
        'tier': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'long'},
    }

    def __init__(self, **kwargs):
        super(IotDpsSkuInfo, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.tier = None
        self.capacity = kwargs.get('capacity', None)
