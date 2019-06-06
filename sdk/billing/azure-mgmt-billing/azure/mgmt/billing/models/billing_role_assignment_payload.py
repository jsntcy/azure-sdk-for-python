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


class BillingRoleAssignmentPayload(Model):
    """The payload use to update role assignment on a scope.

    :param principal_id: The user's principal id that the role gets assigned
     to
    :type principal_id: str
    :param billing_role_definition_id: The role definition id
    :type billing_role_definition_id: str
    """

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'billing_role_definition_id': {'key': 'billingRoleDefinitionId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(BillingRoleAssignmentPayload, self).__init__(**kwargs)
        self.principal_id = kwargs.get('principal_id', None)
        self.billing_role_definition_id = kwargs.get('billing_role_definition_id', None)
