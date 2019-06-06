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


class EnrollmentAccountListResult(Model):
    """Result of listing enrollment accounts.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: The list of enrollment accounts.
    :vartype value: list[~azure.mgmt.billing.models.EnrollmentAccount]
    :ivar next_link: The link (url) to the next page of results.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[EnrollmentAccount]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(EnrollmentAccountListResult, self).__init__(**kwargs)
        self.value = None
        self.next_link = None
