# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Hospital(models.Model):
    _name = "valerio.factura"
    _description = 'Facturas'

    client = fields.Char("Client")
    payment = fields.Integer(string="Payment")
    bill = fields.Date(string="Bill")
    expiration = fields.Date(string="Expiration")
    dendor = fields.Selection(selection=[('admin', 'Admin'),
                                        ('dendor', 'Dendor')], string='dendor')
    state = fields.Selection(selection=[('active', 'Active'),
                                        ('inactive', 'Inactive')], string='State')



# class StudentStudent(models.Model):
#     _name = 'student.student'
#
#     name = fields.Char(string='Name', required=True)
#     age = fields.Integer(string='Age')
#     photo = fields.Binary(string='Image')
#     gender = fields.Selection([('male', 'Male'),('female','Female')], string='Gender')
#     texto = fields.Text('esto es un campo de Texto')
#     student_dob = fields.Date(string="Date of Birth")
#     student_blood_group = fields.Selection([('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
#      	('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
#     	string='Blood Group')
#     nationality = fields.Many2one('res.country', string='Nationality')
#

# import logging
#
# _logger = logging.getLogger(__name__)
#
#
# class AccountInvoice(models.Model):
#     _inherit = "account.invoice"
#
#     sale_type = fields.Selection(selection=[('01', 'National Sales'),
#                                             ('02', 'Foreign Sales')],
#                                  string=('Sales Type'))
#
#
# class SaleOrder (models.Model):
#     _inherit =  "sale.order"
#     #crear campo en Base de Datos
#     export_sale = fields.Boolean(string = 'Export Sale')
#     #ir al xml... en views
#
#     #declaradores @api.one
#     @api.one
#     def print_console(self):
#         _logger.info("Mensaje de Tarea")
#
#         #vistas

# tarea crear modelo
