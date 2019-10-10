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


class TrainRequest(Model):
    """Request parameter to train a new custom model.

    All required parameters must be populated in order to send to Azure.

    :param source: Required. Source path containing the training documents.
    :type source: str
    :param source_filter: Filter to apply to the documents in the source path
     for training.
    :type source_filter:
     ~azure.cognitiveservices.formrecognizer.models.TrainSourceFilter
    :param use_label_file: Specify if label file should be used for training.
     Default value: False .
    :type use_label_file: bool
    """

    _validation = {
        'source': {'required': True, 'max_length': 2048, 'min_length': 0},
    }

    _attribute_map = {
        'source': {'key': 'source', 'type': 'str'},
        'source_filter': {'key': 'sourceFilter', 'type': 'TrainSourceFilter'},
        'use_label_file': {'key': 'useLabelFile', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(TrainRequest, self).__init__(**kwargs)
        self.source = kwargs.get('source', None)
        self.source_filter = kwargs.get('source_filter', None)
        self.use_label_file = kwargs.get('use_label_file', False)
