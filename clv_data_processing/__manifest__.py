# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Data Processing',
    'summary': 'Data Processing Module used by CLVsol Solutions.',
    'version': '4.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'images': [],
    'depends': [
        'clv_base',
        'clv_global_log',
    ],
    'data': [
        'security/data_processing_security.xml',
        'security/ir.model.access.csv',
        'views/data_processing_template_view.xml',
        'views/data_processing_template_log_view.xml',
        'views/data_processing_schedule_view.xml',
        'views/data_processing_schedule_log_view.xml',
        'views/data_processing_batch_view.xml',
        'views/data_processing_batch_log_view.xml',
        'views/data_processing_batch_member_view.xml',
        'views/referenceable_model_view.xml',
        'data/data_processing_batch_member.xml',
        # 'wizard/data_processing_mass_edit_view.xml',
        # 'wizard/data_processing_template_mass_edit_view.xml',
        # 'wizard/data_processing_schedule_mass_edit_view.xml',
        # 'wizard/data_processing_schedule_exec_view.xml',
        # 'wizard/data_processing_batch_exec_view.xml',
    ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}