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


class FormFieldsReport(Model):
    """Report for a custom model training field.

    All required parameters must be populated in order to send to Azure.

    :param field_name: Required. Training field name.
    :type field_name: str
    :param accuracy: Required. Estimated extraction accuracy for this field.
    :type accuracy: float
    """

    _validation = {
        'field_name': {'required': True},
        'accuracy': {'required': True},
    }

    _attribute_map = {
        'field_name': {'key': 'fieldName', 'type': 'str'},
        'accuracy': {'key': 'accuracy', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(FormFieldsReport, self).__init__(**kwargs)
        self.field_name = kwargs.get('field_name', None)
        self.accuracy = kwargs.get('accuracy', None)
