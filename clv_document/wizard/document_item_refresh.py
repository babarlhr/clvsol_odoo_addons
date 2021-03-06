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

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class DocumentItemRefresh(models.TransientModel):
    _name = 'clv.document.item_refresh'

    def _default_document_ids(self):
        return self._context.get('active_ids')
    document_ids = fields.Many2many(
        comodel_name='clv.document',
        relation='clv_document_item_refresh_rel',
        string='Documents',
        default=_default_document_ids
    )

    @api.multi
    def _reopen_form(self):
        self.ensure_one()
        action = {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }
        return action

    @api.multi
    def do_document_refresh(self):
        self.ensure_one()

        DocumentItem = self.env['clv.document.item']

        for document in self.document_ids:

            _logger.info(u'%s %s %s', '>>>>>', document.code, document.document_type_id.name)

            items = []
            for item in document.document_type_id.item_ids:

                document_item = DocumentItem.search([
                    ('document_id', '=', document.id),
                    ('code', '=', item.code),
                ])

                if document_item.id is not False:
                    break

                if item.document_display:
                    items.append((0, 0, {'code': item.code,
                                         'name': item.name,
                                         'sequence': item.sequence,
                                         }))
            document.item_ids = items

            _logger.info(u'%s %s', '>>>>>>>>>>', items)

        return True
