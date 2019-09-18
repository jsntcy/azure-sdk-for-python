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

from .settings_py3 import Settings


class UebaSettings(Settings):
    """Represents settings for User and Entity Behavior Analytics enablement.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param etag: Etag of the azure resource
    :type etag: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :ivar atp_license_status: Determines whether the tenant has ATP (Advanced
     Threat Protection) license. Possible values include: 'Enabled', 'Disabled'
    :vartype atp_license_status: str or
     ~azure.mgmt.securityinsight.models.LicenseStatus
    :param is_enabled: Determines whether User and Entity Behavior Analytics
     is enabled for this workspace.
    :type is_enabled: bool
    :ivar status_in_mcas: Determines whether User and Entity Behavior
     Analytics is enabled from MCAS (Microsoft Cloud App Security). Possible
     values include: 'Enabled', 'Disabled'
    :vartype status_in_mcas: str or
     ~azure.mgmt.securityinsight.models.StatusInMcas
    """

    _validation = {
        'kind': {'required': True},
        'atp_license_status': {'readonly': True},
        'status_in_mcas': {'readonly': True},
    }

    _attribute_map = {
        'etag': {'key': 'etag', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'atp_license_status': {'key': 'properties.atpLicenseStatus', 'type': 'str'},
        'is_enabled': {'key': 'properties.isEnabled', 'type': 'bool'},
        'status_in_mcas': {'key': 'properties.statusInMcas', 'type': 'str'},
    }

    def __init__(self, *, etag: str=None, is_enabled: bool=None, **kwargs) -> None:
        super(UebaSettings, self).__init__(etag=etag, **kwargs)
        self.atp_license_status = None
        self.is_enabled = is_enabled
        self.status_in_mcas = None
        self.kind = 'UebaSettings'
