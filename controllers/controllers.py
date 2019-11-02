# -*- coding: utf-8 -*-
from odoo import http

# class Ldelacruz(http.Controller):
#     @http.route('/ldelacruz/ldelacruz/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ldelacruz/ldelacruz/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ldelacruz.listing', {
#             'root': '/ldelacruz/ldelacruz',
#             'objects': http.request.env['ldelacruz.ldelacruz'].search([]),
#         })

#     @http.route('/ldelacruz/ldelacruz/objects/<model("ldelacruz.ldelacruz"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ldelacruz.object', {
#             'object': obj
#         })