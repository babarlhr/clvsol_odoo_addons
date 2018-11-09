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


class LabTestRequestOff(models.Model):
    _inherit = 'clv.lab_test.off.request'

    off_instance_id = fields.Many2one(
        comodel_name='clv.off.instance',
        string='Off Instance',
        required=True,
    )


class LabTestReporttOff(models.Model):
    _inherit = 'clv.lab_test.off.report'

    off_instance_id = fields.Many2one(
        comodel_name='clv.off.instance',
        string='Off Instance',
        required=True,
    )