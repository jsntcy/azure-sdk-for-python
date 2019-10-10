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


class TextWord(Model):
    """An object representing a word.

    All required parameters must be populated in order to send to Azure.

    :param text: Required. The text content of the word.
    :type text: str
    :param bounding_box: Required. Bounding box of an extracted word.
    :type bounding_box: list[float]
    :param confidence: Required. Confidence value.
    :type confidence: float
    """

    _validation = {
        'text': {'required': True},
        'bounding_box': {'required': True},
        'confidence': {'required': True},
    }

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'bounding_box': {'key': 'boundingBox', 'type': '[float]'},
        'confidence': {'key': 'confidence', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(TextWord, self).__init__(**kwargs)
        self.text = kwargs.get('text', None)
        self.bounding_box = kwargs.get('bounding_box', None)
        self.confidence = kwargs.get('confidence', None)
