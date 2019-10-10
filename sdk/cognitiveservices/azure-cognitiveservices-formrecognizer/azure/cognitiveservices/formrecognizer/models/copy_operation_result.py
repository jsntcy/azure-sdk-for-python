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


class CopyOperationResult(Model):
    """Status and result of copy custom model operation.

    All required parameters must be populated in order to send to Azure.

    :param status: Required. Get status of copy custom model operation.
     Possible values include: 'notStarted', 'running', 'succeeded', 'failed'
    :type status: str or
     ~azure.cognitiveservices.formrecognizer.models.OperationStatus
    :param created_date_time: Required. Date and time (UTC) when the copy
     custom model operation was submitted.
    :type created_date_time: datetime
    :param last_updated_date_time: Required. Date and time (UTC) when the
     status is last updated.
    :type last_updated_date_time: datetime
    :param copy_result: Required. Copy custom model operation result.
    :type copy_result:
     ~azure.cognitiveservices.formrecognizer.models.CopyResult
    """

    _validation = {
        'status': {'required': True},
        'created_date_time': {'required': True},
        'last_updated_date_time': {'required': True},
        'copy_result': {'required': True},
    }

    _attribute_map = {
        'status': {'key': 'status', 'type': 'OperationStatus'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'last_updated_date_time': {'key': 'lastUpdatedDateTime', 'type': 'iso-8601'},
        'copy_result': {'key': 'copyResult', 'type': 'CopyResult'},
    }

    def __init__(self, **kwargs):
        super(CopyOperationResult, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.created_date_time = kwargs.get('created_date_time', None)
        self.last_updated_date_time = kwargs.get('last_updated_date_time', None)
        self.copy_result = kwargs.get('copy_result', None)
