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

from odoo import models, fields


class HistoryMarker(models.Model):
    _inherit = 'clv.history_marker'

    lab_test_type_ids = fields.One2many(
        comodel_name='clv.lab_test.type',
        inverse_name='history_marker_id',
        string='Lab Test Types',
        readonly=True
    )

    lab_test_request_ids = fields.One2many(
        comodel_name='clv.lab_test.request',
        inverse_name='history_marker_id',
        string='Lab Test Requests',
        readonly=True
    )

    lab_test_result_ids = fields.One2many(
        comodel_name='clv.lab_test.result',
        inverse_name='history_marker_id',
        string='Lab Test Results',
        readonly=True
    )

    lab_test_report_ids = fields.One2many(
        comodel_name='clv.lab_test.report',
        inverse_name='history_marker_id',
        string='Lab Test Reports',
        readonly=True
    )


class LabTestType(models.Model):
    _inherit = 'clv.lab_test.type'

    history_marker_id = fields.Many2one(
        comodel_name='clv.history_marker',
        string='History Marker',
        ondelete='restrict'
    )


class LabTestRequest(models.Model):
    _inherit = 'clv.lab_test.request'

    history_marker_id = fields.Many2one(
        comodel_name='clv.history_marker',
        string='History Marker',
        ondelete='restrict'
    )


class LabTestResult(models.Model):
    _inherit = 'clv.lab_test.result'

    history_marker_id = fields.Many2one(
        comodel_name='clv.history_marker',
        string='History Marker',
        ondelete='restrict'
    )


class LabTestReport(models.Model):
    _inherit = 'clv.lab_test.report'

    history_marker_id = fields.Many2one(
        comodel_name='clv.history_marker',
        string='History Marker',
        ondelete='restrict'
    )
