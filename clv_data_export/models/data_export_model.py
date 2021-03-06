# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from datetime import *

from odoo import api, fields, models


class ObjectDataExport(models.AbstractModel):
    _name = 'clv.object.data_export'

    name = fields.Char(string='Name', index=True, required=True)

    label = fields.Char(string='Label')

    model_id = fields.Many2one(
        comodel_name='ir.model',
        string='Model',
        ondelete='restrict',
        # domain="[('model','in',['clv.person','clv.address'])]"
    )
    model_model = fields.Char(string='Model', related='model_id.model', store=False, readonly=True)

    model_items = fields.Char(
        string='Model Items',
        compute='compute_model_items',
        store=False
    )

    @api.depends('model_model')
    def compute_model_items(self):
        pass

    date_data_export = fields.Datetime(
        string="Report Date", required=True, readonly=True,
        default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

    notes = fields.Text(string='Notes')

    active = fields.Boolean(string='Active', default=True)

    def data_export_dir_path(self):
        return ''

    def data_export_file_name(self):
        return '<model>_<label>_<code>_<timestamp>.xls'
