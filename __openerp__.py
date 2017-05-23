# -*- coding: utf-8 -*-
{
    'name': "Citas",

    'summary': """
        - Módulo para fines educativos""",

    'description': """
        Al menos una cita diferente cada día.
    """,

    'author': "Ángel Luis Díaz González",
    #'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'application' : True,
}