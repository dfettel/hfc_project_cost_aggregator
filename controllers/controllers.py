# -*- coding: utf-8 -*-
from odoo import http

# class MyModule(http.Controller):
#     @http.route('/hfc_project_cost_aggregator/hfc_project_cost_aggregator/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hfc_project_cost_aggregator/hfc_project_cost_aggregator/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hfc_project_cost_aggregator.listing', {
#             'root': '/hfc_project_cost_aggregator/hfc_project_cost_aggregator',
#             'objects': http.request.env['hfc_project_cost_aggregator.hfc_project_cost_aggregator'].search([]),
#         })

#     @http.route('/hfc_project_cost_aggregator/hfc_project_cost_aggregator/objects/<model("hfc_project_cost_aggregator.hfc_project_cost_aggregator"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hfc_project_cost_aggregator.object', {
#             'object': obj
#         })