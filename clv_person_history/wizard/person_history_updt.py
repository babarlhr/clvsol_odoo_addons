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
from odoo import exceptions

_logger = logging.getLogger(__name__)


class PersonHistoryUpdate(models.TransientModel):
    _name = 'clv.person.history_updt'

    def _default_person_ids(self):
        return self._context.get('active_ids')
    person_ids = fields.Many2many(
        comodel_name='clv.person',
        relation='clv_person_history_updt_rel',
        string='Persons',
        default=_default_person_ids
    )
    sign_in_date = fields.Date(
        string='Sign in date',
        required=False,
    )
    sign_out_date = fields.Date(
        string="Sign out date",
        required=False
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
    def do_person_history_updt(self):
        self.ensure_one()

        PersonHistory = self.env['clv.person.history']

        for person in self.person_ids:

            if self.sign_out_date is False:
                raise exceptions.ValidationError('The "Sign out date" has not been defined!')
                return self._reopen_form()

            if self.sign_in_date is False:
                raise exceptions.ValidationError('The "Sign in date" has not been defined!')
                return self._reopen_form()

            _logger.info(u'%s %s', '>>>>>', person.name)

            if person.history_marker_id.id is not False:

                person_history = PersonHistory.search([
                    ('person_id', '=', person.id),
                    ('history_marker_id', '=', person.history_marker_id.id),
                    ('sign_out_date', '=', False),
                ])

                if person_history.id is False:

                    person_history_2 = PersonHistory.search([
                        ('person_id', '=', person.id),
                        ('sign_out_date', '=', False),
                    ])
                    if person_history_2.id is not False:
                        person_history_2.sign_out_date = self.sign_out_date
                        _logger.info(u'%s %s %s %s', '>>>>>>>>>>', person_history_2.history_marker_id.name,
                                                     person_history_2.sign_in_date,
                                                     person_history_2.sign_out_date)

                    m2m_list = []
                    for category_id in person.category_ids:
                        m2m_list.append((4, category_id.id))
                    category_ids = m2m_list
                    values = {
                        'person_id': person.id,
                        'category_ids': category_ids,
                        'date_reference': person.date_reference,
                        'age_reference': person.age_reference,
                        'estimated_age': person.estimated_age,
                        'responsible_id': person.responsible_id.id,
                        'caregiver_id': person.caregiver_id.id,
                        'address_id': person.address_id.id,
                        'person_address_role_id': person.person_address_role_id.id,
                        'sign_in_date': self.sign_in_date,
                        'history_marker_id': person.history_marker_id.id,
                    }
                    person_history = PersonHistory.create(values)
                    _logger.info(u'%s %s %s %s', '>>>>>>>>>>', person_history.history_marker_id.name,
                                                 person_history.sign_in_date,
                                                 person_history.sign_out_date)

                else:
                    m2m_list = []
                    for category_id in person.category_ids:
                        m2m_list.append((4, category_id.id))
                    m2m_list_2 = []
                    for category_id in person_history.category_ids:
                        m2m_list_2.append((4, category_id.id))
                    if m2m_list != m2m_list_2:
                        person_history.category_ids = m2m_list
                    if person_history.date_reference != person.date_reference:
                        person_history.date_reference = person.date_reference
                    if person_history.age_reference != person.age_reference:
                        person_history.age_reference = person.age_reference
                    if person_history.estimated_age != person.estimated_age:
                        person_history.estimated_age = person.estimated_age
                    if person_history.responsible_id.id != person.responsible_id.id:
                        person_history.responsible_id = person.responsible_id.id
                    if person_history.caregiver_id.id != person.caregiver_id.id:
                        person_history.caregiver_id = person.caregiver_id.id
                    if person_history.address_id.id != person.address_id.id:
                        person_history.address_id = person.address_id.id
                    if person_history.person_address_role_id.id != person.person_address_role_id.id:
                        person_history.person_address_role_id = person.person_address_role_id.id
                    _logger.info(u'%s %s %s %s', '>>>>>>>>>>', person_history.history_marker_id.name,
                                                 person_history.sign_in_date,
                                                 person_history.sign_out_date)

            else:

                person_history = PersonHistory.search([
                    ('person_id', '=', person.id),
                    ('sign_out_date', '=', False),
                ])

                if person_history.id is not False:
                    person_history.sign_out_date = self.sign_out_date
                    _logger.info(u'%s %s %s %s', '>>>>>>>>>>', person_history.history_marker_id.name,
                                                 person_history.sign_in_date,
                                                 person_history.sign_out_date)

        return True

    @api.multi
    def do_populate_all_persons(self):
        self.ensure_one()

        Person = self.env['clv.person']
        persons = Person.search([])

        self.person_ids = persons

        return self._reopen_form()
