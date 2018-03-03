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

from openerp import fields, models


class CardAnotation(models.Model):
    _description = 'Card Annotation'
    _name = 'clv.card.annotation'
    _inherit = 'clv.object.annotation'

    card_id = fields.Many2one(
        comodel_name='clv.card',
        string='Card',
        ondelete='cascade'
    )


class Card(models.Model):
    _inherit = "clv.card"

    annotation_ids = fields.One2many(
        comodel_name='clv.card.annotation',
        inverse_name='card_id',
        string='Annotations'
    )
