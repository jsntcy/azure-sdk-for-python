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


class DataTable(Model):
    """Information about the extracted table contained in a page.

    All required parameters must be populated in order to send to Azure.

    :param rows: Required. Number of rows.
    :type rows: int
    :param columns: Required. Number of columns.
    :type columns: int
    :param cells: Required. List of cells contained in the table.
    :type cells:
     list[~azure.cognitiveservices.formrecognizer.models.DataTableCell]
    """

    _validation = {
        'rows': {'required': True, 'minimum': 1},
        'columns': {'required': True, 'minimum': 1},
        'cells': {'required': True},
    }

    _attribute_map = {
        'rows': {'key': 'rows', 'type': 'int'},
        'columns': {'key': 'columns', 'type': 'int'},
        'cells': {'key': 'cells', 'type': '[DataTableCell]'},
    }

    def __init__(self, **kwargs):
        super(DataTable, self).__init__(**kwargs)
        self.rows = kwargs.get('rows', None)
        self.columns = kwargs.get('columns', None)
        self.cells = kwargs.get('cells', None)
