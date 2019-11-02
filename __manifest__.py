# -*- coding: utf-8 -*-
{
    'name': 'valerio',
    'category': 'Vallegrande',
    'version': '0.1',
    'summary': 'Factura ',

    'description': 'Botones Inactivo y activo' ,

    'author': "valerio",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list



    # any module necessary for this one to work correctly
    'depends': [
        'base',
        #'account'
        #'sale_management',
        'account_accountant',
    ],

    # always loaded
    'data': [


        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/factura.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
       # 'demo/demo.xml',
    ],

    # 'images': [],
    # 'license': 'AGPL-3',
    # 'installable': True,
    # 'application': False,
    # 'auto_install': False,

}