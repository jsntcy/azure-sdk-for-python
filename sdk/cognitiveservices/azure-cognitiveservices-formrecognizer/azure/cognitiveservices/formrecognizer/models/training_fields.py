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


class TrainingFields(Model):
    """List of trained field.

    All required parameters must be populated in order to send to Azure.

    :param fields: Required. List of fields used to train the model and the
     train operation error reported by each.
    :type fields:
     list[~azure.cognitiveservices.formrecognizer.models.FormFieldsReport]
    :param average_model_accuracy: Required. Average accuracy.
    :type average_model_accuracy: float
    """

    _validation = {
        'fields': {'required': True},
        'average_model_accuracy': {'required': True},
    }

    _attribute_map = {
        'fields': {'key': 'fields', 'type': '[FormFieldsReport]'},
        'average_model_accuracy': {'key': 'averageModelAccuracy', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(TrainingFields, self).__init__(**kwargs)
        self.fields = kwargs.get('fields', None)
        self.average_model_accuracy = kwargs.get('average_model_accuracy', None)
