# -*- coding: utf-8 -*-
from openerp import http

# class Citasaldg(http.Controller):
#     @http.route('/citasaldg/citasaldg/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/citasaldg/citasaldg/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('citasaldg.listing', {
#             'root': '/citasaldg/citasaldg',
#             'objects': http.request.env['citasaldg.citasaldg'].search([]),
#         })

#     @http.route('/citasaldg/citasaldg/objects/<model("citasaldg.citasaldg"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('citasaldg.object', {
#             'object': obj
#         })